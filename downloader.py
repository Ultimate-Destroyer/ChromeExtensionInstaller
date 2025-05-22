import requests
import zipfile
import tempfile
import os

def download_and_extract(repo):
    api_url = f"https://api.github.com/repos/{repo}/releases/latest"
    try:
        release_info = requests.get(api_url, timeout=10).json()
        zip_url = release_info['zipball_url']
    except Exception as e:
        raise RuntimeError(f"Failed to fetch release info: {e}")

    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, "extension.zip")
    try:
        zip_response = requests.get(zip_url, timeout=20)
        with open(zip_path, "wb") as f:
            f.write(zip_response.content)
    except Exception as e:
        raise RuntimeError(f"Failed to download ZIP: {e}")

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        extracted_folders = [os.path.join(temp_dir, d) for d in os.listdir(temp_dir) if os.path.isdir(os.path.join(temp_dir, d))]
        extension_folder = extracted_folders[0]
    except Exception as e:
        raise RuntimeError(f"Failed to extract ZIP: {e}")

    return extension_folder
