import os
from bs4 import BeautifulSoup
import time
from deep_translator import GoogleTranslator
from concurrent.futures import ThreadPoolExecutor

file_path = 'ahc-ro-aro/syllabus/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

def extract_text_and_icon(element):
    if not element:
        return None, None
    text_to_translate = element.get_text(strip=True)
    icon_html = ""
    for child in element.children:
        if child.name == 'i':
            icon_html = str(child)
            text_to_translate = text_to_translate.replace(child.get_text(strip=True), "").strip()
    return text_to_translate, icon_html

elements_to_translate = []
elements_to_translate.extend(soup.select('h2.subject-title a'))
elements_to_translate.extend(soup.select('span.subsection-title'))
elements_to_translate.extend(soup.select('span.syllabus-text a'))

unique_texts = set()
for el in elements_to_translate:
    text, _ = extract_text_and_icon(el)
    if text:
        unique_texts.add(text)

unique_texts = list(unique_texts)
print(f"Total unique strings to translate: {len(unique_texts)}")

translation_cache = {}

def fetch_translation(text):
    if not text:
        return text
    translator = GoogleTranslator(source='en', target='hi')
    retries = 3
    for attempt in range(retries):
        try:
            res = translator.translate(text)
            time.sleep(0.5) # respect rate limit
            return res
        except Exception as e:
            if attempt == retries - 1:
                print(f"Error translating '{text}': {e}")
                return text
            time.sleep(2)

# Use ThreadPoolExecutor to fetch translations concurrently
with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch_translation, unique_texts))

for en_text, hi_text in zip(unique_texts, results):
    translation_cache[en_text] = hi_text

for el in elements_to_translate:
    text, icon_html = extract_text_and_icon(el)
    if not text:
        continue
    
    translated_text = translation_cache.get(text, text)
    new_html = f'<span class="lang-hi">{translated_text}</span><span class="lang-en" style="display: none;">{text}</span> {icon_html}'
    el.clear()
    el.append(BeautifulSoup(new_html, 'html.parser'))

# Add Language Toggle Button
header = soup.select_one('.syllabus-header')
if header:
    toggle_html = """
    <div class="lang-toggle-container" style="text-align: center; margin-top: 15px;">
        <button id="langToggleBtn" class="tab-btn" style="display: inline-flex; align-items: center; gap: 8px; margin: 0 auto; background: var(--accent-gradient); color: white;">
            <i class="fas fa-language"></i> View in English
        </button>
    </div>
    """
    header.append(BeautifulSoup(toggle_html, 'html.parser'))

# Add JavaScript for Toggle
script_html = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    const langBtn = document.getElementById('langToggleBtn');
    let currentLang = 'hi';
    
    if(langBtn) {
        langBtn.addEventListener('click', function() {
            const hiElements = document.querySelectorAll('.lang-hi');
            const enElements = document.querySelectorAll('.lang-en');
            
            if (currentLang === 'hi') {
                hiElements.forEach(el => el.style.display = 'none');
                enElements.forEach(el => el.style.display = 'inline');
                langBtn.innerHTML = '<i class="fas fa-language"></i> हिंदी में देखें';
                currentLang = 'en';
            } else {
                hiElements.forEach(el => el.style.display = 'inline');
                enElements.forEach(el => el.style.display = 'none');
                langBtn.innerHTML = '<i class="fas fa-language"></i> View in English';
                currentLang = 'hi';
            }
        });
    }
});
</script>
"""
body = soup.find('body')
if body:
    body.append(BeautifulSoup(script_html, 'html.parser'))

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Done translating and adding toggle.")