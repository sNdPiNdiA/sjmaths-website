import os
import json

parent_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\History-of-Early-VedicRigvedic-Period"
subdirs = [
    "Economic-Aspects",
    "Evolution-of-Political-Organisation",
    "Extent-and-Geography-of-the-Rig-Vedic-Period",
    "Issues-Concerning-Religion-and-Culture",
    "Societal-Setup",
    "Sources-for-Information-about-Vedic-Society-and-Culture"
]

def check_file(filepath):
    if not os.path.exists(filepath):
        return f"File does not exist: {filepath}"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    sections = data.get("deepDive", {}).get("sections", [])
    issues = []
    
    # Store all question texts to find exact duplicates
    q_texts = set()
    dup_count = 0
    
    for s_idx, sec in enumerate(sections):
        mastery = sec.get("masteryZone", [])
        for q_idx, q in enumerate(mastery):
            # Check for placeholders
            q_text = q.get("q", "")
            sol_text = q.get("sol", "")
            
            # Simple check for duplicates
            if q_text in q_texts:
                dup_count += 1
            else:
                q_texts.add(q_text)
            
            for key, val in q.items():
                if isinstance(val, str):
                    if "{" in val and "}" in val:
                        issues.append(f"Sec {s_idx+1} Q {q_idx+1} has placeholder: {val[:60]}...")
                    if "Variant" in val or "विविधता" in val:
                        issues.append(f"Sec {s_idx+1} Q {q_idx+1} has 'Variant': {val[:60]}...")
                    if "Query" in val or "Parameter" in val or "Value X" in val:
                        issues.append(f"Sec {s_idx+1} Q {q_idx+1} has query template: {val[:60]}...")
                        
    res = f"File: {filepath}\n"
    res += f"  Total sections: {len(sections)}\n"
    res += f"  Total duplicate questions: {dup_count}\n"
    if issues:
        res += f"  Issues found:\n"
        for issue in issues[:10]:
            res += f"    - {issue}\n"
        if len(issues) > 10:
            res += f"    - ... and {len(issues) - 10} more issues.\n"
    else:
        res += f"  No template/placeholder issues found.\n"
    return res

for subdir in subdirs:
    print("==================================================")
    print(f"Auditing Subtopic: {subdir}")
    print("==================================================")
    eng_path = os.path.join(parent_dir, subdir, "content.json")
    hin_path = os.path.join(parent_dir, subdir, "hi", "content.json")
    print(check_file(eng_path))
    print(check_file(hin_path))
