import json
import os

# Import all modular sections and questions
from questions_data.section1 import sec1_en, sec1_hi
from questions_data.section2 import sec2_en, sec2_hi
from questions_data.section3 import sec3_en, sec3_hi
from questions_data.section4 import sec4_en, sec4_hi
from questions_data.section5 import sec5_en, sec5_hi
from questions_data.practice import practice_en, practice_hi
from questions_data.mock import mock_en, mock_hi

# EN content.json
print("Merging English content.json...")
with open('content.json', 'r', encoding='utf-8') as f:
    en_data = json.load(f)

en_data['deepDive']['sections'][0]['masteryZone'] = sec1_en
en_data['deepDive']['sections'][1]['masteryZone'] = sec2_en
en_data['deepDive']['sections'][2]['masteryZone'] = sec3_en
en_data['deepDive']['sections'][3]['masteryZone'] = sec4_en
en_data['deepDive']['sections'][4]['masteryZone'] = sec5_en

en_data['practiceQuestions'] = practice_en
en_data['mockTestQuestions'] = mock_en

en_data['labels']['tabs']['practice'] = "2. Practice Zone (50 Qs)"
en_data['labels']['practiceZoneHeader']['title'] = "Practice Zone: 50 Questions"
en_data['labels']['mockIntro']['description'] = "Contains 10 multi-statement questions testing conceptual understanding and site locations. 1/3 negative marking applies."

with open('content.json', 'w', encoding='utf-8') as f:
    json.dump(en_data, f, ensure_ascii=False, indent=2)

# HI content.json
print("Merging Hindi hi/content.json...")
with open('hi/content.json', 'r', encoding='utf-8') as f:
    hi_data = json.load(f)

hi_data['deepDive']['sections'][0]['masteryZone'] = sec1_hi
hi_data['deepDive']['sections'][1]['masteryZone'] = sec2_hi
hi_data['deepDive']['sections'][2]['masteryZone'] = sec3_hi
hi_data['deepDive']['sections'][3]['masteryZone'] = sec4_hi
hi_data['deepDive']['sections'][4]['masteryZone'] = sec5_hi

hi_data['practiceQuestions'] = practice_hi
hi_data['mockTestQuestions'] = mock_hi

hi_data['labels']['tabs']['practice'] = "2. अभ्यास क्षेत्र (50 प्रश्न)"
hi_data['labels']['practiceZoneHeader']['title'] = "अभ्यास क्षेत्र: 50 प्रश्न"
hi_data['labels']['mockIntro']['description'] = "अवधारणात्मक समझ और स्थलों की स्थिति का परीक्षण करने वाले 10 बहु-कथनीय प्रश्न शामिल हैं। 1/3 नकारात्मक अंकन प्रणाली लागू है।"

with open('hi/content.json', 'w', encoding='utf-8') as f:
    json.dump(hi_data, f, ensure_ascii=False, indent=2)

print("SUCCESS: Merged all sections, practice questions, and mock questions into English and Hindi content.json.")
print(f"Total questions merged: Sec1={len(sec1_en)}, Sec2={len(sec2_en)}, Sec3={len(sec3_en)}, Sec4={len(sec4_en)}, Sec5={len(sec5_en)}, Practice={len(practice_en)}, Mock={len(mock_en)}")
