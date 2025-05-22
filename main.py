import sys
import time
from downloader import download_and_extract
from browser_launcher import find_browser, launch_browser
from overlay import OverlayGuide
from utils import open_extensions_page_with_pyautogui

REPO = "vedantchalke36/pcm-scoremate"

def main():
    print("Downloading and extracting extension...")
    try:
        extension_folder = download_and_extract(REPO)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    print(f"Extension extracted to: {extension_folder}")

    try:
        chrome_path = find_browser()
    except Exception as e:
        print(f"Error: {e}")
        print("Google Chrome was not found. Please install Google Chrome and try again.")
        sys.exit(1)

    print(f"Found Chrome at: {chrome_path}")
    print("Opening Chrome (new window)...")
    launch_browser(chrome_path, "")  # Open Chrome with no URL

    # Automatically detect Chrome window and dial chrome://extensions
    open_extensions_page_with_pyautogui()
    time.sleep(2)  # Wait for the page to load

    print("Follow the on-screen arrows and instructions.")

    # Guide steps: (x, y, text)
    steps = [
        (1650, 250, "1. Enable 'Developer mode' (top right)\nPress Enter here after you do it"),  # text left
        (180, 305, "2. Click 'Load unpacked'\nPress Enter here after you do it"),                 # text right
        (600, 600, f"3. In the dialog, select:\n{extension_folder}\nPress Enter here after installing"),  # text below
    ]

    OverlayGuide(steps)
    print("Done! The extension should now be installed.")

if __name__ == "__main__":
    main()
