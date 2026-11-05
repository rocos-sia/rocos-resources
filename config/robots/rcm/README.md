# RCM 机械臂

| 项目 | 内容 |
| --- | --- |
| 型号名称 | `rcm`，配置版本沿用 `1.0.0` |
| URDF 名称 | `RCM机械臂-URDF.SLDASM` |
| 模型链 | `base_link → Link_9` |
| 活动关节 | 8 个；`joint_1`、`joint_3` 为移动关节，单位 m；其余为 rad |
| mimic | `joint_6 = joint_5`，`joint_7 = -joint_5` |
| 硬件槽位 | 8 个驱动（ID 0–7）和 1 个力传感器（ID 8） |
| 默认后端 | MuJoCo，共享内存 ID 0，周期 1000 μs |
| 设备档案 | [rcm_sim](../../devices/rcm_sim/README.md)，仿真实例 |

## 文件

| 文件或目录 | 作用 |
| --- | --- |
| [robot.yaml](robot.yaml) | 型号、模型链、硬件与 App 连接参数选择 |
| [hardware.yaml](hardware.yaml) | 驱动/传感器、关节绑定、换算、PDO 与限制 |
| [master.yaml](master.yaml) | App 连接已运行仿真器的参数；不启动仿真器 |
| [RCM.urdf](RCM.urdf) | 几何、惯性、关节与 mimic 描述 |
| [meshes/](meshes/) | `base_link.STL` 和 `Link_1.STL` 至 `Link_8.STL`，共 9 个 |
| [mjcf/](mjcf/README.md) | RCM 仿真场景、模型、碰撞近似和仿真器入口 |

## 使用与已知模型特征

通过 rocos-cfg 配置 [app_rcm.yaml](../../app_rcm.yaml)，先启动 `mjcf/mujoco.yaml` 对应的仿真器，再运行 App。型号的 `master.yaml` 只描述连接，不与仿真器启动 YAML 互换。

当前 URDF 保留原始模型参数：部分连杆声明约 612.27 kg；Link_9 的 `arm7.STL` 外观引用处于 XML 注释中，因此该连杆没有活动的 URDF mesh 引用。MJCF 用圆柱表示该传感器，并使用 Link_4 凸分解碰撞近似，细节见仿真说明。没有补造缺失的传感器网格，也没有在整理时修正惯性或限位。

## 来源

整理自 rocos-app 的 `config/robots/rcm/`，保留 SolidWorks 导出的模型名称、原关节顺序及 mesh 文件大小写。实机序列号与本设备标定数据应另建真实设备档案。
