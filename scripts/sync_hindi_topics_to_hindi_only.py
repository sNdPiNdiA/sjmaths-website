import os
import sys
import re
import json
import argparse
from bs4 import BeautifulSoup

# Ensure UTF-8 output on Windows console
sys.stdout.reconfigure(encoding='utf-8')

MAP_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsssc-intermediate-level\hindi\badges_tags_hindi_map.json"
HINDI_BASE_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsssc-intermediate-level\hindi"

with open(MAP_PATH, "r", encoding="utf-8") as f:
    BADGES_MAP = json.load(f)

# Custom curated overrides for high-frequency UPSSSC exam terminology
BADGES_MAP.update({
    "UPSSSC Exam Trap": "परीक्षा जाल / विशेष ध्यान",
    "UPSSSC Exam Trend": "परीक्षा प्रवृत्ति",
    "Direct Exam Fact": "सीधा परीक्षा तथ्य",
    "Identification Trick": "पहचान की ट्रिक",
    "Exam Trap Alert": "सावधानी / परीक्षा जाल",
    "Strict Binary": "द्वि-विभाजन नियम",
    "Binary Classification": "दो भेद / द्वि-विभाजन",
    "Honorific Plural": "आदरार्थक बहुवचन",
    "Self-Reference Plural": "स्वाभिमानसूचक बहुवचन",
    "Direct Verb Link": "सीधा क्रिया संबंध",
    "Easy": "सरल",
    "Medium": "मध्यम",
    "Hard": "कठिन",
    "Gender Identification - Easy": "लिंग पहचान - सरल",
    "Gender Identification - Medium": "लिंग पहचान - मध्यम",
    "Gender Identification - Hard": "लिंग पहचान - कठिन",
    "Number Rules - Easy": "वचन नियम - सरल",
    "Number Rules - Medium": "वचन नियम - मध्यम",
    "Number Rules - Hard": "वचन नियम - कठिन",
    "Pointwise Notes": "बिंदुवार नोट्स",
    "30 Practice MCQs": "30 अभ्यास प्रश्न",
    "15-Q Mini Test": "15 प्रश्न मिनी टेस्ट"
})

def clean_hindi_option(txt):
    m = re.match(r'^([A-D]\.\s*)(.*)$', txt)
    if not m:
        return txt
    prefix = m.group(1)
    body = m.group(2).strip()
    
    if ' / ' not in body:
        return txt
        
    parts = body.split(' / ')
    if len(parts) == 2:
        return prefix + parts[1].strip()
    elif len(parts) == 3:
        return prefix + parts[2].strip()
    elif len(parts) == 4:
        return prefix + ' / '.join(parts[2:]).strip()
    elif len(parts) == 5:
        return prefix + ' / '.join(parts[3:]).strip()
    elif len(parts) == 6:
        return prefix + ' / '.join(parts[3:]).strip()
    elif len(parts) == 8:
        return prefix + ' / '.join(parts[4:]).strip()
    else:
        half = len(parts) // 2
        return prefix + ' / '.join(parts[half:]).strip()

def process_html_file(file_path, is_dry_run=True):
    with open(file_path, "r", encoding="utf-8") as f:
        raw_html = f.read()

    soup = BeautifulSoup(raw_html, "html.parser")

    # 1. Breadcrumbs
    for a in soup.select(".breadcrumbs-path a"):
        if "#subj-hin" in a.get("href", ""):
            en_span = a.find("span", class_="lang-en")
            hi_span = a.find("span", class_="lang-hi")
            if en_span and hi_span:
                en_span.string = hi_span.get_text(strip=True)

    bc_en = soup.select_one(".breadcrumbs-path > span.lang-en")
    bc_hi = soup.select_one(".breadcrumbs-path > span.lang-hi")
    if bc_en and bc_hi:
        bc_en.string = bc_hi.get_text(strip=True)

    # 2. Tabs Navigation Bar
    for btn in soup.select(".topic-tabs-bar .topic-tab-btn"):
        en_span = btn.find("span", class_="lang-en")
        hi_span = btn.find("span", class_="lang-hi")
        if en_span and hi_span:
            en_span.string = hi_span.get_text(strip=True)

    # 3. Topic Header
    header = soup.select_one(".topic-header")
    if header:
        meta_tag = header.select_one(".topic-meta-tag")
        if meta_tag:
            en = meta_tag.find("span", class_="lang-en")
            hi = meta_tag.find("span", class_="lang-hi")
            if en and hi:
                en.clear()
                en.append(BeautifulSoup(hi.decode_contents(), "html.parser"))

        h1 = header.select_one("h1")
        if h1:
            en = h1.find("span", class_="lang-en")
            hi = h1.find("span", class_="lang-hi")
            if en and hi:
                en.clear()
                en.append(BeautifulSoup(hi.decode_contents(), "html.parser"))

        subtitle = header.select_one(".topic-subtitle")
        if subtitle:
            en = subtitle.find("span", class_="lang-en")
            hi = subtitle.find("span", class_="lang-hi")
            if en and hi:
                en.clear()
                en.append(BeautifulSoup(hi.decode_contents(), "html.parser"))

    # 4. Tab 1 Notes
    for sec in soup.select("#pane-notes .notes-section"):
        h2 = sec.find("h2")
        if h2:
            en = h2.find("span", class_="lang-en")
            hi = h2.find("span", class_="lang-hi")
            if en and hi:
                en.clear()
                en.append(BeautifulSoup(hi.decode_contents(), "html.parser"))

        for ptr in sec.select(".exam-pointer"):
            en = ptr.find("span", class_="lang-en")
            hi = ptr.find("span", class_="lang-hi")
            if en and hi:
                en.clear()
                en.append(BeautifulSoup(hi.decode_contents(), "html.parser"))

        for th in sec.select("table.fact-table th"):
            en = th.find("span", class_="lang-en")
            hi = th.find("span", class_="lang-hi")
            if en and hi:
                en.clear()
                en.append(BeautifulSoup(hi.decode_contents(), "html.parser"))

        for td in sec.select("table.fact-table td"):
            en = td.find("span", class_="lang-en")
            hi = td.find("span", class_="lang-hi")
            if en and hi:
                en.clear()
                en.append(BeautifulSoup(hi.decode_contents(), "html.parser"))

        for li in sec.select(".point-list li"):
            badge = li.find("span", class_="key-badge")
            if badge:
                b_txt = badge.get_text(strip=True)
                if b_txt in BADGES_MAP:
                    badge.string = BADGES_MAP[b_txt]
            en = li.find("span", class_="lang-en")
            hi = li.find("span", class_="lang-hi")
            if en and hi:
                en.clear()
                en.append(BeautifulSoup(hi.decode_contents(), "html.parser"))

    # 5. Tab 2 Practice Quiz
    for card in soup.select("#pane-quiz .question-card"):
        tag = card.select_one(".q-tag")
        if tag:
            tag_text = tag.get_text(strip=True)
            if tag_text in BADGES_MAP:
                tag.string = BADGES_MAP[tag_text]

        q_en = card.select_one(".q-text.lang-en")
        q_hi = card.select_one(".q-text.lang-hi")
        if q_en and q_hi:
            q_en.clear()
            q_en.append(BeautifulSoup(q_hi.decode_contents(), "html.parser"))

        for btn in card.select(".options-grid .opt-btn"):
            txt = btn.get_text(strip=True)
            btn.string = clean_hindi_option(txt)

        sol_badge = card.select_one(".sol-badge")
        if sol_badge:
            en = sol_badge.find("span", class_="lang-en")
            hi = sol_badge.find("span", class_="lang-hi")
            if en and hi:
                en.clear()
                en.append(BeautifulSoup(hi.decode_contents(), "html.parser"))

        sol_en = card.select_one(".sol-text.lang-en")
        sol_hi = card.select_one(".sol-text.lang-hi")
        if sol_en and sol_hi:
            sol_en.clear()
            sol_en.append(BeautifulSoup(sol_hi.decode_contents(), "html.parser"))

    # 6. Tab 3 Mini Test
    inst = soup.select_one(".test-instruction")
    if inst:
        en = inst.find("span", class_="lang-en")
        hi = inst.find("span", class_="lang-hi")
        if en and hi:
            en.clear()
            en.append(BeautifulSoup(hi.decode_contents(), "html.parser"))

    for tq in soup.select("#pane-test .test-q-box"):
        stem_en = tq.select_one(".tq-stem.lang-en")
        stem_hi = tq.select_one(".tq-stem.lang-hi")
        if stem_en and stem_hi:
            stem_en.clear()
            stem_en.append(BeautifulSoup(stem_hi.decode_contents(), "html.parser"))

        for lbl in tq.select(".tq-options label, .test-opt"):
            inp = lbl.find("input")
            txt = lbl.get_text(strip=True)
            cleaned = clean_hindi_option(txt)
            lbl.clear()
            if inp:
                lbl.append(inp)
                lbl.append(" " + cleaned)
            else:
                lbl.string = cleaned

    submit_btn = soup.find("button", id="testSubmitBtn")
    if submit_btn:
        en = submit_btn.find("span", class_="lang-en")
        hi = submit_btn.find("span", class_="lang-hi")
        if en and hi:
            en.clear()
            en.append(BeautifulSoup(hi.decode_contents(), "html.parser"))

    for b in soup.select(".test-scorecard button"):
        en = b.find("span", class_="lang-en")
        hi = b.find("span", class_="lang-hi")
        if en and hi:
            en.clear()
            en.append(BeautifulSoup(hi.decode_contents(), "html.parser"))

    mod_html = str(soup)

    # 7. Test Data Script: Replace solEn with solHi
    def repl_test_data(match):
        ans = match.group(1)
        sol_hi = match.group(3)
        return f'"ans":"{ans}","solEn":"{sol_hi}","solHi":"{sol_hi}"'

    mod_html = re.sub(r'"ans":\s*"([A-D])",\s*"solEn":\s*"([^"]*)",\s*"solHi":\s*"([^"]*)"', repl_test_data, mod_html)

    # 8. Sanity Validations
    en_tags = len(re.findall(r'class="[^"]*\blang-en\b[^"]*"', mod_html))
    hi_tags = len(re.findall(r'class="[^"]*\blang-hi\b[^"]*"', mod_html))
    tag_diff = abs(en_tags - hi_tags)
    
    quiz_count = len(re.findall(r'class="question-card"', mod_html))
    test_count = len(re.findall(r'class="test-q-box"', mod_html))
    test_ans_count = len(re.findall(r'\{\s*"ans"\s*:', mod_html))

    status = "OK" if (tag_diff == 0 and quiz_count == 30 and test_count == 15 and test_ans_count == 15) else "WARN"
    print(f"[{status}] {os.path.basename(os.path.dirname(file_path))}: EN={en_tags}, HI={hi_tags}, Diff={tag_diff}, Quiz={quiz_count}, Test={test_count}, TestData={test_ans_count}")

    if not is_dry_run:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(mod_html)

    return status == "OK"

def main():
    parser = argparse.ArgumentParser(description="Synchronize Hindi topics to Hindi only in both toggles")
    parser.add_argument("--topic", type=str, default=None, help="Specific topic slug to process")
    parser.add_argument("--write", action="store_true", help="Write changes to disk (default is dry-run)")
    args = parser.parse_args()

    topics = [d for d in os.listdir(HINDI_BASE_DIR) if os.path.isdir(os.path.join(HINDI_BASE_DIR, d))]
    topics.sort()

    if args.topic:
        topics = [t for t in topics if t == args.topic or args.topic in t]

    print(f"Starting Hindi sync. Total topics to process: {len(topics)}. Mode: {'WRITE' if args.write else 'DRY RUN'}\n")

    success_count = 0
    for t in topics:
        p = os.path.join(HINDI_BASE_DIR, t, "index.html")
        if not os.path.exists(p):
            print(f"[MISSING] {t}/index.html does not exist!")
            continue
        ok = process_html_file(p, is_dry_run=not args.write)
        if ok:
            success_count += 1

    print(f"\nCompleted! {success_count} / {len(topics)} topics passed validation.")

if __name__ == "__main__":
    main()
