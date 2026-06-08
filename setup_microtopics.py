import os
import re
import glob
from bs4 import BeautifulSoup

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def setup_microtopics():
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
        m = re.match(r'\.\./([^/]+)/?', href)
        if not m:
            continue
            
        folder_name = m.group(1)
        subject_name = link.text.strip()
        subject_name = re.sub(r'\s*$', '', subject_name)
        
        target_dir = os.path.join(base_dir, 'ahc-ro-aro', folder_name)
        os.makedirs(target_dir, exist_ok=True)
        
        # Cleanup previously generated flat .html files to avoid duplicates
        existing_htmls = glob.glob(os.path.join(target_dir, '*.html'))
        for old_file in existing_htmls:
            if not old_file.endswith('index.html'):
                os.remove(old_file)
        
        details_blocks = card.find_all('details', class_='syllabus-subsection')
        
        index_links_html = ""
        
        for details in details_blocks:
            category_title_span = details.find('span', class_='subsection-title')
            category_title = category_title_span.text.strip() if category_title_span else "Topics"
            
            index_links_html += f"        <h3>{category_title}</h3>\n        <div class=\"topic-grid\">\n"
            
            items = details.find_all('li', class_='syllabus-item')
            for item in items:
                text_span = item.find('span', class_='syllabus-text')
                if text_span:
                    item_text = text_span.text.strip()
                    topic_slug = slugify(item_text)
                    
                    # For SEO, we use a directory with index.html
                    topic_dir = os.path.join(target_dir, topic_slug)
                    os.makedirs(topic_dir, exist_ok=True)
                    
                    index_links_html += f"            <a href=\"{topic_slug}/\" class=\"topic-card\">{item_text}</a>\n"
                    
                    # Generate the stub file inside the new directory
                    stub_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{item_text} - {subject_name} | SJMaths</title>
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
        .content-placeholder {{
            margin-top: 30px;
            padding: 20px;
            background: #f0f0f0;
            border: 2px dashed #ccc;
            text-align: center;
            color: #666;
            border-radius: 8px;
        }}
        .back-link {{
            display: inline-block;
            margin-top: 20px;
            color: #8e44ad;
            text-decoration: none;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="../" class="back-link">&larr; Back to {subject_name}</a>
        <h1>{item_text}</h1>
        <div class="content-placeholder">
            <p>Content for <strong>{item_text}</strong> will be added here.</p>
        </div>
    </div>
</body>
</html>"""
                    stub_path = os.path.join(topic_dir, 'index.html')
                    if not os.path.exists(stub_path):
                        with open(stub_path, 'w', encoding='utf-8') as sf:
                            sf.write(stub_content)
                            
            index_links_html += "        </div>\n"
            
        # Create the index.html content for the subject folder
        page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{subject_name} - Topics | SJMaths</title>
    <link rel="stylesheet" href="/assets/css/main.min.css">
    <style>
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #f9f9f9;
            color: #333;
            line-height: 1.6;
        }}
        .container {{
            max-width: 900px;
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
            margin-top: 30px;
            margin-bottom: 15px;
        }}
        .topic-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 15px;
        }}
        .topic-card {{
            display: block;
            padding: 15px;
            background: #fdfdfd;
            border: 1px solid #eaeaea;
            border-radius: 6px;
            text-decoration: none;
            color: #333;
            font-weight: 500;
            transition: all 0.2s ease;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        }}
        .topic-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(142, 68, 173, 0.15);
            border-color: #8e44ad;
            color: #8e44ad;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{subject_name}</h1>
        <p>Select a topic below to view or add its content.</p>
{index_links_html}
        <p style="margin-top: 40px;"><a href="../syllabus/" style="color: #8e44ad; text-decoration: none; font-weight: bold;">&larr; Back to Syllabus</a></p>
    </div>
</body>
</html>"""
        
        index_file = os.path.join(target_dir, 'index.html')
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(page_html)
            
        print(f"Generated directory structure for {folder_name} and cleaned up flat .html files.")

if __name__ == '__main__':
    setup_microtopics()