---
name: paper-loom
description: Plan, draft, or revise research papers by aligning problems, challenges, methods, and evidence, and maintaining explicit purpose and transition records for sections, paragraphs, and sentences. Use for paper organization, introduction or abstract logic, experiment narratives, and disconnected academic prose.
---

# Paper Loom

Build an argument the reader can follow, then make each unit of prose advance it. Maintain clean prose and an explicit hierarchy of intent records. Work in the user’s chosen language; the Chinese equivalent of these instructions is [SKILL.zh-CN.md](SKILL.zh-CN.md).

## Working contract

- For a whole-paper task, maintain an overall outline and **one separate document per section, paragraph, and sentence**, including the abstract. Each records purpose, content, and its connections to preceding and following units. Copy the corresponding [templates](assets/templates/en/outline.md) as needed; the full schema and layout are in [workflow](references/workflow.en.md).
- For a local edit, update that unit, affected ancestors, and adjacent transitions. Do not expand a paragraph request into a whole-paper rewrite. If files cannot be written, return the same records inline under their intended paths without claiming to have saved them.
- Use the manuscript as the authority for exact wording. Stable IDs and ordered lists connect the records; update both neighbors when moving or deleting a unit. Keep annotations out of submission prose.
- Preserve facts, quantitative results, citation scope, and genuine uncertainty. Distinguish observed evidence from planned experiments. A polished narrative does not repair a missing experiment or establish a causal relationship.

## Work from whole to parts

1. **Argument.** Define the reader, research question, stakes, central claim, and evidence status. Map background needs → challenges → insights → design choices → experiments → supported claims. Allow many-to-many links; remove orphan contributions or unsupported claims. Plan experiments around questions before implementation details.
2. **Sections.** Give each section a distinct purpose, the reader knowledge it assumes, what it adds, and why the next section follows. Allocate space by argumentative importance and the user’s venue constraints.
3. **Paragraphs.** Outline the function and main point of every paragraph before rewriting it. Prefer one paragraph with one main job. Give related-work categories a common organizing dimension relevant to the problem; explain the important coverage without pretending the taxonomy exhausts a field.
4. **Sentences.** Identify each sentence’s main assertion, what it takes from the preceding context, what new information it adds, and what it makes possible next. Reorder, split, merge, or supply a missing explanation when the chain breaks. Do not fix a missing premise merely by adding a connective.
5. **Reconcile.** Read the clean prose without annotations. Then check that all records still match it, all claim-to-evidence links are accurate, and the abstract and conclusion make the same scoped claims as the body.

For a new draft, plan top-down. For an existing draft, first map what it actually says; keep observed wording separate from proposed intent so that annotations reveal gaps instead of inventing coherence.

## Section priorities

Read [section guidance](references/sections.en.md) when outlining a section.

- **Abstract:** preserve enough background to motivate the task; connect the gap to the approach and report the most informative supported result. Compress implementation detail before removing the causal bridge.
- **Introduction:** lead the reader from a meaningful setting to a specific unresolved problem. Organize prior work by the relevant approach or assumption, explain the residual difficulty, derive challenges, then present the insight and design response. These are rhetorical functions, not a fixed paragraph count or mandatory ordering.
- **Method:** explain what is designed, why it addresses the stated challenge, and how its parts interact before exposing local mechanics. Keep details necessary to understand or reproduce the central mechanism.
- **Experiments:** ask what each experiment establishes, describe the comparison and metric needed to answer it, report the result, then state its implication. Separate overall effectiveness from evidence about its cause. Use the user’s space budget to prioritize distinct claims, not a fixed number of experiments.

## Sentence continuity and style

Use old information to introduce the new contribution when helpful: a repeated concept, a precise referent, or an explicit relation can connect sentences. Do not force identical opening words or repeat conclusions for rhythm. Record the actual relationship: motivation, refinement, example, contrast, cause, consequence, evidence, or synthesis. “Continues the previous sentence” is not an adequate annotation.

Give each sentence a dominant emphasis; split competing claims, but keep relationships that are clearer together. Prefer concrete verbs and stable terminology. Avoid gratuitous hyphenated labels, em-dash interruptions, and semicolon chains, especially in English. Retain conventional compounds, necessary punctuation, and mathematical minus signs. Punctuation cannot substitute for an explanation.

Use the [contrastive examples](references/examples.en.md) for specific failure patterns. A [worked example](examples/README.md) shows how the documents fit together. Do not copy its fictional content into a manuscript.

## Completion check

Deliver the clean draft, argument outline, requested per-unit records, and a short account of material logical changes. Explicitly mark unresolved evidence needs in the working records. Finish when the agreed scope has a coherent reading order, a main purpose for every unit, justified transitions, and claims matched to evidence. Do not promise acceptance or add research work beyond the user’s request.
