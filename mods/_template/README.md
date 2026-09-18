# Mod 模板

根据 mod 来源选择对应模板：

- 第三方 Steam 创意工坊 mod：复制 `_template/workshop/`；
- 基于上游 mod 的个人优化版本：复制 `_template/derived/`。

每个真实 mod 目录都需要同时包含 `README.md`、`metadata.yaml` 和 `references/`。

真实 mod 的 CK3 游戏文件修改完成后，Agent 按根目录 `AGENTS.md` 自动部署到本机 Steam 库的 `Crusader Kings III/mod/` 目录；模板本身不部署。

## Agent 维护约定

以根目录 [AGENTS.md](../../AGENTS.md) 为准。只维护 Windows，不制作 Linux 或便携发行包。
本机初次导入、游戏目录快照回收、在线下载须分别记录，不能将本机文件称为线上最新版本。
Steam 游戏目录副本不等于 Launcher 实际加载副本；更新现用补丁时核对用户目录、外部.mod路径及启用列表。
网页读取失败保留成功读取时间为null或旧值，另记尝试时间和状态。组合补丁用additional_upstreams记录全部额外上游。
修改游戏文件后检查指纹并部署；仅文档修改无需重新部署。提交前运行 `python tools/validate_repository.py`（仓库根目录）。
