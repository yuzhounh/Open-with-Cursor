# Add Cursor Editor Right-Click Menu Options for Windows

This guide will explain how to add right-click menu options for the Cursor editor to files, folders, and folder backgrounds by modifying the Windows registry, thereby improving work efficiency.

## Precautions

- Modifying the registry may affect system stability. Be sure to back up the relevant registry entries before proceeding.
- Make sure to replace the paths in the examples with the actual installation path of Cursor.exe on your system.
- If you encounter issues, you can undo the changes by deleting the added registry entries.

## Add Right-Click Menu Option for Files

1. Open the Registry Editor (press Win+R, type "regedit" and press Enter).
2. Navigate to `HKEY_CLASSES_ROOT\*\shell`.
3. Right-click the "shell" folder, select "New" > "Key", and name it "Cursor".
4. In the right pane, set the "(Default)" value to "Open with Cursor".
5. Create a string value named "Icon" and set it to the full path of Cursor.exe:
   `C:\Users\YourUsername\AppData\Local\Programs\Cursor\Cursor.exe`
6. Create a "command" subkey under "Cursor".
7. In "command", set the "(Default)" value to:
   `"C:\Users\YourUsername\AppData\Local\Programs\Cursor\Cursor.exe" "%V"`

## Add Right-Click Menu Option for Folders

1. Navigate to `HKEY_CLASSES_ROOT\Directory\shell`.
2. Follow steps 3-7 as described above to add the right-click menu option for folders.

## Add Right-Click Menu Option for Folder Backgrounds

1. Navigate to `HKEY_CLASSES_ROOT\Directory\Background\shell`.
2. Follow steps 3-7 as described above to add the right-click menu option for folder backgrounds.

## Apply Changes

After completing the above steps, do one of the following to apply the changes:

- Restart File Explorer
- Log out and log back into Windows

Now, you should see the "Open with Cursor" option when right-clicking on files, folders, and empty spaces within folders, which will greatly improve your work efficiency.
