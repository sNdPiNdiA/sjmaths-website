import json
import os
import sys

# Add current directory to path so questions_data can be imported directly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import all modular sections and questions
from questions_data.section1 import section1_en, section1_hi
from questions_data.section2 import section2_en, section2_hi
from questions_data.section3 import section3_en, section3_hi
from questions_data.section4 import section4_en, section4_hi
from questions_data.section5 import section5_en, section5_hi
from questions_data.practice import practice_en, practice_hi
from questions_data.mock import mock_en, mock_hi

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

en_data['labels']['tabs']['practice'] = "2. Practice Zone (50 Qs)"
en_data['labels']['practiceZoneHeader']['title'] = "Practice Zone: 50 Questions"
en_data['labels']['mockIntro']['description'] = "Contains 10 multi-statement questions testing conceptual understanding and site identification. 1/3 negative marking applies."

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

hi_data['labels']['tabs']['practice'] = "2. अभ्यास क्षेत्र (50 प्रश्न)"
hi_data['labels']['practiceZoneHeader']['title'] = "अभ्यास क्षेत्र: 50 प्रश्न"
hi_data['labels']['mockIntro']['description'] = "अवधारणात्मक समझ और स्थलों की पहचान का परीक्षण करने वाले 10 बहु-कथनीय प्रश्न शामिल हैं। 1/3 नकारात्मक अंकन प्रणाली लागू है।"

with open('hi/content.json', 'w', encoding='utf-8') as f:
    json.dump(hi_data, f, ensure_ascii=False, indent=2)

print("SUCCESS: Merged all sections, practice questions, and mock questions into English and Hindi content.json.")
print(f"Total questions merged: Sec1={len(section1_en)}, Sec2={len(section2_en)}, Sec3={len(section3_en)}, Sec4={len(section4_en)}, Sec5={len(section5_en)}, Practice={len(practice_en)}, Mock={len(mock_en)}")
print(f"Total overall questions: {len(section1_en)+len(section2_en)+len(section3_en)+len(section4_en)+len(section5_en)+len(practice_en)+len(mock_en)}")
