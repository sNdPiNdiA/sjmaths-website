import os
import re
from collections import Counter

def audit_encoding(directory):
    encoding_artifacts = Counter()
    files_with_artifacts = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # regex for non-ascii
                        non_ascii = re.findall(r'[^\x00-\x7F]+', content)
                        
                        for seq in non_ascii:
                             encoding_artifacts[seq] += 1
                             if seq not in files_with_artifacts:
                                 files_with_artifacts[seq] = set()
                             files_with_artifacts[seq].add(path)

                except Exception as e:
                    print(f"Error reading {path}: {e}")

    with open('encoding_report_utf8.txt', 'w', encoding='utf-8') as f:
        f.write("--- Encoding Artifacts Found ---\n")
        for artifact, count in encoding_artifacts.most_common():
            f.write(f"Artifact: {repr(artifact)} | Count: {count}\n")
            # print first 3 files
            files = list(files_with_artifacts[artifact])[:3]
            f.write(f"  Files: {files}\n")

target_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\chapter-wise-notes"
audit_encoding(target_dir)
