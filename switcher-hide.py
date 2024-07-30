import os
import subprocess
import ctypes

def is_hidden(folder):
    """Check if a folder is hidden."""
    try:
        attrs = ctypes.windll.kernel32.GetFileAttributesW(folder)
        return bool(attrs & 2)  # 2 is FILE_ATTRIBUTE_HIDDEN
    except Exception:
        return False

def toggle_hidden(folder):
    """Toggle hidden attribute for a folder and its contents."""
    folder = folder.strip()
    
    if not os.path.exists(folder) or not os.path.isdir(folder):
        print(f"{folder} - Error: Not found or not a directory")
        return

    was_hidden = is_hidden(folder)
    
    try:
        if was_hidden:
            subprocess.run(['attrib', '-H', '/S', '/D', folder], shell=True, check=True)
        else:
            subprocess.run(['attrib', '+H', '/S', '/D', folder], shell=True, check=True)
        
        now_hidden = is_hidden(folder)
        
        if now_hidden != was_hidden:
            status = "hidden" if now_hidden else "revealed"
            print(f"{folder} - {status}")
        else:
            print(f"{folder} - Error: Failed to toggle visibility")
    except subprocess.CalledProcessError:
        print(f"{folder} - Error: Failed to change attributes")

def main():
    with open('folders.txt', 'r') as file:
        folders = file.readlines()
    for folder in folders:
        toggle_hidden(folder.strip())

if __name__ == "__main__":
    main()