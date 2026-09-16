# CK3 Mods 仓库说明

## 项目目标

本仓库用于管理《十字军之王 3》（Crusader Kings 3）的个人 mods，并明确区分：

- `workshop`：Steam 创意工坊中其他作者公开发布的 mod 的本地快照；
- `derived`：基于其他作者 mod 修改、优化或扩展后的个人版本。

## 目录约定

```text
.
├── AGENTS.md
└── mods/
    ├── README.md
    ├── workshop/
    │   └── <mod-id>/
    │       ├── README.md
    │       ├── metadata.yaml
    │       ├── references/
    │       │   ├── description.md
    │       │   ├── comments.md
    │       │   └── updates.md
    │       ├── descriptor.mod
    │       └── ... CK3 mod 文件
    ├── derived/
    │   └── <mod-id>/
    │       ├── README.md
    │       ├── metadata.yaml
    │       ├── references/
    │       │   ├── description.md
    │       │   ├── comments.md
    │       │   └── updates.md
    │       ├── descriptor.mod
    │       └── ... CK3 mod 文件
    └── _template/
        ├── README.md
        ├── workshop/
        └── derived/
```

- `<mod-id>` 是稳定、唯一的 mod 目录名；优先使用小写字母、数字和连字符。
- `workshop/<mod-id>/` 只能存放第三方公开 mod 的本地快照及其同步元数据。
- `derived/<mod-id>/` 只能存放基于上游 mod 的个人修改版本及其上游、发布元数据。
- `_template/` 只是新 mod 的模板，不是可加载的 mod。
- 每个真实 mod 目录都必须有 `README.md` 和 `metadata.yaml`。
- `references/` 保存原 mod 的描述、更新记录和评论区的结构化摘要，不属于 CK3 可加载文件。
- CK3 的 `common/`、`events/`、`gui/`、`localisation/` 等游戏文件直接放在对应 mod 目录下，除非该 mod 的打包方式另有要求。
- 不要把多个 mod 的游戏文件混在同一个目录中，也不要把第三方快照和个人修改混在同一个目录中。

## Agent 工作规则

1. 修改前先读取本文件、`mods/README.md`，以及目标 mod 的 `README.md`、`metadata.yaml` 和 `references/`。
2. 新增第三方公开 mod 时，使用 `mods/_template/workshop/` 模板；新增个人优化版本时，使用 `mods/_template/derived/` 模板。
3. 修改 mod 功能、前置关系、兼容版本、上游版本或加载顺序时，同步更新说明和元数据。
4. 前置 mod 必须使用明确的 mod 名称或仓库内相对路径；如果前置关系不确定，保留待确认标记，不要猜测。
5. 保持每个 mod 的变更隔离。除非用户明确要求，不要修改其他 mod 或共享游戏文件。
6. 不要擅自覆盖或删除用户已有的 mod 文件；下载或更新时先保存到临时位置，比较后再替换。
7. 不要把 Steam 凭据、访问令牌、Cookie 或其他秘密写入仓库。
8. 新增或修改 CK3 脚本后，尽量运行项目已有的检查；如果没有自动化检查，至少核对文件路径、descriptor 配置、前置 mod 和加载顺序。

## 第三方 Workshop mod 的同步

`workshop` mod 的 `metadata.yaml` 必须记录 Steam Workshop URL 或 item ID，以及：

```text
https://steamworkshopdownloader.io/
```

当用户要求同步、检查更新，或运行约定的定期同步任务时：

1. 从元数据读取 Workshop item ID，使用上述网站当前提供的公开下载流程获取最新版本。
2. 将下载内容放到临时目录，先比较文件差异和版本信息，不要直接覆盖本地快照。
3. 确认下载成功且内容完整后，再更新 mod 文件、`last_synced_at`、`source_revision` 和 `README.md` 中受影响的信息。
4. 如果网站不可用、下载结果不完整或无法确认版本，不得伪造成功；保留现有快照并明确报告阻塞原因。
5. 遵守 Steam、下载站和原作者的使用许可及发布规则；下载不等于获得再发布权限。

## 原 mod 描述、更新记录和评论

在同步、更新或发布任何 `workshop`/`derived` mod 前，Agent 必须阅读对应原 mod 的 Steam Workshop 页面，包括：

- mod 描述、依赖、兼容版本和作者声明；
- 更新记录、公告和已知问题；
- 评论区中与安装、兼容性、报错和最新版本有关的信息。

页面地址、描述/评论/更新记录的最近读取时间必须写入 `metadata.yaml`。将阅读结果整理到 `references/description.md`、`references/comments.md` 和 `references/updates.md`，并保留来源 URL 与页面更新时间。

- `references/` 应保存可跨设备阅读的摘要和关键链接，而不是假设每次都能访问 Steam。
- 评论只记录与 mod 维护有关的技术结论、日期和链接；不要批量复制用户名或其他不必要的个人信息，也不要复制整页内容。
- Steam 页面不可访问时，可以阅读最近一次本地快照，但必须标记为过期并报告 `last_read_at`；不能把过期信息当成当前事实。
- SteamCMD 负责获取 mod 文件，不等于能够提供完整描述和评论；页面信息仍需通过 Workshop 页面或可访问的官方信息接口阅读。

## Derived mod 的更新与发布

`derived` mod 的 `metadata.yaml` 必须记录：

- 上游 Workshop mod 的 URL 或 item ID；
- 最近一次采用的上游版本或快照标识；
- 本地修改摘要；
- 个人版本的发布状态、Workshop URL 或 item ID（如果已经发布）。
- 上游描述、评论和更新记录的 URL、最近读取时间及 `references/` 快照位置。

更新 derived mod 时：

1. 按上面的同步流程获取上游最新快照，并保留当前个人修改。
2. 对比上游变化，将本地修改重新应用或合并；冲突必须记录并等待处理，不能静默覆盖。
3. 核对功能、前置 mod、加载顺序和 CK3 版本，更新 `README.md` 和 `metadata.yaml`。
4. 只有用户明确要求发布时，才使用 Steam 官方客户端或其他经授权的上传方式发布；发布后记录版本、日期和 Workshop 地址。
5. 没有上传权限或工具时，Agent 必须明确说明无法完成发布，不得声称已经发布。

## 说明文档最低要求

每个 mod 的 `README.md` 至少包含：

- mod 名称和唯一标识；
- mod 类型：`workshop` 或 `derived`；
- 功能概述；
- 前置 mod（没有则明确写“无”）；
- 适用的 CK3 版本；
- 安装方式和加载顺序；
- 已知冲突或限制；
- 对 `workshop` mod：上游 Workshop 地址和最近同步信息；
- 对 `derived` mod：上游地址、本地修改摘要和发布状态；
- 原 mod 描述、更新记录和评论的最近读取时间，以及对应的 `references/` 文件。
