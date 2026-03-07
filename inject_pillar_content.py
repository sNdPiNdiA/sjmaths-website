import os
import re

ROOT_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website"

# Mapping directory names to rich SEO Content snippets
SEO_CONTENT_MAP = {
    'chapter-wise-notes': {
        'title': 'Chapter-wise Revision Notes & Formulas',
        'desc': 'Our comprehensive chapter-wise notes provide clear, concise summaries of all critical concepts, theorems, and formulas. Use these notes for quick revision before your exams to ensure maximum retention.',
        'faq1_q': 'Are these notes aligned with the latest syllabus?',
        'faq1_a': 'Yes, all our notes are strictly aligned with the latest NCERT/CBSE rationalised syllabus.',
        'faq2_q': 'How should I use these notes for Board Exams?',
        'faq2_a': 'We recommend reading these notes immediately after completing the NCERT textbook chapters, and revising them multiple times in the weeks leading up to the final board exams.'
    },
    'ncert-exercise-practice': {
        'title': 'Step-by-Step NCERT Solutions',
        'desc': 'Master your textbook with our detailed, step-by-step NCERT exercise solutions. Understanding how to lay out your answers is crucial for securing full marks in descriptive board questions.',
        'faq1_q': 'Are there alternative methods provided?',
        'faq1_a': 'Where applicable, we provide both the standard textbook method and short-trick approaches to verify your answers.',
        'faq2_q': 'Why is practicing NCERT exercises so important?',
        'faq2_a': 'The CBSE board exams are primarily based on the concepts laid out in the NCERT textbook. Mastering these exercises guarantees a strong fundamental base.'
    },
    'previous-year-questions': {
        'title': '10 Years Previous Year Questions (PYQs)',
        'desc': 'Practicing past board exam questions is the single most effective way to understand the exam pattern, the weightage of topics, and the exact language the examiners use.',
        'faq1_q': 'Are these questions sorted by chapter?',
        'faq1_a': 'Yes, all PYQs are meticulously categorized by chapter to allow targeted practice.',
        'faq2_q': 'Do these include marking schemes?',
        'faq2_a': 'Absolutely. The solutions provided follow the official CBSE step-marking parameters so you know exactly where marks are awarded.'
    },
    'full-length-test-papers': {
        'title': 'Full-Length Mock Board Papers',
        'desc': 'Simulate the exact exam environment with our full-length mock tests. Practicing timed papers improves your speed, accuracy, and helps manage exam anxiety.',
        'faq1_q': 'Are these tests based on the latest exam pattern?',
        'faq1_a': 'Yes, all sample papers follow the latest CBSE blueprint, including Objective Type, Case-Based, and Assertion-Reasoning questions.',
        'faq2_q': 'How strict should I be with time?',
        'faq2_a': 'Treat these exactly like the real 3-hour exam. Set a timer and do not look at the solutions until the time is up.'
    },
    'worksheets': {
        'title': 'Printable Topic-wise Worksheets',
        'desc': 'Reinforce your daily learning with topic-specific worksheets. These are perfect for homework practice, school assignments, or targeted revision of weak areas.',
        'faq1_q': 'Can these be printed?',
        'faq1_a': 'Yes, the worksheets are designed in a printer-friendly layout.',
        'faq2_q': 'Are answers provided?',
        'faq2_a': 'Detailed answer keys are provided alongside the worksheets so students can self-assess their progress.'
    },
    'tests': {
        'title': 'Interactive Chapter Tests & MCQs',
        'desc': 'Quickly assess your conceptual clarity with our fast-paced objective tests. Perfect for mastering the 1-mark section of your board exams.',
        'faq1_q': 'Are these tests timed?',
        'faq1_a': 'Yes, to help you build speed for the objective section of the paper.',
        'faq2_q': 'Do you cover Assertion-Reasoning?',
        'faq2_a': 'Yes, our tests heavily feature Assertion-Reasoning and Case-Based MCQs as per the latest exam trends.'
    }
}


def build_seo_html(cls_num, hub_type):
    data = SEO_CONTENT_MAP.get(hub_type)
    if not data:
        return ""

    html = f"""
    <section class="seo-pillar-content" style="max-width: 900px; margin: 40px auto; padding: 30px; background: rgba(255, 255, 255, 0.9); border-radius: 16px; box-shadow: var(--card-shadow, 0 10px 30px rgba(0,0,0,0.05)); border: 1px solid rgba(0,0,0,0.05); animation: fadeIn 0.8s ease-out;">
        <h2 style="text-align: center; color: var(--primary-dark, #6c3483); margin-bottom: 20px; font-size: 1.8rem;">Class {cls_num} Maths: {data['title']}</h2>
        
        <p style="color: var(--text-main, #2c3e50); font-size: 1.1rem; line-height: 1.6; margin-bottom: 30px; text-align: center;">
            {data['desc']}
        </p>

        <h3 style="color: var(--primary, #8e44ad); font-size: 1.4rem; margin-bottom: 15px; border-bottom: 2px solid rgba(142, 68, 173, 0.2); padding-bottom: 10px;">Frequently Asked Questions</h3>
        
        <div class="faq-item" style="margin-bottom: 20px;">
            <h4 style="font-size: 1.1rem; font-weight: 600; color: var(--text-main, #2c3e50); margin-bottom: 8px;">{data['faq1_q']}</h4>
            <p style="color: var(--text-light, #7f8c8d); line-height: 1.5;">{data['faq1_a']}</p>
        </div>
        
        <div class="faq-item" style="margin-bottom: 10px;">
            <h4 style="font-size: 1.1rem; font-weight: 600; color: var(--text-main, #2c3e50); margin-bottom: 8px;">{data['faq2_q']}</h4>
            <p style="color: var(--text-light, #7f8c8d); line-height: 1.5;">{data['faq2_a']}</p>
        </div>
    </section>
"""
    return html

def main():
    modified_count = 0
    
    # We want to iterate classes folder -> class-X -> sub-hubs -> index.html
    classes_dir = os.path.join(ROOT_DIR, 'classes')
    
    for class_folder in os.listdir(classes_dir):
        if not class_folder.startswith('class-'):
            continue
            
        cls_num = class_folder.split('-')[1] # '9', '10', '11', '12'
        class_path = os.path.join(classes_dir, class_folder)
        
        for sub_hub in os.listdir(class_path):
            if sub_hub not in SEO_CONTENT_MAP:
                continue
                
            hub_path = os.path.join(class_path, sub_hub)
            index_file = os.path.join(hub_path, 'index.html')
            
            if not os.path.exists(index_file):
                continue
                
            with open(index_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check if we already injected it
            if 'class="seo-pillar-content"' in content:
                print(f"Skipping {sub_hub}/index.html - Already has SEO pillar content.")
                continue
                
            # Inject right before the closing </main> or <!-- SECTION 7 --> 
            # Sub-hubs usually have <main class="chapters-container"> or similar.
            # We want to insert it right before the closing </main> tag.
            
            seo_html = build_seo_html(cls_num, sub_hub)
            
            if '</main>' in content:
                content = content.replace('</main>', seo_html + '\n    </main>')
                
                with open(index_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_count += 1
                print(f"Injected SEO content to {class_folder}/{sub_hub}/index.html")
            else:
                print(f"WARNING: Could not find </main> tag in {class_folder}/{sub_hub}/index.html")

    print(f"\nProcess Complete. Total files updated with deep SEO content: {modified_count}")

if __name__ == "__main__":
    main()
