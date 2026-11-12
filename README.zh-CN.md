# Paper Loom：从全文论证到逐句衔接的科研写作 Skill

[English](README.md)

**让论文从全文问题到每一句话，都有明确的目的和可追溯的逻辑。**

Paper Loom（论文织机）将问题、方法与证据织成全文主线，再连接章节、段落和句子。

这个中英双语 skill 将科研写作组织为“先论证、后结构、再表达”：先对应问题、挑战、洞察、方法和证据，再逐层维护章节、段落和句子的目的、内容及前后承接。摘要也采用同一套方法。

逻辑连贯并不是多加几个“因此”“然而”。真正需要检查的是：读者刚刚知道了什么，还缺哪一步解释，下一句为什么应当接在这里。

## 输出什么

```text
manuscript.md                    不含标注的干净正文
narrative/
  outline.md                     全文论证、证据对应与阅读顺序
  sections/SEC-INTRO.md           章节目的与逐段提纲
  paragraphs/P-INTRO-01.md        段落目的与逐句提纲
  sentences/S-INTRO-001.md        原句、重点、前后承接及证据状态
```

每个章节、每个段落、每个句子各有独立 Markdown 文档，使用稳定 ID 相互链接。正文是措辞的唯一准本；标注记录必须随正文更新。总表用于索引，不能替代这些独立记录。

默认完整论文模式覆盖所有正文句子，包括摘要。用户只要求改一个段落时，保持局部范围，只更新受影响记录和紧邻的衔接关系。

## 安装

先克隆仓库：

```sh
git clone https://github.com/lllbbbyyy/paper-loom.git
cd paper-loom
```

可安装目录为 [`skills/paper-loom`](skills/paper-loom)。在仓库根目录执行以下命令，可新装到 Codex 的 skills 目录：

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/paper-loom "${CODEX_HOME:-$HOME/.codex}/skills/"
```

已有同名 skill 时先检查差异，再决定如何替换。其他助手可直接读取 `SKILL.md` 及其相对路径引用的资源。

默认入口为英文。若希望安装中文入口，在**已安装的副本中**用 `SKILL.zh-CN.md` 替换 `SKILL.md`。两版名称和行为一致，安装其中一版即可；两版均可处理中文或英文论文。

## 使用示例

> 请使用 $paper-loom 重组这篇论文。先建立问题、挑战、洞察、方法和证据的对应关系，再为每个章节、段落和句子分别维护文档，说明目的、内容及前后承接。先从引言开始，正文与标注分开保存。

> 请使用 $paper-loom 只修改这段摘要。保留所有实验事实，明确每句的作用，修复逻辑跳跃，不增加没有证据的主张。

> 请使用 $paper-loom 先规划实验。根据文章要证明的主张，说明每项实验为什么需要、能排除什么解释，再决定具体实现和指标。

## 项目内容

- [中文 skill](skills/paper-loom/SKILL.zh-CN.md) / [English skill](skills/paper-loom/SKILL.md)
- [工作流程与文档约定](skills/paper-loom/references/workflow.zh-CN.md)
- [各章节组织方法](skills/paper-loom/references/sections.zh-CN.md)
- [正反例及原因分析](skills/paper-loom/references/examples.zh-CN.md)
- [中文模板](skills/paper-loom/assets/templates/zh-CN) / [English templates](skills/paper-loom/assets/templates/en)
- [完整双语微型示例](skills/paper-loom/examples/README.md)：包含实际的逐章节、逐段、逐句文档
- [行为评估用例](evals/cases.md) / [核验记录](VALIDATION.md)

示例均为虚构教学材料，不能当作真实论文的事实或引用。skill 无须绑定模型、API 或其他 skill，也不要求上传论文。论证闭环依靠明确主张和证据，不能靠补造实验或夸大相关工作不足实现。

## 贡献与许可

修改规范见 [CONTRIBUTING.md](CONTRIBUTING.md)。两种语言的规则和字段保持语义一致；新增规则应对应具体写作问题，并配套正反例。

采用 [MIT 许可证](LICENSE)。
