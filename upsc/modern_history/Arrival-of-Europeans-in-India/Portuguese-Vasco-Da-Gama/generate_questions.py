import json
import os
import sys

# Append questions_data directory to search path
sys.path.append(os.path.join(os.path.dirname(__file__), 'questions_data'))

# Import all modular sections and questions
from section1 import section1_en, section1_hi
from section2 import section2_en, section2_hi
from section3 import section3_en, section3_hi
from section4 import section4_en, section4_hi
from section5 import section5_en, section5_hi
from practice import practice_en, practice_hi
from mock import mock_en, mock_hi

# EN content.json
print("Merging English content.json...")
with open('content.json', 'r', encoding='utf-8') as f:
    en_data = json.load(f)

en_data['deepDive']['sections'][0]['masteryZone'] = section1_en
en_data['deepDive']['sections'][1]['masteryZone'] = section2_en
en_data['deepDive']['sections'][2]['masteryZone'] = section3_en
en_data['deepDive']['sections'][3]['masteryZone'] = section4_en
en_data['deepDive']['sections'][4]['masteryZone'] = section5_en

en_data['practiceQuestions'] = practice_en
en_data['mockTestQuestions'] = mock_en

# Ensure labels object exists
if 'labels' not in en_data:
    en_data['labels'] = {}
if 'tabs' not in en_data['labels']:
    en_data['labels']['tabs'] = {}
if 'practiceZoneHeader' not in en_data['labels']:
    en_data['labels']['practiceZoneHeader'] = {}
if 'mockIntro' not in en_data['labels']:
    en_data['labels']['mockIntro'] = {}
if 'mockPlay' not in en_data['labels']:
    en_data['labels']['mockPlay'] = {
        "prevBtn": "Previous",
        "nextBtn": "Next",
        "submitBtn": "Submit Test"
    }

en_data['labels']['tabs']['practice'] = "2. Practice Zone (50 Qs)"
en_data['labels']['practiceZoneHeader']['title'] = "Practice Zone: 50 Questions"
en_data['labels']['mockIntro']['title'] = "UPSC Prelims Mock Exam"
en_data['labels']['mockIntro']['description'] = "Contains 10 multi-statement questions testing conceptual understanding of Vasco da Gama's voyages, diplomatic disputes, routes, and geopolitical impact. 1/3 negative marking applies."
en_data['labels']['mockIntro']['startBtn'] = "Start Mock Exam"
en_data['labels']['clickToExpand'] = "Click to Expand"

with open('content.json', 'w', encoding='utf-8') as f:
    json.dump(en_data, f, ensure_ascii=False, indent=2)

# HI content.json
print("Merging Hindi hi/content.json...")
with open('hi/content.json', 'r', encoding='utf-8') as f:
    hi_data = json.load(f)

hi_data['deepDive']['sections'][0]['masteryZone'] = section1_hi
hi_data['deepDive']['sections'][1]['masteryZone'] = section2_hi
hi_data['deepDive']['sections'][2]['masteryZone'] = section3_hi
hi_data['deepDive']['sections'][3]['masteryZone'] = section4_hi
hi_data['deepDive']['sections'][4]['masteryZone'] = section5_hi

hi_data['practiceQuestions'] = practice_hi
hi_data['mockTestQuestions'] = mock_hi

# Ensure labels object exists
if 'labels' not in hi_data:
    hi_data['labels'] = {}
if 'tabs' not in hi_data['labels']:
    hi_data['labels']['tabs'] = {}
if 'practiceZoneHeader' not in hi_data['labels']:
    hi_data['labels']['practiceZoneHeader'] = {}
if 'mockIntro' not in hi_data['labels']:
    hi_data['labels']['mockIntro'] = {}
if 'mockPlay' not in hi_data['labels']:
    hi_data['labels']['mockPlay'] = {
        "prevBtn": "पिछला",
        "nextBtn": "अगला",
        "submitBtn": "टेस्ट सबमिट करें"
    }

hi_data['labels']['tabs']['practice'] = "2. अभ्यास क्षेत्र (50 प्रश्न)"
hi_data['labels']['practiceZoneHeader']['title'] = "अभ्यास क्षेत्र: 50 प्रश्न"
hi_data['labels']['mockIntro']['title'] = "यूपीएससी प्रीलिम्स मॉक परीक्षा"
hi_data['labels']['mockIntro']['description'] = "वास्को डी गामा की यात्राओं, राजनयिक विवादों, मार्गों और उनके प्रभाव की वैचारिक समझ का परीक्षण करने वाले 10 बहु-कथनीय प्रश्न शामिल हैं। 1/3 नकारात्मक अंकन प्रणाली लागू है।"
hi_data['labels']['mockIntro']['startBtn'] = "मॉक टेस्ट शुरू करें"
hi_data['labels']['clickToExpand'] = "विस्तार करने के लिए क्लिक करें"

with open('hi/content.json', 'w', encoding='utf-8') as f:
    json.dump(hi_data, f, ensure_ascii=False, indent=2)

print("SUCCESS: Merged all sections, practice questions, and mock questions into English and Hindi content.json.")
print(f"Total questions merged: Sec1={len(section1_en)}, Sec2={len(section2_en)}, Sec3={len(section3_en)}, Sec4={len(section4_en)}, Sec5={len(section5_en)}, Practice={len(practice_en)}, Mock={len(mock_en)}")
