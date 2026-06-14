import os
import json
import time
import re
from deep_translator import GoogleTranslator

BASE_DIR = r"C:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\history-of-india\indus-valley-civilization"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

translator = GoogleTranslator(source='en', target='hi')

# Cache to prevent duplicate translations and speed up
translation_cache = {}

def clean_translated_html(text):
    # Fix broken style/CSS translations by Google Translate
    replacements = {
        r"फ़ॉन्ट-वेट:\s*800;?": "font-weight: 800;",
        r"फ़ॉन्ट-वजन:\s*800;?": "font-weight: 800;",
        r"फ़ॉन्ट-भार:\s*800;?": "font-weight: 800;",
        r"font-weight:\s*800;?": "font-weight: 800;",
        r"और\s*amp;": "&amp;",
        r"&amp;\s*amp;": "&amp;",
        r"class='premium-table'": "class=\"premium-table\"",
        r"class='premium-table-container'": "class=\"premium-table-container\"",
    }
    for pattern, repl in replacements.items():
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
    return text

def translate_html_text(text):
    if not isinstance(text, str) or not text.strip():
        return text
    
    if text in translation_cache:
        return translation_cache[text]

    # If the text has an SVG block, we need to translate the parts around it,
    # and only translate the <text> nodes inside the SVG.
    if "<svg" in text:
        parts = []
        last_idx = 0
        # Find all SVG blocks
        for match in re.finditer(r'(<svg.*?</svg>)', text, re.DOTALL):
            start, end = match.span()
            # 1. Translate the HTML before the SVG
            before_svg = text[last_idx:start]
            if before_svg.strip():
                parts.append(translate_html_text(before_svg))
            else:
                parts.append(before_svg)
            
            # 2. Process the SVG block (translate only <text> contents)
            svg_content = match.group(1)
            def translate_svg_text(svg_match):
                text_val = svg_match.group(2)
                if re.search(r'[a-zA-Z]', text_val) and not text_val.startswith('&') and not text_val.endswith(';'):
                    try:
                        translated = translator.translate(text_val)
                        time.sleep(0.1)
                        return f'{svg_match.group(1)}{translated}</text>'
                    except Exception:
                        return svg_match.group(0)
                return svg_match.group(0)
            
            translated_svg = re.sub(r'(<text[^>]*>)(.*?)</text>', translate_svg_text, svg_content)
            parts.append(translated_svg)
            last_idx = end
        
        # 3. Translate the remaining HTML after the last SVG
        after_svg = text[last_idx:]
        if after_svg.strip():
            parts.append(translate_html_text(after_svg))
        else:
            parts.append(after_svg)
            
        full_result = "".join(parts)
        translation_cache[text] = full_result
        return clean_translated_html(full_result)

    # Normal text / HTML string translation
    for attempt in range(3):
        try:
            translated = translator.translate(text)
            translated = clean_translated_html(translated)
            translation_cache[text] = translated
            time.sleep(0.1)  # Sleep to prevent rate-limiting
            return translated
        except Exception as e:
            print(f"Error translating: {text[:30]}... Attempt {attempt+1}. Error: {e}")
            time.sleep(1)
            
    return text

def translate_structure(data, key_context=None):
    if isinstance(data, dict):
        new_dict = {}
        for k, v in data.items():
            if k in ["type", "ans", "icon", "parentUrl", "key", "val", "opts_en"]:
                new_dict[k] = v
            elif k == "opts" and isinstance(v, list):
                new_dict[k] = [translate_html_text(item) for item in v]
            else:
                new_dict[k] = translate_structure(v, k)
        return new_dict
    elif isinstance(data, list):
        return [translate_structure(item, key_context) for item in data]
    elif isinstance(data, str):
        if key_context == "type":
            return data
        return translate_html_text(data)
    else:
        return data

def main():
    # 1. Translate theory.json
    print("Translating theory.json...")
    with open(os.path.join(BASE_DIR, "theory.json"), "r", encoding="utf-8") as f:
        theory_data = json.load(f)
    
    if "breadcrumbs" in theory_data:
        theory_data["breadcrumbs"]["parent"] = "भारत का इतिहास"
        theory_data["breadcrumbs"]["current"] = "सिंधु घाटी सभ्यता"
        
    translated_theory = translate_structure(theory_data)
    
    with open(os.path.join(HI_DIR, "theory.json"), "w", encoding="utf-8") as f:
        json.dump(translated_theory, f, ensure_ascii=False, indent=4)
    print("theory.json translated successfully!")

    # 2. Translate practice.json
    print("Translating practice.json...")
    with open(os.path.join(BASE_DIR, "practice.json"), "r", encoding="utf-8") as f:
        practice_data = json.load(f)
    
    translated_practice = translate_structure(practice_data)
    
    with open(os.path.join(HI_DIR, "practice.json"), "w", encoding="utf-8") as f:
        json.dump(translated_practice, f, ensure_ascii=False, indent=4)
    print("practice.json translated successfully!")

    # 3. Translate mastery.json
    print("Translating mastery.json...")
    with open(os.path.join(BASE_DIR, "mastery.json"), "r", encoding="utf-8") as f:
        mastery_data = json.load(f)
        
    translated_mastery = translate_structure(mastery_data)
    
    with open(os.path.join(HI_DIR, "mastery.json"), "w", encoding="utf-8") as f:
        json.dump(translated_mastery, f, ensure_ascii=False, indent=4)
    print("mastery.json translated successfully!")

if __name__ == "__main__":
    main()
