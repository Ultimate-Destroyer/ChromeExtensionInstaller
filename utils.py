import time
import pyautogui
import pygetwindow as gw
import sys

def wait_for_chrome_window(timeout=15):
    """Wait for a new Chrome window to appear and return its title."""
    print("Waiting for Chrome window to appear...")
    start = time.time()
    while time.time() - start < timeout:
        windows = [w for w in gw.getAllTitles() if w and 'chrome' in w.lower()]
        if windows:
            return windows[0]
        time.sleep(0.3)
    raise RuntimeError("Chrome window did not appear in time.")

def focus_chrome_window(window_title):
    """Focus the Chrome window with the given title."""
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        windows[0].activate()
        time.sleep(0.5)

def open_extensions_page_with_pyautogui():
    # Wait for Chrome window
    try:
        window_title = wait_for_chrome_window()
        focus_chrome_window(window_title)
    except Exception as e:
        print(f"Could not focus Chrome window: {e}")
        return
    # Focus address bar and type URL
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.2)
    pyautogui.write('chrome://extensions', interval=0.05)
    pyautogui.press('enter')
