import os
import json
import sys

# Force stdout to use UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

parent_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\History-of-Later-Vedic-Period"
subdirs = [
    "Development-of-Early-Political-Organisation",
    "Economic-Activities",
    "Extent-and-Geography-of-the-Later-Vedic-Period",
    "Issues-Concerning-Religion-and-Culture",
    "Social-Organisation-and-Hierarchy"
]

def check_file(filepath):
    if not os.path.exists(filepath):
        return f"File does not exist: {filepath}"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    sections = data.get("deepDive", {}).get("sections", [])
    issues = []
    
    q_texts = set()
    dup_count = 0
    
    for s_idx, sec in enumerate(sections):
        mastery = sec.get("masteryZone", [])
        for q_idx, q in enumerate(mastery):
            q_text = q.get("q", "")
            # Strip suffixes like " (Ref: ...)" or " (संदर्भ: ...)" or " (Practice Q...)" etc.
            import re
            clean_q = re.sub(r"\s*\(.*?\)\s*$", "", q_text).strip()
            # Also clean statements or other punctuation if needed
            if clean_q in q_texts:
                dup_count += 1
            else:
                q_texts.add(clean_q)
            
            for key, val in q.items():
                if isinstance(val, str):
                    if "{" in val and "}" in val:
                        issues.append(f"Sec {s_idx+1} Q {q_idx+1} has placeholder: {val[:60]}...")
                    if "Variant" in val or "विविधता" in val:
                        issues.append(f"Sec {s_idx+1} Q {q_idx+1} has 'Variant': {val[:60]}...")
                    if "Query" in val or "Parameter" in val or "Value X" in val:
                        issues.append(f"Sec {s_idx+1} Q {q_idx+1} has query template: {val[:60]}...")
                        
    practice = data.get("practiceQuestions", [])
    prac_dup_count = 0
    for p_idx, q in enumerate(practice):
        q_text = q.get("q", "")
        clean_q = re.sub(r"\s*\(.*?\)\s*$", "", q_text).strip()
        if clean_q in q_texts:
            prac_dup_count += 1
        else:
            q_texts.add(clean_q)

    mock = data.get("mockTestQuestions", [])
    mock_dup_count = 0
    for m_idx, q in enumerate(mock):
        q_text = q.get("q", "")
        clean_q = re.sub(r"\s*\(.*?\)\s*$", "", q_text).strip()
        if clean_q in q_texts:
            mock_dup_count += 1
        else:
            q_texts.add(clean_q)

    res = f"File: {filepath}\n"
    res += f"  Total sections: {len(sections)}\n"
    res += f"  Total duplicate mastery questions: {dup_count}\n"
    res += f"  Total duplicate practice questions: {prac_dup_count}\n"
    res += f"  Total duplicate mock questions: {mock_dup_count}\n"
    if issues:
        res += "  Issues: " + "; ".join(issues[:5]) + "\n"
    return res

for subdir in subdirs:
    print("==================================================")
    print(f"Auditing Later Vedic Subtopic: {subdir}")
    print("==================================================")
    eng_path = os.path.join(parent_dir, subdir, "content.json")
    hin_path = os.path.join(parent_dir, subdir, "hi", "content.json")
    print(check_file(eng_path))
    print(check_file(hin_path))
