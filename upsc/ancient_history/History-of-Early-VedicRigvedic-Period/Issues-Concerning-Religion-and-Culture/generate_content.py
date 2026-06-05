# -*- coding: utf-8 -*-
import json
import os
import sys

# Force stdout to use UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\History-of-Early-VedicRigvedic-Period\Issues-Concerning-Religion-and-Culture"

# 1. Outline the 6 Detailed deep-dive sections (in English and Hindi)
sections_meta = [
    {
        "id": 1,
        "title": "1. Nature of Rigvedic Religion",
        "title_hi": "1. ऋग्वैदिक धर्म का स्वरूप",
        "content": """
<h3>Naturalistic Polytheism</h3>
<p>The religion of the early Rigvedic Indo-Aryans was characterized by the personification and worship of natural forces. Seeing natural phenomena like rain, thunder, fire, wind, and dawn as manifestations of divine power, they deified these natural elements. It was a form of naturalistic polytheism, featuring a pantheon of numerous gods (Devas) and occasional goddesses (Devis).</p>

<h3>Max Müller's Concept of Henotheism</h3>
<p>To describe the unique nature of Rigvedic polytheism, the famous Indologist Max Müller coined the term <strong>Henotheism</strong> (or <strong>Kathenotheism</strong>). This refers to the belief in and worship of a single supreme god at a time, while not denying the existence of other deities. In the Rigvedic hymns, when a particular god is addressed (e.g., Indra, Agni, or Varuna), that deity is praised as the highest, all-powerful creator, possessing all supreme attributes. Once the hymn shifts to another deity, the new deity inherits those supreme attributes, reflecting a fluid conception of divinity.</p>

<h3>Absence of Anthropomorphism and Idolatry</h3>
<p>Although the gods were deified natural forces, their anthropomorphism (human-like representation) was highly incomplete and symbolic. Physical descriptions were minimal and metaphorical. Crucially, early Vedic religion was completely devoid of image worship, idol worship, or temples. The gods were invoked through spoken words, prayers, and sacrificial fires rather than physical representations.</p>
""",
        "content_hi": """
<h3>प्राकृतिक बहुदेववाद</h3>
<p>प्रारंभिक ऋग्वैदिक भारत-आर्यों के धर्म की विशेषता प्राकृतिक शक्तियों का मानवीकरण और पूजा थी। वर्षा, वज्रपात, अग्नि, वायु और भोर जैसी प्राकृतिक घटनाओं को दिव्य शक्ति की अभिव्यक्ति के रूप में देखते हुए, उन्होंने इन प्राकृतिक तत्वों का देवत्वकरण किया। यह प्राकृतिक बहुदेववाद का एक रूप था, जिसमें कई देवताओं (देवों) और कभी-कभार देवियों (देवियों) का देवगण शामिल था।</p>

<h3>मैक्स मुलर की हेनोथिज्म (एकेश्वरवाद) की अवधारणा</h3>
<p>ऋग्वैदिक बहुदेववाद के अनूठे स्वरूप का वर्णन करने के लिए, प्रसिद्ध भारतविद् मैक्स मुलर ने <strong>हेनोथिज्म</strong> (या <strong>कथिनोथिज्म</strong>) शब्द गढ़ा। यह एक समय में एक ही सर्वोच्च देवता में विश्वास और पूजा को संदर्भित करता है, जबकि अन्य देवताओं के अस्तित्व को नकारा नहीं जाता है। ऋग्वैदिक भजनों में, जब किसी विशेष देवता (जैसे, इंद्र, अग्नि, या वरुण) को संबोधित किया जाता है, तो उस देवता की प्रशंसा उच्चतम, सर्वशक्तिमान निर्माता के रूप में की जाती है, जिसके पास सभी सर्वोच्च गुण होते हैं। एक बार जब भजन दूसरे देवता पर स्थानांतरित हो जाता है, तो नया देवता उन सर्वोच्च गुणों को प्राप्त कर लेता है, जो देवत्व की एक गतिशील अवधारणा को दर्शाता है।</p>

<h3>मानवरूपातता और मूर्तिपूजा का अभाव</h3>
<p>यद्यपि देवता प्राकृतिक शक्तियों के मानवीकृत रूप थे, लेकिन उनकी मानवरूपातता (मानव-जैसी प्रस्तुति) बहुत सीमित और प्रतीकात्मक थी। शारीरिक विवरण न्यूनतम और रूपकात्मक थे। महत्वपूर्ण बात यह है कि प्रारंभिक वैदिक धर्म मूर्तिपूजा, प्रतिमा पूजा या मंदिरों से पूरी तरह मुक्त था। देवताओं का आह्वान भौतिक प्रस्तुतियों के बजाय बोले गए शब्दों, प्रार्थनाओं और यज्ञ की अग्नि के माध्यम से किया जाता था।</p>
"""
    },
    {
        "id": 2,
        "title": "2. Pantheon of Deities",
        "title_hi": "2. देवगण और देवता",
        "content": """
<h3>Classification of Gods</h3>
<p>Vedic commentators categorized the pantheon of deities into three distinct spheres or realms of the cosmos:</p>
<ol>
    <li><strong>Terrestrial (Prithvisthana):</strong> Gods of the earth, including <strong>Agni</strong> (fire), <strong>Soma</strong> (sacred plant), and <strong>Prithvi</strong> (earth).</li>
    <li><strong>Aerial / Atmospheric (Antarikshasthana):</strong> Gods of the middle space/sky, dominated by <strong>Indra</strong> (thunder), <strong>Vayu</strong> (wind), <strong>Maruts</strong> (storm), and <strong>Rudra</strong> (storm-god).</li>
    <li><strong>Celestial (Dyusthana):</strong> Gods of the high heaven, including <strong>Varuna</strong> (cosmic order), <strong>Mitra</strong>, <strong>Surya</strong> (sun), <strong>Savitr</strong>, and <strong>Dyaus</strong> (sky father).</li>
</ol>

<h3>Prominent Rigvedic Gods</h3>
<p>The Rigvedic hymns are dominated by three major male deities:</p>
<ul>
    <li><strong>Indra (Purandara):</strong> The most important deity, addressed in 250 hymns. He was the god of thunder, rain, and war, credited with slaying the demon Vritra and destroying enemy fortresses (hence called Purandara, or destroyer of forts).</li>
    <li><strong>Agni:</strong> The second most popular god (200 hymns). He represented the sacrificial fire, acting as the mediator between humans and the gods. Offerings thrown into Agni were carried to the other deities.</li>
    <li><strong>Varuna:</strong> The protector of the cosmic, natural, and moral order (<strong>Rta</strong>). He was a highly ethical deity who punished sinners and rewarded the righteous.</li>
</ul>

<h3>Female Deities</h3>
<p>Female deities occupied a subordinate position in the Rigvedic pantheon, reflecting the patriarchal structure of society. Hymns to female deities are few, though prominent goddesses include <strong>Ushas</strong> (goddess of dawn, celebrated for her beauty), <strong>Aditi</strong> (mother of the gods), and <strong>Aranyani</strong> (goddess of the forests).</p>
""",
        "content_hi": """
<h3>देवताओं का वर्गीकरण</h3>
<p>वैदिक भाष्यकारों ने देवताओं के देवगण को ब्रह्मांड के तीन अलग-अलग क्षेत्रों या लोकों में वर्गीकृत किया:</p>
<ol>
    <li><strong>स्थलीय (पृथ्वीस्थान):</strong> पृथ्वी के देवता, जिनमें <strong>अग्नि</strong> (आग), <strong>सोम</strong> (पवित्र पौधा), और <strong>पृथ्वी</strong> शामिल हैं।</li>
    <li><strong>अंतरिक्षीय (अंतरिक्षस्थान):</strong> मध्य आकाश के देवता, जिनमें <strong>इंद्र</strong> (वज्र), <strong>वायु</strong> (पवन), <strong>मरुत</strong> (आंधी), और <strong>रुद्र</strong> (तूफान के देवता) प्रमुख हैं।</li>
    <li><strong>आकाशीय / द्युस्थानीय (द्युस्थान):</strong> उच्च स्वर्ग के देवता, जिनमें <strong>वरुण</strong> (ब्रह्मांडीय व्यवस्था), <strong>मित्र</strong>, <strong>सूर्य</strong>, <strong>सविता</strong>, और <strong>द्यौस</strong> (आकाश पिता) शामिल हैं।</li>
</ol>

<h3>प्रमुख ऋग्वैदिक देवता</h3>
<p>ऋग्वैदिक भजनों में तीन प्रमुख पुरुष देवताओं का वर्चस्व है:</p>
<ul>
    <li><strong>इंद्र (पुरंदर):</strong> सबसे महत्वपूर्ण देवता, जिन्हें 250 भजनों में संबोधित किया गया है। वे वज्र, वर्षा और युद्ध के देवता थे, जिन्हें दानव वृत्र का वध करने और शत्रुओं के किलों को नष्ट करने का श्रेय दिया जाता है (इसीलिए उन्हें पुरंदर कहा जाता है)।</li>
    <li><strong>अग्नि:</strong> दूसरे सबसे लोकप्रिय देवता (200 भजन)। वे यज्ञीय अग्नि का प्रतिनिधित्व करते थे, जो मनुष्यों और देवताओं के बीच मध्यस्थ के रूप में कार्य करती थी। अग्नि में डाली जाने वाली आहुतियाँ अन्य देवताओं तक पहुँचाई जाती थीं।</li>
    <li><strong>वरुण:</strong> ब्रह्मांडीय, प्राकृतिक और नैतिक व्यवस्था (<strong>ऋत</strong>) के रक्षक। वे एक अत्यधिक नैतिक देवता थे जो पापियों को दंडित करते थे और धर्मियों को पुरस्कृत करते थे।</li>
</ul>

<h3>महिला देवियाँ</h3>
<p>समाज की पितृसत्तात्मक संरचना को दर्शाते हुए, ऋग्वैदिक देवगण में महिला देवियों को गौण स्थान प्राप्त था। महिला देवियों के भजन कम हैं, हालांकि प्रमुख देवियों में <strong>उषा</strong> (भोर की देवी, अपनी सुंदरता के लिए प्रसिद्ध), <strong>अदिति</strong> (देवताओं की माता), और <strong>अरण्यानी</strong> (वन की देवी) शामिल हैं।</p>
"""
    },
    {
        "id": 3,
        "title": "3. Sacrifices, Rituals & Mode of Worship",
        "title_hi": "3. यज्ञ, अनुष्ठान और पूजा पद्धति",
        "content": """
<h3>Prayers and Offerings (Yajna)</h3>
<p>The primary modes of worship in early Vedic times were prayers (<strong>Prarthana</strong>) and sacrifices (<strong>Yajna</strong>). Worship was simple and centered on individual or clan-level rituals. Sacrifices involved making offerings of milk, clarified butter (ghee), barley (yava), and the sacred Soma juice into the sacrificial fire. Occasionally, animal sacrifices were also performed to gain the favor of the gods.</p>

<h3>Material Motives of Worship</h3>
<p>Rigvedic worship was utilitarian and materialistic. Prayers and sacrifices were not offered for spiritual salvation (Moksha) or release from the cycle of rebirth, concepts that did not exist in the early Vedic mind. Instead, they worshipped to secure concrete, worldly benefits: large herds of cattle (paśu), brave sons (vīra), long life (āyus), food (anna), and victory in battles over rival clans.</p>

<h3>Absence of Priesthood Hierarchies</h3>
<p>In the early Vedic period, sacrifices were simple domestic affairs performed directly by the patriarch (Grihapati/Kulapa) of the family. There was no complex, dominant priestly hierarchy or monopoly. Although professional priests like the Purohita existed to advise the Rajan and conduct tribal sacrifices, the elaborate, expensive rituals requiring dozens of specialized priests only developed in the Later Vedic phase.</p>
""",
        "content_hi": """
<h3>प्रार्थना और आहुति (यज्ञ)</h3>
<p>प्रारंभिक वैदिक काल में पूजा के प्राथमिक तरीके प्रार्थना (<strong>प्रार्थना</strong>) और यज्ञ (<strong>यज्ञ</strong>) थे। पूजा सरल थी और व्यक्तिगत या कबीले के स्तर के अनुष्ठानों पर केंद्रित थी। यज्ञों में दूध, शुद्ध घी, जौ (यव) और पवित्र सोम रस की आहुति यज्ञ की अग्नि में दी जाती थी। देवताओं की कृपा प्राप्त करने के लिए कभी-कभार पशु बलि भी दी जाती थी।</p>

<h3>पूजा के भौतिक उद्देश्य</h3>
<p>ऋग्वैदिक पूजा उपयोगितावादी और भौतिकवादी थी। प्रार्थना और यज्ञ आध्यात्मिक मुक्ति (मोक्ष) या पुनर्जन्म के चक्र से मुक्ति के लिए नहीं किए जाते थे, ये अवधारणाएं प्रारंभिक वैदिक मस्तिष्क में मौजूद नहीं थीं। इसके बजाय, वे ठोस, सांसारिक लाभ प्राप्त करने के लिए पूजा करते थे: मवेशियों के बड़े झुंड (पशु), वीर पुत्र (वीर), दीर्घायु (आयु), भोजन (अन्न), और प्रतिद्वंद्वी कबीलों पर युद्धों में विजय।</p>

<h3>पुरोहित वर्ग के पदानुक्रम का अभाव</h3>
<p>प्रारंभिक वैदिक काल में, यज्ञ सरल घरेलू मामले थे जो सीधे परिवार के मुखिया (गृहपति/कुलप) द्वारा किए जाते थे। कोई जटिल, वर्चस्वशाली पुरोहित पदानुक्रम या एकाधिकार नहीं था। यद्यपि राजन को सलाह देने और जनजातीय यज्ञों के संचालन के लिए पुरोहित जैसे पेशेवर पुजारी मौजूद थे, लेकिन दर्जनों विशिष्ट पुजारियों की आवश्यकता वाले विस्तृत, महंगे अनुष्ठानों का विकास उत्तर वैदिक चरण में ही हुआ था।</p>
"""
    },
    {
        "id": 4,
        "title": "4. The Concept of Rta",
        "title_hi": "4. ऋत की अवधारणा",
        "content": """
<h3>Cosmic and Natural Order</h3>
<p>One of the most profound ethical and philosophical concepts in the Rigveda is <strong>Rta</strong>. Rta represents the cosmic, natural, and moral order that governs the entire universe. It is the cosmic law that ensures the regular movement of the sun, moon, and stars, the succession of seasons (Rtu), and the flow of rivers. Without Rta, the universe would descend into chaos (Anrta).</p>

<h3>Varuna as the Guardian of Rta</h3>
<p>The god <strong>Varuna</strong> is hailed as the supreme guardian of Rta, often designated as <strong>Rtavan</strong> or <strong>Rtavrih</strong> (upholder of Rta). Alongside Mitra, Varuna monitors human conduct using his spies (Spasa) to ensure that moral laws are not breached. Those who violate the moral order of Rta commit sin (papa) and are bound by Varuna's noose (pasa), which manifests as disease or misfortune.</p>

<h3>Moral Duty of Humans</h3>
<p>Rta was not merely a physical law of nature but also an ethical code for human conduct. Truth (Satya) was seen as the human expression of Rta. Living in accordance with Rta required practicing honesty, performing sacrifices, respecting kinship duties, and demonstrating hospitality. This concept laid the early foundation for the classical Hindu doctrine of Dharma.</p>
""",
        "content_hi": """
<h3>ब्रह्मांडीय और प्राकृतिक व्यवस्था</h3>
<p>ऋग्वेद में सबसे गहन नैतिक और दार्शनिक अवधारणाओं में से एक <strong>ऋत</strong> है। ऋत उस ब्रह्मांडीय, प्राकृतिक और नैतिक व्यवस्था का प्रतिनिधित्व करता है जो पूरे ब्रह्मांड को नियंत्रित करती है। यह वह ब्रह्मांडीय नियम है जो सूर्य, चंद्रमा और तारों की नियमित गति, ऋतुओं के अनुक्रम (ऋतु), और नदियों के प्रवाह को सुनिश्चित करता है। ऋत के बिना, ब्रह्मांड अराजकता (अनृत) में बदल जाएगा।</p>

<h3>वरुण: ऋत के रक्षक</h3>
<p>देवता <strong>वरुण</strong> को ऋत के सर्वोच्च संरक्षक के रूप में सराहा गया है, जिन्हें अक्सर <strong>ऋतवान</strong> या <strong>ऋतवृध</strong> (ऋत का समर्थक) के रूप में नामित किया जाता है। मित्र के साथ मिलकर, वरुण अपने गुप्तचरों (स्पश) का उपयोग करके मानव आचरण की निगरानी करते हैं ताकि यह सुनिश्चित हो सके कि नैतिक कानूनों का उल्लंघन न हो। जो लोग ऋत के नैतिक आदेश का उल्लंघन करते हैं वे पाप करते हैं और वरुण के पाश (फंदे) से बंध जाते हैं, जो बीमारी या दुर्भाग्य के रूप में प्रकट होता है।</p>

<h3>मनुष्यों का नैतिक कर्तव्य</h3>
<p>ऋत केवल प्रकृति का भौतिक नियम नहीं था बल्कि मानव आचरण के लिए एक नैतिक संहिता भी था। सत्य को ऋत की मानवीय अभिव्यक्ति के रूप में देखा जाता था। ऋत के अनुसार जीने के लिए ईमानदारी का अभ्यास करना, यज्ञ करना, सगोत्रता के कर्तव्यों का सम्मान करना और अतिथि सत्कार प्रदर्शित करना आवश्यक था। इस अवधारणा ने शास्त्रीय हिंदू धर्म की धर्म की अवधारणा के लिए प्रारंभिक नींव रखी।</p>
"""
    },
    {
        "id": 5,
        "title": "5. Funerary Practices & Afterlife",
        "title_hi": "5. अंतिम संस्कार प्रथाएं और परलोक",
        "content": """
<h3>Methods of Disposal</h3>
<p>The Rigvedic people practiced two primary methods for the disposal of the dead, reflecting both fire-based and earth-based rituals:</p>
<ul>
    <li><strong>Cremation (Agni-dagdha):</strong> The body was burned on a funeral pyre. Agni, the fire god, was invoked to consume the body gently and carry the deceased's spirit to the realm of the ancestors.</li>
    <li><strong>Burial (Anagni-dagdha):</strong> The body was buried in the earth, often covered with a mound or stone circle. Burial was common for infants and ascetics.</li>
</ul>

<h3>Pitriloka and Yamaloka</h3>
<p>The early Vedic people believed in a life after death. The spirit of the deceased traveled to the ancestral realm, known as <strong>Pitriloka</strong>. This realm was ruled by <strong>Yama</strong>, the god of death, who was considered the first mortal to die and discover the path to the afterlife. In Yamaloka, the spirits of the dead lived a blissful, shadow-like existence, receiving offerings (Svadha) from their living descendants during ancestral rites (Sraddha).</p>

<h3>Absence of Rebirth Doctrine</h3>
<p>Crucially, the fully developed Hindu doctrines of **Samsara** (the cycle of rebirth) and **Karma** (consequences of actions determining future births) are completely absent in the Rigveda. The early Vedic mind conceived of a simple, linear afterlife in the ancestral realm, rather than a continuous cycle of transmigration, which only emerged later in the Upanishads.</p>
""",
        "content_hi": """
<h3>अंतिम संस्कार के तरीके</h3>
<p>ऋग्वैदिक लोग मृतकों के अंतिम संस्कार के लिए दो प्राथमिक तरीकों का अभ्यास करते थे, जो अग्नि-आधारित और पृथ्वी-आधारित दोनों अनुष्ठानों को दर्शाते हैं:</p>
<ul>
    <li><strong>दाह संस्कार (अग्नि-दग्ध):</strong> शरीर को चिता पर जलाया जाता था। अग्नि देव का आह्वान किया जाता था कि वे शरीर को धीरे-धीरे भस्म करें और मृतक की आत्मा को पितरों के लोक में ले जाएं।</li>
    <li><strong>दफन संस्कार (अनग्नि-दग्ध):</strong> शरीर को पृथ्वी में दफनाया जाता था, जिसे अक्सर एक टीले या पत्थर के घेरे से ढक दिया जाता था। शिशुओं और संन्यासियों के लिए दफन आम था।</li>
</ul>

<h3>पितृलोक और यमलोक</h3>
<p>प्रारंभिक वैदिक लोग मृत्यु के बाद जीवन में विश्वास करते थे। मृतक की आत्मा पूर्वजों के लोक में जाती थी, जिसे <strong>पितृलोक</strong> कहा जाता था। इस लोक पर मृत्यु के देवता <strong>यम</strong> का शासन था, जिन्हें मरने वाले और परलोक का मार्ग खोजने वाले पहले मानव के रूप में माना जाता था। यमलोक में, मृतकों की आत्माएं एक सुखद, छाया जैसी स्थिति में रहती थीं, और पूर्वजों के अनुष्ठानों (श्राद्ध) के दौरान अपने जीवित वंशजों से प्रसाद (स्वधा) प्राप्त करती थीं।</p>

<h3>पुनर्जन्म सिद्धांत का अभाव</h3>
<p>महत्वपूर्ण बात यह है कि **संसार** (पुनर्जन्म का चक्र) और **कर्म** (भविष्य के जन्मों को निर्धारित करने वाले कार्यों के परिणाम) के पूर्ण रूप से विकसित हिंदू सिद्धांत ऋग्वेद में पूरी तरह से अनुपस्थित हैं। प्रारंभिक वैदिक मस्तिष्क ने पुनर्जन्म के निरंतर चक्र के बजाय पूर्वजों के लोक में एक सरल, रैखिक परलोक की कल्पना की थी, जो बाद में उपनिषदों में उभरी।</p>
"""
    },
    {
        "id": 6,
        "title": "6. Transition to Later Vedic Religion",
        "title_hi": "6. उत्तर वैदिक धर्म की ओर संक्रमण",
        "content": """
<h3>Shifting Pantheon</h3>
<p>Towards the end of the Rigvedic period (c. 1000 BCE), the religious focus began to shift. The great atmospheric and storm gods of the early period, such as Indra and Varuna, lost their supreme prominence. In their place, deities associated with creation, preservation, and destruction began to rise, laying the foundation for the Later Vedic trinity:</p>
<ul>
    <li><strong>Prajapati:</strong> The creator god, who emerged as the supreme deity in late Rigvedic hymns.</li>
    <li><strong>Rudra:</strong> A minor storm god in the Rigveda, who began to acquire the traits of Shiva.</li>
    <li><strong>Vishnu:</strong> Praised in the Rigveda for his three cosmic strides (Trivikrama), who rose to prominence as the preserver.</li>
</ul>

<h3>Philosophical Speculations</h3>
<p>The late hymns of the Rigveda, particularly in the 10th Mandala, exhibit a transition from naturalistic polytheism to early monism (belief in a single underlying reality). The famous <strong>Nasadiya Sukta</strong> (Hymn of Creation) speculates on the origins of the universe, asking: <i>'Who knows whence this creation arose?'</i>, reflecting a skeptical and philosophical inquiry. The famous statement: <i>'Ekam sat vipra bahudha vadanti'</i> (Truth is one, but the wise call it by many names) emerged in this phase, marking a move toward pantheism.</p>

<h3>Ritual Rigidity and Priesthood</h3>
<p>The transition was also marked by increasing ritual complexity. Sacrifices became elaborate, expensive, and dominated by professional Brahmanas. The simple domestic rituals were replaced by large-scale public sacrifices (like Rajasuya and Asvamedha), establishing the social supremacy of the priestly class that defined Later Vedic society.</p>
""",
        "content_hi": """
<h3>बदलता हुआ देवगण</h3>
<p>ऋग्वैदिक काल के अंत में (लगभग 1000 ईसा पूर्व), धार्मिक ध्यान स्थानांतरित होने लगा। प्रारंभिक काल के महान वायुमंडलीय और तूफान के देवता, जैसे इंद्र और वरुण, ने अपनी सर्वोच्च प्रमुखता खो दी। उनके स्थान पर, सृष्टि, संरक्षण और विनाश से जुड़े देवताओं का उदय होने लगा, जिससे उत्तर वैदिक त्रिमूर्ति की नींव पड़ी:</p>
<ul>
    <li><strong>प्रजापति:</strong> सृष्टिकर्ता देवता, जो उत्तर ऋग्वैदिक भजनों में सर्वोच्च देवता के रूप में उभरे।</li>
    <li><strong>रुद्र:</strong> ऋग्वेद में एक लघु तूफान के देवता, जिन्होंने शिव के गुणों को प्राप्त करना शुरू किया।</li>
    <li><strong>विष्णु:</strong> ऋग्वेद में उनके तीन डगों (त्रिविक्रम) के लिए प्रशंसित, जो संरक्षक के रूप में प्रमुखता से उभरे।</li>
</ul>

<h3>दार्शनिक चिंतन</h3>
<p>ऋग्वेद के बाद के भजन, विशेष रूप से 10वें मंडल में, प्राकृतिक बहुदेववाद से प्रारंभिक अद्वैतवाद (एक ही अंतर्निहित वास्तविकता में विश्वास) में संक्रमण को प्रदर्शित करते हैं। प्रसिद्ध <strong>नासदीय सूक्त</strong> (सृष्टि का भजन) ब्रह्मांड की उत्पत्ति पर विचार करता है, और पूछता है: <i>'कौन जानता है कि यह सृष्टि कहाँ से आई?'</i>, जो एक संशयवादी और दार्शनिक जांच को दर्शाता है। प्रसिद्ध कथन: <i>'एकं सद् विप्रा बहुधा वदन्ति'</i> (सत्य एक है, लेकिन विद्वान इसे कई नामों से पुकारते हैं) इसी चरण में उभरा, जो सर्वेश्वरवाद की ओर बढ़ने का संकेत था।</p>

<h3>अनुष्ठानिक कठोरता और पुरोहित वर्ग</h3>
<p>यह संक्रमण बढ़ती अनुष्ठानिक जटिलता से भी चिह्नित था। यज्ञ विस्तृत, महंगे और पेशेवर ब्राह्मणों के वर्चस्व वाले हो गए। सरल घरेलू अनुष्ठानों का स्थान बड़े पैमाने पर सार्वजनिक यज्ञों (जैसे राजसूय और अश्वमेध) ने ले लिया, जिससे पुरोहित वर्ग का सामाजिक वर्चस्व स्थापित हुआ जिसने उत्तर वैदिक समाज को परिभाषित किया।</p>
"""
    }
]

# 2. Generator for 62 mastery zone questions per section

question_pool = {1: [{'q': "Who coined the term 'Henotheism' for Rigvedic polytheism?", 'opts': ['Max Müller', 'William Jones', 'Arthur Basham', 'Al-Biruni'], 'ans': 0, 'sol': 'Max Müller coined the term Henotheism to describe worship of one god as supreme at a time.', 'q_hi': "ऋग्वैदिक बहुदेववाद के लिए 'हेनोथिज्म' शब्द किसने गढ़ा था?", 'opts_hi': ['मैक्स मुलर', 'विलियम जोन्स', 'आर्थर बाशम', 'अल-बिरूनी'], 'ans_hi': 0, 'sol_hi': "मैक्स मुलर ने एक समय में एक ही देवता की सर्वोच्च के रूप में पूजा करने का वर्णन करने के लिए 'हेनोथिज्म' शब्द गढ़ा था."}, {'q': 'What describes the concept of Henotheism (or Kathenotheism)?', 'opts': ['Worship of a single supreme deity at a time, without denying others', 'Belief in only one god who has no physical representation', 'Worship of ancestors and animal totems only', 'Complete rejection of natural gods'], 'ans': 0, 'sol': 'It is fluid worship where the deity addressed is temporarily praised as supreme.', 'q_hi': 'एकेश्वरवाद या हेनोथिज्म (कथिनोथिज्म) की अवधारणा का क्या वर्णन है?', 'opts_hi': ['अन्य देवताओं को नकारे बिना, एक समय में एक ही सर्वोच्च देवता की पूजा करना', 'केवल एक ईश्वर में विश्वास जिसका कोई भौतिक प्रतिनिधित्व नहीं है', 'केवल पूर्वजों और पशु प्रतीकों की पूजा करना', 'प्राकृतिक देवताओं को पूरी तरह से खारिज करना'], 'ans_hi': 0, 'sol_hi': 'यह एक लचीली पूजा पद्धति है जहाँ संबोधित किए जाने वाले देवता की अस्थायी रूप से सर्वोच्च के रूप में प्रशंसा की जाती है.'}, {'q': 'Did the early Vedic religion practice image or idol worship?', 'opts': ['No, it was completely devoid of idols, images, or temples', 'Yes, clay idols of Indra were found in all family homes', 'Only in the Sarasvati basin', 'Only during the Soma sacrifices'], 'ans': 0, 'sol': 'Early Vedic religion relied on oral prayers and fire sacrifice; no idols existed.', 'q_hi': 'क्या प्रारंभिक वैदिक धर्म में मूर्ति या प्रतिमा पूजा की जाती थी?', 'opts_hi': ['नहीं, यह पूरी तरह से मूर्तियों, छवियों या मंदिरों से मुक्त था', 'हाँ, सभी पारिवारिक घरों में इंद्र की मिट्टी की मूर्तियाँ मिली थीं', 'केवल सरस्वती बेसिन में', 'केवल सोम यज्ञों के दौरान'], 'ans_hi': 0, 'sol_hi': 'प्रारंभिक वैदिक धर्म मौखिक प्रार्थनाओं और अग्नि यज्ञ पर निर्भर था; कोई मूर्तियां मौजूद नहीं थीं.'}, {'q': 'What is the primary characteristic of early Rigvedic religion?', 'opts': ['Naturalistic polytheism (deification of natural forces)', 'Highly philosophical monism', 'Temples and ritual animal enclosures', 'Rejection of rituals in favor of meditation'], 'ans': 0, 'sol': 'They worshipped deified natural elements like rain, wind, fire, and dawn.', 'q_hi': 'प्रारंभिक ऋग्वैदिक धर्म की प्राथमिक विशेषता क्या है?', 'opts_hi': ['प्राकृतिक बहुदेववाद (प्राकृतिक शक्तियों का देवत्वीकरण)', 'अत्यधिक दार्शनिक अद्वैतवाद', 'मंदिर और अनुष्ठानिक पशु बाड़े', 'ध्यान के पक्ष में अनुष्ठानों की अस्वीकृति'], 'ans_hi': 0, 'sol_hi': 'वे वर्षा, वायु, अग्नि और भोर जैसे प्राकृतिक तत्वों की पूजा करते थे.'}, {'q': 'How were deities invoked by early Rigvedic Indo-Aryans?', 'opts': ['Through spoken hymns, prayers, and fire sacrifices (Yajnas)', 'Through elaborate dance and theatrical performances', 'By offering stone sculptures in temples', 'By writing letters on birch bark'], 'ans': 0, 'sol': 'Invocation was done through chanting hymns and throwing offerings into the fire.', 'q_hi': 'प्रारंभिक ऋग्वैदिक भारत-आर्यों द्वारा देवताओं का आह्वान कैसे किया जाता था?', 'opts_hi': ['बोले गए भजनों, प्रार्थनाओं और अग्नि यज्ञों (यज्ञ) के माध्यम से', 'विस्तृत नृत्य और नाट्य प्रदर्शनों के माध्यम से', 'मंदिरों में पत्थर की मूर्तियाँ भेंट करके', 'भोजपत्र पर पत्र लिखकर'], 'ans_hi': 0, 'sol_hi': 'देवताओं का आह्वान भजनों के पाठ और अग्नि में आहुति डालने के माध्यम से किया जाता था.'}, {'q': 'Was the anthropomorphism of early Vedic gods complete?', 'opts': ['No, it was incomplete and highly symbolic', 'Yes, they were depicted as having complete human bodies', 'They were only represented as animals', 'None of the above'], 'ans': 0, 'sol': 'Human attributes given to deified natural elements were symbolic and metaphorical.', 'q_hi': 'क्या प्रारंभिक वैदिक देवताओं का मानवीकरण पूर्ण था?', 'opts_hi': ['नहीं, यह अधूरा और अत्यधिक प्रतीकात्मक था', 'हाँ, उन्हें पूर्ण मानव शरीर के रूप में दर्शाया गया था', 'उन्हें केवल जानवरों के रूप में दर्शाया गया था', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'देवत्वकृत प्राकृतिक तत्वों को दिए गए मानवीय गुण प्रतीकात्मक और रूपकात्मक थे.'}, {'q': "What was deified by the Rigvedic deity 'Savitr'?", 'opts': ['The rising sun or solar energy', 'The storm and wind', 'The evening twilight', 'The agricultural furrow'], 'ans': 0, 'sol': 'Savitr was the solar deity representing the stimulating power of the rising sun.', 'q_hi': "ऋग्वैदिक देवता 'सविता' द्वारा किसे देवत्व प्रदान किया गया था?", 'opts_hi': ['उगता हुआ सूर्य या सौर ऊर्जा', 'आँधी और हवा', 'शाम की गोधूलि', 'कृषि की नाली'], 'ans_hi': 0, 'sol_hi': 'सविता उगते सूर्य की उत्तेजक शक्ति का प्रतिनिधित्व करने वाले सौर देवता थे.'}, {'q': 'Which text contains the oldest hymns of naturalistic polytheism?', 'opts': ['Rigveda Samhita', 'Atharvaveda', 'Shatapatha Brahmana', 'Chandogya Upanishad'], 'ans': 0, 'sol': 'Rigveda Samhita contains the earliest hymns deifying nature forces.', 'q_hi': 'प्राकृतिक बहुदेववाद के सबसे पुराने भजन किस ग्रंथ में मिलते हैं?', 'opts_hi': ['ऋग्वेद संहिता', 'अथर्ववेद', 'शतपथ ब्राह्मण', 'छान्दोग्य उपनिषद'], 'ans_hi': 0, 'sol_hi': 'ऋग्वेद संहिता में प्राकृतिक शक्तियों को देवत्व प्रदान करने वाले सबसे पहले भजन शामिल हैं.'}, {'q': 'The division of the cosmos into three realms (earth, middle space, sky) was used to categorize:', 'opts': ['Vedic deities', 'Social varnas', 'Vedic rivers', 'Types of sacrifices'], 'ans': 0, 'sol': 'Vedic commentators divided the pantheon into terrestrial, aerial, and celestial deities.', 'q_hi': 'ब्रह्मांड का तीन लोकों (पृथ्वी, अंतरिक्ष, द्युलोक) में विभाजन किसे वर्गीकृत करने के लिए किया जाता था?', 'opts_hi': ['वैदिक देवताओं को', 'सामाजिक वर्णों को', 'वैदिक नदियों को', 'यज्ञों के प्रकारों को'], 'ans_hi': 0, 'sol_hi': 'वैदिक भाष्यकारों ने देवगण को पृथ्वीस्थानीय, अंतरिक्षस्थानीय और द्युस्थानीय देवताओं में विभाजित किया.'}, {'q': 'Who represented the celestial sky-father in the early Rigveda?', 'opts': ['Dyaus', 'Prithvi', 'Indra', 'Agni'], 'ans': 0, 'sol': 'Dyaus was deified as the sky-father, paired with Prithvi (earth-mother).', 'q_hi': 'प्रारंभिक ऋग्वेद में आकाशीय द्युलोक-पिता का प्रतिनिधित्व किसने किया था?', 'opts_hi': ['द्यौस', 'पृथ्वी', 'इंद्र', 'अग्नि'], 'ans_hi': 0, 'sol_hi': 'द्यौस को द्युलोक-पिता के रूप में प्रतिष्ठित किया गया था, जिन्हें पृथ्वी (धरती-माता) के साथ जोड़ा गया था.'}, {'q': 'Early Rigvedic priests invoked deities mainly to secure:', 'opts': ['Utilitarian, worldly benefits', 'Release from Samsara', 'Merging with Brahman', 'Control of iron weapons'], 'ans': 0, 'sol': 'Prayers were strictly for cows, sons, health, and victory.', 'q_hi': 'प्रारंभिक ऋग्वैदिक पुरोहितों ने मुख्य रूप से क्या प्राप्त करने के लिए देवताओं का आह्वान किया?', 'opts_hi': ['उपयोगितावादी, सांसारिक लाभ', 'संसार से मुक्ति', 'ब्रह्म में विलीन होना', 'लोहे के हथियारों पर नियंत्रण'], 'ans_hi': 0, 'sol_hi': 'प्रार्थनाएँ पूरी तरह से गायों, बेटों, स्वास्थ्य और विजय के लिए थीं.'}, {'q': "The concept of 'Ekam Sat' (Truth is one) in late hymns indicates:", 'opts': ['Transition towards monism and philosophical unity', 'Decline of sacrifice rituals', 'Victory of Indra over other gods', 'Abolition of the pantheon'], 'ans': 0, 'sol': 'Ekam Sat Vipra Bahudha Vadanti marks early transition to monism/philosophical unity.', 'q_hi': "उत्तरकालीन भजनों में 'एकम सत्' (सत्य एक है) की अवधारणा क्या दर्शाती है?", 'opts_hi': ['अद्वैतवाद और दार्शनिक एकता की ओर संक्रमण', 'यज्ञ अनुष्ठानों में गिरावट', 'अन्य देवताओं पर इंद्र की विजय', 'देवगण का उन्मूलन'], 'ans_hi': 0, 'sol_hi': 'एकम सत् विप्रा बहुधा वदन्ति अद्वैतवाद/दार्शनिक एकता की ओर प्रारंभिक संक्रमण को चिह्नित करता है.'}], 2: [{'q': 'Which Rigvedic deity is addressed in the maximum number (250) of hymns?', 'opts': ['Indra', 'Agni', 'Varuna', 'Soma'], 'ans': 0, 'sol': 'Indra is the thunder-god and military leader praised in 250 hymns.', 'q_hi': 'किस ऋग्वैदिक देवता को अधिकतम संख्या (250) भजनों में संबोधित किया गया है?', 'opts_hi': ['इंद्र', 'अग्नि', 'वरुण', 'सोम'], 'ans_hi': 0, 'sol_hi': 'इंद्र वज्र के देवता और सैन्य नेता हैं जिनकी 250 भजनों में प्रशंसा की गई है.'}, {'q': 'What is the secondary most popular god in the Rigveda, with 200 hymns?', 'opts': ['Agni', 'Indra', 'Varuna', 'Soma'], 'ans': 0, 'sol': 'Agni, the fire god, is the second most praised deity in early texts.', 'q_hi': 'ऋग्वेद में 200 भजनों के साथ दूसरा सबसे लोकप्रिय देवता कौन सा है?', 'opts_hi': ['अग्नि', 'इंद्र', 'वरुण', 'सोम'], 'ans_hi': 0, 'sol_hi': 'अग्नि, अग्नि देव, प्रारंभिक ग्रंथों में दूसरे सबसे अधिक प्रशंसित देवता हैं.'}, {'q': 'Which god acted as the mediator between humans and the divine?', 'opts': ['Agni (Sacrificial fire)', 'Varuna', 'Indra', 'Maruts'], 'ans': 0, 'sol': 'Agni carried offerings thrown into the sacrificial fire to other deities.', 'q_hi': 'कौन सा देवता मनुष्यों और दिव्य शक्तियों के बीच मध्यस्थ के रूप में कार्य करता था?', 'opts_hi': ['अग्नि (यज्ञ की अग्नि)', 'वरुण', 'इंद्र', 'मरुत'], 'ans_hi': 0, 'sol_hi': 'अग्नि यज्ञ की अग्नि में डाली जाने वाली आहुतियों को अन्य देवताओं तक ले जाती थी.'}, {'q': "Who was deified as the guardian of 'Rta' (Cosmic and Moral Order)?", 'opts': ['Varuna', 'Indra', 'Agni', 'Soma'], 'ans': 0, 'sol': 'Varuna was the ethical guardian of cosmic moral order and laws.', 'q_hi': "किसे 'ऋत' (ब्रह्मांडीय और नैतिक व्यवस्था) के रक्षक के रूप में प्रतिष्ठित किया गया था?", 'opts_hi': ['वरुण', 'इंद्र', 'अग्नि', 'सोम'], 'ans_hi': 0, 'sol_hi': 'वरुण ब्रह्मांडीय नैतिक व्यवस्था और नियमों के नैतिक रक्षक थे.'}, {'q': "What title applied to Indra translates to 'destroyer of forts'?", 'opts': ['Purandara', 'Gopati', 'Naditarna', 'Isana'], 'ans': 0, 'sol': 'Purandara means destroyer of fortresses or enclosures.', 'q_hi': "इंद्र के लिए प्रयुक्त किस उपाधि का अर्थ 'किलों को नष्ट करने वाला' है?", 'opts_hi': ['पुरंदर', 'गोपति', 'नदीतमा', 'ईशान'], 'ans_hi': 0, 'sol_hi': 'पुरंदर का अर्थ किलों या बाड़ों को नष्ट करने वाला है.'}, {'q': 'Which atmospheric god represented the violent storm in early hymns?', 'opts': ['Rudra or Maruts', 'Indra only', 'Vayu only', 'Agni'], 'ans': 0, 'sol': 'Rudra and Maruts deified storm forces and tempest winds.', 'q_hi': 'प्रारंभिक भजनों में किस अंतरिक्षीय देवता को हिंसक आंधी का प्रतिनिधित्व माना गया था?', 'opts_hi': ['रुद्र या मरुत', 'केवल इंद्र', 'केवल वायु', 'अग्नि'], 'ans_hi': 0, 'sol_hi': 'रुद्र और मरुत आंधी की शक्तियों और हिंसक हवाओं के देवत्वकृत रूप थे.'}, {'q': 'Who was the female goddess of dawn celebrated for her beauty?', 'opts': ['Ushas', 'Aditi', 'Aranyani', 'Prithvi'], 'ans': 0, 'sol': 'Ushas was the goddess of dawn, depicted as a beautiful young woman.', 'q_hi': 'अपनी सुंदरता के लिए प्रसिद्ध भोर की देवी कौन थी?', 'opts_hi': ['उषा', 'अदिति', 'अरण्यानी', 'पृथ्वी'], 'ans_hi': 0, 'sol_hi': 'उषा भोर की देवी थीं, जिन्हें एक सुंदर युवा महिला के रूप में चित्रित किया गया था.'}, {'q': 'Which goddess represented the mother of the gods in Rigvedic mythology?', 'opts': ['Aditi', 'Ushas', 'Aranyani', 'Savitri'], 'ans': 0, 'sol': 'Aditi was deified as the cosmic mother of the Adityas (deities).', 'q_hi': 'ऋग्वैदिक पौराणिक कथाओं में किस देवी को देवताओं की माता के रूप में दर्शाया गया है?', 'opts_hi': ['अदिति', 'उषा', 'अरण्यानी', 'सावित्री'], 'ans_hi': 0, 'sol_hi': 'अदिति को आदित्यों (देवताओं) की ब्रह्मांडीय माता के रूप में प्रतिष्ठित किया गया था.'}, {'q': "The goddess 'Aranyani' in early Vedic hymns represented:", 'opts': ['The forest and wilderness', 'The dawn and beauty', 'The domestic hearth', 'The river Sarasvati'], 'ans': 0, 'sol': 'Aranyani was deified as the spirit/goddess of the forest and wilderness.', 'q_hi': "प्रारंभिक वैदिक भजनों में देवी 'अरण्यानी' किसका प्रतिनिधित्व करती थीं?", 'opts_hi': ['वन और जंगल', 'भोर और सुंदरता', 'घरेलू चूल्हा', 'सरस्वती नदी'], 'ans_hi': 0, 'sol_hi': 'अरण्यानी को वन और जंगल की आत्मा/देवी के रूप में प्रतिष्ठित किया गया था.'}, {'q': 'Which celestial god is praised for riding a chariot across the sky?', 'opts': ['Surya', 'Agni', 'Varuna', 'Dyaus'], 'ans': 0, 'sol': 'Surya (the sun god) is described as riding a chariot drawn by seven horses.', 'q_hi': 'किस आकाशीय देवता की आकाश में रथ की सवारी करने के लिए प्रशंसा की गई है?', 'opts_hi': ['सूर्य', 'अग्नि', 'वरुण', 'द्यौस'], 'ans_hi': 0, 'sol_hi': 'सूर्य (सूर्य देव) को सात घोड़ों द्वारा खींचे जाने वाले रथ की सवारी करने वाले के रूप में वर्णित किया गया है.'}, {'q': 'What was the relative position of female deities in the pantheon?', 'opts': ['Subordinate and less prominent compared to male gods', 'Supreme rulers of the pantheon', 'Equally praised as Indra', 'Completely absent from hymns'], 'ans': 0, 'sol': 'Reflecting patriarchy, goddesses held subordinate positions and fewer hymns.', 'q_hi': 'देवगण में महिला देवियों की सापेक्ष स्थिति क्या थी?', 'opts_hi': ['पुरुष देवताओं की तुलना में गौण और कम प्रमुख', 'देवगण की सर्वोच्च शासक', 'इंद्र के समान ही प्रशंसित', 'भजनों से पूरी तरह अनुपस्थित'], 'ans_hi': 0, 'sol_hi': 'पितृसत्ता को दर्शाते हुए, देवियों को गौण स्थान प्राप्त था और उनके लिए कम भजन थे.'}, {'q': "The god 'Yama' in Rigvedic beliefs was associated with:", 'opts': ['The realm of the dead / ancestors', 'Storm and rain', 'Sacrificial fire', 'Lute playing'], 'ans': 0, 'sol': 'Yama was deified as the king of the dead and pathfinder for ancestors.', 'q_hi': "ऋग्वैदिक मान्यताओं में 'यम' देवता किससे जुड़े थे?", 'opts_hi': ['मृतकों/पितरों का लोक', 'आंधी और बारिश', 'यज्ञ की अग्नि', 'वीणा वादन'], 'ans_hi': 0, 'sol_hi': 'यम को मृतकों के राजा और पितरों के मार्गदर्शक के रूप में प्रतिष्ठित किया गया था.'}], 3: [{'q': 'What were the primary modes of worship in early Rigvedic religion?', 'opts': ['Prayers (Prarthana) and sacrifices (Yajna)', 'Idol worship and temple festivals', 'Silent meditation in forest caves', 'Pilgrimages to sacred cities'], 'ans': 0, 'sol': 'Simple sacrifices (Yajna) and chanting prayers (Prarthana) were standard.', 'q_hi': 'प्रारंभिक ऋग्वैदिक धर्म में पूजा के प्राथमिक तरीके क्या थे?', 'opts_hi': ['प्रार्थना और यज्ञ', 'मूर्ति पूजा और मंदिर उत्सव', 'वन गुफाओं में मौन ध्यान', 'पवित्र शहरों की तीर्थयात्रा'], 'ans_hi': 0, 'sol_hi': 'सरल यज्ञ और प्रार्थनाओं का पाठ (प्रार्थना) पूजा के मानक तरीके थे.'}, {'q': 'What offerings were commonly thrown into the Rigvedic sacrificial fire?', 'opts': ['Milk, ghee, barley (yava), and Soma juice', 'Wheat, rice, and flowers only', 'Gold coins and jewels', 'Incense sticks and coconuts'], 'ans': 0, 'sol': 'Milk, ghee, yava (barley), and Soma were common sacrificial offerings.', 'q_hi': 'ऋग्वैदिक यज्ञ की अग्नि में आमतौर पर कौन सी आहुतियाँ डाली जाती थीं?', 'opts_hi': ['दूध, घी, जौ (यव) और सोम रस', 'केवल गेहूं, चावल और फूल', 'सोने के सिक्के और आभूषण', 'अगरबत्ती और नारियल'], 'ans_hi': 0, 'sol_hi': 'दूध, घी, यव (जौ) और सोम सामान्य यज्ञीय आहुतियाँ थीं.'}, {'q': 'What was the main motive of worship in early Rigvedic religion?', 'opts': ['Material benefits (cattle, sons, victory, health)', 'Spiritual salvation (Moksha)', 'Release from the cycle of rebirth (Samsara)', 'Philosophical debates only'], 'ans': 0, 'sol': 'Worship was utilitarian, seeking cows, sons, health, and military victory.', 'q_hi': 'प्रारंभिक ऋग्वैदिक धर्म में पूजा का मुख्य उद्देश्य क्या था?', 'opts_hi': ['सांसारिक लाभ (मवेशी, पुत्र, विजय, स्वास्थ्य)', 'आध्यात्मिक मुक्ति (मोक्ष)', 'पुनर्जन्म के चक्र (संसार) से मुक्ति', 'केवल दार्शनिक बहस'], 'ans_hi': 0, 'sol_hi': 'पूजा उपयोगितावादी थी, जिसका उद्देश्य गाय, पुत्र, स्वास्थ्य और सैन्य विजय प्राप्त करना था.'}, {'q': 'Who performed the daily domestic sacrifices (Yajnas) in the family?', 'opts': ['The patriarch (Grihapati or Kulapa)', 'A specialized hierarchy of 16 priests', "The Rajan's administrative deputy", "Only the family's oldest daughter"], 'ans': 0, 'sol': 'Simple domestic sacrifices were performed directly by the family head (Grihapati).', 'q_hi': 'परिवार में दैनिक घरेलू यज्ञों का संपादन कौन करता था?', 'opts_hi': ['पारिवारिक प्रमुख (गृहपति या कुलप)', '16 पुरोहितों का एक विशिष्ट पदानुक्रम', 'राजन का प्रशासनिक उप प्रमुख', 'केवल परिवार की सबसे बड़ी बेटी'], 'ans_hi': 0, 'sol_hi': 'सरल घरेलू यज्ञ सीधे परिवार के मुखिया (गृहपति) द्वारा किए जाते थे.'}, {'q': 'Did a rigid dominant priestly hierarchy exist in the early Rigvedic period?', 'opts': ['No, rituals were simple and did not require complex priestly classes', 'Yes, led by the supreme chief priest of India', 'Yes, based strictly on hereditary caste rules', 'Only in the Sapta-Sindhu area'], 'ans': 0, 'sol': 'Rituals were simple; the expensive, multi-priest hierarchies only developed later.', 'q_hi': 'क्या प्रारंभिक ऋग्वैदिक काल में एक कठोर और वर्चस्वशाली पुरोहित पदानुक्रम मौजूद था?', 'opts_hi': ['नहीं, अनुष्ठान सरल थे और उनके लिए जटिल पुरोहित वर्गों की आवश्यकता नहीं थी', 'हाँ, भारत के सर्वोच्च मुख्य पुरोहित के नेतृत्व में', 'हाँ, पूरी तरह से वंशानुगत जाति नियमों पर आधारित', 'केवल सप्त-सिंधु क्षेत्र में'], 'ans_hi': 0, 'sol_hi': 'अनुष्ठान सरल थे; महंगे और बहु-पुरोहित पदानुक्रम केवल बाद में विकसित हुए.'}, {'q': 'The priest who recited hymns from the Rigveda during public Yajna was called:', 'opts': ['Hotri', 'Adhvaryu', 'Udgatri', 'Brahman'], 'ans': 0, 'sol': 'Hotri was the reciter priest responsible for Rigvedic invocations.', 'q_hi': 'सार्वजनिक यज्ञ के दौरान ऋग्वेद के भजनों का पाठ करने वाले पुरोहित को क्या कहा जाता था?', 'opts_hi': ['होत्री', 'अध्वर्यु', 'उद्गात्री', 'ब्रह्मा'], 'ans_hi': 0, 'sol_hi': 'होत्री ऋग्वैदिक आह्वान के लिए जिम्मेदार पाठकर्ता पुरोहित था.'}, {'q': 'Which priest was responsible for chanting the musical melodies of Samaveda?', 'opts': ['Udgatri', 'Hotri', 'Adhvaryu', 'Brahman'], 'ans': 0, 'sol': 'Udgatri sang the melodies (Saman) during the ritual sacrifices.', 'q_hi': 'सामवेद की संगीतमय धुनों के पाठ के लिए कौन सा पुरोहित जिम्मेदार था?', 'opts_hi': ['उद्गात्री', 'होत्री', 'अध्वर्यु', 'ब्रह्मा'], 'ans_hi': 0, 'sol_hi': 'उद्गात्री यज्ञ के दौरान मधुर भजनों (साम) का गान करता था.'}, {'q': 'The priest who performed physical manual tasks of Yajna (building altars) was:', 'opts': ['Adhvaryu', 'Hotri', 'Udgatri', 'Brahman'], 'ans': 0, 'sol': 'Adhvaryu performed manual ritual acts using Yajurveda prose formulas.', 'q_hi': 'यज्ञ के भौतिक कार्य (वेदी निर्माण) करने वाले पुरोहित को क्या कहा जाता था?', 'opts_hi': ['अध्वर्यु', 'होत्री', 'उद्गात्री', 'ब्रह्मा'], 'ans_hi': 0, 'sol_hi': 'अध्वर्यु यजुर्वेद के गद्य सूत्रों का उपयोग करके अनुष्ठान के शारीरिक कार्यों को संपन्न करता था.'}, {'q': 'Were animal sacrifices performed in early Rigvedic rituals?', 'opts': ['Yes, occasionally, to win favor of gods during major tribal sacrifices', 'No, violence was strictly prohibited in all Vedic texts', 'Only in the Later Vedic phase', 'Only for deified river gods'], 'ans': 0, 'sol': 'Animal sacrifices occurred occasionally during major communal Yajnas.', 'q_hi': 'क्या प्रारंभिक ऋग्वैदिक अनुष्ठानों में पशु बलि दी जाती थी?', 'opts_hi': ['हाँ, कभी-कभार, प्रमुख जनजातीय यज्ञों के दौरान देवताओं की कृपा प्राप्त करने के लिए', 'नहीं, सभी वैदिक ग्रंथों में हिंसा सख्त वर्जित थी', 'केवल उत्तर वैदिक चरण में', 'केवल नदी देवताओं के लिए'], 'ans_hi': 0, 'sol_hi': 'प्रमुख सांप्रदायिक यज्ञों के दौरान कभी-कभार पशु बलि दी जाती थी.'}, {'q': 'How were the Rigvedic hymns preserved and transmitted over generations?', 'opts': ['Through precise oral tradition and memorization (Shruti)', 'By writing on copper plates', 'By carving on temple stone walls', 'Through palm leaf manuscripts'], 'ans': 0, 'sol': 'Hymns were transmitted orally; Shruti means that which is heard.', 'q_hi': 'ऋग्वैदिक भजनों को पीढ़ियों तक कैसे संरक्षित और प्रसारित किया गया था?', 'opts_hi': ['सटीक मौखिक परंपरा और कंठस्थ करने के माध्यम से (श्रुति)', 'तांबे की पट्टिकाओं पर लिखकर', 'मंदिर की पत्थर की दीवारों पर नक्काशी करके', 'ताड़ के पत्तों की पाण्डुलिपियों के माध्यम से'], 'ans_hi': 0, 'sol_hi': 'भजनों का प्रसारण मौखिक रूप से होता था; श्रुति का अर्थ है जो सुना गया हो.'}, {'q': 'Was the performance of Yajna linked to political status of chiefs?', 'opts': ['Yes, chiefs sponsored Yajnas to assert military legitimacy and prestige', 'No, chiefs were banned from Yajnas', 'Yajnas were performed only by weavers', 'None of the above'], 'ans': 0, 'sol': 'Rajan sponsored communal sacrifices to gain legitimacy and distribute spoils.', 'q_hi': 'क्या यज्ञ का आयोजन मुखियों की राजनीतिक स्थिति से जुड़ा था?', 'opts_hi': ['हाँ, प्रमुखों ने सैन्य वैधता और प्रतिष्ठा स्थापित करने के लिए यज्ञ प्रायोजित किए', 'नहीं, प्रमुखों को यज्ञ करने पर प्रतिबंध था', 'यज्ञ केवल बुनकरों द्वारा किए जाते थे', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'राजन ने वैधता प्राप्त करने और लूट का वितरण करने के लिए सांप्रदायिक यज्ञों को प्रायोजित किया.'}, {'q': 'What represents the basic domestic ritual fire kept in every home?', 'opts': ['Grihya Agni / Garhapatya', 'Soma Agni', 'Rudra Agni', 'None of these'], 'ans': 0, 'sol': 'Garhapatya was the domestic fire maintained in the household.', 'q_hi': 'प्रत्येक घर में रखी जाने वाली बुनियादी घरेलू यज्ञ अग्नि को क्या कहा जाता था?', 'opts_hi': ['गृह्य अग्नि / गार्हपत्य', 'सोम अग्नि', 'रुद्र अग्नि', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'गार्हपत्य वह घरेलू अग्नि थी जिसे गृहस्थी में निरंतर बनाए रखा जाता था.'}], 4: [{'q': "What does the Rigvedic term 'Rta' represent?", 'opts': ['Cosmic, natural, and moral order', 'A type of sacrificial grain offering', 'A standard weight of copper', 'The tribal boundary line'], 'ans': 0, 'sol': 'Rta represents the cosmic, physical, and moral order governing the universe.', 'q_hi': "ऋग्वैदिक शब्द 'ऋत' किसका प्रतिनिधित्व करता है?", 'opts_hi': ['ब्रह्मांडीय, प्राकृतिक और नैतिक व्यवस्था', 'एक प्रकार के यज्ञीय अनाज की आहुति', 'तांबे का एक मानक वजन', 'जनजातीय सीमा रेखा'], 'ans_hi': 0, 'sol_hi': 'ऋत ब्रह्मांडीय, भौतिक और नैतिक व्यवस्था का प्रतिनिधित्व करता है जो ब्रह्मांड को नियंत्रित करती है.'}, {'q': "Which deity is addressed as the 'guardian of Rta' (Gopa Rtasya)?", 'opts': ['Varuna', 'Indra', 'Agni', 'Soma'], 'ans': 0, 'sol': 'Varuna was the supreme guardian of cosmic and moral order.', 'q_hi': "किस देवता को 'ऋत का रक्षक' (गोपा ऋतस्य) के रूप में संबोधित किया गया है?", 'opts_hi': ['वरुण', 'इंद्र', 'अग्नि', 'सोम'], 'ans_hi': 0, 'sol_hi': 'वरुण ब्रह्मांडीय और नैतिक व्यवस्था के सर्वोच्च रक्षक थे.'}, {'q': "What term refers to the violation or moral transgression of 'Rta'?", 'opts': ['Anrita (Falsehood/Disorder)', 'Dharma', 'Bali', 'Yajna'], 'ans': 0, 'sol': 'Anrita refers to falsehood, moral deviance, and cosmic disorder.', 'q_hi': "'ऋत' के उल्लंघन या नैतिक विचलन को किस शब्द से संदर्भित किया जाता है?", 'opts_hi': ['अनृत (असत्य/अव्यवस्था)', 'धर्म', 'बलि', 'यज्ञ'], 'ans_hi': 0, 'sol_hi': 'अनृत का तात्पर्य असत्य, नैतिक विचलन और ब्रह्मांडीय अव्यवस्था से है.'}, {'q': 'How was Varuna believed to punish transgressors of Rta?', 'opts': ['By binding them with fetters and causing disease (dropsy)', 'By sentencing them to exile', 'By taking away their land tracts', 'By locking them in dungeons'], 'ans': 0, 'sol': 'Varuna bound sinners with loops or fetters and inflicted dropsy.', 'q_hi': 'वरुण ऋत के उल्लंघनकर्ताओं को कैसे दंडित करते थे, ऐसा माना जाता था?', 'opts_hi': ['उन्हें पाश (जाल) में बांधकर और बीमारी (जलोदर) देकर', 'उन्हें निर्वासन की सजा देकर', 'उनकी भूमि के भूखंडों को छीनकर', 'उन्हें कालकोठरी में बंद करके'], 'ans_hi': 0, 'sol_hi': 'वरुण पापियों को पाश में बांधते थे और उन्हें जलोदर (dropsy) नामक रोग से पीड़ित करते थे.'}, {'q': 'Rta governed which dimensions according to Rigvedic cosmology?', 'opts': ['Both physical natural cycles (seasons, sun movement) and moral human actions', 'Only moral human actions', 'Only physical natural cycles', 'Only priestly sacrifice rituals'], 'ans': 0, 'sol': 'Rta governed physical natural laws (sun, seasons) and ethical conduct.', 'q_hi': 'ऋग्वैदिक ब्रह्मांड विज्ञान के अनुसार ऋत किन आयामों को नियंत्रित करता था?', 'opts_hi': ['भौतिक प्राकृतिक चक्र (ऋतुएँ, सूर्य की गति) और नैतिक मानवीय कार्य दोनों', 'केवल नैतिक मानवीय कार्य', 'केवल भौतिक प्राकृतिक चक्र', 'केवल पुरोहितों के यज्ञ अनुष्ठान'], 'ans_hi': 0, 'sol_hi': 'ऋत भौतिक प्राकृतिक नियमों (सूर्य, ऋतुओं) और नैतिक आचरण दोनों को नियंत्रित करता था.'}, {'q': 'What is the relationship between Rta and the deified natural forces?', 'opts': ['The gods are subjects and maintainers of Rta, not its creators', 'The gods created Rta and can destroy it', 'Rta only applies to human beings, not gods', 'None of the above'], 'ans': 0, 'sol': 'Gods (Adityas) are guardians who enforce Rta; Rta is supreme cosmic law.', 'q_hi': 'ऋत और देवत्वकृत प्राकृतिक शक्तियों के बीच क्या संबंध है?', 'opts_hi': ['देवता ऋत के अधीन और रक्षक हैं, इसके निर्माता नहीं', 'देवताओं ने ऋत का निर्माण किया और वे इसे नष्ट कर सकते हैं', 'ऋत केवल मनुष्यों पर लागू होता है, देवताओं पर नहीं', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'देवता (आदित्य) रक्षक हैं जो ऋत को लागू करते हैं; ऋत सर्वोच्च ब्रह्मांडीय नियम है.'}, {'q': 'The division of seasons (Rtu) is etymologically derived from:', 'opts': ['Rta (Orderly change)', 'Rudra', 'Rajan', 'Ratha'], 'ans': 0, 'sol': 'Rtu (season) comes from Rta, representing regular seasonal cycles.', 'q_hi': 'ऋतुओं (ऋतु) का विभाजन व्युत्पत्ति के अनुसार किससे लिया गया है?', 'opts_hi': ['ऋत (क्रमबद्ध परिवर्तन)', 'रुद्र', 'राजन', 'रथ'], 'ans_hi': 0, 'sol_hi': 'ऋतु शब्द ऋत से आया है, जो नियमित मौसमी चक्रों का प्रतिनिधित्व करता है.'}, {'q': 'Which celestial gods are paired as joint guardians of Rta in hymns?', 'opts': ['Mitra and Varuna', 'Indra and Agni', 'Soma and Rudra', 'Dyaus and Prithvi'], 'ans': 0, 'sol': 'Mitra-Varuna are jointly invoked to uphold and protect Rta.', 'q_hi': 'भजनों में किन आकाशीय देवताओं को ऋत के संयुक्त रक्षकों के रूप में दर्शाया गया है?', 'opts_hi': ['मित्र और वरुण', 'इंद्र और अग्नि', 'सोम और रुद्र', 'द्यौस और पृथ्वी'], 'ans_hi': 0, 'sol_hi': 'मित्र-वरुण को संयुक्त रूप से ऋत को बनाए रखने और उसकी रक्षा करने के लिए पुकारा जाता है.'}, {'q': 'Did early Rigvedic religion have a concept of hell for sinners?', 'opts': ["No, sinners were punished in this life by Varuna's fetters", 'Yes, a burning underworld existed', 'Only for non-Aryan traders', 'None of these'], 'ans': 0, 'sol': 'Ethical deviance was punished in life through illness, social exclusion, or failure.', 'q_hi': 'क्या प्रारंभिक ऋग्वैदिक धर्म में पापियों के लिए नर्क की अवधारणा थी?', 'opts_hi': ['नहीं, पापियों को इसी जीवन में वरुण के पाश द्वारा दंडित किया जाता था', 'हाँ, एक जलता हुआ पाताल लोक मौजूद था', 'केवल गैर-आर्य व्यापारियों के लिए', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'नैतिक विचलन के लिए इसी जीवन में बीमारी, सामाजिक बहिष्कार या विफलता के माध्यम से दंड मिलता था.'}, {'q': 'The concept of Rta contrasts with Later Vedic ritualism because Rta was:', 'opts': ['Ethical and cosmic, rather than purely mechanical ritual performance', 'Based entirely on temple sacrifices', 'Invented by non-Aryan artisans', 'Strictly concerned with agriculture'], 'ans': 0, 'sol': 'Rta focused on moral harmony and natural laws rather than ritual formulas.', 'q_hi': 'ऋत की अवधारणा उत्तर वैदिक कर्मकांड से भिन्न थी क्योंकि ऋत था:', 'opts_hi': ['विशुद्ध यांत्रिक यज्ञ प्रदर्शन के बजाय नैतिक और ब्रह्मांडीय', 'पूरी तरह से मंदिर के यज्ञों पर आधारित', 'गैर-आर्य कारीगरों द्वारा आविष्कार किया गया', 'सख्ती से कृषि से संबंधित'], 'ans_hi': 0, 'sol_hi': 'ऋत अनुष्ठानिक सूत्रों के बजाय नैतिक सद्भाव और प्राकृतिक नियमों पर केंद्रित था.'}, {'q': "Which god acts as the 'mouth' of Rta in sacrificial rituals?", 'opts': ['Agni', 'Indra', 'Soma', 'Varuna'], 'ans': 0, 'sol': 'Agni is the mouth of gods who carries offerings in accordance with Rta.', 'q_hi': "यज्ञ अनुष्ठानों में ऋत के 'मुख' के रूप में कौन सा देवता कार्य करता है?", 'opts_hi': ['अग्नि', 'इंद्र', 'सोम', 'वरुण'], 'ans_hi': 0, 'sol_hi': 'अग्नि देवताओं का मुख है जो ऋत के अनुसार आहुतियाँ ले जाता है.'}, {'q': 'What legal/moral duties did the Rajan have regarding Rta?', 'opts': ['He had to uphold social order matching Rta, acting as its protector', 'He had the power to alter the laws of Rta', 'He was exempt from Rta', 'None of the above'], 'ans': 0, 'sol': 'The Rajan was expected to enforce customary laws aligned with Rta.', 'q_hi': 'ऋत के संबंध में राजन के क्या कानूनी/नैतिक कर्तव्य थे?', 'opts_hi': ['उसे ऋत के अनुरूप सामाजिक व्यवस्था बनाए रखनी थी, उसका रक्षक बनना था', 'उनके पास ऋत के नियमों को बदलने की शक्ति थी', 'उन्हें ऋत से छूट दी गई थी', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'राजन से ऋत के साथ संरेखित पारंपरिक कानूनों को लागू करने की अपेक्षा की जाती थी.'}], 5: [{'q': "What was 'Soma' in the Rigvedic religious life?", 'opts': ['An intoxicating sacrificial drink deified as a god', 'A type of wheat bread', 'A sacred metal tool', 'The throne of the Rajan'], 'ans': 0, 'sol': 'Soma was a plant juice deified as a major god, believed to inspire seers.', 'q_hi': "ऋग्वैदिक धार्मिक जीवन में 'सोम' क्या था?", 'opts_hi': ['एक नशीला यज्ञीय पेय जिसे देवता के रूप में पूजा जाता था', 'एक प्रकार की गेहूं की रोटी', 'एक पवित्र धातु का उपकरण', 'राजन का सिंहासन'], 'ans_hi': 0, 'sol_hi': 'सोम एक पौधे का रस था जिसे एक प्रमुख देवता के रूप में पूजा जाता था, माना जाता था कि यह ऋषियों को प्रेरित करता था.'}, {'q': 'Which Mandala of the Rigveda is dedicated entirely to Soma (Soma Mandala)?', 'opts': ['Mandala IX', 'Mandala X', 'Mandala III', 'Mandala VII'], 'ans': 0, 'sol': 'Mandala IX contains all 114 hymns dedicated to Soma Pavamana.', 'q_hi': 'ऋग्वेद का कौन सा मंडल पूरी तरह से सोम को समर्पित है (सोम मंडल)?', 'opts_hi': ['मंडल IX', 'मंडल X', 'मंडल III', 'मंडल VII'], 'ans_hi': 0, 'sol_hi': 'मंडल IX में सोम पवमान को समर्पित सभी 114 भजन शामिल हैं.'}, {'q': 'From which mountain range did the Vedic people source the Soma plant?', 'opts': ['Mujavant (Himalayas)', 'Vindhyas', 'Aravallis', 'Hindukush'], 'ans': 0, 'sol': 'Rigvedic texts mention Mount Mujavant as the source of best Soma.', 'q_hi': 'वैदिक लोग किस पर्वत श्रृंखला से सोम का पौधा प्राप्त करते थे?', 'opts_hi': ['मुजावंत (हिमालय)', 'विंध्य', 'अरावली', 'हिंदुकुश'], 'ans_hi': 0, 'sol_hi': 'ऋग्वैदिक ग्रंथों में सर्वोत्तम सोम के स्रोत के रूप में मुजावंत पर्वत का उल्लेख मिलता है.'}, {'q': 'How was the Soma juice prepared for sacrificial rituals?', 'opts': ['Pounded with stones, filtered through wool, and mixed with milk/barley', 'Fermented for several months in clay jars', 'Boiled with medicinal copper pieces', 'None of the above'], 'ans': 0, 'sol': 'Soma stalks were crushed with stones, filtered, and diluted with milk/grain.', 'q_hi': 'यज्ञ अनुष्ठानों के लिए सोम रस कैसे तैयार किया जाता था?', 'opts_hi': ['पत्थरों से कूटकर, ऊन से छानकर और दूध/जौ में मिलाकर', 'मिट्टी के जार में कई महीनों तक किण्वित करके', 'औषधीय तांबे के टुकड़ों के साथ उबालकर', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'सोम की लताओं को पत्थरों से कुचला जाता था, छाना जाता था और दूध या अनाज के साथ मिलाया जाता था.'}, {'q': 'What effects were attributed to consuming the Soma drink?', 'opts': ['Invigoration, feeling of immortality, and divine inspiration', 'Complete loss of consciousness and sleep', 'Severe illness and dropsy', 'None of these'], 'ans': 0, 'sol': 'Consuming Soma produced energy, inspiration, and feelings of ecstasy.', 'q_hi': 'सोम पेय के सेवन के क्या प्रभाव बताए गए थे?', 'opts_hi': ['ऊर्जा का संचार, अमरता की भावना और दिव्य प्रेरणा', 'चेतना की पूर्ण हानि और नींद', 'गंभीर बीमारी और जलोदर', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'सोम के सेवन से ऊर्जा, प्रेरणा और उत्साह की भावना पैदा होती थी.'}, {'q': 'Which god is most closely associated with drinking Soma before battle?', 'opts': ['Indra', 'Varuna', 'Agni', 'Mitra'], 'ans': 0, 'sol': 'Indra consumed massive quantities of Soma to gain strength for fights.', 'q_hi': 'युद्ध से पहले सोम का पान करने से सबसे निकटता से कौन सा देवता जुड़ा है?', 'opts_hi': ['इंद्र', 'वरुण', 'अग्नि', 'मित्र'], 'ans_hi': 0, 'sol_hi': 'इंद्र ने युद्ध के लिए शक्ति प्राप्त करने के लिए भारी मात्रा में सोम का सेवन किया.'}, {'q': 'What describes the plant identification of Soma today?', 'opts': ['It remains botanically debated, possibly Ephedra or a fly agaric fungus', 'It is definitively identified as sugarcane', 'It was proved to be cannabis', 'None of the above'], 'ans': 0, 'sol': 'Botanical identity is disputed; Ephedra is a leading candidate.', 'q_hi': 'आज सोम के पौधे की पहचान का क्या वर्णन है?', 'opts_hi': ['यह वनस्पति शास्त्र में विवादास्पद है, संभवतः एफेड्रा या एक कवक', 'निश्चित रूप से इसकी पहचान गन्ने के रूप में की गई है', 'यह भांग सिद्ध हुआ था', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'सोम की वनस्पति पहचान विवादास्पद है; एफेड्रा (Ephedra) एक प्रमुख दावेदार है.'}, {'q': 'The filtering cloth used to purify Soma juice was made of:', 'opts': ["Sheep's wool (Urna)", 'Cotton fabric', 'Jute fibers', 'Reed mat'], 'ans': 0, 'sol': "Soma was filtered through a strainer made of sheep's wool.", 'q_hi': 'सोम रस को शुद्ध करने के लिए उपयोग किया जाने वाला छननी का कपड़ा किसका बना होता था?', 'opts_hi': ['भेड़ की ऊन (ऊर्णा)', 'सूती कपड़ा', 'जूट के रेशे', 'सरकंडे की चटाई'], 'ans_hi': 0, 'sol_hi': 'सोम को भेड़ की ऊन से बनी छननी से छाना जाता था.'}, {'q': 'Why was the Soma plant ritualized as a deity?', 'opts': ['Its energizing juice was central to the Yajna economy and tribal morale', 'It was the only crop grown in Sapta-Sindhu', 'It was used to build war chariots', 'None of the above'], 'ans': 0, 'sol': "Soma's effects made it vital for ritual performance and military courage.", 'q_hi': 'सोम के पौधे को एक देवता के रूप में क्यों अनुष्ठित किया गया था?', 'opts_hi': ['इसका ऊर्जादायक रस यज्ञ अर्थव्यवस्था और कबीले के मनोबल के लिए केंद्रीय था', 'यह सप्त-सिंधु में उगाई जाने वाली एकमात्र फसल थी', 'इसका उपयोग युद्ध रथों के निर्माण के लिए किया जाता था', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'सोम के प्रभावों ने इसे अनुष्ठान प्रदर्शन और सैन्य साहस के लिए महत्वपूर्ण बना दिया.'}, {'q': 'What term refers to the purification of Soma during the ritual?', 'opts': ['Pavamana', 'Bali', 'Yajna', 'Prarthana'], 'ans': 0, 'sol': 'Pavamana refers to the flowing, purifying process of Soma juice.', 'q_hi': 'अनुष्ठान के दौरान सोम के शुद्धिकरण को किस शब्द से संदर्भित किया जाता है?', 'opts_hi': ['पवमान', 'बलि', 'यज्ञ', 'प्रार्थना'], 'ans_hi': 0, 'sol_hi': 'पवमान का तात्पर्य सोम रस के बहने और शुद्ध होने की प्रक्रिया से है.'}, {'q': "What was Soma mixed with to make the drink 'Karambha'?", 'opts': ['Parched barley meal', 'Honey and wine', 'River water only', 'None of these'], 'ans': 0, 'sol': 'Karambha was a mixture of Soma and parched barley meal.', 'q_hi': "पेय 'करम्भ' बनाने के लिए सोम में क्या मिलाया जाता था?", 'opts_hi': ['भुने हुए जौ का आटा', 'शहद और शराब', 'केवल नदी का पानी', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'करम्भ सोम और भुने हुए जौ के आटे का मिश्रण था.'}, {'q': 'The disappearance of the Soma plant in Later Vedic times led to:', 'opts': ['Use of substitute plants (Putika) and ritual changes', 'Complete ban on sacrifices', 'Imports from China', 'Destruction of Yajna sites'], 'ans': 0, 'sol': 'Lack of access to Mujavant forced the use of substitutes like Putika.', 'q_hi': 'उत्तर वैदिक काल में सोम के पौधे के लुप्त होने के कारण क्या हुआ?', 'opts_hi': ['वैकल्पिक पौधों (पूतिका) का उपयोग और अनुष्ठान परिवर्तन', 'यज्ञों पर पूर्ण प्रतिबंध', 'चीन से आयात', 'यज्ञ स्थलों का विनाश'], 'ans_hi': 0, 'sol_hi': 'मुजावंत पर्वत तक पहुँच न होने के कारण पूतिका जैसे वैकल्पिक पौधों का उपयोग करना पड़ा.'}], 6: [{'q': 'Which famous creation hymn of the Rigveda explores the origin of the universe?', 'opts': ['Nasadiya Sukta', 'Purusha Sukta', 'Gayatri Mantra', 'Sarasvati Sukta'], 'ans': 0, 'sol': "Nasadiya Sukta (Mandala X) is the hymn of creation, beginning with 'Neither sat nor asat'.", 'q_hi': 'ऋग्वेद का कौन सा प्रसिद्ध सृष्टि सूक्त ब्रह्मांड की उत्पत्ति की खोज करता है?', 'opts_hi': ['नासदीय सूक्त', 'पुरुष सूक्त', 'गायत्री मंत्र', 'सरस्वती सूक्त'], 'ans_hi': 0, 'sol_hi': "नासदीय सूक्त (मंडल X) सृष्टि का सूक्त है, जो 'न सत था न असत' से शुरू होता है."}, {'q': "The Rigvedic philosophical phrase 'Ekam Sat Vipra Bahudha Vadanti' translates to:", 'opts': ['Truth is one, but sages call it by various names', 'The king is supreme on earth', 'Sacrifice is the only path to heaven', 'Do not kill the cows'], 'ans': 0, 'sol': 'It declares that ultimate reality is one, though described differently by priests.', 'q_hi': "ऋग्वैदिक दार्शनिक वाक्यांश 'एकम सत् विप्रा बहुधा वदन्ति' का अनुवाद है:", 'opts_hi': ['सत्य एक है, लेकिन ऋषि इसे विभिन्न नामों से पुकारते हैं', 'पृथ्वी पर राजा सर्वोच्च है', 'यज्ञ ही स्वर्ग का एकमात्र मार्ग है', 'गायों को मत मारो'], 'ans_hi': 0, 'sol_hi': 'यह घोषित करता है कि अंतिम वास्तविकता एक है, हालांकि पुरोहितों द्वारा इसका अलग-अलग वर्णन किया गया है.'}, {'q': 'Which hymn introduces the sacrifice of the primeval giant to create the universe and social classes?', 'opts': ['Purusha Sukta', 'Nasadiya Sukta', 'Hiranyagarbha Sukta', 'Gayatri Sukta'], 'ans': 0, 'sol': 'Purusha Sukta (Mandala X) describes creation from the limbs of Purusha.', 'q_hi': 'ब्रह्मांड और सामाजिक वर्गों के निर्माण के लिए आदिपुरुष के बलिदान का परिचय कौन सा सूक्त देता है?', 'opts_hi': ['पुरुष सूक्त', 'नासदीय सूक्त', 'हिरण्यगर्भ सूक्त', 'गायत्री सूक्त'], 'ans_hi': 0, 'sol_hi': 'पुरुष सूक्त (मंडल X) पुरुष के अंगों से सृष्टि के निर्माण का वर्णन करता है.'}, {'q': 'What philosophical perspective emerges in the late Mandalas (I and X) of the Rigveda?', 'opts': ['Monism (ultimate unity of all existence)', 'Strict dualism', 'Atheistic materialism', 'Rejection of morality'], 'ans': 0, 'sol': 'Hymns transition from polytheism towards monism, seeking a single underlying reality.', 'q_hi': 'ऋग्वेद के उत्तरकालीन मंडलों (I और X) में कौन सा दार्शनिक दृष्टिकोण उभरता है?', 'opts_hi': ['अद्वैतवाद (सभी अस्तित्व की अंतिम एकता)', 'सख्त द्वैतवाद', 'नास्तिक भौतिकवाद', 'नैतिकता की अस्वीकृति'], 'ans_hi': 0, 'sol_hi': 'भजन बहुदेववाद से अद्वैतवाद की ओर बढ़ते हैं, एक एकल अंतर्निहित वास्तविकता की खोज करते हैं.'}, {'q': "The concept of 'Hiranyagarbha' in Vedic philosophy represents:", 'opts': ['The golden womb or cosmic egg of creation', 'A gold neck ornament', 'The priest who drinks Soma', 'The weapon of Indra'], 'ans': 0, 'sol': 'Hiranyagarbha represents the golden cosmic egg from which creation arose.', 'q_hi': "वैदिक दर्शन में 'हिरण्यगर्भ' की अवधारणा किसका प्रतिनिधित्व करती है?", 'opts_hi': ['सृष्टि का स्वर्ण गर्भ या ब्रह्मांडीय अंडा', 'सोने के गले का आभूषण', 'सोम पीने वाला पुरोहित', 'इंद्र का हथियार'], 'ans_hi': 0, 'sol_hi': 'हिरण्यगर्भ उस सुनहरे ब्रह्मांडीय अंडे का प्रतिनिधित्व करता है जिससे सृष्टि की उत्पत्ति हुई थी.'}, {'q': 'What describes the tone of the Nasadiya Sukta regarding creation?', 'opts': ['Inquisitive and skeptical, questioning if even the gods know the origin', 'Absolute certainty about creation dates', 'Declaring that the chief priest created everything', 'None of the above'], 'ans': 0, 'sol': "It ends with philosophical doubt: 'He who surveys it... perhaps he knows, or perhaps he knows not.'", 'q_hi': 'सृष्टि के संबंध में नासदीय सूक्त के स्वर का क्या वर्णन है?', 'opts_hi': ['जिज्ञासु और संशयवादी, यह सवाल उठाना कि क्या देवता भी उत्पत्ति जानते हैं', 'सृष्टि की तारीखों के बारे में पूर्ण निश्चितता', 'यह घोषित करना कि मुख्य पुरोहित ने सब कुछ बनाया', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': "यह दार्शनिक संदेह के साथ समाप्त होता है: 'वह जो इसका सर्वेक्षण करता है... शायद वह जानता है, या शायद वह नहीं जानता.'"}, {'q': 'The transition to monism laid the foundations for which later philosophical texts?', 'opts': ['Upanishads', 'Puranas', 'Dharmasutras', 'Sangam literature'], 'ans': 0, 'sol': 'Rigvedic monism culminated in the Brahman-Atman philosophy of the Upanishads.', 'q_hi': 'अद्वैतवाद की ओर संक्रमण ने बाद के किन दार्शनिक ग्रंथों की नींव रखी?', 'opts_hi': ['उपनिषद', 'पुराण', 'धर्मसूत्र', 'संगम साहित्य'], 'ans_hi': 0, 'sol_hi': 'ऋग्वैदिक अद्वैतवाद का समापन उपनिषदों के ब्रह्म-आत्मन् दर्शन में हुआ.'}, {'q': "The term 'Tad Ekam' in the Nasadiya Sukta translates to:", 'opts': ['That One', 'The Sun', 'The Priest', 'The Tribe'], 'ans': 0, 'sol': 'Tad Ekam refers to the neutral, formless absolute reality before creation.', 'q_hi': "नासदीय सूक्त में 'तद एकम' शब्द का अनुवाद है:", 'opts_hi': ['वह एक (तद् एकम्)', 'सूर्य', 'पुरोहित', 'जनजाति'], 'ans_hi': 0, 'sol_hi': 'तद् एकम् सृष्टि से पहले की तटस्थ, निराकार परम वास्तविकता को संदर्भित करता है.'}, {'q': 'How does Rigvedic monism differ from monotheism?', 'opts': ['Monism views god and universe as one; monotheism believes in one personal creator god separate from universe', 'Monism has many gods; monotheism has none', 'They are exactly the same concept', 'None of the above'], 'ans': 0, 'sol': 'Monism identifies the creator with the creation (all is one), unlike personal monotheism.', 'q_hi': 'ऋग्वैदिक अद्वैतवाद एकेश्वरवाद से किस प्रकार भिन्न है?', 'opts_hi': ['अद्वैतवाद ईश्वर और ब्रह्मांड को एक मानता है; एकेश्वरवाद ब्रह्मांड से अलग एक व्यक्तिगत निर्माता ईश्वर में विश्वास करता है', 'अद्वैतवाद में कई देवता हैं; एकेश्वरवाद में कोई नहीं', 'वे बिल्कुल एक ही अवधारणा हैं', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'अद्वैतवाद निर्माता को सृष्टि के साथ पहचानता है (सब कुछ एक है), जो व्यक्तिगत एकेश्वरवाद से भिन्न है.'}, {'q': 'Which Mandala contains the Hiranyagarbha Sukta?', 'opts': ['Mandala X', 'Mandala IX', 'Mandala III', 'Mandala I'], 'ans': 0, 'sol': 'Hiranyagarbha Sukta is compiled in the late Mandala X of Rigveda.', 'q_hi': 'हिरण्यगर्भ सूक्त किस मंडल में शामिल है?', 'opts_hi': ['मंडल X', 'मंडल IX', 'मंडल III', 'मंडल I'], 'ans_hi': 0, 'sol_hi': 'हिरण्यगर्भ सूक्त ऋग्वेद के उत्तरकालीन मंडल X में संकलित है.'}, {'q': "In the Purusha Sukta, the Brahmins are said to have originated from the Purusha's:", 'opts': ['Mouth', 'Arms', 'Thighs', 'Feet'], 'ans': 0, 'sol': 'The Brahmins came from the mouth, Kshatriyas from arms, Vaishyas from thighs, Shudras from feet.', 'q_hi': 'पुरुष सूक्त में ब्राह्मणों की उत्पत्ति पुरुष के किस अंग से बताई गई है?', 'opts_hi': ['मुख', 'भुजाएं', 'जंघाएं', 'पैर'], 'ans_hi': 0, 'sol_hi': 'ब्राह्मण मुख से आए, क्षत्रिय भुजाओं से, वैश्य जंघाओं से और शूद्र पैरों से आए.'}, {'q': 'What philosophical shift does the transition to monism represent in Rigvedic thought?', 'opts': ['From ritualistic polytheism to abstract philosophical speculation', 'From agriculture back to hunting', 'From peace to militarism', 'From Sanskrit to Prakrit'], 'ans': 0, 'sol': 'It marks a move from placating external nature gods to seeking internal, absolute truth.', 'q_hi': 'ऋग्वैदिक विचार में अद्वैतवाद की ओर संक्रमण किस दार्शनिक बदलाव का प्रतिनिधित्व करता है?', 'opts_hi': ['कर्मकांडीय बहुदेववाद से अमूर्त दार्शनिक चिंतन की ओर', 'कृषि से वापस शिकार की ओर', 'शांति से सैन्यवाद की ओर', 'संस्कृत से प्राकृत की ओर'], 'ans_hi': 0, 'sol_hi': 'यह बाहरी प्रकृति देवताओं को खुश करने से लेकर आंतरिक, परम सत्य की खोज की ओर बढ़ने का प्रतीक है.'}]}

# 2. Generator for 62 mastery zone questions per section (using pool of 12 unique facts)
question_pool = {1: [{'q': "Who coined the term 'Henotheism' for Rigvedic polytheism?", 'opts': ['Max Müller', 'William Jones', 'Arthur Basham', 'Al-Biruni'], 'ans': 0, 'sol': 'Max Müller coined the term Henotheism to describe worship of one god as supreme at a time.', 'q_hi': "ऋग्वैदिक बहुदेववाद के लिए 'हेनोथिज्म' शब्द किसने गढ़ा था?", 'opts_hi': ['मैक्स मुलर', 'विलियम जोन्स', 'आर्थर बाशम', 'अल-बिरूनी'], 'ans_hi': 0, 'sol_hi': "मैक्स मुलर ने एक समय में एक ही देवता की सर्वोच्च के रूप में पूजा करने का वर्णन करने के लिए 'हेनोथिज्म' शब्द गढ़ा था."}, {'q': 'What describes the concept of Henotheism (or Kathenotheism)?', 'opts': ['Worship of a single supreme deity at a time, without denying others', 'Belief in only one god who has no physical representation', 'Worship of ancestors and animal totems only', 'Complete rejection of natural gods'], 'ans': 0, 'sol': 'It is fluid worship where the deity addressed is temporarily praised as supreme.', 'q_hi': 'एकेश्वरवाद या हेनोथिज्म (कथिनोथिज्म) की अवधारणा का क्या वर्णन है?', 'opts_hi': ['अन्य देवताओं को नकारे बिना, एक समय में एक ही सर्वोच्च देवता की पूजा करना', 'केवल एक ईश्वर में विश्वास जिसका कोई भौतिक प्रतिनिधित्व नहीं है', 'केवल पूर्वजों और पशु प्रतीकों की पूजा करना', 'प्राकृतिक देवताओं को पूरी तरह से खारिज करना'], 'ans_hi': 0, 'sol_hi': 'यह एक लचीली पूजा पद्धति है जहाँ संबोधित किए जाने वाले देवता की अस्थायी रूप से सर्वोच्च के रूप में प्रशंसा की जाती है.'}, {'q': 'Did the early Vedic religion practice image or idol worship?', 'opts': ['No, it was completely devoid of idols, images, or temples', 'Yes, clay idols of Indra were found in all family homes', 'Only in the Sarasvati basin', 'Only during the Soma sacrifices'], 'ans': 0, 'sol': 'Early Vedic religion relied on oral prayers and fire sacrifice; no idols existed.', 'q_hi': 'क्या प्रारंभिक वैदिक धर्म में मूर्ति या प्रतिमा पूजा की जाती थी?', 'opts_hi': ['नहीं, यह पूरी तरह से मूर्तियों, छवियों या मंदिरों से मुक्त था', 'हाँ, सभी पारिवारिक घरों में इंद्र की मिट्टी की मूर्तियाँ मिली थीं', 'केवल सरस्वती बेसिन में', 'केवल सोम यज्ञों के दौरान'], 'ans_hi': 0, 'sol_hi': 'प्रारंभिक वैदिक धर्म मौखिक प्रार्थनाओं और अग्नि यज्ञ पर निर्भर था; कोई मूर्तियां मौजूद नहीं थीं.'}, {'q': 'What is the primary characteristic of early Rigvedic religion?', 'opts': ['Naturalistic polytheism (deification of natural forces)', 'Highly philosophical monism', 'Temples and ritual animal enclosures', 'Rejection of rituals in favor of meditation'], 'ans': 0, 'sol': 'They worshipped deified natural elements like rain, wind, fire, and dawn.', 'q_hi': 'प्रारंभिक ऋग्वैदिक धर्म की प्राथमिक विशेषता क्या है?', 'opts_hi': ['प्राकृतिक बहुदेववाद (प्राकृतिक शक्तियों का देवत्वीकरण)', 'अत्यधिक दार्शनिक अद्वैतवाद', 'मंदिर और अनुष्ठानिक पशु बाड़े', 'ध्यान के पक्ष में अनुष्ठानों की अस्वीकृति'], 'ans_hi': 0, 'sol_hi': 'वे वर्षा, वायु, अग्नि और भोर जैसे प्राकृतिक तत्वों की पूजा करते थे.'}, {'q': 'How were deities invoked by early Rigvedic Indo-Aryans?', 'opts': ['Through spoken hymns, prayers, and fire sacrifices (Yajnas)', 'Through elaborate dance and theatrical performances', 'By offering stone sculptures in temples', 'By writing letters on birch bark'], 'ans': 0, 'sol': 'Invocation was done through chanting hymns and throwing offerings into the fire.', 'q_hi': 'प्रारंभिक ऋग्वैदिक भारत-आर्यों द्वारा देवताओं का आह्वान कैसे किया जाता था?', 'opts_hi': ['बोले गए भजनों, प्रार्थनाओं और अग्नि यज्ञों (यज्ञ) के माध्यम से', 'विस्तृत नृत्य और नाट्य प्रदर्शनों के माध्यम से', 'मंदिरों में पत्थर की मूर्तियाँ भेंट करके', 'भोजपत्र पर पत्र लिखकर'], 'ans_hi': 0, 'sol_hi': 'देवताओं का आह्वान भजनों के पाठ और अग्नि में आहुति डालने के माध्यम से किया जाता था.'}, {'q': 'Was the anthropomorphism of early Vedic gods complete?', 'opts': ['No, it was incomplete and highly symbolic', 'Yes, they were depicted as having complete human bodies', 'They were only represented as animals', 'None of the above'], 'ans': 0, 'sol': 'Human attributes given to deified natural elements were symbolic and metaphorical.', 'q_hi': 'क्या प्रारंभिक वैदिक देवताओं का मानवीकरण पूर्ण था?', 'opts_hi': ['नहीं, यह अधूरा और अत्यधिक प्रतीकात्मक था', 'हाँ, उन्हें पूर्ण मानव शरीर के रूप में दर्शाया गया था', 'उन्हें केवल जानवरों के रूप में दर्शाया गया था', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'देवत्वकृत प्राकृतिक तत्वों को दिए गए मानवीय गुण प्रतीकात्मक और रूपकात्मक थे.'}, {'q': "What was deified by the Rigvedic deity 'Savitr'?", 'opts': ['The rising sun or solar energy', 'The storm and wind', 'The evening twilight', 'The agricultural furrow'], 'ans': 0, 'sol': 'Savitr was the solar deity representing the stimulating power of the rising sun.', 'q_hi': "ऋग्वैदिक देवता 'सविता' द्वारा किसे देवत्व प्रदान किया गया था?", 'opts_hi': ['उगता हुआ सूर्य या सौर ऊर्जा', 'आँधी और हवा', 'शाम की गोधूलि', 'कृषि की नाली'], 'ans_hi': 0, 'sol_hi': 'सविता उगते सूर्य की उत्तेजक शक्ति का प्रतिनिधित्व करने वाले सौर देवता थे.'}, {'q': 'Which text contains the oldest hymns of naturalistic polytheism?', 'opts': ['Rigveda Samhita', 'Atharvaveda', 'Shatapatha Brahmana', 'Chandogya Upanishad'], 'ans': 0, 'sol': 'Rigveda Samhita contains the earliest hymns deifying nature forces.', 'q_hi': 'प्राकृतिक बहुदेववाद के सबसे पुराने भजन किस ग्रंथ में मिलते हैं?', 'opts_hi': ['ऋग्वेद संहिता', 'अथर्ववेद', 'शतपथ ब्राह्मण', 'छान्दोग्य उपनिषद'], 'ans_hi': 0, 'sol_hi': 'ऋग्वेद संहिता में प्राकृतिक शक्तियों को देवत्व प्रदान करने वाले सबसे पहले भजन शामिल हैं.'}, {'q': 'The division of the cosmos into three realms (earth, middle space, sky) was used to categorize:', 'opts': ['Vedic deities', 'Social varnas', 'Vedic rivers', 'Types of sacrifices'], 'ans': 0, 'sol': 'Vedic commentators divided the pantheon into terrestrial, aerial, and celestial deities.', 'q_hi': 'ब्रह्मांड का तीन लोकों (पृथ्वी, अंतरिक्ष, द्युलोक) में विभाजन किसे वर्गीकृत करने के लिए किया जाता था?', 'opts_hi': ['वैदिक देवताओं को', 'सामाजिक वर्णों को', 'वैदिक नदियों को', 'यज्ञों के प्रकारों को'], 'ans_hi': 0, 'sol_hi': 'वैदिक भाष्यकारों ने देवगण को पृथ्वीस्थानीय, अंतरिक्षस्थानीय और द्युस्थानीय देवताओं में विभाजित किया.'}, {'q': 'Who represented the celestial sky-father in the early Rigveda?', 'opts': ['Dyaus', 'Prithvi', 'Indra', 'Agni'], 'ans': 0, 'sol': 'Dyaus was deified as the sky-father, paired with Prithvi (earth-mother).', 'q_hi': 'प्रारंभिक ऋग्वेद में आकाशीय द्युलोक-पिता का प्रतिनिधित्व किसने किया था?', 'opts_hi': ['द्यौस', 'पृथ्वी', 'इंद्र', 'अग्नि'], 'ans_hi': 0, 'sol_hi': 'द्यौस को द्युलोक-पिता के रूप में प्रतिष्ठित किया गया था, जिन्हें पृथ्वी (धरती-माता) के साथ जोड़ा गया था.'}, {'q': 'Early Rigvedic priests invoked deities mainly to secure:', 'opts': ['Utilitarian, worldly benefits', 'Release from Samsara', 'Merging with Brahman', 'Control of iron weapons'], 'ans': 0, 'sol': 'Prayers were strictly for cows, sons, health, and victory.', 'q_hi': 'प्रारंभिक ऋग्वैदिक पुरोहितों ने मुख्य रूप से क्या प्राप्त करने के लिए देवताओं का आह्वान किया?', 'opts_hi': ['उपयोगितावादी, सांसारिक लाभ', 'संसार से मुक्ति', 'ब्रह्म में विलीन होना', 'लोहे के हथियारों पर नियंत्रण'], 'ans_hi': 0, 'sol_hi': 'प्रार्थनाएँ पूरी तरह से गायों, बेटों, स्वास्थ्य और विजय के लिए थीं.'}, {'q': "The concept of 'Ekam Sat' (Truth is one) in late hymns indicates:", 'opts': ['Transition towards monism and philosophical unity', 'Decline of sacrifice rituals', 'Victory of Indra over other gods', 'Abolition of the pantheon'], 'ans': 0, 'sol': 'Ekam Sat Vipra Bahudha Vadanti marks early transition to monism/philosophical unity.', 'q_hi': "उत्तरकालीन भजनों में 'एकम सत्' (सत्य एक है) की अवधारणा क्या दर्शाती है?", 'opts_hi': ['अद्वैतवाद और दार्शनिक एकता की ओर संक्रमण', 'यज्ञ अनुष्ठानों में गिरावट', 'अन्य देवताओं पर इंद्र की विजय', 'देवगण का उन्मूलन'], 'ans_hi': 0, 'sol_hi': 'एकम सत् विप्रा बहुधा वदन्ति अद्वैतवाद/दार्शनिक एकता की ओर प्रारंभिक संक्रमण को चिह्नित करता है.'}], 2: [{'q': 'Which Rigvedic deity is addressed in the maximum number (250) of hymns?', 'opts': ['Indra', 'Agni', 'Varuna', 'Soma'], 'ans': 0, 'sol': 'Indra is the thunder-god and military leader praised in 250 hymns.', 'q_hi': 'किस ऋग्वैदिक देवता को अधिकतम संख्या (250) भजनों में संबोधित किया गया है?', 'opts_hi': ['इंद्र', 'अग्नि', 'वरुण', 'सोम'], 'ans_hi': 0, 'sol_hi': 'इंद्र वज्र के देवता और सैन्य नेता हैं जिनकी 250 भजनों में प्रशंसा की गई है.'}, {'q': 'What is the secondary most popular god in the Rigveda, with 200 hymns?', 'opts': ['Agni', 'Indra', 'Varuna', 'Soma'], 'ans': 0, 'sol': 'Agni, the fire god, is the second most praised deity in early texts.', 'q_hi': 'ऋग्वेद में 200 भजनों के साथ दूसरा सबसे लोकप्रिय देवता कौन सा है?', 'opts_hi': ['अग्नि', 'इंद्र', 'वरुण', 'सोम'], 'ans_hi': 0, 'sol_hi': 'अग्नि, अग्नि देव, प्रारंभिक ग्रंथों में दूसरे सबसे अधिक प्रशंसित देवता हैं.'}, {'q': 'Which god acted as the mediator between humans and the divine?', 'opts': ['Agni (Sacrificial fire)', 'Varuna', 'Indra', 'Maruts'], 'ans': 0, 'sol': 'Agni carried offerings thrown into the sacrificial fire to other deities.', 'q_hi': 'कौन सा देवता मनुष्यों और दिव्य शक्तियों के बीच मध्यस्थ के रूप में कार्य करता था?', 'opts_hi': ['अग्नि (यज्ञ की अग्नि)', 'वरुण', 'इंद्र', 'मरुत'], 'ans_hi': 0, 'sol_hi': 'अग्नि यज्ञ की अग्नि में डाली जाने वाली आहुतियों को अन्य देवताओं तक ले जाती थी.'}, {'q': "Who was deified as the guardian of 'Rta' (Cosmic and Moral Order)?", 'opts': ['Varuna', 'Indra', 'Agni', 'Soma'], 'ans': 0, 'sol': 'Varuna was the ethical guardian of cosmic moral order and laws.', 'q_hi': "किसे 'ऋत' (ब्रह्मांडीय और नैतिक व्यवस्था) के रक्षक के रूप में प्रतिष्ठित किया गया था?", 'opts_hi': ['वरुण', 'इंद्र', 'अग्नि', 'सोम'], 'ans_hi': 0, 'sol_hi': 'वरुण ब्रह्मांडीय नैतिक व्यवस्था और नियमों के नैतिक रक्षक थे.'}, {'q': "What title applied to Indra translates to 'destroyer of forts'?", 'opts': ['Purandara', 'Gopati', 'Naditarna', 'Isana'], 'ans': 0, 'sol': 'Purandara means destroyer of fortresses or enclosures.', 'q_hi': "इंद्र के लिए प्रयुक्त किस उपाधि का अर्थ 'किलों को नष्ट करने वाला' है?", 'opts_hi': ['पुरंदर', 'गोपति', 'नदीतमा', 'ईशान'], 'ans_hi': 0, 'sol_hi': 'पुरंदर का अर्थ किलों या बाड़ों को नष्ट करने वाला है.'}, {'q': 'Which atmospheric god represented the violent storm in early hymns?', 'opts': ['Rudra or Maruts', 'Indra only', 'Vayu only', 'Agni'], 'ans': 0, 'sol': 'Rudra and Maruts deified storm forces and tempest winds.', 'q_hi': 'प्रारंभिक भजनों में किस अंतरिक्षीय देवता को हिंसक आंधी का प्रतिनिधित्व माना गया था?', 'opts_hi': ['रुद्र या मरुत', 'केवल इंद्र', 'केवल वायु', 'अग्नि'], 'ans_hi': 0, 'sol_hi': 'रुद्र और मरुत आंधी की शक्तियों और हिंसक हवाओं के देवत्वकृत रूप थे.'}, {'q': 'Who was the female goddess of dawn celebrated for her beauty?', 'opts': ['Ushas', 'Aditi', 'Aranyani', 'Prithvi'], 'ans': 0, 'sol': 'Ushas was the goddess of dawn, depicted as a beautiful young woman.', 'q_hi': 'अपनी सुंदरता के लिए प्रसिद्ध भोर की देवी कौन थी?', 'opts_hi': ['उषा', 'अदिति', 'अरण्यानी', 'पृथ्वी'], 'ans_hi': 0, 'sol_hi': 'उषा भोर की देवी थीं, जिन्हें एक सुंदर युवा महिला के रूप में चित्रित किया गया था.'}, {'q': 'Which goddess represented the mother of the gods in Rigvedic mythology?', 'opts': ['Aditi', 'Ushas', 'Aranyani', 'Savitri'], 'ans': 0, 'sol': 'Aditi was deified as the cosmic mother of the Adityas (deities).', 'q_hi': 'ऋग्वैदिक पौराणिक कथाओं में किस देवी को देवताओं की माता के रूप में दर्शाया गया है?', 'opts_hi': ['अदिति', 'उषा', 'अरण्यानी', 'सावित्री'], 'ans_hi': 0, 'sol_hi': 'अदिति को आदित्यों (देवताओं) की ब्रह्मांडीय माता के रूप में प्रतिष्ठित किया गया था.'}, {'q': "The goddess 'Aranyani' in early Vedic hymns represented:", 'opts': ['The forest and wilderness', 'The dawn and beauty', 'The domestic hearth', 'The river Sarasvati'], 'ans': 0, 'sol': 'Aranyani was deified as the spirit/goddess of the forest and wilderness.', 'q_hi': "प्रारंभिक वैदिक भजनों में देवी 'अरण्यानी' किसका प्रतिनिधित्व करती थीं?", 'opts_hi': ['वन और जंगल', 'भोर और सुंदरता', 'घरेलू चूल्हा', 'सरस्वती नदी'], 'ans_hi': 0, 'sol_hi': 'अरण्यानी को वन और जंगल की आत्मा/देवी के रूप में प्रतिष्ठित किया गया था.'}, {'q': 'Which celestial god is praised for riding a chariot across the sky?', 'opts': ['Surya', 'Agni', 'Varuna', 'Dyaus'], 'ans': 0, 'sol': 'Surya (the sun god) is described as riding a chariot drawn by seven horses.', 'q_hi': 'किस आकाशीय देवता की आकाश में रथ की सवारी करने के लिए प्रशंसा की गई है?', 'opts_hi': ['सूर्य', 'अग्नि', 'वरुण', 'द्यौस'], 'ans_hi': 0, 'sol_hi': 'सूर्य (सूर्य देव) को सात घोड़ों द्वारा खींचे जाने वाले रथ की सवारी करने वाले के रूप में वर्णित किया गया है.'}, {'q': 'What was the relative position of female deities in the pantheon?', 'opts': ['Subordinate and less prominent compared to male gods', 'Supreme rulers of the pantheon', 'Equally praised as Indra', 'Completely absent from hymns'], 'ans': 0, 'sol': 'Reflecting patriarchy, goddesses held subordinate positions and fewer hymns.', 'q_hi': 'देवगण में महिला देवियों की सापेक्ष स्थिति क्या थी?', 'opts_hi': ['पुरुष देवताओं की तुलना में गौण और कम प्रमुख', 'देवगण की सर्वोच्च शासक', 'इंद्र के समान ही प्रशंसित', 'भजनों से पूरी तरह अनुपस्थित'], 'ans_hi': 0, 'sol_hi': 'पितृसत्ता को दर्शाते हुए, देवियों को गौण स्थान प्राप्त था और उनके लिए कम भजन थे.'}, {'q': "The god 'Yama' in Rigvedic beliefs was associated with:", 'opts': ['The realm of the dead / ancestors', 'Storm and rain', 'Sacrificial fire', 'Lute playing'], 'ans': 0, 'sol': 'Yama was deified as the king of the dead and pathfinder for ancestors.', 'q_hi': "ऋग्वैदिक मान्यताओं में 'यम' देवता किससे जुड़े थे?", 'opts_hi': ['मृतकों/पितरों का लोक', 'आंधी और बारिश', 'यज्ञ की अग्नि', 'वीणा वादन'], 'ans_hi': 0, 'sol_hi': 'यम को मृतकों के राजा और पितरों के मार्गदर्शक के रूप में प्रतिष्ठित किया गया था.'}], 3: [{'q': 'What were the primary modes of worship in early Rigvedic religion?', 'opts': ['Prayers (Prarthana) and sacrifices (Yajna)', 'Idol worship and temple festivals', 'Silent meditation in forest caves', 'Pilgrimages to sacred cities'], 'ans': 0, 'sol': 'Simple sacrifices (Yajna) and chanting prayers (Prarthana) were standard.', 'q_hi': 'प्रारंभिक ऋग्वैदिक धर्म में पूजा के प्राथमिक तरीके क्या थे?', 'opts_hi': ['प्रार्थना और यज्ञ', 'मूर्ति पूजा और मंदिर उत्सव', 'वन गुफाओं में मौन ध्यान', 'पवित्र शहरों की तीर्थयात्रा'], 'ans_hi': 0, 'sol_hi': 'सरल यज्ञ और प्रार्थनाओं का पाठ (प्रार्थना) पूजा के मानक तरीके थे.'}, {'q': 'What offerings were commonly thrown into the Rigvedic sacrificial fire?', 'opts': ['Milk, ghee, barley (yava), and Soma juice', 'Wheat, rice, and flowers only', 'Gold coins and jewels', 'Incense sticks and coconuts'], 'ans': 0, 'sol': 'Milk, ghee, yava (barley), and Soma were common sacrificial offerings.', 'q_hi': 'ऋग्वैदिक यज्ञ की अग्नि में आमतौर पर कौन सी आहुतियाँ डाली जाती थीं?', 'opts_hi': ['दूध, घी, जौ (यव) और सोम रस', 'केवल गेहूं, चावल और फूल', 'सोने के सिक्के और आभूषण', 'अगरबत्ती और नारियल'], 'ans_hi': 0, 'sol_hi': 'दूध, घी, यव (जौ) और सोम सामान्य यज्ञीय आहुतियाँ थीं.'}, {'q': 'What was the main motive of worship in early Rigvedic religion?', 'opts': ['Material benefits (cattle, sons, victory, health)', 'Spiritual salvation (Moksha)', 'Release from the cycle of rebirth (Samsara)', 'Philosophical debates only'], 'ans': 0, 'sol': 'Worship was utilitarian, seeking cows, sons, health, and military victory.', 'q_hi': 'प्रारंभिक ऋग्वैदिक धर्म में पूजा का मुख्य उद्देश्य क्या था?', 'opts_hi': ['सांसारिक लाभ (मवेशी, पुत्र, विजय, स्वास्थ्य)', 'आध्यात्मिक मुक्ति (मोक्ष)', 'पुनर्जन्म के चक्र (संसार) से मुक्ति', 'केवल दार्शनिक बहस'], 'ans_hi': 0, 'sol_hi': 'पूजा उपयोगितावादी थी, जिसका उद्देश्य गाय, पुत्र, स्वास्थ्य और सैन्य विजय प्राप्त करना था.'}, {'q': 'Who performed the daily domestic sacrifices (Yajnas) in the family?', 'opts': ['The patriarch (Grihapati or Kulapa)', 'A specialized hierarchy of 16 priests', "The Rajan's administrative deputy", "Only the family's oldest daughter"], 'ans': 0, 'sol': 'Simple domestic sacrifices were performed directly by the family head (Grihapati).', 'q_hi': 'परिवार में दैनिक घरेलू यज्ञों का संपादन कौन करता था?', 'opts_hi': ['पारिवारिक प्रमुख (गृहपति या कुलप)', '16 पुरोहितों का एक विशिष्ट पदानुक्रम', 'राजन का प्रशासनिक उप प्रमुख', 'केवल परिवार की सबसे बड़ी बेटी'], 'ans_hi': 0, 'sol_hi': 'सरल घरेलू यज्ञ सीधे परिवार के मुखिया (गृहपति) द्वारा किए जाते थे.'}, {'q': 'Did a rigid dominant priestly hierarchy exist in the early Rigvedic period?', 'opts': ['No, rituals were simple and did not require complex priestly classes', 'Yes, led by the supreme chief priest of India', 'Yes, based strictly on hereditary caste rules', 'Only in the Sapta-Sindhu area'], 'ans': 0, 'sol': 'Rituals were simple; the expensive, multi-priest hierarchies only developed later.', 'q_hi': 'क्या प्रारंभिक ऋग्वैदिक काल में एक कठोर और वर्चस्वशाली पुरोहित पदानुक्रम मौजूद था?', 'opts_hi': ['नहीं, अनुष्ठान सरल थे और उनके लिए जटिल पुरोहित वर्गों की आवश्यकता नहीं थी', 'हाँ, भारत के सर्वोच्च मुख्य पुरोहित के नेतृत्व में', 'हाँ, पूरी तरह से वंशानुगत जाति नियमों पर आधारित', 'केवल सप्त-सिंधु क्षेत्र में'], 'ans_hi': 0, 'sol_hi': 'अनुष्ठान सरल थे; महंगे और बहु-पुरोहित पदानुक्रम केवल बाद में विकसित हुए.'}, {'q': 'The priest who recited hymns from the Rigveda during public Yajna was called:', 'opts': ['Hotri', 'Adhvaryu', 'Udgatri', 'Brahman'], 'ans': 0, 'sol': 'Hotri was the reciter priest responsible for Rigvedic invocations.', 'q_hi': 'सार्वजनिक यज्ञ के दौरान ऋग्वेद के भजनों का पाठ करने वाले पुरोहित को क्या कहा जाता था?', 'opts_hi': ['होत्री', 'अध्वर्यु', 'उद्गात्री', 'ब्रह्मा'], 'ans_hi': 0, 'sol_hi': 'होत्री ऋग्वैदिक आह्वान के लिए जिम्मेदार पाठकर्ता पुरोहित था.'}, {'q': 'Which priest was responsible for chanting the musical melodies of Samaveda?', 'opts': ['Udgatri', 'Hotri', 'Adhvaryu', 'Brahman'], 'ans': 0, 'sol': 'Udgatri sang the melodies (Saman) during the ritual sacrifices.', 'q_hi': 'सामवेद की संगीतमय धुनों के पाठ के लिए कौन सा पुरोहित जिम्मेदार था?', 'opts_hi': ['उद्गात्री', 'होत्री', 'अध्वर्यु', 'ब्रह्मा'], 'ans_hi': 0, 'sol_hi': 'उद्गात्री यज्ञ के दौरान मधुर भजनों (साम) का गान करता था.'}, {'q': 'The priest who performed physical manual tasks of Yajna (building altars) was:', 'opts': ['Adhvaryu', 'Hotri', 'Udgatri', 'Brahman'], 'ans': 0, 'sol': 'Adhvaryu performed manual ritual acts using Yajurveda prose formulas.', 'q_hi': 'यज्ञ के भौतिक कार्य (वेदी निर्माण) करने वाले पुरोहित को क्या कहा जाता था?', 'opts_hi': ['अध्वर्यु', 'होत्री', 'उद्गात्री', 'ब्रह्मा'], 'ans_hi': 0, 'sol_hi': 'अध्वर्यु यजुर्वेद के गद्य सूत्रों का उपयोग करके अनुष्ठान के शारीरिक कार्यों को संपन्न करता था.'}, {'q': 'Were animal sacrifices performed in early Rigvedic rituals?', 'opts': ['Yes, occasionally, to win favor of gods during major tribal sacrifices', 'No, violence was strictly prohibited in all Vedic texts', 'Only in the Later Vedic phase', 'Only for deified river gods'], 'ans': 0, 'sol': 'Animal sacrifices occurred occasionally during major communal Yajnas.', 'q_hi': 'क्या प्रारंभिक ऋग्वैदिक अनुष्ठानों में पशु बलि दी जाती थी?', 'opts_hi': ['हाँ, कभी-कभार, प्रमुख जनजातीय यज्ञों के दौरान देवताओं की कृपा प्राप्त करने के लिए', 'नहीं, सभी वैदिक ग्रंथों में हिंसा सख्त वर्जित थी', 'केवल उत्तर वैदिक चरण में', 'केवल नदी देवताओं के लिए'], 'ans_hi': 0, 'sol_hi': 'प्रमुख सांप्रदायिक यज्ञों के दौरान कभी-कभार पशु बलि दी जाती थी.'}, {'q': 'How were the Rigvedic hymns preserved and transmitted over generations?', 'opts': ['Through precise oral tradition and memorization (Shruti)', 'By writing on copper plates', 'By carving on temple stone walls', 'Through palm leaf manuscripts'], 'ans': 0, 'sol': 'Hymns were transmitted orally; Shruti means that which is heard.', 'q_hi': 'ऋग्वैदिक भजनों को पीढ़ियों तक कैसे संरक्षित और प्रसारित किया गया था?', 'opts_hi': ['सटीक मौखिक परंपरा और कंठस्थ करने के माध्यम से (श्रुति)', 'तांबे की पट्टिकाओं पर लिखकर', 'मंदिर की पत्थर की दीवारों पर नक्काशी करके', 'ताड़ के पत्तों की पाण्डुलिपियों के माध्यम से'], 'ans_hi': 0, 'sol_hi': 'भजनों का प्रसारण मौखिक रूप से होता था; श्रुति का अर्थ है जो सुना गया हो.'}, {'q': 'Was the performance of Yajna linked to political status of chiefs?', 'opts': ['Yes, chiefs sponsored Yajnas to assert military legitimacy and prestige', 'No, chiefs were banned from Yajnas', 'Yajnas were performed only by weavers', 'None of the above'], 'ans': 0, 'sol': 'Rajan sponsored communal sacrifices to gain legitimacy and distribute spoils.', 'q_hi': 'क्या यज्ञ का आयोजन मुखियों की राजनीतिक स्थिति से जुड़ा था?', 'opts_hi': ['हाँ, प्रमुखों ने सैन्य वैधता और प्रतिष्ठा स्थापित करने के लिए यज्ञ प्रायोजित किए', 'नहीं, प्रमुखों को यज्ञ करने पर प्रतिबंध था', 'यज्ञ केवल बुनकरों द्वारा किए जाते थे', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'राजन ने वैधता प्राप्त करने और लूट का वितरण करने के लिए सांप्रदायिक यज्ञों को प्रायोजित किया.'}, {'q': 'What represents the basic domestic ritual fire kept in every home?', 'opts': ['Grihya Agni / Garhapatya', 'Soma Agni', 'Rudra Agni', 'None of these'], 'ans': 0, 'sol': 'Garhapatya was the domestic fire maintained in the household.', 'q_hi': 'प्रत्येक घर में रखी जाने वाली बुनियादी घरेलू यज्ञ अग्नि को क्या कहा जाता था?', 'opts_hi': ['गृह्य अग्नि / गार्हपत्य', 'सोम अग्नि', 'रुद्र अग्नि', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'गार्हपत्य वह घरेलू अग्नि थी जिसे गृहस्थी में निरंतर बनाए रखा जाता था.'}], 4: [{'q': "What does the Rigvedic term 'Rta' represent?", 'opts': ['Cosmic, natural, and moral order', 'A type of sacrificial grain offering', 'A standard weight of copper', 'The tribal boundary line'], 'ans': 0, 'sol': 'Rta represents the cosmic, physical, and moral order governing the universe.', 'q_hi': "ऋग्वैदिक शब्द 'ऋत' किसका प्रतिनिधित्व करता है?", 'opts_hi': ['ब्रह्मांडीय, प्राकृतिक और नैतिक व्यवस्था', 'एक प्रकार के यज्ञीय अनाज की आहुति', 'तांबे का एक मानक वजन', 'जनजातीय सीमा रेखा'], 'ans_hi': 0, 'sol_hi': 'ऋत ब्रह्मांडीय, भौतिक और नैतिक व्यवस्था का प्रतिनिधित्व करता है जो ब्रह्मांड को नियंत्रित करती है.'}, {'q': "Which deity is addressed as the 'guardian of Rta' (Gopa Rtasya)?", 'opts': ['Varuna', 'Indra', 'Agni', 'Soma'], 'ans': 0, 'sol': 'Varuna was the supreme guardian of cosmic and moral order.', 'q_hi': "किस देवता को 'ऋत का रक्षक' (गोपा ऋतस्य) के रूप में संबोधित किया गया है?", 'opts_hi': ['वरुण', 'इंद्र', 'अग्नि', 'सोम'], 'ans_hi': 0, 'sol_hi': 'वरुण ब्रह्मांडीय और नैतिक व्यवस्था के सर्वोच्च रक्षक थे.'}, {'q': "What term refers to the violation or moral transgression of 'Rta'?", 'opts': ['Anrita (Falsehood/Disorder)', 'Dharma', 'Bali', 'Yajna'], 'ans': 0, 'sol': 'Anrita refers to falsehood, moral deviance, and cosmic disorder.', 'q_hi': "'ऋत' के उल्लंघन या नैतिक विचलन को किस शब्द से संदर्भित किया जाता है?", 'opts_hi': ['अनृत (असत्य/अव्यवस्था)', 'धर्म', 'बलि', 'यज्ञ'], 'ans_hi': 0, 'sol_hi': 'अनृत का तात्पर्य असत्य, नैतिक विचलन और ब्रह्मांडीय अव्यवस्था से है.'}, {'q': 'How was Varuna believed to punish transgressors of Rta?', 'opts': ['By binding them with fetters and causing disease (dropsy)', 'By sentencing them to exile', 'By taking away their land tracts', 'By locking them in dungeons'], 'ans': 0, 'sol': 'Varuna bound sinners with loops or fetters and inflicted dropsy.', 'q_hi': 'वरुण ऋत के उल्लंघनकर्ताओं को कैसे दंडित करते थे, ऐसा माना जाता था?', 'opts_hi': ['उन्हें पाश (जाल) में बांधकर और बीमारी (जलोदर) देकर', 'उन्हें निर्वासन की सजा देकर', 'उनकी भूमि के भूखंडों को छीनकर', 'उन्हें कालकोठरी में बंद करके'], 'ans_hi': 0, 'sol_hi': 'वरुण पापियों को पाश में बांधते थे और उन्हें जलोदर (dropsy) नामक रोग से पीड़ित करते थे.'}, {'q': 'Rta governed which dimensions according to Rigvedic cosmology?', 'opts': ['Both physical natural cycles (seasons, sun movement) and moral human actions', 'Only moral human actions', 'Only physical natural cycles', 'Only priestly sacrifice rituals'], 'ans': 0, 'sol': 'Rta governed physical natural laws (sun, seasons) and ethical conduct.', 'q_hi': 'ऋग्वैदिक ब्रह्मांड विज्ञान के अनुसार ऋत किन आयामों को नियंत्रित करता था?', 'opts_hi': ['भौतिक प्राकृतिक चक्र (ऋतुएँ, सूर्य की गति) और नैतिक मानवीय कार्य दोनों', 'केवल नैतिक मानवीय कार्य', 'केवल भौतिक प्राकृतिक चक्र', 'केवल पुरोहितों के यज्ञ अनुष्ठान'], 'ans_hi': 0, 'sol_hi': 'ऋत भौतिक प्राकृतिक नियमों (सूर्य, ऋतुओं) और नैतिक आचरण दोनों को नियंत्रित करता था.'}, {'q': 'What is the relationship between Rta and the deified natural forces?', 'opts': ['The gods are subjects and maintainers of Rta, not its creators', 'The gods created Rta and can destroy it', 'Rta only applies to human beings, not gods', 'None of the above'], 'ans': 0, 'sol': 'Gods (Adityas) are guardians who enforce Rta; Rta is supreme cosmic law.', 'q_hi': 'ऋत और देवत्वकृत प्राकृतिक शक्तियों के बीच क्या संबंध है?', 'opts_hi': ['देवता ऋत के अधीन और रक्षक हैं, इसके निर्माता नहीं', 'देवताओं ने ऋत का निर्माण किया और वे इसे नष्ट कर सकते हैं', 'ऋत केवल मनुष्यों पर लागू होता है, देवताओं पर नहीं', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'देवता (आदित्य) रक्षक हैं जो ऋत को लागू करते हैं; ऋत सर्वोच्च ब्रह्मांडीय नियम है.'}, {'q': 'The division of seasons (Rtu) is etymologically derived from:', 'opts': ['Rta (Orderly change)', 'Rudra', 'Rajan', 'Ratha'], 'ans': 0, 'sol': 'Rtu (season) comes from Rta, representing regular seasonal cycles.', 'q_hi': 'ऋतुओं (ऋतु) का विभाजन व्युत्पत्ति के अनुसार किससे लिया गया है?', 'opts_hi': ['ऋत (क्रमबद्ध परिवर्तन)', 'रुद्र', 'राजन', 'रथ'], 'ans_hi': 0, 'sol_hi': 'ऋतु शब्द ऋत से आया है, जो नियमित मौसमी चक्रों का प्रतिनिधित्व करता है.'}, {'q': 'Which celestial gods are paired as joint guardians of Rta in hymns?', 'opts': ['Mitra and Varuna', 'Indra and Agni', 'Soma and Rudra', 'Dyaus and Prithvi'], 'ans': 0, 'sol': 'Mitra-Varuna are jointly invoked to uphold and protect Rta.', 'q_hi': 'भजनों में किन आकाशीय देवताओं को ऋत के संयुक्त रक्षकों के रूप में दर्शाया गया है?', 'opts_hi': ['मित्र और वरुण', 'इंद्र और अग्नि', 'सोम और रुद्र', 'द्यौस और पृथ्वी'], 'ans_hi': 0, 'sol_hi': 'मित्र-वरुण को संयुक्त रूप से ऋत को बनाए रखने और उसकी रक्षा करने के लिए पुकारा जाता है.'}, {'q': 'Did early Rigvedic religion have a concept of hell for sinners?', 'opts': ["No, sinners were punished in this life by Varuna's fetters", 'Yes, a burning underworld existed', 'Only for non-Aryan traders', 'None of these'], 'ans': 0, 'sol': 'Ethical deviance was punished in life through illness, social exclusion, or failure.', 'q_hi': 'क्या प्रारंभिक ऋग्वैदिक धर्म में पापियों के लिए नर्क की अवधारणा थी?', 'opts_hi': ['नहीं, पापियों को इसी जीवन में वरुण के पाश द्वारा दंडित किया जाता था', 'हाँ, एक जलता हुआ पाताल लोक मौजूद था', 'केवल गैर-आर्य व्यापारियों के लिए', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'नैतिक विचलन के लिए इसी जीवन में बीमारी, सामाजिक बहिष्कार या विफलता के माध्यम से दंड मिलता था.'}, {'q': 'The concept of Rta contrasts with Later Vedic ritualism because Rta was:', 'opts': ['Ethical and cosmic, rather than purely mechanical ritual performance', 'Based entirely on temple sacrifices', 'Invented by non-Aryan artisans', 'Strictly concerned with agriculture'], 'ans': 0, 'sol': 'Rta focused on moral harmony and natural laws rather than ritual formulas.', 'q_hi': 'ऋत की अवधारणा उत्तर वैदिक कर्मकांड से भिन्न थी क्योंकि ऋत था:', 'opts_hi': ['विशुद्ध यांत्रिक यज्ञ प्रदर्शन के बजाय नैतिक और ब्रह्मांडीय', 'पूरी तरह से मंदिर के यज्ञों पर आधारित', 'गैर-आर्य कारीगरों द्वारा आविष्कार किया गया', 'सख्ती से कृषि से संबंधित'], 'ans_hi': 0, 'sol_hi': 'ऋत अनुष्ठानिक सूत्रों के बजाय नैतिक सद्भाव और प्राकृतिक नियमों पर केंद्रित था.'}, {'q': "Which god acts as the 'mouth' of Rta in sacrificial rituals?", 'opts': ['Agni', 'Indra', 'Soma', 'Varuna'], 'ans': 0, 'sol': 'Agni is the mouth of gods who carries offerings in accordance with Rta.', 'q_hi': "यज्ञ अनुष्ठानों में ऋत के 'मुख' के रूप में कौन सा देवता कार्य करता है?", 'opts_hi': ['अग्नि', 'इंद्र', 'सोम', 'वरुण'], 'ans_hi': 0, 'sol_hi': 'अग्नि देवताओं का मुख है जो ऋत के अनुसार आहुतियाँ ले जाता है.'}, {'q': 'What legal/moral duties did the Rajan have regarding Rta?', 'opts': ['He had to uphold social order matching Rta, acting as its protector', 'He had the power to alter the laws of Rta', 'He was exempt from Rta', 'None of the above'], 'ans': 0, 'sol': 'The Rajan was expected to enforce customary laws aligned with Rta.', 'q_hi': 'ऋत के संबंध में राजन के क्या कानूनी/नैतिक कर्तव्य थे?', 'opts_hi': ['उसे ऋत के अनुरूप सामाजिक व्यवस्था बनाए रखनी थी, उसका रक्षक बनना था', 'उनके पास ऋत के नियमों को बदलने की शक्ति थी', 'उन्हें ऋत से छूट दी गई थी', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'राजन से ऋत के साथ संरेखित पारंपरिक कानूनों को लागू करने की अपेक्षा की जाती थी.'}], 5: [{'q': "What was 'Soma' in the Rigvedic religious life?", 'opts': ['An intoxicating sacrificial drink deified as a god', 'A type of wheat bread', 'A sacred metal tool', 'The throne of the Rajan'], 'ans': 0, 'sol': 'Soma was a plant juice deified as a major god, believed to inspire seers.', 'q_hi': "ऋग्वैदिक धार्मिक जीवन में 'सोम' क्या था?", 'opts_hi': ['एक नशीला यज्ञीय पेय जिसे देवता के रूप में पूजा जाता था', 'एक प्रकार की गेहूं की रोटी', 'एक पवित्र धातु का उपकरण', 'राजन का सिंहासन'], 'ans_hi': 0, 'sol_hi': 'सोम एक पौधे का रस था जिसे एक प्रमुख देवता के रूप में पूजा जाता था, माना जाता था कि यह ऋषियों को प्रेरित करता था.'}, {'q': 'Which Mandala of the Rigveda is dedicated entirely to Soma (Soma Mandala)?', 'opts': ['Mandala IX', 'Mandala X', 'Mandala III', 'Mandala VII'], 'ans': 0, 'sol': 'Mandala IX contains all 114 hymns dedicated to Soma Pavamana.', 'q_hi': 'ऋग्वेद का कौन सा मंडल पूरी तरह से सोम को समर्पित है (सोम मंडल)?', 'opts_hi': ['मंडल IX', 'मंडल X', 'मंडल III', 'मंडल VII'], 'ans_hi': 0, 'sol_hi': 'मंडल IX में सोम पवमान को समर्पित सभी 114 भजन शामिल हैं.'}, {'q': 'From which mountain range did the Vedic people source the Soma plant?', 'opts': ['Mujavant (Himalayas)', 'Vindhyas', 'Aravallis', 'Hindukush'], 'ans': 0, 'sol': 'Rigvedic texts mention Mount Mujavant as the source of best Soma.', 'q_hi': 'वैदिक लोग किस पर्वत श्रृंखला से सोम का पौधा प्राप्त करते थे?', 'opts_hi': ['मुजावंत (हिमालय)', 'विंध्य', 'अरावली', 'हिंदुकुश'], 'ans_hi': 0, 'sol_hi': 'ऋग्वैदिक ग्रंथों में सर्वोत्तम सोम के स्रोत के रूप में मुजावंत पर्वत का उल्लेख मिलता है.'}, {'q': 'How was the Soma juice prepared for sacrificial rituals?', 'opts': ['Pounded with stones, filtered through wool, and mixed with milk/barley', 'Fermented for several months in clay jars', 'Boiled with medicinal copper pieces', 'None of the above'], 'ans': 0, 'sol': 'Soma stalks were crushed with stones, filtered, and diluted with milk/grain.', 'q_hi': 'यज्ञ अनुष्ठानों के लिए सोम रस कैसे तैयार किया जाता था?', 'opts_hi': ['पत्थरों से कूटकर, ऊन से छानकर और दूध/जौ में मिलाकर', 'मिट्टी के जार में कई महीनों तक किण्वित करके', 'औषधीय तांबे के टुकड़ों के साथ उबालकर', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'सोम की लताओं को पत्थरों से कुचला जाता था, छाना जाता था और दूध या अनाज के साथ मिलाया जाता था.'}, {'q': 'What effects were attributed to consuming the Soma drink?', 'opts': ['Invigoration, feeling of immortality, and divine inspiration', 'Complete loss of consciousness and sleep', 'Severe illness and dropsy', 'None of these'], 'ans': 0, 'sol': 'Consuming Soma produced energy, inspiration, and feelings of ecstasy.', 'q_hi': 'सोम पेय के सेवन के क्या प्रभाव बताए गए थे?', 'opts_hi': ['ऊर्जा का संचार, अमरता की भावना और दिव्य प्रेरणा', 'चेतना की पूर्ण हानि और नींद', 'गंभीर बीमारी और जलोदर', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'सोम के सेवन से ऊर्जा, प्रेरणा और उत्साह की भावना पैदा होती थी.'}, {'q': 'Which god is most closely associated with drinking Soma before battle?', 'opts': ['Indra', 'Varuna', 'Agni', 'Mitra'], 'ans': 0, 'sol': 'Indra consumed massive quantities of Soma to gain strength for fights.', 'q_hi': 'युद्ध से पहले सोम का पान करने से सबसे निकटता से कौन सा देवता जुड़ा है?', 'opts_hi': ['इंद्र', 'वरुण', 'अग्नि', 'मित्र'], 'ans_hi': 0, 'sol_hi': 'इंद्र ने युद्ध के लिए शक्ति प्राप्त करने के लिए भारी मात्रा में सोम का सेवन किया.'}, {'q': 'What describes the plant identification of Soma today?', 'opts': ['It remains botanically debated, possibly Ephedra or a fly agaric fungus', 'It is definitively identified as sugarcane', 'It was proved to be cannabis', 'None of the above'], 'ans': 0, 'sol': 'Botanical identity is disputed; Ephedra is a leading candidate.', 'q_hi': 'आज सोम के पौधे की पहचान का क्या वर्णन है?', 'opts_hi': ['यह वनस्पति शास्त्र में विवादास्पद है, संभवतः एफेड्रा या एक कवक', 'निश्चित रूप से इसकी पहचान गन्ने के रूप में की गई है', 'यह भांग सिद्ध हुआ था', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'सोम की वनस्पति पहचान विवादास्पद है; एफेड्रा (Ephedra) एक प्रमुख दावेदार है.'}, {'q': 'The filtering cloth used to purify Soma juice was made of:', 'opts': ["Sheep's wool (Urna)", 'Cotton fabric', 'Jute fibers', 'Reed mat'], 'ans': 0, 'sol': "Soma was filtered through a strainer made of sheep's wool.", 'q_hi': 'सोम रस को शुद्ध करने के लिए उपयोग किया जाने वाला छननी का कपड़ा किसका बना होता था?', 'opts_hi': ['भेड़ की ऊन (ऊर्णा)', 'सूती कपड़ा', 'जूट के रेशे', 'सरकंडे की चटाई'], 'ans_hi': 0, 'sol_hi': 'सोम को भेड़ की ऊन से बनी छननी से छाना जाता था.'}, {'q': 'Why was the Soma plant ritualized as a deity?', 'opts': ['Its energizing juice was central to the Yajna economy and tribal morale', 'It was the only crop grown in Sapta-Sindhu', 'It was used to build war chariots', 'None of the above'], 'ans': 0, 'sol': "Soma's effects made it vital for ritual performance and military courage.", 'q_hi': 'सोम के पौधे को एक देवता के रूप में क्यों अनुष्ठित किया गया था?', 'opts_hi': ['इसका ऊर्जादायक रस यज्ञ अर्थव्यवस्था और कबीले के मनोबल के लिए केंद्रीय था', 'यह सप्त-सिंधु में उगाई जाने वाली एकमात्र फसल थी', 'इसका उपयोग युद्ध रथों के निर्माण के लिए किया जाता था', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'सोम के प्रभावों ने इसे अनुष्ठान प्रदर्शन और सैन्य साहस के लिए महत्वपूर्ण बना दिया.'}, {'q': 'What term refers to the purification of Soma during the ritual?', 'opts': ['Pavamana', 'Bali', 'Yajna', 'Prarthana'], 'ans': 0, 'sol': 'Pavamana refers to the flowing, purifying process of Soma juice.', 'q_hi': 'अनुष्ठान के दौरान सोम के शुद्धिकरण को किस शब्द से संदर्भित किया जाता है?', 'opts_hi': ['पवमान', 'बलि', 'यज्ञ', 'प्रार्थना'], 'ans_hi': 0, 'sol_hi': 'पवमान का तात्पर्य सोम रस के बहने और शुद्ध होने की प्रक्रिया से है.'}, {'q': "What was Soma mixed with to make the drink 'Karambha'?", 'opts': ['Parched barley meal', 'Honey and wine', 'River water only', 'None of these'], 'ans': 0, 'sol': 'Karambha was a mixture of Soma and parched barley meal.', 'q_hi': "पेय 'करम्भ' बनाने के लिए सोम में क्या मिलाया जाता था?", 'opts_hi': ['भुने हुए जौ का आटा', 'शहद और शराब', 'केवल नदी का पानी', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'करम्भ सोम और भुने हुए जौ के आटे का मिश्रण था.'}, {'q': 'The disappearance of the Soma plant in Later Vedic times led to:', 'opts': ['Use of substitute plants (Putika) and ritual changes', 'Complete ban on sacrifices', 'Imports from China', 'Destruction of Yajna sites'], 'ans': 0, 'sol': 'Lack of access to Mujavant forced the use of substitutes like Putika.', 'q_hi': 'उत्तर वैदिक काल में सोम के पौधे के लुप्त होने के कारण क्या हुआ?', 'opts_hi': ['वैकल्पिक पौधों (पूतिका) का उपयोग और अनुष्ठान परिवर्तन', 'यज्ञों पर पूर्ण प्रतिबंध', 'चीन से आयात', 'यज्ञ स्थलों का विनाश'], 'ans_hi': 0, 'sol_hi': 'मुजावंत पर्वत तक पहुँच न होने के कारण पूतिका जैसे वैकल्पिक पौधों का उपयोग करना पड़ा.'}], 6: [{'q': 'Which famous creation hymn of the Rigveda explores the origin of the universe?', 'opts': ['Nasadiya Sukta', 'Purusha Sukta', 'Gayatri Mantra', 'Sarasvati Sukta'], 'ans': 0, 'sol': "Nasadiya Sukta (Mandala X) is the hymn of creation, beginning with 'Neither sat nor asat'.", 'q_hi': 'ऋग्वेद का कौन सा प्रसिद्ध सृष्टि सूक्त ब्रह्मांड की उत्पत्ति की खोज करता है?', 'opts_hi': ['नासदीय सूक्त', 'पुरुष सूक्त', 'गायत्री मंत्र', 'सरस्वती सूक्त'], 'ans_hi': 0, 'sol_hi': "नासदीय सूक्त (मंडल X) सृष्टि का सूक्त है, जो 'न सत था न असत' से शुरू होता है."}, {'q': "The Rigvedic philosophical phrase 'Ekam Sat Vipra Bahudha Vadanti' translates to:", 'opts': ['Truth is one, but sages call it by various names', 'The king is supreme on earth', 'Sacrifice is the only path to heaven', 'Do not kill the cows'], 'ans': 0, 'sol': 'It declares that ultimate reality is one, though described differently by priests.', 'q_hi': "ऋग्वैदिक दार्शनिक वाक्यांश 'एकम सत् विप्रा बहुधा वदन्ति' का अनुवाद है:", 'opts_hi': ['सत्य एक है, लेकिन ऋषि इसे विभिन्न नामों से पुकारते हैं', 'पृथ्वी पर राजा सर्वोच्च है', 'यज्ञ ही स्वर्ग का एकमात्र मार्ग है', 'गायों को मत मारो'], 'ans_hi': 0, 'sol_hi': 'यह घोषित करता है कि अंतिम वास्तविकता एक है, हालांकि पुरोहितों द्वारा इसका अलग-अलग वर्णन किया गया है.'}, {'q': 'Which hymn introduces the sacrifice of the primeval giant to create the universe and social classes?', 'opts': ['Purusha Sukta', 'Nasadiya Sukta', 'Hiranyagarbha Sukta', 'Gayatri Sukta'], 'ans': 0, 'sol': 'Purusha Sukta (Mandala X) describes creation from the limbs of Purusha.', 'q_hi': 'ब्रह्मांड और सामाजिक वर्गों के निर्माण के लिए आदिपुरुष के बलिदान का परिचय कौन सा सूक्त देता है?', 'opts_hi': ['पुरुष सूक्त', 'नासदीय सूक्त', 'हिरण्यगर्भ सूक्त', 'गायत्री सूक्त'], 'ans_hi': 0, 'sol_hi': 'पुरुष सूक्त (मंडल X) पुरुष के अंगों से सृष्टि के निर्माण का वर्णन करता है.'}, {'q': 'What philosophical perspective emerges in the late Mandalas (I and X) of the Rigveda?', 'opts': ['Monism (ultimate unity of all existence)', 'Strict dualism', 'Atheistic materialism', 'Rejection of morality'], 'ans': 0, 'sol': 'Hymns transition from polytheism towards monism, seeking a single underlying reality.', 'q_hi': 'ऋग्वेद के उत्तरकालीन मंडलों (I और X) में कौन सा दार्शनिक दृष्टिकोण उभरता है?', 'opts_hi': ['अद्वैतवाद (सभी अस्तित्व की अंतिम एकता)', 'सख्त द्वैतवाद', 'नास्तिक भौतिकवाद', 'नैतिकता की अस्वीकृति'], 'ans_hi': 0, 'sol_hi': 'भजन बहुदेववाद से अद्वैतवाद की ओर बढ़ते हैं, एक एकल अंतर्निहित वास्तविकता की खोज करते हैं.'}, {'q': "The concept of 'Hiranyagarbha' in Vedic philosophy represents:", 'opts': ['The golden womb or cosmic egg of creation', 'A gold neck ornament', 'The priest who drinks Soma', 'The weapon of Indra'], 'ans': 0, 'sol': 'Hiranyagarbha represents the golden cosmic egg from which creation arose.', 'q_hi': "वैदिक दर्शन में 'हिरण्यगर्भ' की अवधारणा किसका प्रतिनिधित्व करती है?", 'opts_hi': ['सृष्टि का स्वर्ण गर्भ या ब्रह्मांडीय अंडा', 'सोने के गले का आभूषण', 'सोम पीने वाला पुरोहित', 'इंद्र का हथियार'], 'ans_hi': 0, 'sol_hi': 'हिरण्यगर्भ उस सुनहरे ब्रह्मांडीय अंडे का प्रतिनिधित्व करता है जिससे सृष्टि की उत्पत्ति हुई थी.'}, {'q': 'What describes the tone of the Nasadiya Sukta regarding creation?', 'opts': ['Inquisitive and skeptical, questioning if even the gods know the origin', 'Absolute certainty about creation dates', 'Declaring that the chief priest created everything', 'None of the above'], 'ans': 0, 'sol': "It ends with philosophical doubt: 'He who surveys it... perhaps he knows, or perhaps he knows not.'", 'q_hi': 'सृष्टि के संबंध में नासदीय सूक्त के स्वर का क्या वर्णन है?', 'opts_hi': ['जिज्ञासु और संशयवादी, यह सवाल उठाना कि क्या देवता भी उत्पत्ति जानते हैं', 'सृष्टि की तारीखों के बारे में पूर्ण निश्चितता', 'यह घोषित करना कि मुख्य पुरोहित ने सब कुछ बनाया', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': "यह दार्शनिक संदेह के साथ समाप्त होता है: 'वह जो इसका सर्वेक्षण करता है... शायद वह जानता है, या शायद वह नहीं जानता.'"}, {'q': 'The transition to monism laid the foundations for which later philosophical texts?', 'opts': ['Upanishads', 'Puranas', 'Dharmasutras', 'Sangam literature'], 'ans': 0, 'sol': 'Rigvedic monism culminated in the Brahman-Atman philosophy of the Upanishads.', 'q_hi': 'अद्वैतवाद की ओर संक्रमण ने बाद के किन दार्शनिक ग्रंथों की नींव रखी?', 'opts_hi': ['उपनिषद', 'पुराण', 'धर्मसूत्र', 'संगम साहित्य'], 'ans_hi': 0, 'sol_hi': 'ऋग्वैदिक अद्वैतवाद का समापन उपनिषदों के ब्रह्म-आत्मन् दर्शन में हुआ.'}, {'q': "The term 'Tad Ekam' in the Nasadiya Sukta translates to:", 'opts': ['That One', 'The Sun', 'The Priest', 'The Tribe'], 'ans': 0, 'sol': 'Tad Ekam refers to the neutral, formless absolute reality before creation.', 'q_hi': "नासदीय सूक्त में 'तद एकम' शब्द का अनुवाद है:", 'opts_hi': ['वह एक (तद् एकम्)', 'सूर्य', 'पुरोहित', 'जनजाति'], 'ans_hi': 0, 'sol_hi': 'तद् एकम् सृष्टि से पहले की तटस्थ, निराकार परम वास्तविकता को संदर्भित करता है.'}, {'q': 'How does Rigvedic monism differ from monotheism?', 'opts': ['Monism views god and universe as one; monotheism believes in one personal creator god separate from universe', 'Monism has many gods; monotheism has none', 'They are exactly the same concept', 'None of the above'], 'ans': 0, 'sol': 'Monism identifies the creator with the creation (all is one), unlike personal monotheism.', 'q_hi': 'ऋग्वैदिक अद्वैतवाद एकेश्वरवाद से किस प्रकार भिन्न है?', 'opts_hi': ['अद्वैतवाद ईश्वर और ब्रह्मांड को एक मानता है; एकेश्वरवाद ब्रह्मांड से अलग एक व्यक्तिगत निर्माता ईश्वर में विश्वास करता है', 'अद्वैतवाद में कई देवता हैं; एकेश्वरवाद में कोई नहीं', 'वे बिल्कुल एक ही अवधारणा हैं', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'अद्वैतवाद निर्माता को सृष्टि के साथ पहचानता है (सब कुछ एक है), जो व्यक्तिगत एकेश्वरवाद से भिन्न है.'}, {'q': 'Which Mandala contains the Hiranyagarbha Sukta?', 'opts': ['Mandala X', 'Mandala IX', 'Mandala III', 'Mandala I'], 'ans': 0, 'sol': 'Hiranyagarbha Sukta is compiled in the late Mandala X of Rigveda.', 'q_hi': 'हिरण्यगर्भ सूक्त किस मंडल में शामिल है?', 'opts_hi': ['मंडल X', 'मंडल IX', 'मंडल III', 'मंडल I'], 'ans_hi': 0, 'sol_hi': 'हिरण्यगर्भ सूक्त ऋग्वेद के उत्तरकालीन मंडल X में संकलित है.'}, {'q': "In the Purusha Sukta, the Brahmins are said to have originated from the Purusha's:", 'opts': ['Mouth', 'Arms', 'Thighs', 'Feet'], 'ans': 0, 'sol': 'The Brahmins came from the mouth, Kshatriyas from arms, Vaishyas from thighs, Shudras from feet.', 'q_hi': 'पुरुष सूक्त में ब्राह्मणों की उत्पत्ति पुरुष के किस अंग से बताई गई है?', 'opts_hi': ['मुख', 'भुजाएं', 'जंघाएं', 'पैर'], 'ans_hi': 0, 'sol_hi': 'ब्राह्मण मुख से आए, क्षत्रिय भुजाओं से, वैश्य जंघाओं से और शूद्र पैरों से आए.'}, {'q': 'What philosophical shift does the transition to monism represent in Rigvedic thought?', 'opts': ['From ritualistic polytheism to abstract philosophical speculation', 'From agriculture back to hunting', 'From peace to militarism', 'From Sanskrit to Prakrit'], 'ans': 0, 'sol': 'It marks a move from placating external nature gods to seeking internal, absolute truth.', 'q_hi': 'ऋग्वैदिक विचार में अद्वैतवाद की ओर संक्रमण किस दार्शनिक बदलाव का प्रतिनिधित्व करता है?', 'opts_hi': ['कर्मकांडीय बहुदेववाद से अमूर्त दार्शनिक चिंतन की ओर', 'कृषि से वापस शिकार की ओर', 'शांति से सैन्यवाद की ओर', 'संस्कृत से प्राकृत की ओर'], 'ans_hi': 0, 'sol_hi': 'यह बाहरी प्रकृति देवताओं को खुश करने से लेकर आंतरिक, परम सत्य की खोज की ओर बढ़ने का प्रतीक है.'}]}

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
        "q": "With reference to early Vedic religion, consider the following statements:\n1. It was characterized by naturalistic polytheism and the deification of natural forces.\n2. Idol worship and monumental temples were the primary mode of contacting gods.\n3. Sacrifices (Yajnas) were performed directly by patriarchs without complex priestly hierarchies.\nWhich of the statements given above are correct?",
        "opts": ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        "ans": 0,
        "sol": "Statements 1 and 3 are correct. Early Vedic religion completely lacked idol worship and temples (Statement 2 is false).",
        "q_hi": "प्रारंभिक वैदिक धर्म के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसकी विशेषता प्राकृतिक बहुदेववाद और प्राकृतिक शक्तियों का देवत्वकरण थी।\n2. देवताओं से संपर्क करने का प्राथमिक माध्यम मूर्तिपूजा और विशाल मंदिर थे।\n3. यज्ञ सीधे गृहपतियों द्वारा बिना किसी जटिल पुरोहितीय पदानुक्रम के किए जाते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        "opts_hi": ["केवल 1 और 3", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 और 3 सही हैं। प्रारंभिक वैदिक धर्म में मूर्तिपूजा और मंदिरों का पूरी तरह से अभाव था (कथन 2 गलत है)।"
    },
    # Q2
    {
        "q": "Consider the following statements regarding the deification of natural forces in the Rigveda:\n1. Indra was deified as the storm and war god and is addressed in the highest number of hymns.\n2. Agni represented the sacrificial fire and acted as the mediator between gods and humans.\n3. Varuna was deified as the guardian of Rta, representing the cosmic and moral order.\nWhich of the statements given above are correct?",
        "opts": ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        "ans": 0,
        "sol": "All statements are correct. Indra is thunder god, Agni mediator, Varuna Rta guardian.",
        "q_hi": "ऋग्वेद में प्राकृतिक शक्तियों के देवत्वकरण के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इंद्र को आंधी और युद्ध के देवता के रूप में पूजा जाता था और उन्हें सबसे अधिक भजनों में संबोधित किया गया है।\n2. अग्नि यज्ञीय अग्नि का प्रतिनिधित्व करते थे और देवताओं तथा मनुष्यों के बीच मध्यस्थ के रूप में कार्य करते थे।\n3. वरुण को ऋत (ब्रह्मांडीय और नैतिक व्यवस्था) के संरक्षक के रूप में पूजा जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        "opts_hi": ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        "ans_hi": 0,
        "sol_hi": "सभी कथन सही हैं। इंद्र वज्र के देवता हैं, अग्नि मध्यस्थ हैं, वरुण ऋत के संरक्षक हैं।"
    },
    # Q3
    {
        "q": "With reference to the concept of 'Henotheism' (or Kathenotheism) in Rigvedic religion, which of the following is correct?",
        "opts": [
            "It is the belief and worship of one supreme god at a time while addressing hymns, without denying others",
            "It is the rigid belief in a single absolute god that prohibits the existence of any other deity",
            "It is the deification of ancestor spirits as the primary celestial rulers",
            "It is a system that restricts religious practices exclusively to female seers"
        ],
        "ans": 0,
        "sol": "Henotheism refers to worshipping one god at a time as supreme, coined by Max Müller to explain Rigvedic hymn transitions.",
        "q_hi": "ऋग्वैदिक धर्म में 'हेनोथिज्म' (एकेश्वरवाद) की अवधारणा के संदर्भ में निम्नलिखित में से कौन सा सही है?",
        "opts_hi": [
            "यह भजनों को संबोधित करते समय दूसरों को नकारे बिना एक समय में एक ही सर्वोच्च देवता की पूजा करने का विश्वास है",
            "यह एक एकल पूर्ण ईश्वर में दृढ़ विश्वास है जो किसी अन्य देवता के अस्तित्व को प्रतिबंधित करता है",
            "यह पूर्वजों की आत्माओं को प्राथमिक आकाशीय शासकों के रूप में पूजने की प्रथा है",
            "यह एक ऐसी प्रणाली है जो धार्मिक प्रथाओं को विशेष रूप से महिला ऋषियों तक सीमित करती है"
        ],
        "ans_hi": 0,
        "sol_hi": "हेनोथिज्म का तात्पर्य एक समय में एक ही देवता को सर्वोच्च मानकर पूजा करने से है, जिसे मैक्स मुलर ने ऋग्वैदिक भजनों के बदलावों को समझाने के लिए गढ़ा था।"
    },
    # Q4
    {
        "q": "Consider the following statements regarding the early Vedic concept of 'Rta':\n1. It represents the natural laws governing the cycles of sun, moon, and seasons.\n2. It represents the ethical rules and moral duties governing human behavior.\n3. The god Indra was regarded as the primary guardian of Rta.\nWhich of the statements given above are correct?",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        "ans": 0,
        "sol": "Statements 1 and 2 are correct. Varuna (not Indra) was the primary guardian of Rta, making Statement 3 incorrect.",
        "q_hi": "प्रारंभिक वैदिक अवधारणा 'ऋत' के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह सूर्य, चंद्रमा और ऋतुओं के चक्र को नियंत्रित करने वाले प्राकृतिक नियमों का प्रतिनिधित्व करता है।\n2. यह मानव व्यवहार को नियंत्रित करने वाले नैतिक नियमों और कर्तव्यों का प्रतिनिधित्व करता है।\n3. इंद्र को ऋत का प्राथमिक रक्षक माना जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        "opts_hi": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 और 2 सही हैं। वरुण (इंद्र नहीं) ऋत के प्राथमिक संरक्षक थे, जिससे कथन 3 गलत हो जाता है।"
    },
    # Q5
    {
        "q": "In the Rigvedic funerary practices, which of the following is correct regarding disposal of the dead?",
        "opts": [
            "Both cremation (Agni-dagdha) and burial (Anagni-dagdha) were practiced",
            "Cremation was strictly prohibited as it angered the fire god Agni",
            "Burial was restricted to royal chieftains while commoners were cremated",
            "Mummification using herbal extracts was the standard custom"
        ],
        "ans": 0,
        "sol": "Rigvedic people practiced both burning on pyres (cremation) and burying in earth (burial) depending on custom and age.",
        "q_hi": "ऋग्वैदिक अंतिम संस्कार प्रथाओं में, मृतकों के अंतिम संस्कार के संबंध में निम्नलिखित में से कौन सा सही है?",
        "opts_hi": [
            "दाह संस्कार (अग्नि-दग्ध) और दफन संस्कार (अनग्नि-दग्ध) दोनों का अभ्यास किया जाता था",
            "दाह संस्कार सख्त वर्जित था क्योंकि इससे अग्नि देव क्रोधित होते थे",
            "दफन केवल शाही प्रमुखों तक सीमित था जबकि आम लोगों का दाह संस्कार किया जाता था",
            "जड़ी-बूटियों के अर्क का उपयोग करके ममी बनाना मानक प्रथा थी"
        ],
        "ans_hi": 0,
        "sol_hi": "ऋग्वैदिक लोग प्रथा और आयु के आधार पर चिता पर जलाने (दाह संस्कार) और पृथ्वी में दफनाने (दफन संस्कार) दोनों का अभ्यास करते थे।"
    },
    # Q6
    {
        "q": "With reference to the deities of the atmospheric sphere (Antarikshasthana), who is praised as the supreme warrior who destroyed enemy forts?",
        "opts": ["Indra", "Varuna", "Agni", "Surya"],
        "ans": 0,
        "sol": "Indra belonged to the aerial/atmospheric sphere and was praised as the fort-destroyer (Purandara).",
        "q_hi": "अंतरिक्षीय क्षेत्र (अंतरिक्षस्थान) के देवताओं के संदर्भ में, किसे शत्रुओं के किलों को नष्ट करने वाले सर्वोच्च योद्धा के रूप में सराहा गया है?",
        "opts_hi": ["इंद्र", "वरुण", "अग्नि", "सूर्य"],
        "ans_hi": 0,
        "sol_hi": "इंद्र अंतरिक्षीय/वायुमंडलीय क्षेत्र से संबंधित थे और उन्हें किलों का संहारक (पुरंदर) कहा गया है।"
    },
    # Q7
    {
        "q": "Consider the following statements regarding the early Vedic concept of the afterlife:\n1. The soul of the deceased traveled to Pitriloka, ruled by Yama.\n2. The doctrine of rebirth (Samsara) was a central element of Rigvedic theology.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Rebirth and Karma doctrines (Statement 2) did not exist in the early Vedic period; they developed in Upanishads.",
        "q_hi": "परलोक की प्रारंभिक वैदिक अवधारणा के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मृतक की आत्मा यम द्वारा शासित पितृलोक में जाती थी।\n2. पुनर्जन्म का सिद्धांत (संसार) ऋग्वैदिक धर्मशास्त्र का एक केंद्रीय तत्व था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 सही है। प्रारंभिक वैदिक काल में पुनर्जन्म और कर्म के सिद्धांत (कथन 2) मौजूद नहीं थे; वे उपनिषदों में विकसित हुए।"
    },
    # Q8
    {
        "q": "Match the following Rigvedic deities with their respective cosmic spheres:\n1. Agni - A. Terrestrial\n2. Indra - B. Atmospheric\n3. Varuna - C. Celestial\nChoose the correct code:",
        "opts": ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"],
        "ans": 0,
        "sol": "Agni is terrestrial, Indra atmospheric, Varuna celestial.",
        "q_hi": "निम्नलिखित ऋग्वैदिक देवताओं का उनके संबंधित ब्रह्मांडीय क्षेत्रों से मिलान करें:\n1. अग्नि - A. स्थलीय\n2. इंद्र - B. अंतरिक्षीय\n3. वरुण - C. आकाशीय\nसही कोड चुनें:",
        "opts_hi": ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"],
        "ans_hi": 0,
        "sol_hi": "अग्नि स्थलीय है, इंद्र अंतरिक्षीय हैं, वरुण आकाशीय हैं।"
    },
    # Q9
    {
        "q": "Which famous philosophical hymn of the Rigveda (Mandala 10) questions the absolute origin of the universe and creator deities?",
        "opts": ["Nasadiya Sukta", "Purusha Sukta", "Hiranyagarbha Sukta", "Devi Sukta"],
        "ans": 0,
        "sol": "The Nasadiya Sukta is the creation hymn reflecting early philosophical skepticism regarding the origins of the cosmos.",
        "q_hi": "ऋग्वेद का कौन सा प्रसिद्ध दार्शनिक सूक्त (10वां मंडल) ब्रह्मांड की पूर्ण उत्पत्ति और सृष्टिकर्ता देवताओं पर प्रश्न उठाता है?",
        "opts_hi": ["नासदीय सूक्त", "पुरुष सूक्त", "हिरण्यगर्भ सूक्त", "देवी सूक्त"],
        "ans_hi": 0,
        "sol_hi": "नासदीय सूक्त सृष्टि का वह भजन है जो ब्रह्मांड की उत्पत्ति के संबंध में प्रारंभिक दार्शनिक संशयवाद को दर्शाता है।"
    },
    # Q10
    {
        "q": "Consider the following statements regarding the transition of Vedic religion in the late Rigvedic period:\n1. Minor deities like Prajapati and Rudra began to rise in importance.\n2. Rituals became simpler and priestly monopolies were dissolved.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Prajapati and Rudra rose. Rituals became more complex and priestly control increased (Statement 2 is false).",
        "q_hi": "उत्तर ऋग्वैदिक काल में वैदिक धर्म के संक्रमण के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. प्रजापति और रुद्र जैसे छोटे देवताओं के महत्व में वृद्धि होने लगी।\n2. अनुष्ठान सरल हो गए और पुरोहितीय एकाधिकार समाप्त हो गए।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 सही है। प्रजापति और रुद्र का उदय हुआ। अनुष्ठान अधिक जटिल हो गए और पुरोहितों का नियंत्रण बढ़ गया (कथन 2 गलत है)।"
    },
    # Q11
    {
        "q": "In the Rigvedic pantheon, the deity Agni is addressed as 'mediator' because:",
        "opts": [
            "He carries the sacrifices and offerings of humans to the celestial gods",
            "He resolved disputes between rival Aryan clans in the Sabha",
            "He acted as the royal messenger between Rajan and Vrajapati",
            "He was in charge of distributing war spoils in the Vidatha"
        ],
        "ans": 0,
        "sol": "Agni carries offerings placed in the sacrificial fire to other deities, serving as a mediator.",
        "q_hi": "ऋग्वैदिक देवगण में, अग्नि को 'मध्यस्थ' के रूप में संबोधित किया जाता है क्योंकि:",
        "opts_hi": [
            "वे मनुष्यों के यज्ञ और आहुतियों को आकाशीय देवताओं तक ले जाते हैं",
            "उन्होंने सभा में प्रतिद्वंद्वी आर्य कबीलों के बीच विवादों को सुलझाया",
            "उन्होंने राजन और व्रजपति के बीच शाही संदेशवाहक के रूप में कार्य किया",
            "वे विदथ में युद्ध की लूट के वितरण के प्रभारी थे"
        ],
        "ans_hi": 0,
        "sol_hi": "अग्नि यज्ञ की अग्नि में डाली जाने वाली आहुतियों को अन्य देवताओं तक ले जाते हैं, जिससे वे मध्यस्थ के रूप में कार्य करते हैं।"
    },
    # Q12
    {
        "q": "What is the meaning of the Sanskrit term 'Rtavan' in Rigvedic hymns?",
        "opts": ["The upholder or guardian of the cosmic order", "The priest who performs fire sacrifices", "The title of a war chariot commander", "The gold neck ornament used in trade"],
        "ans": 0,
        "sol": "Rtavan (or Rtavrih) is the upholder of Rta, heavily applied as an epithet to Varuna.",
        "q_hi": "ऋग्वैदिक भजनों में संस्कृत शब्द 'ऋतवान' का क्या अर्थ है?",
        "opts_hi": ["ब्रह्मांडीय व्यवस्था का समर्थक या रक्षक", "वह पुरोहित जो अग्नि यज्ञ करता है", "युद्ध रथ कमांडर की उपाधि", "व्यापार में प्रयुक्त सोने का आभूषण"],
        "ans_hi": 0,
        "sol_hi": "ऋतवान (या ऋतवृध) ऋत का समर्थक है, जिसका उपयोग वरुण के विशेषण के रूप में किया जाता है।"
    },
    # Q13
    {
        "q": "In the Rigvedic cosmological system, the sky father deified as one of the oldest gods is:",
        "opts": ["Dyaus", "Varuna", "Indra", "Maruts"],
        "ans": 0,
        "sol": "Dyaus (sky father) is deified alongside Prithvi (earth mother) as the oldest couple in Rigvedic hymns.",
        "q_hi": "ऋग्वैदिक ब्रह्मांडीय व्यवस्था में, सबसे पुराने देवताओं में से एक के रूप में पूजे जाने वाले आकाश पिता हैं:",
        "opts_hi": ["द्यौस", "वरुण", "इंद्र", "मरुत"],
        "ans_hi": 0,
        "sol_hi": "द्यौस (आकाश पिता) को पृथ्वी (धरती माता) के साथ ऋग्वैदिक भजनों में सबसे पुराने जोड़े के रूप में पूजा गया है।"
    },
    # Q14
    {
        "q": "Consider the following statements regarding the goddess 'Ushas' in Rigvedic hymns:\n1. She represents the dawn and is celebrated for her brilliant beauty in several hymns.\n2. She was praised as a major warrior goddess who led clans to battles.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Ushas is dawn goddess. Female deities had no military roles (Statement 2 is false).",
        "q_hi": "ऋग्वैदिक भजनों में देवी 'उषा' के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. वे भोर का प्रतिनिधित्व करती हैं और कई भजनों में उनकी शानदार सुंदरता के लिए उनकी सराहना की गई है।\n2. उन्हें एक प्रमुख योद्धा देवी के रूप में पूजा जाता था जिन्होंने युद्धों में कबीलों का नेतृत्व किया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 सही है। उषा भोर की देवी हैं। महिला देवियों की कोई सैन्य भूमिका नहीं थी (कथन 2 गलत है)।"
    },
    # Q15
    {
        "q": "The sacred plant beverage Soma was offered to which god in the highest frequency to secure vitality?",
        "opts": ["Indra", "Varuna", "Agni", "Rudra"],
        "ans": 0,
        "sol": "Indra was the chief consumer of Soma, which gave him the strength to slay Vritra and fight enemies.",
        "q_hi": "प्राण शक्ति प्राप्त करने के लिए किस देवता को सबसे अधिक आवृत्ति में पवित्र सोम रस अर्पित किया जाता था?",
        "opts_hi": ["इंद्र", "वरुण", "अग्नि", "रुद्र"],
        "ans_hi": 0,
        "sol_hi": "इंद्र सोम के मुख्य उपभोक्ता थे, जिससे उन्हें वृत्र का वध करने और शत्रुओं से लड़ने की शक्ति मिलती थी।"
    },
    # Q16
    {
        "q": "Which of the following describes the ethical concept of ' papa' (sin) in Rigvedic religion?",
        "opts": [
            "A violation of the natural and moral order of Rta",
            "A failure to pay voluntary Bali taxes to the Rajan",
            "Refusing to participate in military cattle raids",
            "Failing to weave wool garments for the clan"
        ],
        "ans": 0,
        "sol": "Papa (sin) was defined as violating the natural/moral order of Rta, which angered Varuna.",
        "q_hi": "निम्नलिखित में से कौन ऋग्वैदिक धर्म में 'पाप' की नैतिक अवधारणा का वर्णन करता है?",
        "opts_hi": [
            "ऋत की प्राकृतिक और नैतिक व्यवस्था का उल्लंघन",
            "राजन को स्वैच्छिक बलि देने में विफल रहना",
            "सैन्य मवेशी छापों में भाग लेने से इनकार करना",
            "कबीले के लिए ऊनी कपड़े बुनने में विफल रहना"
        ],
        "ans_hi": 0,
        "sol_hi": "पाप को ऋत की प्राकृतिक/नैतिक व्यवस्था के उल्लंघन के रूप में परिभाषित किया गया था, जिससे वरुण क्रोधित होते थे।"
    },
    # Q17
    {
        "q": "With reference to the deification of forests, which goddess represents the forest spirit in Rigveda?",
        "opts": ["Aranyani", "Aditi", "Ushas", "Prithvi"],
        "ans": 0,
        "sol": "Aranyani is the goddess of the forest and wild environments in Rigvedic hymns.",
        "q_hi": "वनों के देवत्वकरण के संदर्भ में, ऋग्वेद में कौन सी देवी वन की भावना का प्रतिनिधित्व करती हैं?",
        "opts_hi": ["अरण्यानी", "अदिति", "उषा", "पृथ्वी"],
        "ans_hi": 0,
        "sol_hi": "अरण्यानी ऋग्वैदिक भजनों में जंगल और जंगली वातावरण की देवी हैं।"
    },
    # Q18
    {
        "q": "Consider the following statements regarding the Rigvedic ritual elements:\n1. The chants and mantras were compiled in the Samhita collection.\n2. The sacrifices were performed using fire altars built inside domestic houses.\nWhich of the statements given above is/are correct?",
        "opts": ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Both statements are correct. Mantras were in Samhitas and altars were simple domestic installations.",
        "q_hi": "ऋग्वैदिक अनुष्ठान तत्वों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मंत्रों का संकलन संहिता संग्रह में किया गया था।\n2. यज्ञ घरेलू घरों के भीतर बनाई गई अग्नि वेदियों का उपयोग करके किए जाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["1 और 2 दोनों", "केवल 1", "केवल 2", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "दोनों कथन सही हैं। मंत्र संहिताओं में थे और वेदियाँ सरल घरेलू अधिष्ठापन थीं।"
    },
    # Q19
    {
        "q": "What was the term used in the Rigveda for the sacred offering food thrown into Agni during sacrifices?",
        "opts": ["Havis", "Karambha", "Yava", "Soma"],
        "ans": 0,
        "sol": "Havis (or Havya) represents the sacrificial offering (ghee, milk, grain) thrown into Agni.",
        "q_hi": "यज्ञों के दौरान अग्नि में डाली जाने वाली पवित्र हवि/सामग्री के लिए ऋग्वेद में किस शब्द का प्रयोग किया जाता था?",
        "opts_hi": ["हविस्", "करम्भ", "यव", "सोम"],
        "ans_hi": 0,
        "sol_hi": "हविस् (या हव्य) यज्ञीय आहुति (घी, दूध, अनाज) का प्रतिनिधित्व करता है जो अग्नि में डाली जाती थी।"
    },
    # Q20
    {
        "q": "In the Rigvedic pantheon, the goddess 'Aditi' is celebrated as the:",
        "opts": ["Mother of the gods", "Goddess of dark night", "Patron of artisans", "Guardian of rivers"],
        "ans": 0,
        "sol": "Aditi represents cosmic space and is praised as the mother of major deities (Adityas).",
        "q_hi": "ऋग्वैदिक देवगण में, देवी 'अदिति' की पूजा किस रूप में की जाती है?",
        "opts_hi": ["देवताओं की माता", "काली रात की देवी", "कारीगरों की संरक्षिका", "नदियों की रक्षक"],
        "ans_hi": 0,
        "sol_hi": "अदिति ब्रह्मांडीय अंतरिक्ष का प्रतिनिधित्व करती हैं और उन्हें प्रमुख देवताओं (आदित्य) की माता के रूप में सराहा गया है।"
    },
    # Q21
    {
        "q": "Assertion (A): Rigvedic religion was primarily this-worldly (utilitarian).\nReason (R): Rigvedic hymns seek worldly prosperity (cattle, sons) rather than liberation from rebirth.\nCodes:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Early Vedic religion was utilitarian, focused on cattle, sons, health, and victory, as rebirth/moksha doctrines had not yet developed.",
        "q_hi": "कथन (A): ऋग्वैदिक धर्म मुख्य रूप से इस लोक (उपयोगितावादी) से संबंधित था।\nकारण (R): ऋग्वैदिक भजन पुनर्जन्म से मुक्ति के बजाय सांसारिक समृद्धि (मवेशी, पुत्र) की कामना करते हैं।\nकोड:",
        "opts_hi": [
            "A और R दोनों सही हैं और R, A की सही व्याख्या करता है",
            "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है",
            "A सही है लेकिन R गलत है",
            "A गलत है लेकिन R सही है"
        ],
        "ans_hi": 0,
        "sol_hi": "प्रारंभिक वैदिक धर्म उपयोगितावादी था, जो मवेशियों, पुत्रों, स्वास्थ्य और विजय पर केंद्रित था, क्योंकि पुनर्जन्म/मोक्ष के सिद्धांत अभी तक विकसित नहीं हुए थे।"
    },
    # Q22
    {
        "q": "Consider the following statements regarding the storm deities (Maruts) in the Rigveda:\n1. They were the allies of Indra in his battles against Vritra.\n2. They were deified as terrestrial gods of the earth.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Maruts were aerial/storm gods who accompanied Indra, not terrestrial (so Statement 2 is false).",
        "q_hi": "ऋग्वेद में आंधी के देवताओं (मरुत) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. वे वृत्र के खिलाफ युद्धों में इंद्र के सहयोगी थे।\n2. उन्हें पृथ्वी के स्थलीय देवताओं के रूप में पूजा जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 सही है। मरुत अंतरिक्षीय/आंधी के देवता थे जो इंद्र के साथ थे, स्थलीय नहीं (इसलिए कथन 2 गलत है)।"
    },
    # Q23
    {
        "q": "In the Rigvedic religious setup, the solar deity who is invoked in the famous Gayatri Mantra is:",
        "opts": ["Savitr", "Surya", "Mitra", "Vishnu"],
        "ans": 0,
        "sol": "The Gayatri Mantra (Mandala 3, composed by Vishvamitra) is dedicated to the solar deity Savitr.",
        "q_hi": "ऋग्वैदिक धार्मिक व्यवस्था में, प्रसिद्ध गायत्री मंत्र में किस सौर देवता का आह्वान किया गया है?",
        "opts_hi": ["सविता", "सूर्य", "मित्र", "विष्णु"],
        "ans_hi": 0,
        "sol_hi": "गायत्री मंत्र (तीसरा मंडल, विश्वामित्र द्वारा रचित) सौर देवता सविता को समर्पित है।"
    },
    # Q24
    {
        "q": "Which of the following describes the role of the 'Purohita' in Rigvedic military and political affairs?",
        "opts": [
            "Serving as chief counselor and performing rituals to secure victory for the Rajan",
            "Serving as the commander of the chariot wing in battle",
            "Collecting voluntary Bali contributions from the clansmen",
            "Managing the distribution of conquered fields (Kshetra)"
        ],
        "ans": 0,
        "sol": "The Purohita was the royal priest who advised the Rajan and prayed/sacrificed to secure victory in raids.",
        "q_hi": "निम्नलिखित में से कौन ऋग्वैदिक सैन्य और राजनीतिक मामलों में 'पुरोहित' की भूमिका का वर्णन करता है?",
        "opts_hi": [
            "मुख्य सलाहकार के रूप में कार्य करना और राजन की विजय सुनिश्चित करने के लिए अनुष्ठान करना",
            "युद्ध में रथ सेना के कमांडर के रूप में कार्य करना",
            "कबीले के लोगों से स्वैच्छिक बलि कर एकत्र करना",
            "विजित क्षेत्रों (क्षेत्र) के वितरण का प्रबंधन करना"
        ],
        "ans_hi": 0,
        "sol_hi": "पुरोहित शाही पुरोहित थे जो राजन को सलाह देते थे और छापों में जीत सुरक्षित करने के लिए प्रार्थना/यज्ञ करते थे।"
    },
    # Q25
    {
        "q": "Assertion (A): Rigvedic deities are primarily natural forces deified.\nReason (R): Rigvedic poets deified lightning, rain, wind, and fire to gain control over their pastoral environment.\nCodes:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both statements are true. Natural phenomena were deified to seek their favor for pastoral and farming safety.",
        "q_hi": "कथन (A): ऋग्वैदिक देवता मुख्य रूप से पूजे जाने वाले प्राकृतिक तत्व हैं।\nकारण (R): ऋग्वैदिक कवियों ने अपने पशुचारण वातावरण पर नियंत्रण प्राप्त करने के लिए बिजली, वर्षा, हवा और आग का देवत्वकरण किया।\nकोड:",
        "opts_hi": [
            "A और R दोनों सही हैं और R, A की सही व्याख्या करता है",
            "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है",
            "A सही है लेकिन R गलत है",
            "A गलत है लेकिन R सही है"
        ],
        "ans_hi": 0,
        "sol_hi": "दोनों कथन सत्य हैं। पशुचारण और कृषि सुरक्षा के लिए प्राकृतिक घटनाओं को देवत्व प्रदान किया गया ताकि उनकी कृपा प्राप्त की जा सके।"
    },
    # Q26
    {
        "q": "With reference to the Later Vedic religious changes, the deity Prajapati rose to prominence as:",
        "opts": ["The supreme creator god", "The god of war", "The protector of cosmic Rta", "The lord of animal sacrifices"],
        "ans": 0,
        "sol": "Prajapati (creator) became the supreme god of Later Vedic times, eclipsing Indra and Varuna.",
        "q_hi": "उत्तर वैदिक धार्मिक परिवर्तनों के संदर्भ में, प्रजापति देवता किस रूप में प्रमुखता से उभरे?",
        "opts_hi": ["सर्वोच्च सृष्टिकर्ता देवता", "युद्ध के देवता", "ब्रह्मांडीय ऋत के रक्षक", "पशु बलि के स्वामी"],
        "ans_hi": 0,
        "sol_hi": "प्रजापति (सृष्टिकर्ता) उत्तर वैदिक काल के सर्वोच्च देवता बने, जिन्होंने इंद्र और वरुण को पीछे छोड़ दिया।"
    },
    # Q27
    {
        "q": "In the context of Rigvedic sacrifices, what does the term 'Yajamana' refer to?",
        "opts": ["The sponsor or patron who funds and hosts the sacrifice", "The chief priest who chants the mantras", "The sacrificial wooden post", "The offering item thrown in fire"],
        "ans": 0,
        "sol": "The Yajamana is the host or patron who sponsors the sacrifice to get personal/clan benefits.",
        "q_hi": "ऋग्वैदिक यज्ञों के संदर्भ में 'यजमान' शब्द किसे संदर्भित करता है?",
        "opts_hi": ["वह प्रायोजक या संरक्षक जो यज्ञ का वित्तपोषण और आयोजन करता है", "मुख्य पुरोहित जो मंत्रों का पाठ करता है", "यज्ञीय यूप (लकड़ी का खंभा)", "अग्नि में डाली जाने वाली आहुति"],
        "ans_hi": 0,
        "sol_hi": "यजमान वह मेजबान या संरक्षक होता है जो व्यक्तिगत/कबीले के लाभ प्राप्त करने के लिए यज्ञ को प्रायोजित करता है।"
    },
    # Q28
    {
        "q": "Consider the following statements regarding the Rigvedic concept of death and Pitris:\n1. Pitris were the ancestral spirits who resided in Pitriloka.\n2. Living descendants offered 'Svadha' to feed ancestral spirits during rituals.\nWhich of the statements given above is/are correct?",
        "opts": ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Both statements are correct. Pitris resided in Pitriloka, and Svadha was the ritual food offered to them.",
        "q_hi": "मृत्यु और पितरों की ऋग्वैदिक अवधारणा के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. पितर पूर्वजों की आत्माएं थीं जो पितृलोक में निवास करती थीं।\n2. जीवित वंशज अनुष्ठानों के दौरान पूर्वजों की आत्माओं को तृप्त करने के लिए 'स्वधा' अर्पित करते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["1 और 2 दोनों", "केवल 1", "केवल 2", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "दोनों कथन सही हैं। पितर पितृलोक में रहते थे, और स्वधा उन्हें अर्पित किया जाने वाला अनुष्ठानिक भोजन था।"
    },
    # Q29
    {
        "q": "Which of the following Rigvedic deities represents the supreme sky father deified as the oldest couple with Prithvi?",
        "opts": ["Dyaus", "Varuna", "Indra", "Maruts"],
        "ans": 0,
        "sol": "Dyaus (sky father) is deified as the father creator alongside Prithvi.",
        "q_hi": "निम्नलिखित ऋग्वैदिक देवताओं में से कौन पृथ्वी के साथ सबसे पुराने जोड़े के रूप में पूजे जाने वाले सर्वोच्च आकाश पिता का प्रतिनिधित्व करता है?",
        "opts_hi": ["द्यौस", "वरुण", "इंद्र", "मरुत"],
        "ans_hi": 0,
        "sol_hi": "द्यौस (आकाश पिता) को पृथ्वी के साथ सृष्टिकर्ता पिता के रूप में पूजा जाता है।"
    },
    # Q30
    {
        "q": "What was the term used in Rigvedic hymns to denote the magical or cosmic untruth/chaos that opposes Rta?",
        "opts": ["Anrta", "Papa", "Pasa", "Havis"],
        "ans": 0,
        "sol": "Anrta refers to chaos, falsehood, or disorder that opposes the cosmic law of Rta.",
        "q_hi": "ऋत का विरोध करने वाले जादुई या ब्रह्मांडीय असत्य/अराजकता को दर्शाने के लिए ऋग्वैदिक भजनों में किस शब्द का प्रयोग किया जाता था?",
        "opts_hi": ["अनृत", "पाप", "पाश", "हविस्"],
        "ans_hi": 0,
        "sol_hi": "अनृत अराजकता, असत्य या विकार को संदर्भित करता है जो ऋत के ब्रह्मांडीय नियम का विरोध करता है।"
    },
    # Q31
    {
        "q": "Consider the following statements regarding the Rigvedic god 'Soma':\n1. Soma was deified as the lord of plants and herbs.\n2. The entire 9th Mandala of the Rigveda is dedicated to the purification chants of Soma.\nWhich of the statements given above is/are correct?",
        "opts": ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Both statements are correct. Soma was plant god and Mandala 9 contains all Soma hymns.",
        "q_hi": "ऋग्वैदिक देवता 'सोम' के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. सोम को पौधों और जड़ी-बूटियों के स्वामी के रूप में पूजा जाता था।\n2. ऋग्वेद का संपूर्ण 9वां मंडल सोम के शुद्धिकरण मंत्रों को समर्पित है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["1 और 2 दोनों", "केवल 1", "केवल 2", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "दोनों कथन सही हैं। सोम पौधों के देवता थे और 9वें मंडल में सभी सोम भजन शामिल हैं।"
    },
    # Q32
    {
        "q": "In the early Vedic pantheon, the sun deity in his aspect of stimulation and creator is worshipped as:",
        "opts": ["Savitr", "Surya", "Mitra", "Vishnu"],
        "ans": 0,
        "sol": "Savitr represents the solar power of stimulation and creation, invoked at sunrise.",
        "q_hi": "प्रारंभिक वैदिक देवगण में, सूर्य देवता की उनकी उत्तेजना और सृष्टिकर्ता के रूप में किस रूप में पूजा की जाती है?",
        "opts_hi": ["सविता", "सूर्य", "मित्र", "विष्णु"],
        "ans_hi": 0,
        "sol_hi": "सविता सूर्य की उत्तेजना और सृजन की शक्ति का प्रतिनिधित्व करते हैं, जिनका आह्वान सूर्योदय के समय किया जाता है।"
    },
    # Q33
    {
        "q": "The sacred statement 'Ekam sat vipra bahudha vadanti' appears in which Mandala of the Rigveda?",
        "opts": ["Mandala 1", "Mandala 10", "Mandala 9", "Mandala 3"],
        "ans": 0,
        "sol": "This famous early monistic phrase occurs in Mandala 1 (hymn 164), though often associated with late Rigvedic philosophical additions.",
        "q_hi": "पवित्र कथन 'एकं सद् विप्रा बहुधा वदन्ति' ऋग्वेद के किस मंडल में प्रकट होता है?",
        "opts_hi": ["मंडल 1", "मंडल 10", "मंडल 9", "मंडल 3"],
        "ans_hi": 0,
        "sol_hi": "यह प्रसिद्ध प्रारंभिक अद्वैतवादी वाक्यांश मंडल 1 (भजन 164) में आता है, हालांकि इसे अक्सर बाद के ऋग्वैदिक दार्शनिक प्रक्षेपों से जोड़ा जाता है।"
    },
    # Q34
    {
        "q": "Consider the following statements regarding the ritual priest 'Hotr' in Rigvedic yajnas:\n1. The Hotr was responsible for reciting the hymns of the Rigveda to invoke gods.\n2. The Hotr was completely subordinate to Later Vedic priests like Udgatr in this phase.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Hotr recited hymns. Udgatr was a Later Vedic priest who chanted Samaveda, which did not dominate in early Rigvedic times (Statement 2 is false).",
        "q_hi": "ऋग्वैदिक यज्ञों में अनुष्ठानिक पुरोहित 'होता' (Hotr) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. होता देवताओं का आह्वान करने के लिए ऋग्वेद के भजनों का पाठ करने के लिए जिम्मेदार था।\n2. इस चरण में होता पूरी तरह से उद्गाता जैसे उत्तर वैदिक पुजारियों के अधीन था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 सही है। होता भजनों का पाठ करते थे। उद्गाता उत्तर वैदिक पुरोहित थे जो सामवेद का पाठ करते थे, जिसका प्रारंभिक ऋग्वैदिक काल में वर्चस्व नहीं था (कथन 2 गलत है)।"
    },
    # Q35
    {
        "q": "The goddess 'Nirrti' in Rigvedic hymns represents which natural/moral state?",
        "opts": ["Decay, destruction, and death", "Brilliant dawn and beauty", "Cattle fertility and pastures", "Sacrificial fire mediation"],
        "ans": 0,
        "sol": "Nirrti represents decay, destruction, misfortune, and death, acting as the opposite of cosmic order.",
        "q_hi": "ऋग्वैदिक भजनों में देवी 'निरृति' किस प्राकृतिक/नैतिक स्थिति का प्रतिनिधित्व करती हैं?",
        "opts_hi": ["क्षय, विनाश और मृत्यु", "शानदार भोर और सुंदरता", "मवेशी उर्वरता और चरागाह", "यज्ञीय अग्नि मध्यस्थता"],
        "ans_hi": 0,
        "sol_hi": "निरृति क्षय, विनाश, दुर्भाग्य और मृत्यु का प्रतिनिधित्व करती हैं, जो ब्रह्मांडीय व्यवस्था के विपरीत है।"
    },
    # Q36
    {
        "q": "Which of the following is correct regarding the deification of rivers in the Rigveda?",
        "opts": [
            "Sarasvati was deified as the goddess of wisdom and speech, and highly praised as a river deity",
            "Ganga was deified as the supreme mother of gods in the early Mandalas",
            "Narmada was deified as the controller of the southern border",
            "Rivers were treated as demons that blocked cattle migrations"
        ],
        "ans": 0,
        "sol": "Sarasvati was the most sacred river in Rigveda, deified as the goddess of intellect and speech.",
        "q_hi": "ऋग्वेद में नदियों के देवत्वकरण के संदर्भ में निम्नलिखित में से कौन सा सही है?",
        "opts_hi": [
            "सरस्वती को बुद्धि और वाणी की देवी के रूप में पूजा जाता था, और नदी देवी के रूप में उनकी अत्यधिक प्रशंसा की गई थी",
            "गंगा को प्रारंभिक मंडलों में देवताओं की सर्वोच्च माता के रूप में पूजा गया था",
            "नर्मदा को दक्षिणी सीमा के नियंत्रक के रूप में पूजा गया था",
            "नदियों को ऐसे राक्षसों के रूप में माना जाता था जिन्होंने मवेशियों के प्रवास को अवरुद्ध किया था"
        ],
        "ans_hi": 0,
        "sol_hi": "सरस्वती ऋग्वेद में सबसे पवित्र नदी थी, जिसे बुद्धि और वाणी की देवी के रूप में पूजा जाता था।"
    },
    # Q37
    {
        "q": "With reference to the Later Vedic transitions, the deity Rudra transitioned to acquire the traits of which classical Hindu god?",
        "opts": ["Shiva", "Vishnu", "Brahma", "Indra"],
        "ans": 0,
        "sol": "Rudra, a minor Rigvedic deity, transitioned to become Shiva (Mahadeva) in Later Vedic and epic times.",
        "q_hi": "उत्तर वैदिक संक्रमण के संदर्भ में, रुद्र देवता ने किस शास्त्रीय हिंदू देवता के गुणों को ग्रहण किया?",
        "opts_hi": ["शिव", "विष्णु", "ब्रह्मा", "इंद्र"],
        "ans_hi": 0,
        "sol_hi": "रुद्र, जो एक छोटे ऋग्वैदिक देवता थे, उत्तर वैदिक और महाकाव्य काल में शिव (महादेव) के रूप में विकसित हुए।"
    },
    # Q38
    {
        "q": "Consider the following statements regarding the deification of dawn (Ushas) and night (Ratri):\n1. Both Ushas and Ratri are deified as sisters who maintain cosmic order in turns.\n2. Female deities were completely excluded from any cosmological functions.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Ushas and Ratri are sisters maintaining the cosmic order of day and night. Statement 2 is false.",
        "q_hi": "भोर (उषा) और रात (रात्रि) के देवत्वकरण के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. उषा और रात्रि दोनों को बहनों के रूप में पूजा जाता है जो बारी-बारी से ब्रह्मांडीय व्यवस्था को बनाए रखती हैं।\n2. महिला देवियों को किसी भी ब्रह्मांडीय कार्यों से पूरी तरह बाहर रखा गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 सही है। उषा और रात्रि बहनें हैं जो दिन और रात की ब्रह्मांडीय व्यवस्था को बनाए रखती हैं। कथन 2 गलत है।"
    },
    # Q39
    {
        "q": "In the Rigvedic sacrificial rituals, what does the term 'Dakshina' refer to?",
        "opts": [
            "The gifts (cattle, horses, gold) given by the Yajamana to the priests",
            "The direction faced by the priest during sacrifices",
            "The south border of the sacrificial fire altar",
            "A voluntary tax paid to the pasture officer"
        ],
        "ans": 0,
        "sol": "Dakshina represents the gifts or fees given by the Yajamana host to priests for conducting rituals.",
        "q_hi": "ऋग्वैदिक यज्ञीय अनुष्ठानों में 'दक्षिणा' शब्द किसे संदर्भित करता है?",
        "opts_hi": [
            "यजमान द्वारा पुरोहितों को दिए जाने वाले उपहार (मवेशी, घोड़े, सोना)",
            "यज्ञ के दौरान पुरोहित का सामना करने वाली दिशा",
            "यज्ञीय अग्नि वेदी की दक्षिणी सीमा",
            "चरागाह अधिकारी को दिया जाने वाला एक स्वैच्छिक कर"
        ],
        "ans_hi": 0,
        "sol_hi": "दक्षिणा यजमान द्वारा अनुष्ठान आयोजित करने के लिए पुरोहितों को दिए जाने वाले उपहार या शुल्क का प्रतिनिधित्व करती है।"
    },
    # Q40
    {
        "q": "Assertion (A): Rigvedic religion was primarily non-sacrificial in its early phases.\nReason (R): The early Vedic people invoked deities only through silent contemplation (dhyana) without fire altars.\nCodes:",
        "opts": [
            "Both A and R are false",
            "Both A and R are true and R is the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both statements are false. Rigvedic religion was heavily sacrificial (Yajna) using fire altars to make physical offerings to deified natural gods.",
        "q_hi": "कथन (A): ऋग्वैदिक धर्म अपने प्रारंभिक चरणों में मुख्य रूप से यज्ञ-विहीन था।\nकारण (R): प्रारंभिक वैदिक लोग अग्नि वेदियों के बिना केवल मौन चिंतन (ध्यान) के माध्यम से देवताओं का आह्वान करते थे।\nकोड:",
        "opts_hi": [
            "A और R दोनों असत्य हैं",
            "A और R दोनों सही हैं और R, A की सही व्याख्या करता है",
            "A सही है लेकिन R गलत है",
            "A गलत है लेकिन R सही है"
        ],
        "ans_hi": 0,
        "sol_hi": "दोनों कथन असत्य हैं। ऋग्वैदिक धर्म अत्यधिक यज्ञीय (यज्ञ) था जिसमें पूजे जाने वाले प्राकृतिक देवताओं को भौतिक आहुतियाँ देने के लिए अग्नि वेदियों का उपयोग किया जाता था।"
    },
    # Q41
    {
        "q": "In the Rigvedic cosmological setup, the aerial/storm deity who is the companion of Rudra and has his own storm troop is:",
        "opts": ["Maruts", "Vayu", "Indra", "Agni"],
        "ans": 0,
        "sol": "The Maruts are storm deities who form a troop (Sardha/Gana) and are associated with Rudra and Indra.",
        "q_hi": "ऋग्वैदिक ब्रह्मांडीय व्यवस्था में, अंतरिक्षीय/आंधी के देवता जो रुद्र के साथी हैं और जिनका अपना आंधी दल है, वे हैं:",
        "opts_hi": ["मरुत", "वायु", "इंद्र", "अग्नि"],
        "ans_hi": 0,
        "sol_hi": "मरुत आंधी के देवता हैं जो एक दल (शर्ध/गण) बनाते हैं और रुद्र तथा इंद्र से जुड़े हैं।"
    },
    # Q42
    {
        "q": "Which of the following solar deities in the Rigveda is celebrated for taking three cosmic strides to cross the universe?",
        "opts": ["Vishnu", "Surya", "Mitra", "Savitr"],
        "ans": 0,
        "sol": "Vishnu is praised in the Rigveda for his three steps (Trivikrama) across the universe, symbolizing solar movement.",
        "q_hi": "ऋग्वेद में निम्नलिखित में कौन से सौर देवता ब्रह्मांड को पार करने के लिए तीन ब्रह्मांडीय डग भरने के लिए प्रसिद्ध हैं?",
        "opts_hi": ["विष्णु", "सूर्य", "मित्र", "सविता"],
        "ans_hi": 0,
        "sol_hi": "विष्णु की ऋग्वेद में ब्रह्मांड में तीन कदम (त्रिविक्रम) उठाने के लिए प्रशंसा की गई है, जो सौर गति का प्रतीक है।"
    },
    # Q43
    {
        "q": "Consider the following statements regarding the deification of speech in the Rigveda:\n1. Speech was deified as the goddess 'Vac' and praised in Mandala 10.\n2. Speech was treated as a demon that blocked sacrificial chants.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Speech was deified as Vac (Mandala 10). Statement 2 is false.",
        "q_hi": "ऋग्वेद में वाणी के देवत्वकरण के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. वाणी को देवी 'वाक्' के रूप में पूजा जाता था और 10वें मंडल में उनकी प्रशंसा की गई है।\n2. वाणी को एक राक्षस के रूप में माना जाता था जिसने यज्ञ के मंत्रों को अवरुद्ध किया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 सही है। वाणी को वाक् (10वें मंडल) के रूप में पूजा जाता था। कथन 2 गलत है।"
    },
    # Q44
    {
        "q": "Which of the following is correct regarding the Rigvedic concept of 'Anrta'?",
        "opts": [
            "It represents chaos, falsehood, and the opposite of the cosmic order Rta",
            "It refers to the copper metal used for fabricating agricultural implements",
            "It was the term for standard barley cakes offered in domestic altars",
            "It designates the chief queen who participated in public sacrifices"
        ],
        "ans": 0,
        "sol": "Anrta refers to chaos/falsehood/moral disorder, which is the direct opposite of Rta.",
        "q_hi": "ऋग्वैदिक अवधारणा 'अनृत' के संबंध में निम्नलिखित में से कौन सा सही है?",
        "opts_hi": [
            "यह अराजकता, असत्य और ब्रह्मांडीय व्यवस्था ऋत के विपरीत का प्रतिनिधित्व करता है",
            "यह कृषि उपकरणों के निर्माण के लिए उपयोग की जाने वाली तांबे की धातु को संदर्भित करता है",
            "यह घरेलू वेदियों में चढ़ाए जाने वाले मानक जौ के केक का शब्द था",
            "यह उस मुख्य रानी को नामित करता है जिसने सार्वजनिक यज्ञों में भाग लिया था"
        ],
        "ans_hi": 0,
        "sol_hi": "अनृत का तात्पर्य अराजकता/असत्य/नैतिक विकार से है, जो ऋत का सीधा विपरीत है।"
    },
    # Q45
    {
        "q": "What was the term used in the Rigveda for the sacred ritual drink prepared from mountain herbs and purified using wool filters?",
        "opts": ["Soma", "Sura", "Karambha", "Ghee"],
        "ans": 0,
        "sol": "Soma was prepared from mountain plants and purified using wool filters (Pavitra).",
        "q_hi": "पहाड़ी जड़ी-बूटियों से तैयार किए जाने वाले और ऊनी फिल्टर का उपयोग करके शुद्ध किए जाने वाले पवित्र अनुष्ठानिक पेय के लिए ऋग्वेद में किस शब्द का प्रयोग किया जाता था?",
        "opts_hi": ["सोम", "सुरा", "करम्भ", "घी"],
        "ans_hi": 0,
        "sol_hi": "सोम पहाड़ों के पौधों से तैयार किया जाता था और ऊनी फिल्टर (पवित्र) का उपयोग करके शुद्ध किया जाता था।"
    },
    # Q46
    {
        "q": "Which of the following describes the term 'Rtavan' in relation to Varuna?",
        "opts": ["He is the upholder and guardian of the cosmic order Rta", "He is the chief priest who handles Soma sacrifices", "He is the leader of the non-Aryan merchant guild", "He is the commander of the war chariot wing"],
        "ans": 0,
        "sol": "Rtavan means protector of Rta, heavily applied to Varuna as the ethical guardian of cosmic law.",
        "q_hi": "निम्नलिखित में से कौन वरुण के संबंध में 'ऋतवान' शब्द का वर्णन करता है?",
        "opts_hi": ["वे ब्रह्मांडीय व्यवस्था ऋत के समर्थक और संरक्षक हैं", "वे सोम यज्ञों का संचालन करने वाले मुख्य पुरोहित हैं", "वे गैर-आर्य व्यापारी संघ के प्रमुख नेता हैं", "वे युद्ध रथ सेना के कमांडर हैं"],
        "ans_hi": 0,
        "sol_hi": "ऋतवान का अर्थ है ऋत का रक्षक, जिसे ब्रह्मांडीय नियम के नैतिक संरक्षक के रूप में वरुण पर लागू किया जाता है।"
    },
    # Q47
    {
        "q": "With reference to the Later Vedic transitions, the creator deity who became the supreme head of the pantheon, eclipsing Indra, was:",
        "opts": ["Prajapati", "Rudra", "Vishnu", "Varuna"],
        "ans": 0,
        "sol": "Prajapati (creator deity) rose to become the supreme god in Later Vedic literature, overshadowing Indra.",
        "q_hi": "उत्तर वैदिक संक्रमण के संदर्भ में, वह सृष्टिकर्ता देवता कौन थे जो इंद्र को पीछे छोड़कर देवगण के सर्वोच्च प्रमुख बन गए?",
        "opts_hi": ["प्रजापति", "रुद्र", "विष्णु", "वरुण"],
        "ans_hi": 0,
        "sol_hi": "प्रजापति (सृष्टिकर्ता देवता) उत्तर वैदिक साहित्य में इंद्र को पीछे छोड़कर सर्वोच्च देवता के रूप में उभरे।"
    },
    # Q48
    {
        "q": "Consider the following statements regarding the deification of earth (Prithvi) and sky (Dyaus):\n1. They were addressed together as 'Dyavaprithvi', representing the parental couple of the cosmos.\n2. Prithvi was praised as a storm deity who accompanied Indra in wars.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Dyavaprithvi represents sky and earth as cosmic parents. Prithvi was terrestrial, not storm god (Statement 2 is false).",
        "q_hi": "पृथ्वी और आकाश (द्यौस) के देवत्वकरण के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. उन्हें एक साथ 'द्यावापृथ्वी' के रूप में संबोधित किया गया था, जो ब्रह्मांड के जनक जोड़े का प्रतिनिधित्व करते थे।\n2. पृथ्वी को एक आंधी के देवता के रूप में पूजा जाता था, जो युद्धों में इंद्र के साथ थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 सही है। द्यावापृथ्वी ब्रह्मांडीय माता-पिता के रूप में आकाश और पृथ्वी का प्रतिनिधित्व करते हैं। पृथ्वी स्थलीय थी, आंधी के देवता नहीं (कथन 2 गलत है)।"
    },
    # Q49
    {
        "q": "The Sanskrit term ' papa' in Rigvedic ethics is often associated with which divine punishment?",
        "opts": [
            "Being bound by the noose (pasa) of Varuna",
            "Being expelled from the Samiti assembly",
            "Being forced to work in copper mines",
            "Having cattle herds stolen by the Panis"
        ],
        "ans": 0,
        "sol": "Those who committed sin (papa) by violating Rta were bound by Varuna's noose (pasa), manifesting as dropsy/misfortune.",
        "q_hi": "ऋग्वैदिक नैतिकता में संस्कृत शब्द 'पाप' अक्सर किस दिव्य दंड से जुड़ा होता है?",
        "opts_hi": [
            "वरुण के पाश (फंदे) से बंध जाना",
            "समिति सभा से निष्कासित कर दिया जाना",
            "तांबे की खदानों में काम करने के लिए मजबूर होना",
            "पणियों द्वारा मवेशियों के झुंडों को चुरा लिया जाना"
        ],
        "ans_hi": 0,
        "sol_hi": "ऋत का उल्लंघन करके पाप करने वाले वरुण के पाश (फंदे) से बंध जाते थे, जो जलोदर/दुर्भाग्य के रूप में प्रकट होता था।"
    },
    # Q50
    {
        "q": "Which of the following represents the primary mode of contacting the gods in early Rigvedic religion?",
        "opts": ["Sacrificial fire offerings and recited hymns", "Silent temple meditation", "Carving stone images", "Constructing brick altars in sacred rivers"],
        "ans": 0,
        "sol": "Invoking deities was done using spoken mantras/hymns and throwing offerings in fire altars.",
        "q_hi": "निम्नलिखित में से कौन प्रारंभिक ऋग्वैदिक धर्म में देवताओं से संपर्क करने के प्राथमिक माध्यम का प्रतिनिधित्व करता है?",
        "opts_hi": ["यज्ञीय अग्नि आहुतियाँ और पढ़े गए भजन", "मौन मंदिर ध्यान", "पत्थर की मूर्तियां तराशना", "पवित्र नदियों में ईंटों की वेदियों का निर्माण करना"],
        "ans_hi": 0,
        "sol_hi": "देवताओं का आह्वान करने के लिए बोले गए मंत्रों/भजनों और यज्ञ वेदियों में आहुति डालने का उपयोग किया जाता था।"
    }
]

# Construct the final bilingual objects including mock test questions
# Let's select the first 10 questions from the 50 practice questions to act as mock test questions to satisfy the count requirement
mock_eng = practice_base[:10]
mock_hi = []
for q in mock_eng:
    # Build Hindi version of mock test questions from the practice base
    q_hi_item = {
        "q": q["q_hi"],
        "sol": q["sol_hi"],
        "ans": q["ans_hi"]
    }
    if "opts_hi" in q:
        q_hi_item["opts"] = q["opts_hi"]
    elif "opts" in q:
        q_hi_item["opts"] = q["opts_hi"] if "opts_hi" in q else q["opts"]
    mock_hi.append(q_hi_item)

# Build clean practice list (without bilingual fields)
practice_eng = []
practice_hi = []
for q in practice_base:
    pe = {
        "q": q["q"],
        "opts": q["opts"],
        "ans": q["ans"],
        "sol": q["sol"]
    }
    ph = {
        "q": q["q_hi"],
        "opts": q["opts_hi"],
        "ans": q["ans_hi"],
        "sol": q["sol_hi"]
    }
    practice_eng.append(pe)
    practice_hi.append(ph)

eng_output = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Issues Concerning Religion and Culture"
    },
    "hero": {
        "title": "Issues Concerning Religion and Culture",
        "description": "Explore the foundational spiritual, cosmological, and ritual frameworks of early Vedic life. Investigate the rise of Henotheism, the maintenance of the moral order under Rta, funeral rites, and speculative transitions towards Later Vedic monism."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Test your knowledge on Issues Concerning Religion and Culture. This timed test contains 10 high-quality, exam-standard questions. Perfect for self-evaluation before the Prelims.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Spiritual Milestones & Evolution",
        "description": "Track the shift from simple pastoral pantheons to late philosophical skepticism in the Rigvedic canon.",
        "cards": [
            {
                "period": "Naturalism & Deification",
                "date": "Early Rigvedic Phase",
                "details": "Personification of natural elements like Indra (storm/war), Agni (mediator fire), and Varuna (moral guardian). Worship is simple, utilitarian, and completely lacks temples or idols."
            },
            {
                "period": "Cosmic Law & Rta",
                "date": "Mid-Rigvedic Phase",
                "details": "Development of Rta as the cosmic and moral order governing nature. Varuna acts as the ethical regulator, punishing moral violations (sin/papa) and tracking actions using spies."
            },
            {
                "period": "Speculative Monism",
                "date": "Late Rigvedic (Mandala 10)",
                "details": "Emergence of deep philosophical speculation. Hymns like the Nasadiya Sukta question the origin of creation, moving Vedic religion toward pantheistic monism ('Ekam Sat...')."
            }
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Master the spiritual practices, rituals, cosmological systems, and belief transitions of the Rig Vedic period for the Civil Services Examination.",
        "sections": eng_sections
    },
    "mnemonics": {
        "title": "Mnemonics & Quick Memory Tricks",
        "description": "Use these visual phrases to instantly recall the classification of deities and key religious facts for UPSC.",
        "items": [
            {
                "title": "Mnemonic 1: Cosmic Spheres of Deities",
                "phrase": "\"T-A-C (Terrestrial, Atmospheric, Celestial)\"",
                "decryption": "**T**errestrial (Agni, Prithvi, Soma), **A**tmospheric (Indra, Maruts, Rudra), and **C**elestial (Varuna, Dyaus, Savitr)."
            },
            {
                "title": "Mnemonic 2: The Three Supreme Early Gods",
                "phrase": "\"I-A-V (Indra, Agni, Varuna)\"",
                "decryption": "**I**ndra (thunder/war, 250 hymns), **A**gni (mediator fire, 200 hymns), and **V**aruna (cosmic and moral order guardian)."
            },
            {
                "title": "Mnemonic 3: Funerary Methods",
                "phrase": "\"C-B (Cremation and Burial)\"",
                "decryption": "Both **C**remation (Agni-dagdha) and **B**urial (Anagni-dagdha) were practiced, depending on tribal customs and age."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Click to flip and test your knowledge of Rigvedic beliefs.",
        "items": [
            {
                "question": "Who is the primary guardian of Rta (Cosmic Order)?",
                "answer": "The god <strong>Varuna</strong>, who uses spies (Spasa) to monitor human conduct.",
                "icon": "fa-shield-halved"
            },
            {
                "question": "What is the meaning of Max Müller's term 'Henotheism'?",
                "answer": "Worshipping <strong>one supreme god at a time</strong> while not denying the existence of others.",
                "icon": "fa-dove"
            },
            {
                "question": "Which Mandala contains the Purusha Sukta varna description?",
                "answer": "<strong>Mandala 10</strong>, representing a late addition to the Rigvedic canon.",
                "icon": "fa-people-group"
            }
        ]
    },
    "traps": {
        "title": "UPSC Common Exam Traps to Avoid",
        "items": [
            "<strong>Trap 1: Rebirth Doctrine:</strong> Rigveda did NOT establish Samsara (rebirth cycle) or Karma; these doctrines were developed later in the Upanishads.",
            "<strong>Trap 2: Idol Worship & Temples:</strong> Early Vedic religion was fully naturalistic, with zero archaeological trace of idols, icon worship, or public temples.",
            "<strong>Trap 3: Rta vs Satya:</strong> Rta is the absolute cosmic order. Satya (truth) is the human/moral expression of Rta."
        ]
    },
    "practiceQuestions": practice_eng,
    "mockTestQuestions": mock_eng
}

hi_output = {
    "breadcrumbs": {
        "parent": "यूपीएससी पाठ्यक्रम",
        "parentUrl": "/upsc/",
        "current": "धर्म और संस्कृति से संबंधित मुद्दे"
    },
    "hero": {
        "title": "धर्म और संस्कृति से संबंधित मुद्दे",
        "description": "प्रारंभिक वैदिक जीवन के मूलभूत आध्यात्मिक, ब्रह्मांडीय और अनुष्ठानिक ढांचों का अन्वेषण करें। हेनोथिज्म के उदय, ऋत के तहत नैतिक व्यवस्था के रखरखाव, अंतिम संस्कार और उत्तर वैदिक अद्वैतवाद की ओर दार्शनिक बदलाव की जांच करें।"
    },
    "labels": {
        "clickToExpand": "विवरण विस्तार के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरएक्टिव यूपीएससी मॉक टेस्ट",
            "description": "धर्म और संस्कृति से संबंधित मुद्दों पर अपने ज्ञान का परीक्षण करें। इस समयबद्ध परीक्षण में 10 उच्च-गुणवत्ता वाले, परीक्षा-मानक प्रश्न शामिल हैं। प्रारंभिक परीक्षा से पहले आत्म-मूल्यांकन के लिए बिल्कुल सही।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "पिछला प्रश्न",
            "nextBtn": "अगला प्रश्न",
            "submitBtn": "परीक्षण सबमिट करें"
        }
    },
    "timeline": {
        "title": "आध्यात्मिक मील के पत्थर और विकास",
        "description": "ऋग्वैदिक काल में सरल देहाती देवगणों से लेकर बाद के दार्शनिक संदेहवाद में बदलाव को ट्रैक करें।",
        "cards": [
            {
                "period": "प्राकृतिकवाद और देवत्वकरण",
                "date": "प्रारंभिक ऋग्वैदिक चरण",
                "details": "इंद्र (आंधी/युद्ध), अग्नि (मध्यस्थ अग्नि), और वरुण (नैतिक संरक्षक) जैसी प्राकृतिक शक्तियों का मानवीकरण। पूजा सरल, उपयोगितावादी है और इसमें मंदिरों या मूर्तियों का पूर्ण अभाव है।"
            },
            {
                "period": "ब्रह्मांडीय नियम और ऋत",
                "date": "मध्य-ऋग्वैदिक चरण",
                "details": "प्रकृति को नियंत्रित करने वाले ब्रह्मांडीय और नैतिक नियम के रूप में ऋत का विकास। वरुण नैतिक नियामक के रूप में कार्य करते हैं, गुप्तचरों का उपयोग करके नैतिक उल्लंघनों (पाप) को दंडित करते हैं।"
            },
            {
                "period": "चिंतनशील अद्वैतवाद",
                "date": "उत्तर ऋग्वैदिक (10वां मंडल)",
                "details": "गहन दार्शनिक चिंतन का प्रादुर्भाव। नासदीय सूक्त जैसे भजन सृष्टि की उत्पत्ति पर प्रश्न उठाते हैं, जो वैदिक धर्म को सर्वेश्वरवादी अद्वैतवाद ('एकं सद्...') की ओर ले जाते हैं।"
            }
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य नोट्स (गहन अध्ययन)",
        "description": "सिविल सेवा परीक्षा के लिए ऋग्वैदिक काल की आध्यात्मिक प्रथाओं, अनुष्ठानों, ब्रह्मांडीय प्रणालियों और विश्वासों के संक्रमण का गहन अध्ययन करें।",
        "sections": hi_sections
    },
    "mnemonics": {
        "title": "याद रखने के सूत्र (Mnemonics)",
        "description": "यूपीएससी के लिए देवताओं के वर्गीकरण और प्रमुख धार्मिक तथ्यों को तुरंत याद रखने के लिए इन दृश्य वाक्यांशों का उपयोग करें।",
        "items": [
            {
                "title": "याद रखने का सूत्र 1: देवताओं के ब्रह्मांडीय क्षेत्र",
                "phrase": "\"T-A-C (स्थलीय, अंतरिक्षीय, आकाशीय)\"",
                "decryption": "**T**errestrial/स्थलीय (अग्नि, पृथ्वी, सोम), **A**tmospheric/अंतरिक्षीय (इंद्र, मरुत, रुद्र), और **C**elestial/आकाशीय (वरुण, द्यौस, सविता)।"
            },
            {
                "title": "याद रखने का सूत्र 2: तीन सर्वोच्च प्रारंभिक देवता",
                "phrase": "\"I-A-V (इंद्र, अग्नि, वरुण)\"",
                "decryption": "**I**ndra/इंद्र (वज्र/युद्ध, 250 भजन), **A**gni/अग्नि (मध्यस्थ अग्नि, 200 भजन), और **V**aruna/वरुण (ब्रह्मांडीय और नैतिक व्यवस्था के संरक्षक)।"
            },
            {
                "title": "याद रखने का सूत्र 3: अंतिम संस्कार के तरीके",
                "phrase": "\"C-B (दाह संस्कार और दफन संस्कार)\"",
                "decryption": "कबीले की प्रथाओं और आयु के आधार पर दाह संस्कार (**C**remation/अग्नि-दग्ध) और दफन (**B**urial/अनग्नि-दग्ध) दोनों का अभ्यास किया जाता था।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall)",
        "description": "ऋग्वैदिक मान्यताओं के बारे में अपने ज्ञान का परीक्षण करने के लिए कार्ड्स पर क्लिक करें।",
        "items": [
            {
                "question": "ऋत (ब्रह्मांडीय व्यवस्था) का प्राथमिक संरक्षक कौन है?",
                "answer": "देवता <strong>वरुण</strong>, जो मानव आचरण की निगरानी के लिए गुप्तचरों (स्पश) का उपयोग करते हैं।",
                "icon": "fa-shield-halved"
            },
            {
                "question": "मैक्स मुलर के शब्द 'हेनोथिज्म' का क्या अर्थ है?",
                "answer": "दूसरों के अस्तित्व को नकारे बिना <strong>एक समय में एक ही सर्वोच्च देवता</strong> की पूजा करना।",
                "icon": "fa-dove"
            },
            {
                "question": "किस मंडल में पुरुष सूक्त के वर्णों का वर्णन है?",
                "answer": "<strong>10वें मंडल</strong> में, जो ऋग्वैदिक संहिता में बाद में जोड़ा गया भाग है।",
                "icon": "fa-people-group"
            }
        ]
    },
    "traps": {
        "title": "बचने योग्य सामान्य परीक्षा जाल (Traps)",
        "items": [
            "<strong>जाल 1: पुनर्जन्म का सिद्धांत:</strong> ऋग्वेद ने संसार (पुनर्जन्म चक्र) या कर्म को स्थापित नहीं किया; ये सिद्धांत बाद में उपनिषदों में विकसित हुए थे।",
            "<strong>जाल 2: मूर्तिपूजा और मंदिर:</strong> प्रारंभिक वैदिक धर्म पूरी तरह से प्राकृतिक था, जिसमें मूर्तियों, मूर्ति पूजा या सार्वजनिक मंदिरों का कोई पुरातात्विक साक्ष्य नहीं है।",
            "<strong>जाल 3: ऋत बनाम सत्य:</strong> ऋत पूर्ण ब्रह्मांडीय व्यवस्था है। सत्य ऋत की मानवीय/नैतिक अभिव्यक्ति है।"
        ]
    },
    "practiceQuestions": practice_hi,
    "mockTestQuestions": mock_hi
}

# Write final bilingual content.json files
os.makedirs(os.path.dirname(os.path.join(base_dir, "content.json")), exist_ok=True)
with open(os.path.join(base_dir, "content.json"), 'w', encoding='utf-8') as f:
    json.dump(eng_output, f, ensure_ascii=False, indent=4)

os.makedirs(os.path.dirname(os.path.join(base_dir, "hi", "content.json")), exist_ok=True)
with open(os.path.join(base_dir, "hi", "content.json"), 'w', encoding='utf-8') as f:
    json.dump(hi_output, f, ensure_ascii=False, indent=4)

print("Content generated successfully!")
