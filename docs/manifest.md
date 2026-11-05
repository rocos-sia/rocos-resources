# 资源索引

根目录 `manifest.json` 由 `scripts/generate_manifest.py` 自动生成，遵循[机器人模型及数据统一管理方案](机器人模型及数据统一管理方案.pdf)中的目录分类。不要手工修改生成结果。

## 内容与格式

`schema_version` 为索引格式版本，目前为 `1`；`specification` 是飞书规范链接。所有路径相对仓库根目录，保留大小写并使用 `/`。索引不依赖特定 GitHub 地址，下载整个仓库后仍可按路径读取资源。

| 字段 | 内容 |
| --- | --- |
| `summary` | 资源包数量、文件数量、总字节数，按资源类型与文件类型统计的数量 |
| `resources` | 型号、设备、工具、根级 YAML 模板、脚本集合；包含 `id`、`type`、`name`、`path`、`entrypoint`、`readme`、`file_count` |
| `files` | 逐文件的 `path`、`type`、`format`、`size_bytes`、`sha256` 和所属 `resource` |

资源类型分别为 `robot`、`device`、`tool`、`config_template`、`script_collection`。目录路径或模板文件路径作为稳定的资源 `id`；`files[].resource` 引用它。设备编号直接保留目录原名，包括前导零和已有的 `rcm_sim` 仿真标识。缺少入口或 README 时对应字段为 `null`，脚本集合没有统一入口。

文件类型区分 URDF、mesh、MJCF、ENI、型号/设备/工具配置、主站配置、硬件配置、仿真配置、帧记录、标定数据、维护记录、脚本、文档、许可与来源说明等；未知格式仍保留为 `data`。`format` 是小写扩展名，无扩展名的文本文件为 `text`。文件类型反映目录及文件用途，不表示文件已经通过控制器加载验证。

索引范围为 `config/`、`docs/` 和根目录 Markdown/许可文件；仓库级文档和分类目录的 README 没有所属资源，`resource` 为 `null`。生成器、测试、工作流和索引本身不纳入资源。Git 忽略的未跟踪文件、已删除文件和 `.gitkeep` 不列入。符号链接不受支持，生成器会报错，避免将目录外的数据纳入索引。

设备的 `identification/` 内非说明文件标为 `calibration_data`，保留完整历史路径；说明文件仍属于文档。只有 README 和 `.gitkeep` 的目录不代表已有标定结果。`script_collection` 也可能只有 README，可通过其文件列表判断是否存在实际脚本。

## 本地更新

需要 Git 和 Python 3.10 或更新版本，不需要额外 Python 依赖。在仓库根目录运行：

```bash
python3 scripts/generate_manifest.py
python3 scripts/generate_manifest.py --check
python3 -m unittest discover -s tests -v
```

本地扫描包括 Git 已跟踪文件，以及尚未提交且未被忽略的新文件，因此首次提交前也能生成索引。新增、删除或改动资源后重新生成，和资源一起提交。输出按路径排序，不写入每次变化的生成时间或提交 SHA；内容不变时重复生成的结果完全一致。

## GitHub 自动更新

[工作流](../.github/workflows/update-manifest.yml)在所有分支的 `push` 后执行，也支持在 Actions 页面手动运行。仅在本地执行 `git commit` 不会触发 GitHub Actions，需要推送到 GitHub。

工作流测试生成器，从该分支最新提交生成索引；有变化时，以 `github-actions[bot]` 提交并推回同一分支，仅提交 `manifest.json`。没有变化时不创建提交。同一分支的运行串行处理；若生成期间出现新推送，会重新读取最新分支并生成，最多尝试三次，不强制推送。

工作流声明 `contents: write`，使用仓库内置的 `GITHUB_TOKEN`，无需配置个人令牌。该令牌产生的推送[不会递归触发新的 push 工作流](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)。仓库或组织策略需要允许 Actions 写入；如果分支规则禁止机器人直接提交，自动回写会失败，需要由管理员允许这一维护方式，或在本地生成后随正常 PR 一起提交。不会绕过保护规则。

工作流文件推送到 GitHub 后才会生效；标签推送不更新索引。
