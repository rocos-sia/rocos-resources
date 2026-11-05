# Talon 七轴机械臂

| 项目 | 内容 |
| --- | --- |
| 型号名称 | `talon` |
| 配置版本 | `robot.yaml` 中现有 `1.0.0` |
| 模型链 | `base_link → link_7` |
| 驱动 | `joint_1` 至 `joint_7`，ID 0–6，单位 rad |
| App 默认后端 | ECM，主站 ID 0，周期 1000 μs |
| 设备档案 | [talon_001](../../devices/talon_001/README.md) |

## 文件

| 文件或目录 | 作用 |
| --- | --- |
| [robot.yaml](robot.yaml) | 选择 URDF、硬件和 App 主站配置 |
| [hardware.yaml](hardware.yaml) | 驱动 ID、joint_name、PDO 名称、换算、限位与加速度/jerk |
| [ecm.yaml](ecm.yaml) | App 所读的 `master` 配置，ECM 授权留空 |
| [eni7.xml](eni7.xml) | 当前七轴拓扑的原始 ENI |
| [robot.urdf](robot.urdf) | 七轴几何、模型关节限位及惯性参数 |
| [meshes/](meshes/) | `base_link.STL` 与 `link_1.STL` 至 `link_7.STL`，共 8 个模型网格 |
| [mjcf/](mjcf/README.md) | MuJoCo 模型、场景和仿真启动模板 |

## 使用

根目录 [app.yaml](../../app.yaml) 是 Talon App 模板；通过 rocos-cfg 选择实际设备、主站、网卡及相关路径后再使用。独立主站模板见 [ecm.yaml](../../ecm.yaml) 和 [igh.yaml](../../igh.yaml)。型号内的 `ecm.yaml` 与根目录同名文件供不同消费者读取，不能直接互换。

URDF 使用 `package://self_robot_description/meshes/...` 引用本型号 mesh；保持整个目录一起复制。硬件 PDO 名称及 ENI 对应已有总线资料，现场工程应选取与实际设备一致的配置。

MJCF 与 URDF 为两份已有模型表达，部分限位和仿真伺服参数不同，本次按原样保存。实测零点、运动学和动力学参数进入对应设备档案，不写回通用型号目录。

## 来源

整理自 rocos-app 的 `config/robots/talon/`。URDF 保留 SolidWorks URDF Exporter 原始注释；网格、ENI 和型号资料的独立上游许可尚未附录，详见仓库 [来源说明](../../../THIRD_PARTY_NOTICES.md)。
