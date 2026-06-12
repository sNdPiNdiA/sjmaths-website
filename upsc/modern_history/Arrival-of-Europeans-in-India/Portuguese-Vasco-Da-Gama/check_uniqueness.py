import json

def check_uniqueness(filepath):
    print(f"Checking uniqueness for: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    all_questions = []
    
    # Extract study notes sections (Mastery Zone)
    for idx, sec in enumerate(data['deepDive']['sections']):
        for q in sec['masteryZone']:
            all_questions.append((f"Section {idx+1} Mastery", q.get('q', q.get('statement', ''))))
            
    # Extract practice questions
    for q in data['practiceQuestions']:
        all_questions.append(("Practice", q.get('q', q.get('statement', ''))))
        
    # Extract mock questions
    for q in data['mockTestQuestions']:
        all_questions.append(("Mock", q.get('q', q.get('statement', ''))))
        
    # Count occurrences
    question_texts = [q[1] for q in all_questions]
    unique_texts = set(question_texts)
    
    print(f"Total questions loaded: {len(question_texts)}")
    print(f"Total unique questions: {len(unique_texts)}")
    
    if len(question_texts) != len(unique_texts):
        print("WARNING: Duplicates found!")
        seen = set()
        duplicates = []
        for category, qtext in all_questions:
            if qtext in seen:
                duplicates.append((category, qtext))
            seen.add(qtext)
        for cat, dup in duplicates[:10]:
            print(f"  - Duplicate in {cat}: {dup[:100]}...")
    else:
        print("SUCCESS: All questions are 100% unique!")
    print("-" * 50)

check_uniqueness("content.json")
check_uniqueness("hi/content.json")
