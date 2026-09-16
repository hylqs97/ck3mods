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
5. 保持每个 mod 的变更隔离。除非用户明确要求（包括本地 Steam 部署），不要修改其他 mod 或共享游戏文件。
6. 不要擅自覆盖或删除用户已有的 mod 文件；下载或更新时先保存到临时位置，比较后再替换。
7. 不要把 Steam 凭据、访问令牌、Cookie 或其他秘密写入仓库。
8. 新增或修改 CK3 脚本后，尽量运行项目已有的检查；如果没有自动化检查，至少核对文件路径、descriptor 配置、前置 mod 和加载顺序。

## 本地 Steam 游戏目录部署

完成 `mods/workshop/<mod-id>/` 或 `mods/derived/<mod-id>/` 中会影响 CK3 游戏内容的修改后，Agent 必须自动将新版 mod 部署到本机 Steam 库中对应游戏的 mod 目录。仅修改 `README.md`、`metadata.yaml` 或 `references/` 时不需要部署游戏文件。

目标目录为：

```text
<SteamLibrary>/steamapps/common/Crusader Kings III/mod/<mod-directory-name>/
```

其中 `<SteamLibrary>` 应从本机 Steam 的 `steamapps/libraryfolders.vdf` 或标准 Steam 安装位置解析，不能写死其他机器的绝对路径；`local_deployment.enabled` 缺省或为 `true` 时启用部署，只有用户明确要求时才能设为 `false`。`<mod-directory-name>` 默认使用 `<mod-id>`，如 `metadata.yaml` 中存在非空的 `local_deployment.mod_dir_name` 则使用该值。CK3 的 Steam App ID 是 `1158310`。不得把文件复制到 `steamapps/workshop/content/1158310/`，该目录由 Steam 管理。

部署时必须遵守以下流程：

1. 先确认目标 Steam 库、CK3 游戏目录和目标 mod 目录，不能根据不确定的路径猜测；无法定位或没有权限时必须报告阻塞原因，不得伪造部署成功。
2. 先在临时目录中整理并比较文件，再复制 `descriptor.mod` 和 CK3 游戏文件；排除仓库的 `README.md`、`metadata.yaml`、`references/`、`.git` 和模板文件。
3. 保留仓库中的相对目录结构，不得修改其他 mod 目录或 Steam Workshop 管理目录。目标目录中仅存在于本机的文件不能被静默删除；如需删除旧文件，必须先报告并取得明确确认。
4. 复制完成后检查目标 `descriptor.mod` 和本次变更文件确实存在，并报告实际部署路径。部署失败时保留仓库内容不变。

本地部署不等于发布到 Steam Workshop；上传或发布仍然必须获得用户明确要求和相应授权。

## 第三方 Workshop mod 的同步

`workshop` mod 的 `metadata.yaml` 必须记录 Steam Workshop URL 或 item ID，以及：

```text
https://steamworkshopdownloader.io/
```

每次 Agent 被调用处理 `mods/workshop/<mod-id>/` 时，在进行其他修改前必须先检查本机 Steam 游戏 mod 目录中的对应快照。检查使用本地部署规则解析的 `<SteamLibrary>/steamapps/common/Crusader Kings III/mod/<mod-directory-name>/`，不得使用 `steamapps/workshop/content/1158310/`。

当 `metadata.yaml` 中 `local_sync.enabled` 缺省或为 `true`，且本机源目录存在时，Agent 必须：

1. 只读取 `descriptor.mod` 和 CK3 游戏文件，计算本机源目录的文件指纹，并与仓库的 `source_revision` 及游戏文件进行比较。
2. 如果本机源目录与仓库不同，先将本机内容复制到临时目录。仓库当前游戏文件仍等于已记录的 `source_revision` 时，将本机快照视为最新版并自动更新 `mods/workshop/<mod-id>/`；如果仓库也有未记录的游戏文件修改，则报告冲突，不得静默覆盖。
3. 自动回收时只更新 CK3 游戏文件和 `descriptor.mod`，保留仓库的 `README.md`、`metadata.yaml` 和 `references/`；同时更新 `last_synced_at`、`source_revision`、README 中的同步信息和 `local_sync.last_imported_at`。
4. 在替换仓库快照前完成差异检查；失败时保留原仓库内容，并明确报告失败原因。不能仅因为发现文件不同就声称已经确认是官方更新。

本地源目录不存在、路径不明确或无法访问时，不执行本地回收，也不得伪造同步成功。`local_sync.enabled: false` 只有在用户明确要求停用本地自动回收时才能设置。该自动回收仅适用于 `workshop` 快照，不能将本机目录反向覆盖 `derived` mod。

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
