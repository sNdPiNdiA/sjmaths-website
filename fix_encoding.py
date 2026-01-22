#!/usr/bin/env python3
import os
import glob

base_path = r"c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\ncert-exercise-practice"

# Map of corrupted sequences to correct characters
replacements = {
    'â€"': '–',      # Em-dash
    'â€¦': '…',      # Ellipsis  
    'âˆ'': '−',      # Minus sign
    'âˆš': '√',      # Square root
    'Â©': '©',       # Copyright
    'â€™': ''',      # Right single quote
    'â„': 'π',       # Pi
    'Â': '',         # Remove stray A with macron
}

for filepath in glob.glob(os.path.join(base_path, '**', 'exercise-*.html'), recursive=True):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Apply replacements
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        # Write back if changed
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {os.path.basename(filepath)}")
        else:
            print(f"OK: {os.path.basename(filepath)}")
    except Exception as e:
        print(f"Error in {filepath}: {e}")

print("Done!")
