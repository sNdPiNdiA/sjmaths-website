import json

log_path = r"C:\Users\sande\.gemini\antigravity\brain\bbceb710-116b-455d-8ed7-f5ac7b7ef739\.system_generated\logs\transcript.jsonl"
target_file = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\Prehistory\Prehistoric-Time-Periods\hi\index.html"

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            # Check model responses with tool calls
            if data.get("source") == "MODEL" and "tool_calls" in data:
                for tc in data["tool_calls"]:
                    if tc.get("name") == "write_to_file" and "hi/index.html" in tc.get("args", {}).get("TargetFile", ""):
                        content = tc["args"]["CodeContent"]
                        # Write this content back to the target file
                        with open(target_file, 'w', encoding='utf-8') as out:
                            out.write(content)
                        print("Successfully restored hi/index.html!")
        except Exception as e:
            pass
