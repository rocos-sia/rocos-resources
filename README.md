# ROCOS Resources

集中保存 ROCOS 的机械臂模型、设备档案、工具资源和启动配置模板，供 `rocos-app`、`rocos-ecm`、`rocos-igh`、`rocos-mujoco` 与 `rocos-cfg` 共用。

本仓库按[机器人模型及数据统一管理方案](https://rocos-sia.feishu.cn/wiki/Wj2IwOm8BiYslfkxImicRpArn6g)组织。初版采用普通文件目录，使用 Git 记录资料变化。

## 资源索引

| 资源 | 用途 | 说明 |
| --- | --- | --- |
| [Talon](config/robots/talon/README.md) | 七轴机械臂，ECM 与 MuJoCo 资料 | URDF、硬件参数、ENI、8 个 STL、MJCF |
| [RCM](config/robots/rcm/README.md) | RCM 机械臂，MuJoCo 连接示例 | URDF、8 个驱动槽位、力传感器、9 个 STL、MJCF |
| [talon_001](config/devices/talon_001/README.md) | Talon 设备档案 | 无工具启动配置、已有帧记录、标定归档目录 |
| [rcm_sim](config/devices/rcm_sim/README.md) | RCM 仿真实例档案 | 保留原仿真身份，不代表已登记实机序列号 |
| [demo_gripper](config/tools/demo_gripper/README.md) | 静态示例夹爪 | 模型与名义 TCP |
| [robotiq_2f85](config/tools/robotiq_2f85/README.md) | Robotiq 2F-85 展示模型 | URDF、9 个 STL、原始来源与 BSD-3-Clause 许可 |
| [启动模板](config/README.md) | 软件配置起点 | App、RCM App、ECM、IgH、用户差量和辨识阻抗模板 |

机器可读索引见根目录 [manifest.json](manifest.json)，包含资源包、入口文件和逐文件类型、路径、大小及 SHA-256。索引格式、本地生成方法及 GitHub Actions 配置见 [索引维护说明](docs/manifest.md)。

## 目录

```text
rocos-resources/
  README.md
  CONTRIBUTING.md
  THIRD_PARTY_NOTICES.md
  config/
    README.md
    app.yaml                  # Talon App 模板
    app_rcm.yaml              # RCM 仿真 App 模板
    ecm.yaml                  # 独立 ECM 模板
    igh.yaml                  # 独立 IgH 模板
    user.yaml                 # 用户差量模板
    identified_impedance.yaml # 专项辨识阻抗模板
    robots/<型号>/
    devices/<名称_序列号>/
    tools/<工具名称>/
    scripts/
```

## 获取与使用

从 GitHub 的 **Code → Download ZIP** 下载，或克隆本仓库。解压后保留 `config/` 内部结构。需要单独复制型号或设备时，同时带上它引用的模型、工具和入口模板。

1. 在 `rocos-cfg` 中基于入口模板建立或打开实际工程，选择型号、设备、工具和主站。
2. 更新现场参数，将导出的入口及相关配置放入 `<指定路径>/config`，例如 `/opt/rocos/config`。保留其他设备档案和已有标定历史。
3. 让各程序使用这一份目录中的各自启动文件。**当前程序的 `--config` 接收具体 YAML 文件**；传入整个目录是后续程序适配目标。

例如，配置完成后可使用以下入口（程序需要另外安装）：

```bash
rocosAppMain --config=/opt/rocos/config/app.yaml
# 按工程选用其中一种 EtherCAT 主站：
rocos_ecm --config /opt/rocos/config/ecm.yaml
rocos_igh_master --config /opt/rocos/config/igh.yaml
```

`../web` 等软件资源位置需要按实际安装位置在 `rocos-cfg` 中更新；本仓库不包含 App 的网页程序、主站可执行文件或厂商 SDK。`identified_impedance.yaml` 是专项工具模板，其实际辨识文件需由对应采集/辨识工具产生。

配置路径说明见 [config/README.md](config/README.md)，仿真入口见各型号的 `mjcf/README.md`，新增资料的方法见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 设备档案

实机目录按 `<名称>_<实际序列号>` 建立，保留序列号前导零。每台设备的运动学、动力学、零点、负载、TCP 和维护记录均保存在自己的目录中。每次标定按 `YYYY-MM-DD_NN` 建立子目录，保留原始测量、输出参数及说明。

当前设备目录沿用源配置的 `talon_001` 和 `rcm_sim`。尚未补录的铭牌信息在各设备 README 中标明；不把仿真实例改造成虚构的实机编号。当前没有实测辨识结果，预留目录中只有说明和占位文件。

## 来源与许可

首次整理自 `rocos-sia/rocos-app` 的 `config/` 工作区，包含设备目录中已有的 `frames.yaml` 记录；来源提交与整理说明见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。工具运行缓存不作为源资料复制。

不同模型的来源和许可分别记录；已附带的第三方许可随资源保留。本仓库没有为来源尚未说明授权的模型另行指定统一开源许可证。
