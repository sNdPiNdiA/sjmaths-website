import os
import re

root_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-9\worksheets"

print("Analyzing worksheets for question vs solution counts...")

problem_files = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".html") and filename != "index.html":
            filepath = os.path.join(dirpath, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                
                # Count questions (assuming format "Question X:" or <li> inside <ol class="question-list">)
                # Let's count "Question [0-9]+:" occurrences
                questions = re.findall(r"Question\s+\d+:", content)
                num_questions = len(questions)
                
                # Count answer boxes
                answers = re.findall(r'class="answer-box"', content)
                num_answers = len(answers)
                
                if num_questions != num_answers:
                    print(f"MISMATCH: {filename} has {num_questions} questions but {num_answers} solutions.")
                    problem_files.append((filepath, num_questions, num_answers))
                
                # Check for empty solutions
                # Regex for <div class="answer-box">...</div> content
                # This is a bit rough for regex, but looking for short content might work
                # Actually, let's just rely on the count for now.

if not problem_files:
    print("\nAll worksheets appear to have matching counts of questions and solutions.")
else:
    print(f"\nFound {len(problem_files)} files with mismatches.")
