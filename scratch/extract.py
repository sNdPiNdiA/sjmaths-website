import json
import os

transcript_path = r"C:\Users\sande\.gemini\antigravity\brain\bbceb710-116b-455d-8ed7-f5ac7b7ef739\.system_generated\logs\transcript.jsonl"
output_path = r"c:\Users\sande\Documents\GitHub\sjmaths-website\scratch\user_syllabus_step_76.txt"

os.makedirs(os.path.dirname(output_path), exist_ok=True)

step_76_content = None
step_98_content = None

with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            if data.get('step_index') == 76:
                step_76_content = data.get('content')
            elif data.get('step_index') == 98:
                step_98_content = data.get('content')
        except Exception as e:
            print("Error parsing line:", e)

if step_76_content:
    with open(output_path, 'w', encoding='utf-8') as out:
        out.write(step_76_content)
    print("Successfully extracted step 76 to:", output_path)
    print("Length of step 76:", len(step_76_content))
else:
    print("Step 76 not found in transcript.jsonl")

if step_98_content:
    output_path_98 = r"c:\Users\sande\Documents\GitHub\sjmaths-website\scratch\user_syllabus_step_98.txt"
    with open(output_path_98, 'w', encoding='utf-8') as out:
        out.write(step_98_content)
    print("Successfully extracted step 98 to:", output_path_98)
    print("Length of step 98:", len(step_98_content))
