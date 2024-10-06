# 为Windows添加Cursor编辑器的右键菜单选项

本指南将介绍如何通过修改Windows注册表，为文件、文件夹以及文件夹背景添加Cursor编辑器的右键菜单选项，从而提高工作效率。

## 注意事项

- 修改注册表可能影响系统稳定性，操作前请务必备份相关注册表项。
- 请确保将示例中的路径替换为您系统中Cursor.exe的实际安装路径。
- 如遇问题，可以删除添加的注册表项来撤销更改。

## 为文件添加右键菜单选项

1. 打开注册表编辑器（按Win+R，输入"regedit"并回车）。
2. 导航至 `HKEY_CLASSES_ROOT\*\shell`.
3. 右击"shell"文件夹，选择"新建" > "项"，将其命名为"Cursor".
4. 在右侧窗格中，将"(默认)"值设置为"通过 Cursor 打开".
5. 创建一个名为"Icon"的字符串值，将其设置为Cursor.exe的完整路径：
   `C:\Users\YourUsername\AppData\Local\Programs\Cursor\Cursor.exe`
6. 在"Cursor"下创建"command"子项。
7. 在"command"中，将"(默认)"值设置为：
   `"C:\Users\YourUsername\AppData\Local\Programs\Cursor\Cursor.exe" "%V"`

## 为文件夹添加右键菜单选项

1. 导航至 `HKEY_CLASSES_ROOT\Directory\shell`.
2. 按照上述步骤3-7进行操作，为文件夹添加右键菜单选项。

## 为文件夹背景添加右键菜单选项

1. 导航至 `HKEY_CLASSES_ROOT\Directory\Background\shell`.
2. 按照上述步骤3-7进行操作，为文件夹背景添加右键菜单选项。

## 使更改生效

完成上述步骤后，请执行以下操作之一使更改生效：

- 重启文件资源管理器
- 重新登录Windows

现在，您可以在文件、文件夹，以及文件夹空白处右击时看到"通过 Cursor 打开"的选项，这将大大提高您的工作效率。