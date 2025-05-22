import sys
import os
import shutil
import subprocess

def get_chrome_path_windows():
    try:
        import winreg
    except ImportError:
        return None

    reg_paths = [
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe",
        r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"
    ]
    for reg_path in reg_paths:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as key:
                value, _ = winreg.QueryValueEx(key, None)
                if os.path.exists(value):
                    return value
        except Exception:
            continue
    return None

def find_browser():
    chrome = None
    if sys.platform == "win32":
        chrome = get_chrome_path_windows() or shutil.which("chrome") or shutil.which("chrome.exe")
    elif sys.platform == "darwin":
        chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        if not os.path.exists(chrome):
            chrome = None
    else:
        chrome = shutil.which("google-chrome") or shutil.which("chrome") or shutil.which("chromium-browser")
    if not chrome:
        raise RuntimeError("Google Chrome not found on this system.")
    return chrome

def launch_browser(chrome_path, extensions_url):
    try:
        # Try to open a new tab in an existing Chrome session
        subprocess.Popen([chrome_path, "--new-tab", extensions_url])
    except Exception as e:
        print(f"Failed to launch Chrome: {e}")
