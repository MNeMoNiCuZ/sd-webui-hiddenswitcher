## HiddenSwitcher
This tool quickly hides/unhides your files and folders in A1111 WebUI.

**Note: It only partially hides the models.**

It makes them not show up in the "extra resources" browser (thumbnails), but they still show up in dropdowns.

## How to use
1. Edit the `folders.txt` file with the paths to the folders you wish to toggle visibility on.
2. Run `switcher.bat` to trigger the rename script. This adds or removes a leading `.` from the file names.

This should hide the folder and its content from A1111, as long as you don't have the `Show hidden directories 
(directory is hidden if its name starts with ".".)` option enabled.

3. Run the script again to toggle it back.

### Does it work with symbolic folder linking?
Yes. Make sure you enter the paths to the actual folders, not the symbolic links.

### Can I properly hide the folders instead of adding a . to the names?
Yes. Edit `switcher.bat` and change it to target the `switcher-hide.py` instead of `switcher-rename.py` at the end of the file.
