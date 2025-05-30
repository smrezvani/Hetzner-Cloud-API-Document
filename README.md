# Hetzner Cloud Docs Extractor

This script fetches and extracts the main content from the [Hetzner Cloud Documentation homepage](https://docs.hetzner.cloud/) and saves it as a clean, readable Markdown file.

---

## 📁 Project Files

- `api_doc_extractor.py` – The main Python script.
- `hetzner_cloud_api.md` – Output Markdown file generated from the homepage.

---

## ⚙️ Requirements

- Python 3.8+
- [Playwright](https://playwright.dev/python)
- `beautifulsoup4`, `markdownify`

---

## 🐍 Set Up and Run

Follow these steps to set up a virtual environment, install dependencies, and run the script.

### 1. Clone or Download the Project

```bash
git clone https://github.com/smrezvani/Hetzner-Cloud-API-Document.git
cd Hetzner-Cloud-API-Document
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

#### macOS / Linux:

```bash
source venv/bin/activate
```

#### Windows (CMD):

```cmd
venv\Scripts\activate
```

#### Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install playwright beautifulsoup4 markdownify
playwright install
```

> This command will also install necessary browser binaries for Playwright.

---

### 5. Run the Script

```bash
python api_doc_extractor.py
```

> ✅ The output will be saved in the file `hetzner_cloud_api.md`.

---

## ❓ Troubleshooting

- **TimeoutError**: Try increasing your internet timeout or checking connectivity.
- **Playwright not found**: Ensure you ran `playwright install` after pip install.

---

## 📄 License

MIT License – use freely with attribution.
