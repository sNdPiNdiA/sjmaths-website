import os
from bs4 import BeautifulSoup

file_path = os.path.join("upsssc-up-gk", "agriculture", "index.html")
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")

theory_div = soup.find("div", id="tab-theory")
if theory_div:
    cards = theory_div.find_all("div", class_="card-premium")
    print(f"Theory div found. Total cards: {len(cards)}")
    for i, c in enumerate(cards):
        title = c.find("div", class_="card-title")
        t_en = title.find("span", class_="lang-en").text.strip() if title and title.find("span", class_="lang-en") else (title.text.strip() if title else "No title")
        print(f"Card {i+1}: {t_en}")
else:
    print("tab-theory NOT found!")

practice_div = soup.find("div", id="tab-practice")
print(f"Practice div found: {practice_div is not None}")
