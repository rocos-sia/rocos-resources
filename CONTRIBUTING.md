# 维护资源

## 新增型号

在 `config/robots/<型号>/` 放入型号配置、URDF、mesh、硬件与主站资料，按需增加 `mjcf/`。目录内提供 README，写明型号、模型根/末端、关节与单位、文件作用、来源和适用场景。在 `config/robots/README.md` 与根 README 中增加索引。

保留配置与资源之间的相对路径、mesh 文件名大小写和原始模型参数。型号通用数据放在 `robots/`，单台设备测得的数据放在 `devices/`。

## 新增设备

在 `config/devices/<名称>_<实际序列号>/` 建立 `device.yaml` 与 README。记录实际序列号、关联型号、安装工具和当前采用的标定结果；不要用另一台设备的编号或测量值代替。

使用 `identification/{joint_zero,kinematics,dynamics,payload,tool_tcp}/YYYY-MM-DD_NN/` 保存每次结果和原始数据，README 写明时间、设备安装状态、输入与输出文件及用途。没有结果时保持对应引用为 `null`。维护记录放在 `maintenance/`，旧结果继续保留。

`rcm_sim` 是已有仿真身份；新增实机应使用实际编号另建档案。`frames.yaml` 属于设备记录，不应全局忽略或当作隐含启动覆盖。

## 更新入口与工具

根目录入口 YAML 是模板，使用 `rocos-cfg` 配置实际工程后更新或导出对应文件。模板中不要带入实际 ECM 授权。专项辨识模板中的参数和路径由对应辨识工具的实际输出填写。

工具放入 `config/tools/<名称>/`，保留 `tool.yaml`、URDF、mesh、README 及上游 SOURCE/LICENSE。在设备配置中记录实际安装和 TCP，不用名义值代替实测值。

## 提交资料

提交说明写清涉及的型号/设备、资料变化及用途，可使用 `docs:`、`chore:`、`feat:`、`fix:` 等前缀。标定数据、NPZ、CSV、URDF、STL 等属于资源，应随相应档案保存；工具缓存、日志和临时文件不提交。

提出 PR 时说明来源、目标设备与使用方法。不要在本仓库加入其他项目的构建目录或可执行程序。

修改资源后运行 `python3 scripts/generate_manifest.py` 更新根目录的 `manifest.json`；可用 `--check` 检查是否最新。推送分支后 GitHub Actions 也会自动刷新并提交有变化的索引，详见 [索引维护说明](docs/manifest.md)。
