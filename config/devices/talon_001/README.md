# talon_001 设备档案

| 项目 | 当前记录 |
| --- | --- |
| 配置身份 | `talon_001` |
| 关联型号 | [Talon](../../robots/talon/README.md) |
| 型号配置版本 | 1.0.0，沿用 device.yaml |
| 原目录编号 | 001 |
| 安装工具 | 无，tool_config/tool_install 为 null |
| 已有标定 | 当前未提供实测文件 |

现有设备编号沿用源文件；未补录铭牌序列号、安装位置及维护负责人。

## 文件与使用

[device.yaml](device.yaml) 保存身份、型号和结果引用；[identification](identification/README.md) 保存本设备各次测量；[maintenance](maintenance/README.md) 保存维护记录。

App 模板为 [app.yaml](../../app.yaml)。初始无安装工具，所有 calibration_files 为 null。

[frames.yaml](frames.yaml) 保留源目录中的工具/对象历史记录，其中 active_tool 为 demo_gripper；它与无工具启动模板用途不同，不会自动随 device.yaml 加载。源运行缓存未迁入，恢复历史工具配置时先按实际程序重新导入所需工具。

使用前在 rocos-cfg 中选择实际设备，按现场工程更新入口及相关配置。未提供标定时保留空引用，不以其他设备参数或空文件代替。原有资料与后续结果持续归档在本目录。
