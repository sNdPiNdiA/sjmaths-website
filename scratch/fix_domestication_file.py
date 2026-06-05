import sys
import os

# Add scratch folder to path so we can import generate_practice_upsc
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generate_practice_upsc import practice_raw_eng, practice_raw_hin

build_file_path = r"c:\Users\sande\Documents\GitHub\sjmaths-website\scratch\build_domestication_json.py"

# Read original lines
with open(build_file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Header is lines 1 to 380 (index 0 to 379)
header_content = "".join(lines[:380])

# Footer is lines 892 to 953 (index 891 to 952)
# Wait, index 891 corresponds to line 892. Let's make sure we find line 892.
# We can find line 892 by locating the comment "# 10 English Mock Questions (Multi-statement, UPSC standard)"
footer_start_idx = None
for idx, line in enumerate(lines):
    if "# 10 English Mock Questions (Multi-statement, UPSC standard)" in line:
        footer_start_idx = idx
        break

if footer_start_idx is None:
    raise ValueError("Could not find footer start comment in build_domestication_json.py")

print(f"Header length in lines: 380")
print(f"Footer starts at line: {footer_start_idx + 1}")

footer_content = "".join(lines[footer_start_idx:])

# Build the new content
new_content = header_content

# Append raw_practice_eng
new_content += "raw_practice_eng = [\n"
for q, opts, ans, sol in practice_raw_eng:
    new_content += f"    ({repr(q)}, {repr(opts)}, {ans}, {repr(sol)}),\n"
new_content += "]\n\n"

# Append raw_practice_hin
new_content += "raw_practice_hin = [\n"
for q, opts, ans, sol in practice_raw_hin:
    new_content += f"    ({repr(q)}, {repr(opts)}, {ans}, {repr(sol)}),\n"
new_content += "]\n\n"

# Append footer
new_content += footer_content

# Write to build_domestication_json.py
with open(build_file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("build_domestication_json.py has been successfully fixed and updated!")
