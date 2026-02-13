import os

# Mapping of Artifact -> Correct Character
# Based on analysis of audit report and common mojibake patterns
REPLACEMENTS = {
    'âˆš': '√',       # Square Root
    'âœ”': '✔',       # Checkmark
    'Ã—': '×',        # Multiply
    'â‚¹': '₹',       # Rupee
    'Â²': '²',        # Squared
    'Â³': '³',        # Cubed
    'âš¡': '⚡',      # Lightning
    'â\x81¿': 'ⁿ',    # Superscript n
    'áµ\x90': 'ᵐ',    # Superscript m
    'â™¥': '♥',       # Heart
    'â™¦': '♦',       # Diamond
    'â™\xa0': '♠',    # Spade
    'â™£': '♣',       # Club
    '←\x90': '←',     # Fix arrow artifact
    '\ufeff': '',     # BOM
    'â€“': '–',       # En-dash (if present in this form)
    'â\x8f°': '⏰',    # Alarm clock
}

def fix_encoding(directory):
    count_files = 0
    count_replacements = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    original_content = content
                    file_changed = False
                    
                    for artifact, correct in REPLACEMENTS.items():
                        if artifact in content:
                            content = content.replace(artifact, correct)
                            file_changed = True
                            count_replacements += 1

                    if file_changed:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(f"Fixed: {path}")
                        count_files += 1

                except Exception as e:
                    print(f"Error processing {path}: {e}")

    print(f"\nSummary: Modified {count_files} files.")

target_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\classes\class-10\chapter-wise-notes"
fix_encoding(target_dir)
