import os

base_dir = "upsssc-computer"
folders = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

mermaid_snippet = """<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>mermaid.initialize({startOnLoad:true, theme: 'default'});</script>
"""

updated_count = 0
for f in sorted(folders):
    p = os.path.join(base_dir, f, "index.html")
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as fl:
            content = fl.read()

        if "mermaid.initialize" not in content:
            target = "<!-- JavaScript Script References -->"
            if target in content:
                content = content.replace(target, mermaid_snippet + target)
                with open(p, "w", encoding="utf-8") as fl:
                    fl.write(content)
                print(f"Injected mermaid script in: {f}")
                updated_count += 1
            else:
                print(f"Target anchor not found in: {f}")
        else:
            print(f"Already has mermaid: {f}")

print(f"Total files updated with Mermaid script: {updated_count}")
