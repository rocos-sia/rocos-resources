# 设备档案

每个 `<名称>_<实际序列号>` 目录保存一台设备的配置、标定与维护资料。以下目录保留原有身份：

| 档案 | 关联型号 | 当前数据 |
| --- | --- | --- |
| [talon_001](talon_001/README.md) | Talon 1.0.0 | 无工具启动示例；已有帧记录；未附实测标定 |
| [rcm_sim](rcm_sim/README.md) | RCM 1.0.0 | 仿真实例，无实机标定；`sim` 为仿真标识 |

`talon_001` 的编号沿用源文件，铭牌和维护信息尚未补录。`rcm_sim` 不代表实际序列号；实际设备应按真实编号另建目录。

## 单台设备布局

```text
<名称_序列号>/
  README.md
  device.yaml
  identification/
    README.md
    joint_zero/
    kinematics/
    dynamics/
    payload/
    tool_tcp/
  maintenance/
    README.md
```

各类结果以 `YYYY-MM-DD_NN` 子目录积累，保留原始数据、输出参数、模型及本次说明。`device.yaml` 中的结果引用按它所在目录解析，当前没有结果的字段保持 `null`。

`frames.yaml` 如存在，是该设备已有帧/工具记录，不会成为 App 启动的隐含覆盖。保存到同一档案，避免丢失维护信息；恢复工具安装时按程序实际支持的方式导入/配置。
