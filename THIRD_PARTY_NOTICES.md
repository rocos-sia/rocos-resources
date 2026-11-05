# 资源来源与许可

首次整理日期：2026-11-05。目录约定来自[飞书方案](https://rocos-sia.feishu.cn/wiki/Wj2IwOm8BiYslfkxImicRpArn6g)修订 0.3。

| 资源 | 来源 | 已有许可信息 |
| --- | --- | --- |
| Talon、RCM、示例夹爪、配置模板 | [rocos-app/config](https://github.com/rocos-sia/rocos-app/tree/2d2d94550117a856c976699f504c825f3caeb312/config) 及本地设备记录 | 源目录没有为这些模型附单独许可；保留模型中的原始来源注释 |
| Robotiq 2F-85 | PickNik Robotics，见 [SOURCE.md](config/tools/robotiq_2f85/SOURCE.md) | 保留 [BSD-3-Clause 全文](config/tools/robotiq_2f85/LICENSE) |
| ECM/IgH 入口模板 | 本次按已有 Talon 主站参数和独立主站入口格式整理 | 模板；由 rocos-cfg 按实际工程更新 |

rocos-app 来源提交：`2d2d94550117a856c976699f504c825f3caeb312`。源 `config/` 没有已跟踪文件修改；已有的本地 `devices/talon_001/frames.yaml` 作为设备历史记录保留。`tools/.objects/` 是软件运行缓存，未迁入。

整理时保留模型、ENI 和 mesh 原始内容；补充资源说明、设备档案目录和软件入口模板。ECM 授权值置空；辨识阻抗模板改为引用设备档案中的待填写路径；修正原 README 与注释中依赖 rocos-app 工作目录的用法。

本文件只记录来源，不代替上游许可。未附明确授权的模型，不因与 BSD 工具同仓保存而获得该工具的许可。
