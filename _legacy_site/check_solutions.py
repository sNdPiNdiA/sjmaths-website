import os

root_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-9\worksheets"

missing_solutions = []
total_files = 0
files_with_solutions = 0

print("Checking for worksheets missing solutions...")

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".html") and filename != "index.html":
            total_files += 1
            filepath = os.path.join(dirpath, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                if 'class="answer-box"' not in content:
                    missing_solutions.append(filepath)
                else:
                    files_with_solutions += 1

print(f"Total worksheets found: {total_files}")
print(f"Worksheets with solutions: {files_with_solutions}")
print(f"Worksheets MISSING solutions: {len(missing_solutions)}")

if missing_solutions:
    print("\nFiles missing solutions:")
    for f in missing_solutions:
        print(f)
