import os

def toggle_visibility(folder):
    """Toggle folder visibility by adding or removing a leading period."""
    folder = folder.strip()
    
    # Check if the folder exists as is
    if os.path.exists(folder):
        parent_dir = os.path.dirname(folder)
        folder_name = os.path.basename(folder)
        
        # Folder exists and is "visible", let's "hide" it
        new_name = '.' + folder_name
        new_path = os.path.join(parent_dir, new_name)
        action = "hidden"
    else:
        # Folder doesn't exist, check if it exists with a leading period
        parent_dir = os.path.dirname(folder)
        folder_name = os.path.basename(folder)
        hidden_name = '.' + folder_name
        hidden_path = os.path.join(parent_dir, hidden_name)
        
        if os.path.exists(hidden_path):
            # Folder exists and is "hidden", let's "reveal" it
            new_name = folder_name
            new_path = folder
            folder = hidden_path  # Update folder to the actual path
            action = "revealed"
        else:
            print(f"{folder} - Error: Not found")
            return

    try:
        os.rename(folder, new_path)
        print(f"{folder} - {action}")
    except OSError as e:
        print(f"{folder} - Error: Failed to rename ({e})")

def main():
    with open('folders.txt', 'r') as file:
        folders = file.readlines()
    for folder in folders:
        toggle_visibility(folder.strip())

if __name__ == "__main__":
    main()