# Vassal Manager Reboot

- 标识：`vassal-manager-reboot`；类型：`workshop`；版本：`2.4`；CK3：`1.19.*`。
- 功能：批量管理封臣头衔、政体、契约及保护规则。
- 前置 Mod：无（本地descriptor无声明；线上待复核）。
- 导入时间：2026-09-18T15:56:38+08:00。来源为本机已安装文件，不代表线上最新版本。
- 上游：https://steamcommunity.com/sharedfiles/filedetails/?id=3773800577（2.4）。
- 文件指纹：`sha256:8967338d65387c6205d05a2e9ef677c2253bb99eb1125485bbe5fd2104ebef32`；明细见 references/source-files.json。

## 安装与加载顺序

游戏文件已按AGENTS.md部署至 `G:\SteamLibrary\steamapps\common\Crusader Kings III\mod\vassal-manager-reboot`。此目录是额外本地副本，未改变当前用户mod目录或播放集。
使用时将descriptor及游戏文件复制到CK3用户mod目录，配套外部.mod的path应指向所选目录。不要将同一原版的Workshop副本与此快照同时启用。
原版先加载，其他汉化其次，个人中文补丁最后。廷臣中文补丁还必须在 Automatic Education - Guardian & University Manager 之后。
只维护Windows，不提供Linux发行包。仓库README、metadata、references不参与游戏加载。

## 修改、同步与发布

保持原版游戏文件逐字节一致；原作者README另存 references/original-files/README.md（若存在）。
以后先从Steam游戏mod目录检查本地回收，启用local_sync；本次该目录不存在，按用户要求从Workshop安装目录初次导入。
Git提交状态以仓库历史为准；提交不等于推送或发布Workshop。原作者再发布许可待确认。

## 原mod信息与限制

描述和评论读取尝试：2026-09-18T15:56:38+08:00；未成功读取，最近成功时间为null。更新记录读取状态见 metadata.yaml 与 references/updates.md。
references/description.md、comments.md、updates.md保留来源及访问限制，不伪造页面结论。
上游更新后需重新比对；本地文件校验不代表已在游戏内验证。

## Agent入口

维护前读取 [根AGENTS.md](../../../AGENTS.md) 和本目录metadata、references。遵循Windows专用维护、指纹校验及按需部署规则。核对全部上游与实际加载路径；只改文档时无需部署游戏文件。
