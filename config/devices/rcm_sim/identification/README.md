# rcm_sim 标定与辨识资料

当前没有实测结果，以下目录为归档位置，`.gitkeep` 只用于保留空目录。

| 目录 | 保存内容 |
| --- | --- |
| [joint_zero/](joint_zero/) | 零点测量与结果 |
| [kinematics/](kinematics/) | 原始测量、运动学标定参数、标定模型 |
| [dynamics/](dynamics/) | 原始采样、动力学辨识参数、NPZ/JSON 与模型 |
| [payload/](payload/) | 实际安装状态下的负载测量和结果 |
| [tool_tcp/](tool_tcp/) | TCP 测量、对应工具与安装信息 |

每次结果放到 `类别/YYYY-MM-DD_NN/`，附 README 记录日期、设备、型号、工具和安装状态、数据文件及结果用途，旧结果继续保留。在 device.yaml 或设备说明中记录当前采用哪份结果。

动力学阻抗实验可将同次原始 URDF、`rigid_model.json`、`friction_model.json` 放到 dynamics 的本次目录，并填写 [专项模板](../../../identified_impedance.yaml)。模板数组及增益仍需按本次实验设置。

当前 App 的 device.calibration_files 不能直接消费运动学/动力学 NPZ；先作为设备资料保存，供支持相应格式的工具复用。已有零点、负载或 TCP 结果引用仍应保留其实际格式与上下文。
