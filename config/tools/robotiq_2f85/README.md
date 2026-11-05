# Robotiq 2F-85 工具模型

| 项目 | 内容 |
| --- | --- |
| 名称 / 配置版本 | robotiq_2f85 / 1.0.0 |
| 模型 | [gripper.urdf](gripper.urdf)，根连杆 tool_base |
| 配置 | [tool.yaml](tool.yaml) |
| 网格 | [meshes/](meshes/) 下 9 个 STL |
| 安装与 TCP | 初始单位位姿，需按实际设备配置与标定 |
| 来源 | PickNik Robotics，完整记录见 [SOURCE.md](SOURCE.md) |
| 许可 | [BSD-3-Clause](LICENSE) |

网格包括 robotiq_base 和左右 finger、finger_tip、inner_knuckle、knuckle。URDF 保留 mimic 关系；零位为张开，使用碰撞 STL 简化外观。该资源用于模型展示，不包含夹爪驱动和开合控制。

复制时保留 tool.yaml、URDF、全部 mesh 和来源/许可。通过 rocos-cfg 设置实际法兰/转接板安装关系，TCP 测量及使用记录保存到实际设备档案。不要把单位 TCP 当作指尖或夹持中心的实测值。
