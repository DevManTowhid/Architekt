# Architekt 🌳

**Architekt** is a lightweight CLI utility that transforms ASCII tree structures into live file systems. 

Designed for developers who want to move from architectural design to coding in seconds. Simply define your structure in a text file—or copy it from a design document—and Architekt will handle the directories and file creation for you.

---

## ✨ Features

*   **Intelligent Parsing**: Accurately interprets standard tree symbols like `├──`, `└──`, and `│`.
*   **Recursive Scaffolding**: Automatically creates parent and child directories with proper nesting.
*   **Comment Support**: Ignores inline comments (e.g., `# Entry point`), allowing you to keep your structure files documented.
*   **Zero Dependencies**: Written in pure Python using the `pathlib` and `re` modules.
*   **Error Resilient**: Built-in handling for OS permissions and missing root directories.

## 🚀 Demo

### 1. Define your structure (`project.txt`)

```text
backend/src/
├── main.py          # FastAPI entry point
├── database.py      # SQLAlchemy setup
├── models.py        # DB Schemas
└── api/
    └── v1/
        └── routes.py
```

### 2. Run the command

```bash
treegen project.txt
```

### 3. Result

```plaintext
📁 Created: backend/src
📄 Created: backend/src/main.py
📄 Created: backend/src/database.py
📄 Created: backend/src/models.py
📁 Created: backend/src/api/v1
📄 Created: backend/src/api/v1/routes.py
```

## 🛠️ Installation

### Windows
1. Save `treegen.py` and `treegen.bat` to a folder (e.g., `C:\Scripts`).
2. Add `C:\Scripts` to your System Environment Variables (PATH).
3. Restart your terminal.

### macOS / Linux
1. Move the script:
```bash
sudo mv treegen.py /usr/local/bin/treegen
```
2. Make it executable:
```bash
sudo chmod +x /usr/local/bin/treegen
```

## 📋 Requirements
*   **Python 3.6+**
*   Works on Windows, macOS, and Linux.

---

## 🤝 Contributing
Feel free to fork this repository and submit pull requests. Future plans include a `--reverse` flag to generate trees from existing directories.

**Author:**  [Md Towhidul Alam](https://github.com/DevManTowhid)

**Project:** Part of the [PulseCommerce](https://github.com/DevManTowhid/pulsecommerce-platform) Platform development tools.
