"""
Audit Class 9 exercise nav buttons (Previous / Next).
Checks that each exercise file's prev/next buttons link to valid files
and that the chain of exercises is logically correct.
"""
import os
import re
from pathlib import Path

ROOT = Path(r"c:\Users\sande\Documents\GitHub\sjmaths-website")
EXERCISES_DIR = ROOT / "classes" / "class-9" / "ncert-exercise-practice"

# Regex to find nav button links
NAV_LINK_RE = re.compile(
    r'<a\s+href="([^"]+)"\s+class="nav-btn\s+(btn-prev|btn-next)"[^>]*>\s*(.*?)\s*</a>',
    re.DOTALL | re.IGNORECASE
)

def get_all_exercises():
    """Collect all exercise HTML files, sorted by chapter then exercise number."""
    exercises = []
    for chapter_dir in sorted(EXERCISES_DIR.iterdir()):
        if not chapter_dir.is_dir():
            continue
        # Extract chapter number
        m = re.match(r'chapter-(\d+)', chapter_dir.name)
        if not m:
            continue
        chap_num = int(m.group(1))
        
        for f in sorted(chapter_dir.iterdir()):
            if f.suffix == '.html' and f.name.startswith('exercise-'):
                # Extract exercise numbers
                em = re.match(r'exercise-(\d+)-(\d+)\.html', f.name)
                if em:
                    ex_chap = int(em.group(1))
                    ex_num = int(em.group(2))
                    exercises.append({
                        'path': f,
                        'chapter_num': chap_num,
                        'chapter_dir': chapter_dir.name,
                        'filename': f.name,
                        'exercise_chap': ex_chap,
                        'exercise_num': ex_num
                    })
    
    # Sort by chapter number, then exercise number
    exercises.sort(key=lambda e: (e['chapter_num'], e['exercise_num']))
    return exercises

def extract_nav_links(filepath):
    """Extract prev and next nav button hrefs from an exercise file."""
    content = filepath.read_text(encoding='utf-8', errors='ignore')
    links = {'btn-prev': None, 'btn-next': None}
    labels = {'btn-prev': None, 'btn-next': None}
    
    for match in NAV_LINK_RE.finditer(content):
        href = match.group(1).strip()
        btn_type = match.group(2).strip()
        label = re.sub(r'<[^>]+>', '', match.group(3)).strip()  # strip HTML tags
        links[btn_type] = href
        labels[btn_type] = label
    
    return links, labels

def resolve_link(source_file, href):
    """Resolve an href relative to the source file or project root."""
    if href.startswith('/'):
        resolved = ROOT / href.lstrip('/')
    else:
        resolved = source_file.parent / href
    return resolved.resolve()

def main():
    exercises = get_all_exercises()
    report_lines = []
    
    report_lines.append(f"Class 9 Exercise Nav Button Audit")
    report_lines.append(f"Found {len(exercises)} exercise files across {len(set(e['chapter_num'] for e in exercises))} chapters")
    report_lines.append("=" * 90)
    
    # Print the expected chain
    report_lines.append("\n--- EXPECTED EXERCISE CHAIN ---")
    for i, ex in enumerate(exercises):
        marker = f"  [{i+1}] {ex['chapter_dir']}/{ex['filename']}"
        report_lines.append(marker)
    report_lines.append("")
    
    # Now check each file's nav buttons
    issues = []
    
    for i, ex in enumerate(exercises):
        links, labels = extract_nav_links(ex['path'])
        file_label = f"{ex['chapter_dir']}/{ex['filename']}"
        
        # Determine expected prev/next
        expected_prev = exercises[i - 1] if i > 0 else None
        expected_next = exercises[i + 1] if i < len(exercises) - 1 else None
        
        # Check PREV button
        if links['btn-prev']:
            resolved = resolve_link(ex['path'], links['btn-prev'])
            if not resolved.exists():
                issues.append({
                    'file': file_label,
                    'type': 'PREV',
                    'issue': 'BROKEN LINK (file not found)',
                    'href': links['btn-prev'],
                    'resolved': str(resolved.relative_to(ROOT)) if str(resolved).startswith(str(ROOT)) else str(resolved),
                    'label': labels['btn-prev'],
                    'expected': f"{expected_prev['chapter_dir']}/{expected_prev['filename']}" if expected_prev else "None (first exercise)"
                })
            elif expected_prev:
                # Check if it points to the correct previous exercise
                expected_path = expected_prev['path'].resolve()
                if resolved != expected_path:
                    issues.append({
                        'file': file_label,
                        'type': 'PREV',
                        'issue': 'WRONG TARGET',
                        'href': links['btn-prev'],
                        'resolved': str(resolved.relative_to(ROOT)) if str(resolved).startswith(str(ROOT)) else str(resolved),
                        'label': labels['btn-prev'],
                        'expected': f"{expected_prev['chapter_dir']}/{expected_prev['filename']}",
                        'points_to': str(resolved.relative_to(ROOT))
                    })
        elif i > 0:
            issues.append({
                'file': file_label,
                'type': 'PREV',
                'issue': 'MISSING - no prev button found but expected one',
                'expected': f"{expected_prev['chapter_dir']}/{expected_prev['filename']}" if expected_prev else "N/A"
            })
        
        # Check NEXT button
        if links['btn-next']:
            resolved = resolve_link(ex['path'], links['btn-next'])
            if not resolved.exists():
                issues.append({
                    'file': file_label,
                    'type': 'NEXT',
                    'issue': 'BROKEN LINK (file not found)',
                    'href': links['btn-next'],
                    'resolved': str(resolved.relative_to(ROOT)) if str(resolved).startswith(str(ROOT)) else str(resolved),
                    'label': labels['btn-next'],
                    'expected': f"{expected_next['chapter_dir']}/{expected_next['filename']}" if expected_next else "None (last exercise)"
                })
            elif expected_next:
                # Check if it points to the correct next exercise
                expected_path = expected_next['path'].resolve()
                if resolved != expected_path:
                    issues.append({
                        'file': file_label,
                        'type': 'NEXT',
                        'issue': 'WRONG TARGET',
                        'href': links['btn-next'],
                        'resolved': str(resolved.relative_to(ROOT)) if str(resolved).startswith(str(ROOT)) else str(resolved),
                        'label': labels['btn-next'],
                        'expected': f"{expected_next['chapter_dir']}/{expected_next['filename']}",
                        'points_to': str(resolved.relative_to(ROOT))
                    })
        elif i < len(exercises) - 1:
            issues.append({
                'file': file_label,
                'type': 'NEXT',
                'issue': 'MISSING - no next button found but expected one',
                'expected': f"{expected_next['chapter_dir']}/{expected_next['filename']}" if expected_next else "N/A"
            })
    
    # Print results
    report_lines.append("--- NAV BUTTON ISSUES ---")
    if not issues:
        report_lines.append("All nav buttons are correct!")
    else:
        report_lines.append(f"Found {len(issues)} issues:\n")
        for issue in issues:
            report_lines.append(f"FILE: {issue['file']}")
            report_lines.append(f"  [{issue['type']}] {issue['issue']}")
            if 'href' in issue:
                report_lines.append(f"  href: {issue['href']}")
            if 'resolved' in issue:
                report_lines.append(f"  resolved: {issue['resolved']}")
            if 'points_to' in issue:
                report_lines.append(f"  actually points to: {issue['points_to']}")
            if 'expected' in issue:
                report_lines.append(f"  expected: {issue['expected']}")
            if 'label' in issue:
                report_lines.append(f"  button text: {issue['label']}")
            report_lines.append("")
    
    report_lines.append("=" * 90)
    report_lines.append(f"Total issues: {len(issues)}")
    
    # Write report
    report_path = ROOT / "nav_buttons_report.txt"
    report_path.write_text('\n'.join(report_lines), encoding='utf-8')
    print(f"Report written to {report_path}")
    print(f"Found {len(issues)} issues")

if __name__ == '__main__':
    main()
