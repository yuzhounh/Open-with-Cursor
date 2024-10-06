import winreg
import os
import sys
import ctypes
import locale

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def add_cursor_menu(key_path, cursor_path):
    try:
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)
        cursor_key = winreg.CreateKey(key, "Cursor")
        
        # Detect system default language
        system_language = locale.getdefaultlocale()[0]
        menu_text = "通过 Cursor 打开" if system_language.startswith("zh_") else "Open with Cursor"
        
        winreg.SetValue(cursor_key, "", winreg.REG_SZ, menu_text)
        winreg.SetValueEx(cursor_key, "Icon", 0, winreg.REG_SZ, cursor_path)
        
        command_key = winreg.CreateKey(cursor_key, "command")
        winreg.SetValue(command_key, "", winreg.REG_SZ, f'"{cursor_path}" "%V"')
        
        print(f"Successfully added Cursor menu to {key_path}")
    except WindowsError as e:
        print(f"Error adding Cursor menu to {key_path}: {e}")

def main():
    # Check if the script is running with admin privileges
    if not is_admin():
        print("This script requires administrator privileges to modify the registry. Attempting to restart with elevated permissions...")
        run_as_admin()
        sys.exit()

    # Get the path to Cursor.exe
    cursor_path = os.path.expandvars(r"%LOCALAPPDATA%\Programs\Cursor\Cursor.exe")
    
    if not os.path.exists(cursor_path):
        print("Cursor.exe not found. Please ensure Cursor editor is properly installed.")
        return

    # Add right-click menu for files
    add_cursor_menu(r"*\shell", cursor_path)

    # Add right-click menu for folders
    add_cursor_menu(r"Directory\shell", cursor_path)

    # Add right-click menu for folder background
    add_cursor_menu(r"Directory\Background\shell", cursor_path)

    print("Operation completed. Please restart File Explorer or log out and log back in to Windows for changes to take effect.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()