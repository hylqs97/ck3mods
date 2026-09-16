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
