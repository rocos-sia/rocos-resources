# Talon MuJoCo 资料

| 文件 | 作用 |
| --- | --- |
| [scene.xml](scene.xml) | 场景入口，包含 `talon.xml`、地面、灯光 |
| [talon.xml](talon.xml) | 七关节模型，7 个位置执行器，网格来自 `../meshes/` |
| [mujoco.yaml](mujoco.yaml) | rocos-mujoco 启动模板，硬件来自 `../hardware.yaml` |

启动模板的共享内存 ID 为 0、周期 1000 μs、`visualize: true`。以下命令从资源仓库根目录执行，程序需另外安装：

```bash
rocos_mujoco_sim --config config/robots/talon/mjcf/mujoco.yaml
```

Talon 的 [robot.yaml](../robot.yaml) 当前选择 ECM。若让 App 连接此仿真器，需要通过 rocos-cfg 配置 `master_type: mujoco` 和对应 App 连接参数，并让 ID/周期一致；仅启动本目录的仿真器不会自动更改 App 入口。

保留原有 MJCF 参数。MJCF 的关节范围和位置伺服增益不等同于 URDF/hardware 的所有限制，新增实测结果应放到设备档案。
