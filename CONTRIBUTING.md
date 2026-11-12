# Contributing / 贡献规范

A useful change addresses a demonstrated writing failure without forcing unrelated papers into a fixed mold. Add a concise contrastive example when changing a rule. Preserve evidence, attribution, and author intent.

有效修改应针对具体写作问题，不将所有论文套入同一个结构。规则变化时补充简洁正反例，保留证据、归属与作者意图。

## Bilingual maintenance / 双语维护

- Update both entry points, both corresponding reference files, and both templates when their semantics change.
- Keep required fields and distinctions equivalent. Translate naturally rather than enforcing identical sentence counts.
- Update the worked example and its index together. Exact sentence records must match their manuscript.
- Do not add copied private manuscripts, unpublished findings, service configuration, or credentials.

- 规则变化时同步更新中英入口、对应指南和模板。
- 保持必需字段和概念区分一致，自然翻译，不机械限制句数。
- 同步修改示例和索引，句子卡原句必须对应正文。
- 不加入私人稿件、未公开发现、服务配置或凭据。

## Validation / 核验

Run `python scripts/validate_examples.py` from the repository root. If the skill-creator tooling is available, also run its `quick_validate.py` on `skills/paper-loom`. For the Chinese entry point, validate a temporary copy with `SKILL.zh-CN.md` selected as `SKILL.md`.

在仓库根目录运行 `python scripts/validate_examples.py`。可使用 skill-creator 时，对 `skills/paper-loom` 运行其 `quick_validate.py`。中文入口在临时副本中替换为 `SKILL.md` 后检查。

Use the cases in `evals/cases.md` for behavioral review. Structural checks do not assess scientific merit or prove that a model follows the instructions. Record which checks actually ran and distinguish human/self-review from an independent model evaluation.

用 `evals/cases.md` 检查实际行为。结构检查不评判科学价值，也不能证明模型遵守了指令。记录实际执行的检查，区分自行审阅与独立模型评价。
