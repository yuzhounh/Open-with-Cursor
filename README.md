# Open with Cursor - Context Menu Integration

[![License: MIT](https://img.shields.io/badge/License-MIT-D4A017.svg)](LICENSE)

This project adds Cursor editor options to the Windows context menu for files, folders, and folder backgrounds by modifying the Windows registry.

## Features

- Adds "Open with Cursor" option to the context menu for files, folders, and folder backgrounds
- Adds "通过 Cursor 打开" option to the context menu similarly if the system default language is Chinese

## Usage

Requires Windows and Cursor installed at `%LOCALAPPDATA%\Programs\Cursor\Cursor.exe`. The installer writes to `HKEY_CLASSES_ROOT` and requests administrator privileges.

1. Download or clone this repository.
2. Installation: Run `install-open-with-cursor.exe` with administrator privileges.
3. Restart File Explorer or sign out and back in to see the menu entries.
4. Uninstallation: Run `uninstall-open-with-cursor.exe` with administrator privileges.

## Source Code

The project consists of two Python scripts:

- `install-open-with-cursor.py`: Installs the context menu options
- `uninstall-open-with-cursor.py`: Removes the context menu options

These Python scripts are packaged into executable files using `PyInstaller`.

## Manual Installation Steps

- For detailed manual installation steps, please refer to [README_en.md](README_en.md).
- For detailed manual installation steps (in Chinese), please refer to [README_zh-CN.md](README_zh-CN.md).


## Related Projects

- [Open-with-Cursor-by-reg](https://github.com/yuzhounh/Open-with-Cursor-by-reg) - An alternative using editable `.reg` files and `HKEY_CURRENT_USER` for per-user Cursor integration.

- [Open-with-Antigravity](https://github.com/yuzhounh/Open-with-Antigravity) - A separate Windows context-menu tool for the Antigravity editor, with registry, script, and executable installation options.

- [Open with Cursor in Context Menu](https://github.com/Puliczek/open-with-cursor-context-menu) - A similar project that uses PowerShell scripts to achieve similar functionality.

- [cursor_ext_open-with-cursor-context-menu](https://github.com/eatcosmos/cursor_ext_open-with-cursor-context-menu) - A fork of the above project that adds a batch file for easy installation with a double-click.

- [Cursor Context Menu Installer](https://github.com/hexcreator/open-with-cursor) - A similar project that uses C++ scripts to achieve similar functionality.


## License

This project is licensed under the [MIT License](LICENSE).

## Contact

Jing Wang - wangjing@xynu.edu.cn

Project Link: https://github.com/yuzhounh/Open-with-Cursor

