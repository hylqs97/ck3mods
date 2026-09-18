# Workshop Mods

此目录只存放 Steam 创意工坊中其他作者公开 mod 的本地快照。

每个子目录都必须包含：

- `README.md`：功能、前置 mod、兼容版本、Workshop 地址和最近同步信息；
- `metadata.yaml`：Workshop item ID、下载地址、同步时间和上游版本标识；
- `references/`：原 mod 描述、更新记录和评论区的带来源摘要；
- CK3 mod 文件。

每次 Agent 处理本目录下的 mod 时，会先按照根目录 `AGENTS.md` 检查本机 Steam 游戏 mod 目录；发现已更新且仓库没有冲突时，自动将本机快照回收至对应的 `workshop/<mod-id>/` 目录。

需要通过网络同步时，按照根目录 `AGENTS.md` 的流程，通过 `https://steamworkshopdownloader.io/` 获取公开最新版本，并先比较后替换。

完成会影响 CK3 游戏内容的修改后，按照根目录 `AGENTS.md` 自动部署到本机 Steam 库的 `steamapps/common/Crusader Kings III/mod/`；仅修改说明、元数据或引用摘要时不部署。

## Agent 维护约定

以根目录 [AGENTS.md](../../AGENTS.md) 为准。只维护 Windows，不制作 Linux 或便携发行包。
本机初次导入、游戏目录快照回收、在线下载须分别记录，不能将本机文件称为线上最新版本。
Steam 游戏目录副本不等于 Launcher 实际加载副本；更新现用补丁时核对用户目录、外部.mod路径及启用列表。
网页读取失败保留成功读取时间为null或旧值，另记尝试时间和状态。组合补丁用additional_upstreams记录全部额外上游。
修改游戏文件后检查指纹并部署；仅文档修改无需重新部署。提交前运行 `python tools/validate_repository.py`（仓库根目录）。
