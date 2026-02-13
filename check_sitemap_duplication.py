
import xml.etree.ElementTree as ET
import os
from collections import Counter

base_path = r"c:\Users\sande\Documents\GitHub\sjmaths-website"
sitemaps = [
    "sitemap-main.xml",
    "sitemap-class-9.xml",
    "sitemap-class-10.xml",
    "sitemap-class-11.xml",
    "sitemap-class-12.xml"
]

def get_urls_from_sitemap(filename):
    path = os.path.join(base_path, filename)
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        # Namespace handling
        ns = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [url.find('sitemap:loc', ns).text for url in root.findall('sitemap:url', ns)]
        return urls
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return []

all_sitemap_data = {}


with open("duplication_report.txt", "w") as f:
    f.write("--- Checking for Internal Duplicates ---\n")
    for filename in sitemaps:
        urls = get_urls_from_sitemap(filename)
        all_sitemap_data[filename] = set(urls) # Storing as set for intersection, but needed list for Counter
        
        counts = Counter(urls)
        duplicates = [url for url, count in counts.items() if count > 1]
        
        if duplicates:
            f.write(f"FAILED: {filename} has {len(duplicates)} duplicate(s):\n")
            for url in duplicates:
                f.write(f"  - {url}\n")
        else:
            f.write(f"PASSED: {filename} has no internal duplicates. (Total URLs: {len(urls)})\n")

    f.write("\n--- Checking for Cross-File Duplicates ---\n")
    checked_pairs = set()
    for file1 in sitemaps:
        for file2 in sitemaps:
            if file1 == file2:
                continue
            
            pair = tuple(sorted((file1, file2)))
            if pair in checked_pairs:
                continue
            checked_pairs.add(pair)
            
            urls1 = all_sitemap_data[file1]
            urls2 = all_sitemap_data[file2]
            
            intersection = urls1.intersection(urls2)
            
            if intersection:
                f.write(f"FAILED: Overlap found between {file1} and {file2} ({len(intersection)} URLs):\n")
                count = 0
                for url in intersection:
                    f.write(f"  - {url}\n")
                    count += 1
                    if count >= 10:
                        f.write(f"  ... and {len(intersection) - 10} more.\n")
                        break
            else:
                 f.write(f"PASSED: No overlap between {file1} and {file2}\n")

    f.write("\n--- Summary ---\n")
    total_unique_urls = len(set().union(*all_sitemap_data.values()))
    f.write(f"Total unique URLs across checked sitemaps: {total_unique_urls}\n")
print("Report generated in duplication_report.txt")

