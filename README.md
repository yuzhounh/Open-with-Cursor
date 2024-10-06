# Open with Cursor - Context Menu Integration

This project adds Cursor editor options to the Windows context menu for files, folders, and folder backgrounds by modifying the Windows registry.

## Features

- Adds "Open with Cursor" option to the context menu for files, folders, and folder backgrounds
- Adds "通过 Cursor 打开" option to the context menu similarly if the system default language is Chinese

## Usage

1. Installation: Run `install-open-with-cursor.exe` with administrator privileges.
2. Uninstallation: Run `uninstall-open-with-cursor.exe` with administrator privileges.

## Source Code

The project consists of two Python scripts:

- `install-open-with-cursor.py`: Installs the context menu options
- `uninstall-open-with-cursor.py`: Removes the context menu options

These Python scripts are packaged into executable files using `PyInstaller`.

## Manual Installation Steps

- For detailed manual installation steps, please refer to [README_en.md](https://github.com/yuzhounh/Open-with-Cursor/blob/main/README_en.md).
- For detailed manual installation steps (in Chinese), please refer to [README_zh-CN.md](https://github.com/yuzhounh/Open-with-Cursor/blob/main/README_zh-CN.md).


## Related Projects
- [Open with Cursor in Context Menu](https://github.com/Puliczek/open-with-cursor-context-menu) - A similar project that uses PowerShell scripts to achieve similar functionality.

- [cursor_ext_open-with-cursor-context-menu](https://github.com/eatcosmos/cursor_ext_open-with-cursor-context-menu) - A fork of the above project that adds a batch file for easy installation with a double-click.


## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](LICENSE) file for details.

## Contact

Jing Wang - wangjing@xynu.edu.cn

Project Link: https://github.com/yuzhounh/Open-with-Cursor

