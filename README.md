# Chrome Extension Installer Automation

This project provides a fully automated, user-friendly tool for installing any unpacked Chrome extension directly from a GitHub repository. It is designed to make the process as seamless as possible for end-users, requiring minimal technical knowledge.

---

## How It Works

### 1. **Repository Configuration**
- The repository to be installed is specified in a `repo.json` file (e.g., `"vedantchalke36/pcm-scoremate"`).
- The script reads this value on startup to know which GitHub repository to fetch.

### 2. **Automatic Download and Extraction**
- The tool downloads the latest release or main branch ZIP of the specified repository from GitHub.
- It then extracts the contents to a temporary folder on the user's system.

### 3. **Chrome Detection and Launch**
- The tool automatically locates the Google Chrome browser on the user's system (Windows, macOS, or Linux).
- It launches Chrome (if not already open) and ensures a new window is available for automation.

### 4. **Opening the Extensions Page**
- The tool uses automation to open the `chrome://extensions/` page in Chrome, even if Chrome is already running.
- This is accomplished by simulating keyboard shortcuts to focus the address bar and enter the URL, ensuring reliability across all platforms.

### 5. **Step-by-Step On-Screen Instructions**
- Instead of complex overlays or arrows, the tool displays clear, centered on-screen instructions for each step of the manual installation process.
- The user is guided to:
  1. Enable "Developer mode" in the top right of the extensions page.
  2. Click the "Load unpacked" button.
  3. Select the extracted extension folder in the dialog that appears.
- Each instruction is shown in a large, easy-to-read overlay. The user can proceed through the steps by pressing Enter or clicking anywhere on the overlay.

### 6. **Completion**
- Once all steps are completed, a final message confirms that the extension should now be installed and ready to use in Chrome.

---

## Why This Approach?

- **No Browser Extensions or Manual Setup Required:**  
  The tool does not require any pre-installed browser extensions or manual configuration. Everything is handled automatically from download to installation instructions.
- **Works With Any Display or DPI Setting:**  
  All on-screen instructions are dynamically centered and sized for any screen resolution.
- **No Arrows or Visual Guesswork:**  
  The focus is on clear, actionable instructions, making the process accessible to everyone.
- **Cross-Platform:**  
  Chrome detection and automation work on Windows, macOS, and Linux.

---

## Usage

A pre-built binary is available in the [Releases](https://github.com/Ultimate-Destroyer/ChromeExtensionInstaller/releases/) section for easy use.  
**No Python installation or setup is required for end-users.**

---
