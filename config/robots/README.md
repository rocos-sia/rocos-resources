# 机械臂型号

| 名称 | 型号入口 | 模型链 | 默认 App 后端 | 模型说明 |
| --- | --- | --- | --- | --- |
| [Talon](talon/README.md) | `talon/robot.yaml` | `base_link → link_7` | ECM | 七个 revolute 关节、8 个 STL、ENI 与 MJCF |
| [RCM](rcm/README.md) | `rcm/robot.yaml` | `base_link → Link_9` | MuJoCo | 8 个活动关节，其中两移动关节、两个 mimic；末端固定传感器 |

型号目录保存通用模型、名义硬件参数和主站资料。单台设备的标定结果保存到 [devices](../devices/README.md)，根目录入口通过 rocos-cfg 选择实际型号与设备。

新增型号沿用一个目录一个型号的布局，并附 README、来源和 mesh 说明。URDF/MJCF、硬件与 ENI 保持相对路径和原始命名；`package_version` 是已有配置字段，不在本次整理中改动。
