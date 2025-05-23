import sys
import time
import pyautogui
from downloader import download_and_extract
from browser_launcher import find_browser, launch_browser
from overlay import OverlayMessage  # Save the class above as overlay_message.py

import json

REPO: str = json.load(open('repo.json'))['repo']

def open_extensions_page():
    # Focus address bar, type URL, and press Enter
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.2)
    pyautogui.write('chrome://extensions/', interval=0.03)
    pyautogui.press('enter')
    time.sleep(0.5)

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
    print("Opening Chrome...")
    launch_browser(chrome_path, "")
    time.sleep(2)

    open_extensions_page()

    messages = [
        "1. Enable 'Developer mode' (top right)\n\n",
        "2. Click 'Load unpacked'\n\n",
        "3. Check your terminal for the folder path printed in green,\nselect that and paste in path bar of Load unpacked dialog.\n\n",
        "Done! The extension should now be installed in Chrome."
    ]
    OverlayMessage(messages)

    print(f'\n\nCopy This: \033[32m{extension_folder}\033[0m')

if __name__ == "__main__":
    main()
