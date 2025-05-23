import sys
import time
import pyautogui
import pygetwindow as gw
from downloader import download_and_extract
from browser_launcher import find_browser, launch_browser

REPO = "vedantchalke36/pcm-scoremate"

def wait_for_chrome_window(timeout=15):
    print("Waiting for Chrome window to appear...")
    start = time.time()
    while time.time() - start < timeout:
        windows = [w for w in gw.getAllTitles() if w and 'chrome' in w.lower()]
        if windows:
            return gw.getWindowsWithTitle(windows[0])[0]
        time.sleep(0.3)
    raise RuntimeError("Chrome window did not appear in time.")

def click_button(image, description, timeout=10):
    print(f"Looking for {description} button...")
    start = time.time()
    while time.time() - start < timeout:
        location = pyautogui.locateCenterOnScreen(image, confidence=0.85)
        if location:
            pyautogui.moveTo(location, duration=0.2)
            pyautogui.click()
            print(f"Clicked {description} button.")
            return True
        time.sleep(0.3)
    raise RuntimeError(f"Could not find {description} button on screen. Make sure Chrome is maximized and the screenshot matches.")

def automate_extension_install(extension_folder):
    # Wait for Chrome window and maximize it
    win = wait_for_chrome_window()
    win.activate()
    time.sleep(0.5)
    win.maximize()
    time.sleep(0.7)

    # Go to chrome://extensions
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.2)
    pyautogui.write('chrome://extensions', interval=0.05)
    pyautogui.press('enter')
    time.sleep(1.5)

    # Click "Developer mode" using image recognition
    click_button('images/dev_mode_button.png', "Developer mode")
    time.sleep(0.7)

    # Click "Load unpacked" using image recognition
    click_button('images/load_unpacked_button.png', "Load unpacked")
    time.sleep(1.2)  # Wait for file dialog to open

    # Focus path bar in explorer (Alt+D works in Windows file dialogs)
    pyautogui.hotkey('alt', 'd')
    time.sleep(0.2)
    pyautogui.write(extension_folder, interval=0.02)
    pyautogui.press('enter')
    time.sleep(0.5)  # Wait for the extension to load
    pyautogui.press('enter')
    time.sleep(1.5)  # Wait for Chrome to load the extension

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
    launch_browser(chrome_path, "")
    time.sleep(2)

    print("Automating extension installation...")
    automate_extension_install(extension_folder)

    pyautogui.alert("Done!\nThe extension should now be installed in Chrome.")

if __name__ == "__main__":
    main()
