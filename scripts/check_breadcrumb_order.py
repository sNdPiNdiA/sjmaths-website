
import os

ROOT_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website"
EXCLUDE_DIRS = {
    "node_modules",
    "_legacy_site",
    "_nextjs_migration_backup",
    ".git",
    ".firebase",
    "dataconnect"
}

def check_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return

    header_idx = content.find('id="header-container"')
    bc_idx = content.find('class="breadcrumbs"')

    if bc_idx != -1:
        if header_idx == -1:
             print(f"MISSING_HEADER: {file_path}")
        elif bc_idx < header_idx:
            print(f"WRONG_ORDER: {file_path}")

def main():
    print("Checking for breadcrumbs issues...")
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            if file.endswith(".html"):
                check_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
