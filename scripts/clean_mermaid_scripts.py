import os

base_dir = "upsssc-computer"
folders = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

for f in sorted(folders):
    p = os.path.join(base_dir, f, "index.html")
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as fl:
            content = fl.read()

        # Remove mermaid scripts
        content = content.replace("<script src=\"https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js\"></script>\n", "")
        content = content.replace("<script src=\"https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js\"></script>", "")
        content = content.replace("<script>mermaid.initialize({startOnLoad:true, theme: 'default'});</script>\n", "")
        content = content.replace("<script>mermaid.initialize({startOnLoad:true, theme: 'default'});</script>", "")

        with open(p, "w", encoding="utf-8") as fl:
            fl.write(content)

print("Cleaned mermaid scripts from all files.")
