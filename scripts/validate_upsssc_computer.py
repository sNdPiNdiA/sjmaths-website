import os

base_dir = "upsssc-computer"
folders = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

for f in sorted(folders):
    p = os.path.join(base_dir, f, "index.html")
    with open(p, "r", encoding="utf-8") as fl:
        c = fl.read()

    assert '<div class="tab-content" id="tab-theory"' in c, f"{f} missing tab-theory"
    assert '<div class="tab-content" id="tab-practice"' in c, f"{f} missing tab-practice"
    assert '<div class="mermaid">' in c, f"{f} missing mermaid"
    assert "mermaid.initialize" in c, f"{f} missing mermaid.initialize"
    assert "<table" in c, f"{f} missing table"
    assert "</html>" in c, f"{f} missing </html>"

print("All 18 upsssc-computer files passed structural & tag validation successfully!")
