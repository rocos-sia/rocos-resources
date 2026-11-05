# demo_gripper 示例夹爪

| 项目 | 内容 |
| --- | --- |
| 名称 / 配置版本 | demo_gripper / 1.0.0 |
| 模型 | [gripper.urdf](gripper.urdf)，单根连杆 `gripper_base` |
| 配置 | [tool.yaml](tool.yaml) |
| 网格 | [meshes/finger.stl](meshes/finger.stl)，左右两指复用同一文件 |
| 名义 TCP | 位置 [0, 0, 0.14] m；旋转 [0, 0, 0, 1]（xyzw） |

该包是静态演示几何，不包含夹爪驱动或开合执行器。工具安装到设备的关系由 device.yaml/tool_install 配置，实际 TCP 标定保存到对应设备档案。

复制时保留整个目录，URDF 通过 `package://demo_gripper/meshes/finger.stl` 引用网格。来源为 rocos-app 中同名工具包；没有补写测量数据。
