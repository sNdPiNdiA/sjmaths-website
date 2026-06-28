import os
import re
import subprocess
import glob

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to replace:
    # return [
    #     {
    #         "label": "Core Dimensions",
    #         ...
    #     }
    # ]
    # with the new two-branch structure where the second branch is dynamically interpolated with f"{t}" (or similar).
    # Let's inspect where "GENERAL FALLBACK" is located in the files.
    
    fallback_comment = "# --- GENERAL FALLBACK"
    pos = content.find(fallback_comment)
    if pos == -1:
        fallback_comment = "# Fallback"
        pos = content.find(fallback_comment)
        
    if pos == -1:
        print(f"Skipping (no fallback comment): {filepath}")
        return

    # Let's see if we can find the return statement after this comment
    return_pos = content.find("return [", pos)
    if return_pos == -1:
        print(f"Skipping (no return statement found): {filepath}")
        return
        
    # Match brackets to find the end of the return statement
    bracket_count = 1
    i = return_pos + 8
    while i < len(content) and bracket_count > 0:
        if content[i] == '[':
            bracket_count += 1
        elif content[i] == ']':
            bracket_count -= 1
        i += 1
        
    if bracket_count != 0:
        print(f"Skipping (unbalanced brackets in return statement): {filepath}")
        return
        
    # Replace the return statement with the new, dynamically populated two-branch list.
    # Note: the title variable in these scripts is typically `t`. Let's verify that.
    # The variable is defined as: `t = get_clean_title(folder_name)` in get_custom_branches.
    # So `t` is always available in get_custom_branches.
    
    new_return = f'''return [
        {{
            "label": "Core Dimensions",
            "type": "branch",
            "date": "Theory & Scope",
            "children": [
                {{
                    "label": "Definition & Scope", "type": "sub", "date": "Foundations",
                    "children": [
                        {{"label": f"Theoretical frameworks, core parameters, & geographic scope of {{t}}", "type": "leaf"}},
                        {{"label": "Key conceptual models, historical developments, & academic perspectives", "type": "leaf"}}
                    ]
                }},
                {{
                    "label": "Regional Distribution", "type": "sub", "date": "Spatial Variations",
                    "children": [
                        {{"label": "Spatial mapping, geographic concentrations, and resource distribution models", "type": "leaf"}},
                        {{"label": "Factors determining regional disparities, environmental constraints, & limits", "type": "leaf"}}
                    ]
                }}
            ]
        }},
        {{
            "label": f"{{t}} Focus",
            "type": "branch",
            "date": "Applied Study",
            "children": [
                {{
                    "label": "Policy & Schemes", "type": "sub", "date": "Government Action",
                    "children": [
                        {{"label": f"Major developmental programs, fiscal support, national policies, & planning for {{t}}", "type": "leaf"}},
                        {{"label": f"Regulatory institutions, state monitoring setups, and implementation gaps in {{t}}", "type": "leaf"}}
                    ]
                }},
                {{
                    "label": "Analysis & Issues", "type": "sub", "date": "Critical Review",
                    "children": [
                        {{"label": f"Common examiner traps, environmental impacts, and socio-economic challenges of {{t}}", "type": "leaf"}},
                        {{"label": f"Key case studies, policy suggestions, & sustainable development pathways for {{t}}", "type": "leaf"}}
                    ]
                }}
            ]
        }}
    ]'''

    content = content[:return_pos] + new_return + content[i:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully updated: {filepath}")

def main():
    py_files = glob.glob("add_*_mindmaps.py")
    print(f"Found {len(py_files)} python files.")
    for py_file in py_files:
        if py_file in ['add_chemistry_mindmaps.py', 'add_prehistory_mindmaps.py']:
            continue
        update_file(py_file)
        
    print("\nRe-running all updated scripts...")
    for py_file in py_files:
        if py_file in ['add_chemistry_mindmaps.py', 'add_prehistory_mindmaps.py']:
            continue
        print(f"Running {py_file}...")
        subprocess.run(["python", py_file], check=True)
        print(f"Finished {py_file}\n")

if __name__ == '__main__':
    main()
