# Mods 目录

这里按来源区分两类 mod：

| 目录 | 用途 |
| --- | --- |
| `workshop/` | Steam 创意工坊中其他作者公开 mod 的本地快照 |
| `derived/` | 基于上游 mod 修改、优化或扩展后的个人版本 |

新增 `workshop` mod 时：

1. 创建 `mods/workshop/<mod-id>/`；
2. 复制 `_template/workshop/` 的整个模板目录，包括 `README.md`、`metadata.yaml` 和 `references/`；
3. 记录 Workshop item ID、源地址和下载站地址；
4. 将 CK3 mod 文件放入该目录；
5. 阅读并整理原 mod 的描述、更新记录和评论到 `references/`；
6. 填写功能、前置 mod、兼容版本、同步时间和加载顺序。

新增 `derived` mod 时：

1. 创建 `mods/derived/<mod-id>/`；
2. 复制 `_template/derived/` 的整个模板目录，包括 `README.md`、`metadata.yaml` 和 `references/`；
3. 记录上游 Workshop mod、采用的上游版本和本地修改；
4. 将个人版本的 CK3 mod 文件放入该目录；
5. 阅读并整理上游 mod 的描述、更新记录和评论到 `references/`；
6. 填写功能、前置 mod、更新方式、兼容版本和发布状态。

`_template/` 仅用于创建新 mod，不应作为 mod 加载。同步第三方 mod 时使用 `https://steamworkshopdownloader.io/`，但不要把下载站或上游 mod 默认视为允许再发布。

`references/` 中的内容应是带来源和读取时间的摘要，避免批量复制 Steam 页面或评论全文。

## Workshop 本地快照回收

每次 Agent 处理 `workshop/<mod-id>/` 时，会先检查本机 Steam 游戏 mod 目录中的对应快照。如果本机快照与仓库不同，且仓库没有未记录的游戏文件修改，Agent 会先比较并自动将本机最新版回收至仓库；`README.md`、`metadata.yaml` 和 `references/` 会保留并同步更新。

该自动回收只适用于 `workshop` mod，不会把本机目录反向覆盖 `derived` mod。详细冲突处理和路径规则以根目录 `AGENTS.md` 为准。

## 本地 Steam 部署

修改真实 mod 的 CK3 游戏文件后，Agent 会自动将其部署到本机 Steam 库中的：

```text
<SteamLibrary>/steamapps/common/Crusader Kings III/mod/<mod-directory-name>/
```

默认使用仓库内的 `<mod-id>` 作为 `<mod-directory-name>`；如 `metadata.yaml` 配置了 `local_deployment.mod_dir_name`，则使用配置值。部署只复制 `descriptor.mod` 和 CK3 游戏文件，不复制仓库说明、元数据和 `references/`；详细安全规则以根目录 `AGENTS.md` 为准。

## 已导入 Mod

| 类型 | 目录 | 内容 |
| --- | --- | --- |
| workshop | [automated-courtier-management](workshop/automated-courtier-management/README.md) | 廷臣管理原版 1.3.2 |
| workshop | [automatic-education](workshop/automatic-education/README.md) | 自动教育原版 2.1.0 |
| workshop | [vassal-manager-reboot](workshop/vassal-manager-reboot/README.md) | 封臣管理原版 2.4 |
| derived | [automated-courtier-management-cn](derived/automated-courtier-management-cn/README.md) | 汉化、监护诊断与0岁监护筛选 cn.5 |
| derived | [vassal-manager-reboot-cn](derived/vassal-manager-reboot-cn/README.md) | 封臣管理完整汉化 2.4-cn.1 |

本次为本机文件导入，不是线上更新。页面访问不完整的记录见各mod的references。

## Agent 维护约定

以根目录 [AGENTS.md](../AGENTS.md) 为准。只维护 Windows，不制作 Linux 或便携发行包。
本机初次导入、游戏目录快照回收、在线下载须分别记录，不能将本机文件称为线上最新版本。
Steam 游戏目录副本不等于 Launcher 实际加载副本；更新现用补丁时核对用户目录、外部.mod路径及启用列表。
网页读取失败保留成功读取时间为null或旧值，另记尝试时间和状态。组合补丁用additional_upstreams记录全部额外上游。
修改游戏文件后检查指纹并部署；仅文档修改无需重新部署。提交前运行 `python tools/validate_repository.py`（仓库根目录）。
