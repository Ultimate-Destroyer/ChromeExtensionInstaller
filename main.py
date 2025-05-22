import sys
import time
from downloader import download_and_extract
from browser_launcher import find_browser, launch_browser
from overlay import OverlayGuide

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
    print("Launching Chrome extensions page...")
    extensions_url = "chrome://extensions/"
    launch_browser(chrome_path, extensions_url)
    time.sleep(2)

    # Guide steps: (x, y, text)
    # You may need to adjust these coordinates for your display/browser!
    steps = [
        (300, 100, "1. Enable 'Developer mode' (top right)\nPress Enter here after you do it"),
        (160, 160, "2. Click 'Load unpacked'\nPress Enter here after you do it"),
        (600, 400, f"3. In the dialog, select:\n{extension_folder}\nPress Enter here after installing"),
    ]
    OverlayGuide(steps)
    input("Follow the on-screen arrows and instructions. Press Enter here when done.")
    print("Done! The extension should now be installed.")

if __name__ == "__main__":
    main()
