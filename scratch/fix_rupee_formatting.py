import os
import json

def fix_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace $₹ with ₹$ to put Rupee sign outside math mode
    new_content = content.replace("$₹", "₹$")
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed: {file_path}")

def scan_and_fix(directory):
    for root, dirs, files in os.walk(directory):
        if "node_modules" in dirs:
            dirs.remove("node_modules")
        if ".git" in dirs:
            dirs.remove(".git")
        for file in files:
            if file.endswith(".json"):
                fix_json_file(os.path.join(root, file))

scan_and_fix("ssc-cgl")
print("Rupee formatting scan complete.")
