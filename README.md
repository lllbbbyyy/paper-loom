# Paper Loom

[简体中文](README.zh-CN.md)

**Make a paper’s argument traceable, from its overall question to the job of each sentence.**

Paper Loom weaves problems, methods, and evidence into a coherent argument, connecting sections, paragraphs, and sentences.

It is a bilingual writing skill for research papers. It helps an assistant organize the research story before polishing prose: connect the problem to challenges, insights, design choices, and evidence; then maintain an explicit purpose and transition record for every section, paragraph, and sentence, including the abstract.

A fluent transition is a relationship between ideas, not a supply of words such as “therefore.” The skill asks what the reader has learned, what question remains, and why the next sentence answers it.

## What it produces

```text
manuscript.md                    Clean prose, without annotations
narrative/
  outline.md                     Paper argument, evidence map, reading order
  sections/SEC-INTRO.md           Purpose and ordered paragraph outline
  paragraphs/P-INTRO-01.md        Paragraph purpose and sentence outline
  sentences/S-INTRO-001.md        Exact sentence, focus, incoming/outgoing links
```

Each section, paragraph, and sentence has its own Markdown document. Stable IDs connect the levels. The manuscript is the authoritative text; annotations must reflect its current wording. A synthesis table is an index, not a replacement for the individual records.

The default full-paper workflow covers every prose sentence, including the abstract. A request to revise a single paragraph stays local and updates only its affected records and immediate connections.

## Install

Clone the repository first:

```sh
git clone https://github.com/lllbbbyyy/paper-loom.git
cd paper-loom
```

The portable skill folder is [`skills/paper-loom`](skills/paper-loom). For a Codex-compatible installation, copy that entire folder into your skills directory. From the repository root, for a new installation:

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/paper-loom "${CODEX_HOME:-$HOME/.codex}/skills/"
```

If a skill with this name already exists, review the differences before replacing it. Other assistants can use `SKILL.md` directly together with its relative references and templates.

The default entry point is English. For a Chinese entry point, copy `SKILL.zh-CN.md` over `SKILL.md` **in the installed copy**. Both have the same skill name and behavior; install one, not two competing copies. Either entry point supports manuscripts in either language.

## Use

> Use $paper-loom to reorganize this paper. First map the problem, challenges, insights, method, and evidence. Then maintain a separate document for every section, paragraph, and sentence, explaining its purpose, content, and links to the preceding and following units. Start with the introduction. Keep the clean manuscript separate.

> Use $paper-loom on this abstract only. Preserve the results, identify what each sentence contributes, and repair the transitions without adding unsupported claims.

> Use $paper-loom to plan experiments for this argument. Identify what each proposed experiment would establish before choosing implementations or metrics.

## Included resources

- [English instructions](skills/paper-loom/SKILL.md) · [中文指令](skills/paper-loom/SKILL.zh-CN.md)
- [Workflow and document contract](skills/paper-loom/references/workflow.en.md) · [工作流程与文档约定](skills/paper-loom/references/workflow.zh-CN.md)
- [Section-level guidance](skills/paper-loom/references/sections.en.md) · [章节组织](skills/paper-loom/references/sections.zh-CN.md)
- [Contrastive examples](skills/paper-loom/references/examples.en.md) · [正反例](skills/paper-loom/references/examples.zh-CN.md)
- [English templates](skills/paper-loom/assets/templates/en) · [中文模板](skills/paper-loom/assets/templates/zh-CN)
- [Worked bilingual example](skills/paper-loom/examples/README.md): a short research narrative with actual per-unit documents
- [Behavioral evaluation cases](evals/cases.md) · [Validation notes](VALIDATION.md)

The examples are fictional teaching material. No empirical results or citations should be copied into a real paper. The skill does not require a model provider, API, manuscript upload, or another skill. It does not generate missing evidence to make a story look complete.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep the two language versions semantically aligned. A new rule should solve an observable writing failure and include a useful positive and negative example.

## License

[MIT](LICENSE).
