# Open with Cursor

> Add Cursor to the Windows context menu using the Python or EXE installer.

<p>
  <a href="https://github.com/yuzhounh/Open-with-Cursor/releases/latest"><img src="https://img.shields.io/github/v/release/yuzhounh/Open-with-Cursor?style=flat&amp;color=0969da&amp;label=Release" alt="Latest stable release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-f59e0b?style=flat" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/Platform-Windows-0078d4?style=flat" alt="Platform: Windows">
  <img src="https://img.shields.io/badge/Python-3-3776ab?style=flat&amp;logo=python&amp;logoColor=white" alt="Python: 3">
</p>

<p>
  <a href="https://github.com/yuzhounh/Open-with-Cursor/releases/latest">Latest release</a> · <a href="#usage">Get started</a> · <a href="LICENSE">License</a> · <a href="README_zh-CN.md">中文说明</a>
</p>

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

