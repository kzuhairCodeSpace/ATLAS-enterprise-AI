
from pathlib import Path

#project folders
folders = [
    "app",
    "app/templates",
    "app/static/js",
    "worker",
    "infra",
    "scripts",
    "docs",
]

#project files
files = [
      #root files
      "requirements.txt",
      ".env",
      ".env.example",
      ".gitignore",
      "README.md",

#backend
    "app/__init__.py",
    "app/main.py",
    "app/config.py",
    "app/db.py",
    "app/aws.py",
    "app/vector.py",
    "app/rag.py",
    "app/memory.py",
    "app/guardrails.py",
    "app/graph.py",
    "app/observability.py",

    #frontend
    "app/templates/index.html",
    "app/static/css/style.css",
    "app/static/js/app.js",

    #document ingestion
    "worker/__init__.py",
    "worker/ingest.py",

    #database
    "infra/schema.sql",
    "scripts/init_db.py",

    #documentation
    "docs/SETUP.md",
    "docs/RIUS_OBSERVABILITY.md",
]
def create_structure():
    for folder in folders:
        Path(folder).mkdir(parents=True,exist_ok=True)

    for file in files:
        path = Path(file)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)

    print("project folders and files created successfully!")
    print(f"Total folders: {len(folders)}")
    print(f"Total files: {len(files)}")

if __name__ == "__main__":
    create_structure()





