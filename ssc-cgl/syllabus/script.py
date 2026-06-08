import os
from bs4 import BeautifulSoup
import re

file_path = r"c:\Users\sande\Documents\GitHub\sjmaths-website\ssc-cgl\syllabus\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add missing CSS
css_to_add = """
        /* Subsections - Collapsible details/summary */
        details.syllabus-subsection {
            background: rgba(255, 255, 255, 0.4);
            border: 1px solid rgba(0, 0, 0, 0.05);
            border-radius: 8px;
            margin-bottom: 0.75rem;
            transition: all 0.3s ease;
            overflow: hidden;
        }

        body.dark-mode details.syllabus-subsection {
            background: rgba(255, 255, 255, 0.02);
            border-color: rgba(255, 255, 255, 0.05);
        }

        details.syllabus-subsection[open] {
            background: var(--glass-bg);
            border-color: rgba(142, 68, 173, 0.2);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        }

        summary.subsection-summary {
            padding: 0.8rem 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            list-style: none;
            user-select: none;
        }

        summary.subsection-summary::-webkit-details-marker {
            display: none;
        }

        .subsection-title {
            font-family: 'Outfit', sans-serif;
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--text-dark);
            margin: 0;
            padding: 0;
            border: none;
            text-transform: none;
            letter-spacing: normal;
            flex-grow: 1;
            padding-right: 1rem;
            text-align: left;
        }

        .subsection-meta {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .subsection-progress {
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.15rem 0.5rem;
            background: rgba(0, 0, 0, 0.05);
            color: var(--text-light);
            border-radius: 12px;
            white-space: nowrap;
            transition: all 0.2s ease;
        }

        body.dark-mode .subsection-progress {
            background: rgba(255, 255, 255, 0.08);
        }

        .subsection-progress.completed {
            background: rgba(46, 204, 113, 0.15);
            color: #2ecc71;
        }

        .toggle-icon {
            font-size: 0.8rem;
            color: var(--text-light);
            transition: transform 0.3s ease;
        }

        details.syllabus-subsection[open] .toggle-icon {
            transform: rotate(180deg);
            color: var(--primary);
        }

        details.syllabus-subsection .syllabus-list {
            border-top: 1px solid rgba(0, 0, 0, 0.05);
            padding: 0.5rem;
            margin: 0;
            list-style: none;
        }

        body.dark-mode details.syllabus-subsection .syllabus-list {
            border-top-color: rgba(255, 255, 255, 0.05);
        }

        /* Card scrollable area */
        .card-scrollable {
            overflow-y: auto;
            flex-grow: 1;
            padding-right: 0.5rem;
            max-height: 600px;
        }

        /* Custom Scrollbar for Subject Cards */
        .card-scrollable::-webkit-scrollbar {
            width: 6px;
        }

        .card-scrollable::-webkit-scrollbar-track {
            background: transparent;
        }

        .card-scrollable::-webkit-scrollbar-thumb {
            background: rgba(142, 68, 173, 0.2);
            border-radius: 10px;
        }

        .card-scrollable::-webkit-scrollbar-thumb:hover {
            background: rgba(142, 68, 173, 0.4);
        }
"""
html = html.replace('/* Subsections (For Algebra, Geometry, etc.) */', css_to_add)

# Add JS progress tracker part
js_to_add = """
                // Recalculate and update sub-section checklist progress & badges
                const subsections = document.querySelectorAll('.syllabus-subsection');
                subsections.forEach(sub => {
                    const prefix = sub.getAttribute('data-prefix');
                    const grpIdx = sub.getAttribute('data-grp-idx');
                    const subCheckboxes = sub.querySelectorAll('.syllabus-checkbox');
                    const subTotal = subCheckboxes.length;
                    const subChecked = Array.from(subCheckboxes).filter(cb => cb.checked).length;

                    const progEl = document.getElementById(`${prefix}-prog-${grpIdx}`);
                    if (progEl) {
                        progEl.textContent = `${subChecked}/${subTotal}`;
                        if (subChecked === subTotal && subTotal > 0) {
                            progEl.classList.add('completed');
                        } else {
                            progEl.classList.remove('completed');
                        }
                    }
                });
"""
if "const subsections = document.querySelectorAll('.syllabus-subsection');" not in html:
    html = html.replace('updateProgress();\n        });\n    </script>', js_to_add + '\n            }\n            updateProgress();\n        });\n    </script>')
    # actually wait, the original ssc-cgl html has a function updateProgress() without the sub-section logic. Let me regex replace it properly.

soup = BeautifulSoup(html, 'html.parser')

def process_card(card, subject_prefix):
    # Check if this card already has a card-scrollable div
    if card.find('div', class_='card-scrollable'):
        return
    
    # We will gather all content after the h2 subject-title
    h2 = card.find('h2', class_='subject-title')
    if not h2: return
    
    # Create card-scrollable wrapper
    scrollable_div = soup.new_tag('div', attrs={'class': 'card-scrollable'})
    
    # Process subsections
    # Some cards have <div class="subsection-title"> followed by <ul class="syllabus-list">
    # Others just have <ul class="syllabus-list">
    
    subtitles = card.find_all('div', class_='subsection-title')
    if subtitles:
        # Tier 2 structure
        grp_idx = 0
        current_el = h2.find_next_sibling()
        while current_el:
            next_el = current_el.find_next_sibling()
            if current_el.name == 'div' and 'subsection-title' in current_el.get('class', []):
                title_text = current_el.get_text(strip=True)
                ul = next_el if next_el and next_el.name == 'ul' else None
                
                if ul:
                    details = soup.new_tag('details', attrs={'class': 'syllabus-subsection', 'data-prefix': subject_prefix, 'data-grp-idx': str(grp_idx)})
                    summary = soup.new_tag('summary', attrs={'class': 'subsection-summary'})
                    
                    span_title = soup.new_tag('span', attrs={'class': 'subsection-title'})
                    span_title.string = title_text
                    summary.append(span_title)
                    
                    meta_div = soup.new_tag('div', attrs={'class': 'subsection-meta'})
                    span_prog = soup.new_tag('span', attrs={'class': 'subsection-progress', 'id': f"{subject_prefix}-prog-{grp_idx}"})
                    span_prog.string = "0/0"
                    i_icon = soup.new_tag('i', attrs={'class': 'fas fa-chevron-down toggle-icon'})
                    meta_div.append(span_prog)
                    meta_div.append(i_icon)
                    summary.append(meta_div)
                    
                    details.append(summary)
                    
                    # Clone ul inside details
                    ul_clone = BeautifulSoup(str(ul), 'html.parser').find('ul')
                    details.append(ul_clone)
                    
                    scrollable_div.append(details)
                    grp_idx += 1
                    
                    current_el.extract()
                    ul.extract()
            current_el = next_el
    else:
        # Tier 1 structure - no subtitles, just flat list
        ul = card.find('ul', class_='syllabus-list')
        if ul:
            # Depending on subject_prefix, we can group them
            # We'll just group everything into "All Topics" for simplicity if we don't have hardcoded mappings,
            # But the prompt says "microlist the subjects... just like upsc". Let's create a generic details for the whole list if we can't map.
            # However, I should try to map Tier 1
            mapping = {}
            if 'qa' in subject_prefix:
                mapping = {
                    "Number System & Arithmetic": [1,2,3,4,5,6,7,8,9,10,11,12],
                    "Algebra": [13],
                    "Geometry": [14,15,16,17],
                    "Mensuration": [18,19],
                    "Trigonometry": [20,21],
                    "Statistics & Data Interpretation": [22]
                }
            elif 'gi' in subject_prefix:
                mapping = {
                    "General Reasoning": [1,2,5,6],
                    "Logic & Analysis": [3,4,11,12],
                    "Number & Sequence": [7,13],
                    "Non-Verbal & Coding": [8,9,10]
                }
            elif 'eng' in subject_prefix:
                mapping = {
                    "Vocabulary": [1,2,7,8],
                    "Grammar": [3,4,5,9],
                    "Reading & Comprehension": [6,10,11,12]
                }
            elif 'ga' in subject_prefix:
                mapping = {
                    "Current Events & People": [3,6,7,8,9],
                    "History & Geography": [1,11,12],
                    "Polity & Economy": [13,14],
                    "Static GK & Misc": [2,4,5,10]
                }

            items = ul.find_all('li')
            grp_idx = 0
            if mapping:
                for group_name, indices in mapping.items():
                    details = soup.new_tag('details', attrs={'class': 'syllabus-subsection', 'data-prefix': subject_prefix, 'data-grp-idx': str(grp_idx)})
                    summary = soup.new_tag('summary', attrs={'class': 'subsection-summary'})
                    
                    span_title = soup.new_tag('span', attrs={'class': 'subsection-title'})
                    span_title.string = group_name
                    summary.append(span_title)
                    
                    meta_div = soup.new_tag('div', attrs={'class': 'subsection-meta'})
                    span_prog = soup.new_tag('span', attrs={'class': 'subsection-progress', 'id': f"{subject_prefix}-prog-{grp_idx}"})
                    span_prog.string = "0/0"
                    i_icon = soup.new_tag('i', attrs={'class': 'fas fa-chevron-down toggle-icon'})
                    meta_div.append(span_prog)
                    meta_div.append(i_icon)
                    summary.append(meta_div)
                    
                    details.append(summary)
                    
                    new_ul = soup.new_tag('ul', attrs={'class': 'syllabus-list'})
                    for idx in indices:
                        if idx - 1 < len(items):
                            new_ul.append(items[idx-1].extract())
                    details.append(new_ul)
                    scrollable_div.append(details)
                    grp_idx += 1
            else:
                details = soup.new_tag('details', attrs={'class': 'syllabus-subsection', 'data-prefix': subject_prefix, 'data-grp-idx': '0'})
                summary = soup.new_tag('summary', attrs={'class': 'subsection-summary'})
                span_title = soup.new_tag('span', attrs={'class': 'subsection-title'})
                span_title.string = "All Topics"
                summary.append(span_title)
                meta_div = soup.new_tag('div', attrs={'class': 'subsection-meta'})
                span_prog = soup.new_tag('span', attrs={'class': 'subsection-progress', 'id': f"{subject_prefix}-prog-0"})
                span_prog.string = "0/0"
                i_icon = soup.new_tag('i', attrs={'class': 'fas fa-chevron-down toggle-icon'})
                meta_div.append(span_prog)
                meta_div.append(i_icon)
                summary.append(meta_div)
                details.append(summary)
                ul_clone = BeautifulSoup(str(ul), 'html.parser').find('ul')
                details.append(ul_clone)
                scrollable_div.append(details)
            ul.extract()

    # Move anything left between h2 and end of card (or h2 next siblings) into scrollable_div, EXCEPT we already removed them. Wait, what if there's other stuff?
    # To be safe, we just append scrollable_div right after h2
    h2.insert_after(scrollable_div)

# Process all cards
card_idx = 0
for panel in soup.find_all('div', class_='tab-panel'):
    panel_id = panel.get('id', '')
    for card in panel.find_all('div', class_='subject-card'):
        prefix = f"{panel_id.replace('panel-', '')}-c{card_idx}"
        process_card(card, prefix)
        card_idx += 1

# Fix the script block for subsection progress
html_output = str(soup)

# we need to inject the JS if not done successfully by simple replace
if "const subsections = document.querySelectorAll('.syllabus-subsection');" not in html_output:
    # use regex to insert before the last closing brace of updateProgress
    # find updateProgress() { ... }
    
    js_addition = """
                // Recalculate and update sub-section checklist progress & badges
                const subsections = document.querySelectorAll('.syllabus-subsection');
                subsections.forEach(sub => {
                    const prefix = sub.getAttribute('data-prefix');
                    const grpIdx = sub.getAttribute('data-grp-idx');
                    const subCheckboxes = sub.querySelectorAll('.syllabus-checkbox');
                    const subTotal = subCheckboxes.length;
                    const subChecked = Array.from(subCheckboxes).filter(cb => cb.checked).length;

                    const progEl = document.getElementById(`${prefix}-prog-${grpIdx}`);
                    if (progEl) {
                        progEl.textContent = `${subChecked}/${subTotal}`;
                        if (subChecked === subTotal && subTotal > 0) {
                            progEl.classList.add('completed');
                        } else {
                            progEl.classList.remove('completed');
                        }
                    }
                });
    """
    
    # We will do a safe string replacement on the script
    parts = html_output.split('function updateProgress() {')
    if len(parts) > 1:
        # split by next function or end of script
        inner_parts = parts[1].split('updateProgress();')
        if len(inner_parts) > 1:
            new_script = 'function updateProgress() {' + inner_parts[0] + js_addition + '            }\n            updateProgress();' + 'updateProgress();'.join(inner_parts[1:])
            html_output = parts[0] + new_script
        else:
            # fallback
            pass

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_output)
print("Updated successfully")
