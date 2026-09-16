# Mod 模板

根据 mod 来源选择对应模板：

- 第三方 Steam 创意工坊 mod：复制 `_template/workshop/`；
- 基于上游 mod 的个人优化版本：复制 `_template/derived/`。

每个真实 mod 目录都需要同时包含 `README.md`、`metadata.yaml` 和 `references/`。

真实 mod 的 CK3 游戏文件修改完成后，Agent 按根目录 `AGENTS.md` 自动部署到本机 Steam 库的 `Crusader Kings III/mod/` 目录；模板本身不部署。
