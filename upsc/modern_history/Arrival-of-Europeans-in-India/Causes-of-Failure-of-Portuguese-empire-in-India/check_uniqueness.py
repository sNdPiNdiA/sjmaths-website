import json
import os

BASE_DIR = r"C:\Users\sande\Documents\GitHub\sjmaths-website\upsc\modern_history\Arrival-of-Europeans-in-India\Causes-of-Failure-of-Portuguese-empire-in-India"

def load_questions(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    questions = []
    # Extract masteryZone questions
    for sec in data["deepDive"]["sections"]:
        questions.extend(sec["masteryZone"])
    
    # Extract practiceQuestions
    questions.extend(data["practiceQuestions"])
    
    # Extract mockTestQuestions
    questions.extend(data["mockTestQuestions"])
    
    return questions

def check_uniqueness(lang, filepath):
    if not os.path.exists(filepath):
        print(f"ERROR: File {filepath} does not exist!")
        return False
        
    qs = load_questions(filepath)
    print(f"\nChecking {lang} database: {filepath}")
    print(f"Total questions found: {len(qs)}")
    
    if len(qs) != 370:
        print(f"ERROR: Expected 370 questions, but found {len(qs)}")
        return False
        
    texts = [q["q"] for q in qs]
    unique_texts = set(texts)
    
    if len(unique_texts) != len(texts):
        print(f"ERROR: Found duplicate questions! {len(texts) - len(unique_texts)} duplicates.")
        # Find duplicates
        seen = set()
        duplicates = []
        for t in texts:
            if t in seen:
                duplicates.append(t)
            seen.add(t)
        for d in duplicates[:10]:
            print(f"Duplicate sample: {d}")
        return False
        
    print(f"SUCCESS: All {len(qs)} questions are 100% unique in {lang}.")
    return True

ok_en = check_uniqueness("English", os.path.join(BASE_DIR, "content.json"))
ok_hi = check_uniqueness("Hindi", os.path.join(BASE_DIR, "hi", "content.json"))

if ok_en and ok_hi:
    print("\nALL TESTS PASSED: Uniqueness check successful!")
else:
    print("\nTESTS FAILED: Duplicate questions or wrong count found.")
