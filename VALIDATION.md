# Validation / 核验记录

Initial version, validated on 2026-11-12.

初版核验日期：2026-11-12。

## Executed checks / 已执行检查

- Both the English entry point and a temporary installation using the Chinese entry point passed the skill-creator frontmatter and scaffold validator.
- The example checker passed for each language: 5 sections, 7 paragraphs, and 21 sentences, with separate records for every unit.
- Checks cover exact manuscript/card wording, ordered parent-child lists, sentence adjacency, absent/orphan records, and relative documentation links. Template links are relative to their future output locations and are excluded from repository-link checking.
- Five deliberate mutations in temporary copies were detected: a stale sentence, a removed next-sentence link, a deleted card, an unmapped prose sentence, and an orphan paragraph card.
- The manuscript and cards were reviewed together to replace generic transitions with concrete conceptual handoffs and distinguish sentence purpose from its main assertion.

- 英文入口及以中文入口安装的临时副本均通过 skill-creator 的元数据和模板残留检查。
- 每种语言的示例均通过检查：5 个章节、7 个段落、21 个句子，每个单元有独立记录。
- 检查涵盖正文与句子卡一致性、上下层有序清单、句间邻接、缺失或孤立记录，以及文档相对链接。模板链接针对未来产物路径，不参与仓库链接检查。
- 临时副本中故意制造的五类错误均被发现：过期原句、删除后句链接、删除句子卡、增加未标注正文、增加孤立段落卡。
- 联合审阅正文与标注，将泛泛过渡替换为具体概念交接，并区分句子的作用与实际强调的判断。

Machine-readable results: [evals/structural-results.json](evals/structural-results.json).

机器可读结果：[evals/structural-results.json](evals/structural-results.json)。

## Re-run / 重新检查

```sh
python scripts/validate_examples.py
```

The checker uses the Python standard library and needs no model service. The skill-creator validator is an optional development tool, not an installation dependency.

检查器仅使用 Python 标准库，不调用模型服务。skill-creator 校验器是可选开发工具，不是安装依赖。

## Interpretation / 解释范围

These results establish packaging and example consistency. They do not measure writing quality, assess scientific validity, or demonstrate compliance across models. The cases in [evals/cases.md](evals/cases.md) specify a future behavioral evaluation. No independent model-behavior evaluation has been run for this release.

这些结果验证打包规范和示例一致性，不等于写作质量、科学有效性或跨模型遵循能力的测量。[evals/cases.md](evals/cases.md) 提供后续行为评估用例。本版未开展独立模型行为评价。
