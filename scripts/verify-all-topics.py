import os
import re
import sys
import argparse

# Configure UTF-8 for windows console
sys.stdout.reconfigure(encoding='utf-8')

parser = argparse.ArgumentParser(description="Verify UPSSSC Intermediate Level topic pages")
parser.add_argument("--subject", type=str, default="all", help="Subject directory to verify or 'all'")
parser.add_argument("--topic", type=str, default=None, help="Specific topic slug to verify")
args = parser.parse_args()

base_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsssc-intermediate-level"

all_subjects = [
    "history",
    "polity",
    "geography",
    "economy",
    "rural-development",
    "science-tech",
    "environment",
    "hindi"
]

if args.subject == "all":
    subjects_to_check = all_subjects
elif args.subject in all_subjects or os.path.exists(os.path.join(base_dir, args.subject)):
    subjects_to_check = [args.subject]
else:
    print(f"Unknown subject '{args.subject}'. Available: {all_subjects}")
    sys.exit(1)

total_checked = 0
total_passed = 0
failures = []

for subject in subjects_to_check:
    subject_dir = os.path.join(base_dir, subject)
    if not os.path.exists(subject_dir):
        continue
    
    topics = [d for d in os.listdir(subject_dir) if os.path.isdir(os.path.join(subject_dir, d))]
    topics.sort()
    
    if args.topic:
        topics = [t for t in topics if t == args.topic or args.topic in t]
    
    if not topics:
        continue
        
    print(f"\n==================== Subject: {subject.upper()} ({len(topics)} topics) ====================")
    
    for topic in topics:
        index_path = os.path.join(subject_dir, topic, "index.html")
        total_checked += 1
        
        if not os.path.exists(index_path):
            print(f"❌ [{topic}]: index.html missing!")
            failures.append((subject, topic, ["index.html missing"]))
            continue
        
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check CSS & JS
        has_css = "upsssc-intermediate" in content and ".css" in content
        has_js = "upsssc-intermediate" in content and ".js" in content
        
        # Check bilingual tags
        en_tags = len(re.findall(r'class="[^"]*\blang-en\b[^"]*"', content))
        hi_tags = len(re.findall(r'class="[^"]*\blang-hi\b[^"]*"', content))
        
        # Check practice questions (expect 30)
        practice_qs = len(re.findall(r'class="question-card"|class="practice-question-card"', content))
        
        # Check test questions (expect 15)
        test_qs = len(re.findall(r'class="test-q-box"|class="test-qblock"', content))
        
        # Check test answers (expect 15)
        test_data = re.search(r'window\.upssscTestData\s*=\s*\[(.*?)\];', content, re.DOTALL)
        test_ans_count = len(re.findall(r'\{\s*"ans"\s*:', test_data.group(1))) if test_data else 0
        
        issues = []
        if not has_css:
            issues.append("missing upsssc-intermediate.css")
        if not has_js:
            issues.append("missing upsssc-intermediate.js")
        if practice_qs != 30:
            issues.append(f"practice Qs = {practice_qs} (expected 30)")
        if test_qs != 15:
            issues.append(f"test Qs = {test_qs} (expected 15)")
        if test_ans_count != 15:
            issues.append(f"test answer data count = {test_ans_count} (expected 15)")
        if abs(en_tags - hi_tags) > 25:
            issues.append(f"bilingual imbalance: EN={en_tags}, HI={hi_tags}")
            
        if issues:
            print(f"❌ [{topic}]: " + ", ".join(issues))
            failures.append((subject, topic, issues))
        else:
            total_passed += 1
            print(f"✅ [{topic}]: OK | EN: {en_tags}, HI: {hi_tags} | Practice: {practice_qs} | Test: {test_qs}")

print(f"\n============================================================")
print(f" VERIFICATION SUMMARY:")
print(f" Total Topics Checked: {total_checked}")
print(f" Passed:               {total_passed}")
print(f" Failed:               {len(failures)}")
print(f"============================================================")

if len(failures) == 0 and total_checked > 0:
    print("\n🎉 ALL VERIFIED MICRO-TOPICS PASSED VALIDATION WITH 100% PARITY!")
elif len(failures) > 0:
    print(f"\n⚠️ {len(failures)} TOPIC(S) FAILED VALIDATION.")
