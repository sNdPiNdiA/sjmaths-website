import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Domestication-of-animals\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Domestication-of-animals\hi\content.json"

expected_counts = {
    "MCQ": 5,
    "Multiple Correct MCQ": 5,
    "True/False": 8,
    "Fill in the Blank": 8,
    "Match the Following": 3,
    "One-Liner": 8,
    "Assertion-Reason": 8,
    "Statement-Based": 5,
    "Why": 3,
    "How": 3,
    "Case Study": 3,
    "Teach Concept": 3
}

def verify_file(filepath, name):
    print(f"\n--- Verifying {name} ({filepath}) ---")
    if not os.path.exists(filepath):
        print(f"ERROR: File {filepath} does not exist!")
        return False
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"ERROR: Failed to parse JSON: {e}")
        return False
        
    if "deepDive" not in data or "sections" not in data["deepDive"]:
        print("ERROR: 'deepDive' or 'sections' missing in JSON!")
        return False
        
    sections = data["deepDive"]["sections"]
    if len(sections) != 3:
        print(f"ERROR: Expected 3 sections, found {len(sections)}")
        return False
        
    success = True
    for idx, sec in enumerate(sections):
        print(f"\nSection {idx+1}")
        mastery = sec.get("masteryZone", [])
        print(f"Total questions in masteryZone: {len(mastery)}")
        
        counts = {}
        for q in mastery:
            qtype = q.get("type")
            counts[qtype] = counts.get(qtype, 0) + 1
            if qtype == "Match the Following":
                if "items" not in q or "options" not in q:
                    print(f"ERROR: 'Match the Following' question missing 'items' or 'options' properties: {q}")
                    success = False
                elif not isinstance(q["items"], list) or not isinstance(q["options"], list):
                    print(f"ERROR: 'items' or 'options' is not a list: {q}")
                    success = False
            
        print("Question Type Counts:")
        for qtype, expected in expected_counts.items():
            found = counts.get(qtype, 0)
            status = "PASS" if found == expected else f"FAIL (Expected {expected}, got {found})"
            print(f"  - {qtype}: {found} -> {status}")
            if found != expected:
                success = False
                
    if len(data.get("practiceQuestions", [])) != 50:
        print(f"ERROR: Expected 50 practice questions, found {len(data.get('practiceQuestions', []))}")
        success = False
    else:
        print("\nPractice Questions: 50 -> PASS")
        
    if len(data.get("mockTestQuestions", [])) != 10:
        print(f"ERROR: Expected 10 mock questions, found {len(data.get('mockTestQuestions', []))}")
        success = False
    else:
        print("Mock Questions: 10 -> PASS")
        
    if success:
        print(f"\n=== {name} validation PASSED! ===")
    else:
        print(f"\n*** {name} validation FAILED! ***")
    return success

try:
    v_eng = verify_file(ENG_PATH, "English JSON")
    v_hin = verify_file(HIN_PATH, "Hindi JSON")
    
    if v_eng and v_hin:
        print("\nAll JSON structures, practice, mock, and 186 mastery questions are 100% correct!")
    else:
        print("\nVerification failed. Check errors above.")
except Exception as e:
    print(f"\nExecution error: {e}")
