ABC Importer Tool for Houdini

一个用于导入Alembic (.abc)文件的Houdini工具，支持自定义显示选项。

安装说明：

1. 根据你的操作系统，双击运行对应的安装文件：
   - Windows系统：install_windows.bat
   - Linux系统：install_linux.bat
   - macOS系统：install_mac.bat

2. 在提示时输入你的Houdini版本号（例如：19.5）

3. 等待安装完成

4. 重启Houdini

卸载说明：

1. 双击运行 uninstall_windows.bat
2. 输入你的Houdini版本号
3. 等待卸载完成
4. 重启Houdini

安装文件会自动：
- 创建必要的文件夹
- 复制所需文件到正确位置
- 显示具体的安装路径

默认安装路径：
- Windows：C:/Users/[用户名]/Documents/houdini[版本号]/
- Linux：~/houdini[版本号]/
- macOS：~/Library/Preferences/houdini/[版本号]/

使用方法：

1. 工具会出现在Houdini工具架的"ABC Tools"标签页中
2. 点击ABC Importer图标启动工具
3. 选择源文件夹（ANI/PUB 或 MM/PUB）
4. 选择是否显示导入的几何体
5. 选择一个或多个要导入的文件

功能特点：

- 在ANI/PUB和MM/PUB文件夹之间轻松切换
- 支持多文件选择
- 可选择导入时不显示
- 自动设置和放置节点

常见问题：

Q: 安装后在工具架中看不到工具？
A: 确认以下几点：
   - Houdini版本号输入是否正确
   - 安装路径是否正确
   - 是否已经重启Houdini

Q: 需要修改安装路径？
A: 可以手动复制文件到目标位置：
   - 将abc_importer.py复制到python文件夹
   - 将abcimporter_tools.shelf复制到toolbar文件夹

Q: 支持哪些Houdini版本？
A: 理论上支持所有版本，只需在安装时输入对应的版本号即可。

Q: 如何完全删除工具？
A: 运行uninstall_windows.bat，输入版本号即可完全删除工具。
