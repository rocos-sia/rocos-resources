# 工具资源

| 工具 | 描述 | 根连杆 | 名义 TCP |
| --- | --- | --- | --- |
| [demo_gripper](demo_gripper/README.md) | 静态演示夹爪，1 个连杆、1 个 STL | gripper_base | 平移 [0,0,0.14] m，单位旋转 |
| [robotiq_2f85](robotiq_2f85/README.md) | 2F-85 展示模型，mimic 关节、9 个 STL | tool_base | 单位位姿占位，尚未标定 |

每个目录保留 tool.yaml、URDF、mesh、说明和上游许可。名义模型与默认 TCP 可复用，实际设备安装关系及测量结果放到对应 [devices](../devices/README.md) 档案。

位姿位置使用 m、四元数采用 xyzw。通过 rocos-cfg 配置实际工具和安装；当前两个 App 入口默认都不安装工具。软件生成的 `.objects/` 是运行缓存，不作为资料源。
