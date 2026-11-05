# rcm_sim 设备档案

| 项目 | 当前记录 |
| --- | --- |
| 配置身份 | `rcm_sim` |
| 关联型号 | [RCM](../../robots/rcm/README.md) |
| 型号配置版本 | 1.0.0，沿用 device.yaml |
| 原目录编号 | sim（仿真标识） |
| 安装工具 | 无，tool_config/tool_install 为 null |
| 已有标定 | 当前未提供实测文件 |

此目录沿用仿真身份，不对应已登记实机序列号。新增实机时另建实际编号目录。

## 文件与使用

[device.yaml](device.yaml) 保存身份、型号和结果引用；[identification](identification/README.md) 保存本设备各次测量；[maintenance](maintenance/README.md) 保存维护记录。

App 模板为 [app_rcm.yaml](../../app_rcm.yaml)。无安装工具，也没有实机标定结果。仿真启动入口见 [RCM MJCF](../../robots/rcm/mjcf/README.md)。

使用前在 rocos-cfg 中选择实际设备，按现场工程更新入口及相关配置。未提供标定时保留空引用，不以其他设备参数或空文件代替。原有资料与后续结果持续归档在本目录。
