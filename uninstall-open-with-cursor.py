import winreg
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def remove_cursor_menu(key_path):
    try:
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, f"{key_path}\\Cursor\\command")
        winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, f"{key_path}\\Cursor")
        print(f"Successfully removed Cursor menu from {key_path}")
    except WindowsError as e:
        print(f"Error removing Cursor menu from {key_path}: {e}")

def main():
    if not is_admin():
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return

    # Remove right-click menu for files
    remove_cursor_menu(r"*\shell")

    # Remove right-click menu for folders
    remove_cursor_menu(r"Directory\shell")

    # Remove right-click menu for folder background
    remove_cursor_menu(r"Directory\Background\shell")

    print("Uninstallation completed. Please restart File Explorer or log out and log back in to Windows for changes to take effect.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
