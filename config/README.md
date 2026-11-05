# 配置模板与资源

本目录整体对应部署位置 `<指定路径>/config`，例如 `/opt/rocos/config`。根目录 YAML 为模板，实际设备与参数通过 `rocos-cfg` 配置后更新或导出到目标目录。

## 入口模板

| 文件 | 用途 | 初始选择 |
| --- | --- | --- |
| [app.yaml](app.yaml) | Talon 的 App 组合配置 | `robots/talon/robot.yaml`、`devices/talon_001/device.yaml` |
| [app_rcm.yaml](app_rcm.yaml) | RCM 仿真 App 配置 | `robots/rcm/robot.yaml`、`devices/rcm_sim/device.yaml` |
| [ecm.yaml](ecm.yaml) | 独立 rocos-ecm 启动模板 | 根级参数；Talon ENI；授权留空 |
| [igh.yaml](igh.yaml) | 独立 rocos-igh 启动模板 | ENI 模式；Talon ENI；IgH 专有启动参数 |
| [user.yaml](user.yaml) | App 唯一用户差量模板 | 空映射，继承基础文件 |
| [identified_impedance.yaml](identified_impedance.yaml) | 辨识模型阻抗控制专项模板 | 七轴数组示例，结果路径含待填写的 `<run>` |

型号、设备、工具与脚本分别见 [robots](robots/README.md)、[devices](devices/README.md)、[tools](tools/README.md)、[scripts](scripts/README.md)。

## 使用流程

1. 将 `config/` 放到目标目录。
2. 用 `rocos-cfg` 选择实际型号、设备、工具和主站，设置网卡、周期、路径等工程参数。
3. 将导出的入口及相关配置更新到对应位置，保留其他设备的标定和维护档案。
4. 各程序通过 `--config` 读取对应 YAML。当前不支持直接把目录传给各程序。

`ecm.yaml` 是独立主站的根级配置；`robots/talon/ecm.yaml` 是 App 所读的 `master` 结构，两者用途不同，实际工程参数由 rocos-cfg 一起配置。`igh.yaml` 仅为独立 IgH 的 ENI 模板，不会自动让当前 Talon App 入口切换到 IgH。

`identified_impedance.yaml` 没有实测辨识结果。使用前将原始 URDF、`rigid_model.json`、`friction_model.json` 保存到对应设备本次辨识目录，再填写模板中的路径及实验增益。它由专项程序读取，不作为 `device.yaml` 的动力学辨识结果直接加载。

## 路径和运行资料

`--config` 的路径相对启动工作目录；配置内的相对路径以声明它的 YAML 所在目录为起点。型号包的 mesh、MJCF include 与硬件路径保留原目录关系。使用支持现有 package URI 的 ROCOS 模型消费者时，工具和机器人资源保持原包内布局。

- `scripts: scripts` 对应本目录的脚本资料位置，目前只有说明，尚无启动包装脚本。
- `web_root: ../web` 是 App 网页位置的模板值。资源库没有 `web/`，必须在 rocos-cfg 中改为实际部署的网页目录。
- 日志是运行输出，不作为资源归档。按实际环境设置 `logging.directory`。
- `tool_library: tools` 引用工具目录；App 可能在 `tools/.objects/` 生成缓存，该目录不提交。

## App 差量

`user.yaml` 保留现有 `software`、`robot`、`tool`、`device` 四个命名空间。对象合并、数组整体替换；引用路径相对 `user.yaml`。例如由配置器输出的现场网卡/CPU 参数可以放入 `robot.master`。设备身份与型号信息在对应的 `device.yaml`、`robot.yaml` 维护。

目录中的空标定引用表示尚未提供结果。已有标定文件按设备保存，README 记录用途；保存运动学/动力学文件与程序自动应用它们是两件事。
