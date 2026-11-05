# 脚本资料

源 config/scripts 只有目录占位，本次没有新增自动启动或硬件控制脚本。此处用于后续保存已有的、用途清楚的启动和示例脚本。

当前请在 rocos-cfg 中完成实际配置，再让已安装程序读取具体 YAML：

```bash
rocosAppMain --config=/opt/rocos/config/app.yaml
rocos_ecm --config /opt/rocos/config/ecm.yaml
rocos_igh_master --config /opt/rocos/config/igh.yaml
rocos_mujoco_sim --config /opt/rocos/config/robots/rcm/mjcf/mujoco.yaml
```

按实际工程选择硬件主站或仿真器。目录形式的 `--config` 需程序后续支持；本次仅整理资源，不增加启动包装层。

新增脚本时附用途、依赖、参数和示例；使用 config 内部资源时以脚本/配置文件位置定位，避免依赖某位开发者的工作目录。脚本产生的标定结果保存到对应 devices 档案。
