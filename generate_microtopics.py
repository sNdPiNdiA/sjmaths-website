import os
import re
from bs4 import BeautifulSoup

def generate_subject_pages():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    syllabus_file = os.path.join(base_dir, 'ahc-ro-aro', 'syllabus', 'index.html')
    
    with open(syllabus_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    soup = BeautifulSoup(html_content, 'html.parser')
    subject_cards = soup.find_all('div', class_='subject-card')
    
    for card in subject_cards:
        title_h2 = card.find('h2', class_='subject-title')
        if not title_h2:
            continue
            
        link = title_h2.find('a')
        if not link:
            continue
            
        href = link.get('href', '')
        # Extract folder name, e.g., "../general-science/" -> "general-science"
        m = re.match(r'\.\./([^/]+)/?', href)
        if not m:
            continue
            
        folder_name = m.group(1)
        subject_name = link.text.strip()
        
        # Remove any trailing icons or weird chars if needed
        # Assuming the text is clean enough, but let's strip out the font-awesome icon text just in case.
        subject_name = re.sub(r'\s*$', '', subject_name)
        
        # Now find the microtopics
        details_blocks = card.find_all('details', class_='syllabus-subsection')
        
        microtopics_html = ""
        for details in details_blocks:
            category_title_span = details.find('span', class_='subsection-title')
            category_title = category_title_span.text.strip() if category_title_span else "Topics"
            
            microtopics_html += f"        <h3>{category_title}</h3>\n        <ul>\n"
            
            items = details.find_all('li', class_='syllabus-item')
            for item in items:
                text_span = item.find('span', class_='syllabus-text')
                if text_span:
                    item_text = text_span.text.strip()
                    microtopics_html += f"            <li>{item_text}</li>\n"
                    
            microtopics_html += "        </ul>\n"
            
        # Create the HTML content
        page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{subject_name} - Microtopics | SJMaths</title>
    <link rel="stylesheet" href="/assets/css/main.min.css">
    <style>
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #f9f9f9;
            color: #333;
            line-height: 1.6;
        }}
        .container {{
            max-width: 800px;
            margin: 40px auto;
            padding: 20px 40px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #8e44ad;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }}
        h3 {{
            color: #e74c3c;
            margin-top: 20px;
        }}
        ul {{
            list-style-type: disc;
            padding-left: 20px;
        }}
        li {{
            margin-bottom: 8px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{subject_name}</h1>
        <p>This is the list of microtopics for <strong>{subject_name}</strong> in the AHC RO/ARO Syllabus.</p>
{microtopics_html}
        <p><a href="../syllabus/" style="color: #8e44ad; text-decoration: none; font-weight: bold;">&larr; Back to Syllabus</a></p>
    </div>
</body>
</html>"""
        
        target_dir = os.path.join(base_dir, 'ahc-ro-aro', folder_name)
        os.makedirs(target_dir, exist_ok=True)
        
        target_file = os.path.join(target_dir, 'index.html')
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(page_html)
            
        print(f"Generated {target_file}")

if __name__ == '__main__':
    generate_subject_pages()
