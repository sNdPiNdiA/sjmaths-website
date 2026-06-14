import os
import json
import time
import re
from deep_translator import GoogleTranslator

BASE_DIR = r"C:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\history-of-india\pre-historic-period"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

translator = GoogleTranslator(source='en', target='hi')

# Cache to prevent duplicate translations and speed up
translation_cache = {}

def translate_string(text):
    if not isinstance(text, str) or not text.strip():
        return text
    
    # Check if already translated
    if text in translation_cache:
        return translation_cache[text]
    
    # Special check for SVG diagrams to not translate internal SVG code
    if "<svg" in text:
        # Since it's a huge inline SVG, let's keep it as is, or only translate the texts inside <text> tags if needed.
        # Actually, the SVG has inline English text. If we want a fully localized SVG, we can keep it as is
        # but let's see. In index.html we have some SVG styles. The SVG itself is defined in generate_prehistoric_content.py
        # and has text elements like "Lower Palaeolithic", etc.
        # For simplicity and correctness, we will preserve the SVG elements but we can try translating the text nodes
        # inside or keep the SVG as is. Let's translate the text parts inside <text> tags if they are English.
        # However, to avoid breaking the SVG XML, let's write a regex translation for text tags.
        def translate_svg_text(match):
            text_val = match.group(2)
            # Translate if it contains alphabetical characters and is not a class or variable
            if re.search(r'[a-zA-Z]', text_val) and not text_val.startswith('&') and not text_val.endswith(';'):
                try:
                    translated = translator.translate(text_val)
                    time.sleep(0.1)
                    return f'{match.group(1)}{translated}</text>'
                except Exception:
                    return match.group(0)
            return match.group(0)
        
        translated_svg = re.sub(r'(<text[^>]*>)(.*?)</text>', translate_svg_text, text)
        translation_cache[text] = translated_svg
        return translated_svg

    # Retries for robust API calls
    for attempt in range(3):
        try:
            # Clean text if it has double stars to HTML bold tags
            # The deep_translator might choke on some markdown, but usually it's fine.
            translated = translator.translate(text)
            translation_cache[text] = translated
            time.sleep(0.1) # short pause to avoid rate limiting
            return translated
        except Exception as e:
            print(f"Error translating: {text[:30]}... Attempt {attempt+1}. Error: {e}")
            time.sleep(1)
            
    return text

def translate_structure(data, key_context=None):
    if isinstance(data, dict):
        new_dict = {}
        for k, v in data.items():
            # Skip keys that shouldn't be translated
            if k in ["type", "ans", "icon", "parentUrl", "key", "val", "opts_en"]:
                new_dict[k] = v
            elif k == "opts" and isinstance(v, list):
                # options list
                new_dict[k] = [translate_string(item) for item in v]
            else:
                new_dict[k] = translate_structure(v, k)
        return new_dict
    elif isinstance(data, list):
        return [translate_structure(item, key_context) for item in data]
    elif isinstance(data, str):
        # Do not translate if it's the value of 'type' key
        if key_context == "type":
            return data
        return translate_string(data)
    else:
        return data

def main():
    # 1. Translate theory.json
    print("Translating theory.json...")
    with open(os.path.join(BASE_DIR, "theory.json"), "r", encoding="utf-8") as f:
        theory_data = json.load(f)
    
    # Custom tweaks for breadcrumbs
    if "breadcrumbs" in theory_data:
        theory_data["breadcrumbs"]["parent"] = "भारत का इतिहास"
        theory_data["breadcrumbs"]["current"] = "प्रागैतिहासिक काल"
        
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
