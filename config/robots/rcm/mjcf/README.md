# RCM MuJoCo 资料

| 文件 | 作用 |
| --- | --- |
| [scene.xml](scene.xml) | 完整场景入口，地面、灯光和机器人 |
| [rcm.xml](rcm.xml) | 8 个活动关节、8 个执行器、2 个 mimic 约束及原始惯性 |
| [collision_meshes.xml](collision_meshes.xml) | Link_4 的 40 个凸碰撞块 |
| [mujoco.yaml](mujoco.yaml) | rocos-mujoco 启动模板，硬件来自 `../hardware.yaml` |

## 使用

以下命令从资源仓库根目录执行，程序需另外安装：

```bash
rocos_mujoco_sim --config config/robots/rcm/mjcf/mujoco.yaml
```

再使用 rocos-cfg 输出并部署的 `app_rcm.yaml` 连接 App。两端共用 `../hardware.yaml`，模板 ID=0、周期=1000 μs。App 的 `../master.yaml` 是连接参数，不是仿真器启动文件。

## 关节与控制

两个移动关节 `joint_1`、`joint_3` 的初始位置为 0.03 m；其余为旋转关节。`joint_6`、`joint_7` 用 joint equality 跟随 `joint_5`。执行器槽位 0–7 对应 `joint_1` 至 `joint_8`；第 5、6 槽为零增益占位，独立运动坐标为 6 个。

位置伺服采用原有仿真增益，不自动实现 hardware 中的速度、加速度和 jerk 限制。修改模型后需重启仿真器。

## 几何与参数说明

- 网格来自 `../meshes/`。URDF 中 Link_9 的外观引用已注释；MJCF 用灰色圆柱近似传感器外形。
- 原模型的部分连杆质量约 612.27 kg，总质量约 4922.51 kg；本次保留源数值。
- Link_4 的 40 个凸块由 CoACD 1.0.14 生成，原 STL 用于显示。碰撞块在 group=3 中且透明，透明度不影响接触。
- 原生成参数：threshold=0.01、preprocess_resolution=60、resolution=1000、mcts_nodes=10、mcts_iterations=40、mcts_max_depth=3、max_convex_hull=40、decimate=true、max_ch_vertex=64、seed=0。原记录的最终 concavity 约 0.0562；碰撞边界是近似。
- 地面 z=-0.103 m；惯量由 body 显式提供，避免由网格密度重复估算。

本文件整理原资源的结构与参数；原 rocos-app 文档中记录的仿真结果属于来源历史，不表示本次执行了仿真或实机运行。
