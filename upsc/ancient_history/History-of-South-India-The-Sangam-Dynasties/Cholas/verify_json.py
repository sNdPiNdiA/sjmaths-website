import json
import os
import sys

# Force stdout to use UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\History-of-South-India-The-Sangam-Dynasties\Cholas"

def verify_file(filepath):
    print(f"\n=========================================")
    print(f"Verifying {filepath}...")
    print(f"=========================================")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    sections = data.get("deepDive", {}).get("sections", [])
    print(f"Number of sections: {len(sections)}")
    if len(sections) != 6:
        print("ERROR: Section count is not 6!")
    
    for idx, sec in enumerate(sections):
        mastery = sec.get("masteryZone", [])
        print(f"  Section {idx + 1} ('{sec.get('title')}') Mastery Questions: {len(mastery)}")
        if len(mastery) != 62:
            print(f"  ERROR: Section {idx + 1} has {len(mastery)} questions (expected 62)!")
        
        for q_idx, q in enumerate(mastery):
            for key, val in q.items():
                if isinstance(val, str):
                    if "{" in val and "}" in val:
                        print(f"    WARNING: Possible placeholder '{val}' in section {idx+1} question {q_idx+1} ({key})")
                    if "Variant" in val or "विविधता" in val:
                        print(f"    WARNING: 'Variant' found in section {idx+1} question {q_idx+1} ({key}): {val}")
                    if "Query" in val:
                        print(f"    WARNING: 'Query' found in section {idx+1} question {q_idx+1} ({key}): {val}")

    practice = data.get("practiceQuestions", [])
    print(f"Practice Questions: {len(practice)}")
    if len(practice) != 50:
        print("ERROR: Practice questions count is not 50!")
    
    # Check uniqueness of practice questions
    q_texts = set()
    for q_idx, q in enumerate(practice):
        q_text = q.get("q")
        if q_text in q_texts:
            print(f"  ERROR: Duplicate practice question found at index {q_idx+1}: {q_text[:60]}...")
        q_texts.add(q_text)
        
        for key, val in q.items():
            if isinstance(val, str):
                if "{" in val and "}" in val:
                    print(f"    WARNING: Placeholder in practice question {q_idx+1} ({key}): {val}")

    mock = data.get("mockTestQuestions", [])
    print(f"Mock Test Questions: {len(mock)}")
    if len(mock) != 10:
        print("ERROR: Mock test questions count is not 10!")

verify_file(os.path.join(base_dir, "content.json"))
verify_file(os.path.join(base_dir, "hi", "content.json"))
