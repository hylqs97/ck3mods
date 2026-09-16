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
