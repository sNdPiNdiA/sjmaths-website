import os
import json

base_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation"
required_keys = {"q", "opts", "ans", "sol"}

failed_files = {}

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file == "content.json":
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                
                errors = []
                # Check practiceQuestions
                pq = data.get("practiceQuestions", [])
                for idx, q in enumerate(pq):
                    missing = required_keys - set(q.keys())
                    if missing:
                        errors.append(f"practiceQuestions[{idx}] missing {missing}")
                        
                # Check mockTestQuestions
                mq = data.get("mockTestQuestions", [])
                for idx, q in enumerate(mq):
                    missing = required_keys - set(q.keys())
                    if missing:
                        errors.append(f"mockTestQuestions[{idx}] missing {missing}")
                
                if errors:
                    failed_files[file_path] = len(errors)

            except Exception as e:
                print(f"Could not read/parse {file_path}: {e}")

print("Summary of files with schema errors:")
if not failed_files:
    print("None! All files are 100% correct.")
else:
    for fpath, err_count in failed_files.items():
        print(f"- {fpath}: {err_count} errors")
