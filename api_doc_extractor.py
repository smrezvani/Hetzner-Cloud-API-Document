import sys
from pathlib import Path

from bs4 import BeautifulSoup
import markdownify
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

BASE_URL = "https://docs.hetzner.cloud/"
OUTPUT_FILE = "hetzner_cloud_api.md"

def extract_main_content(html: str) -> tuple[str, str]:
    """Extracts the main content and converts to markdown."""
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find("main") or soup.find("article") or soup.body
    if not main:
        raise ValueError("❌ Could not find main content section.")
    
    title_tag = soup.find("h1") or soup.title
    title = title_tag.get_text(strip=True) if title_tag else "Hetzner Cloud Documentation"
    markdown = markdownify.markdownify(str(main), heading_style="ATX")
    return title, markdown

def fetch_homepage_html() -> str:
    """Loads and renders the homepage using Playwright and returns full HTML."""
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(BASE_URL, wait_until="networkidle", timeout=15000)
            html = page.content()
            browser.close()
            return html
    except PlaywrightTimeoutError:
        raise RuntimeError("❌ Timed out while loading the Hetzner docs homepage.")
    except Exception as e:
        raise RuntimeError(f"❌ Unexpected error during page rendering: {e}")

def save_markdown(title: str, content: str, file_path: str):
    """Saves the markdown content to a file."""
    path = Path(file_path)
    path.write_text(f"# {title}\n\n{content}", encoding="utf-8")
    print(f"✅ Markdown saved to: {path.resolve()}")

def main():
    try:
        print("🔍 Fetching Hetzner Cloud homepage...")
        html = fetch_homepage_html()
        print("🔍 Extracting content...")
        title, content = extract_main_content(html)
        save_markdown(title, content, OUTPUT_FILE)
    except Exception as err:
        print(f"💥 Error: {err}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
