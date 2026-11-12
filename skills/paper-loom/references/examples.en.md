# Contrastive examples

All examples are fictional. They illustrate writing choices, not established scientific findings. A revision may add a premise only when the author’s sources or reasoning support it.

## 1. A connective cannot supply a missing premise

**Weak**

> Hardware configurations are numerous. Neural networks fit nonlinear functions. Therefore, we build a component graph.

The second sentence does not explain why configurations require a graph, and the conclusion introduces decomposition without motivation.

**Better, if the premise is supported**

> Hardware exploration requires predictions for many configurations. The effects of these configurations arise from components with different behaviors. Representing those components explicitly allows the modeling procedure to choose a suitable predictor for each behavior.

Sentence jobs: establish demand → explain relevant heterogeneity → derive a representation choice. The second sentence carries “configurations” forward and introduces “components,” which the third takes up. The repair is the missing relationship, not the word “therefore.”

## 2. Topic continuity without repetitive openings

**Weak**

> Data collection is expensive. Our model has three modules. Rare operating regimes affect accuracy.

**Better**

> Collecting reference measurements is expensive. A limited measurement budget can leave rare operating regimes poorly represented. The acquisition policy therefore prioritizes regimes where additional measurements can resolve the current uncertainty.

“Measurement” connects the first two sentences, and the coverage problem motivates the policy. The exact acquisition rule still belongs in the method section. Repeating “data collection” at the start of every sentence would add repetition without clarifying that rule.

## 3. Related-work categories must explain the gap

**Weak outline**

> Paragraph 1: neural models. Paragraph 2: accelerator papers. Paragraph 3: recent systems. All are insufficient, so we propose three modules.

These categories mix method, domain, and date. The claimed insufficiency has no stated condition.

**Better outline**

> Organize relevant predictors by the information they use: explicit mechanism descriptions and measured input–output observations. Explain each source’s strengths and the conditions under which it is incomplete. Then discuss how approaches combining these sources decide what information to retain and what observations to acquire.

The categories motivate questions about information and acquisition. Their coverage is relative to the modeling task. A combined approach may overlap both categories, and challenges need not be one-to-one with categories.

## 4. Preserve motivation in a short abstract

**Weak**

> We propose X with a graph module, a planner, a validator, and five regressors. X achieves strong results.

**Better**

> Design exploration requires repeated predictions at low cost. Different component behaviors require different modeling assumptions and observations. X coordinates representation and data acquisition to construct task-specific predictors. [Insert a supported accuracy–cost result with its comparison.]

This is a working abstract, not a completed empirical report. It spends words on why coordination is needed before naming the approach. The result placeholder must be resolved or removed before submission.

## 5. Explain a mechanism before its inventory

**Weak**

> The controller uses JSON, three queues, two prompts, and four scorers.

**Better**

> The controller chooses the next modeling action from the current evidence state. If an interface conflict is already confirmed, it requests an experiment that addresses the remaining uncertainty. This avoids asking the diagnostic role to repeat a completed determination.

The revision explains state → decision → reason. Serialization details belong elsewhere unless they affect the claimed mechanism. The method must still specify how conflicts are confirmed and what experiments are permitted.

## 6. Report an experiment as an answer

**Weak**

> We ran twelve scripts and generated 320 files. The variant performs better.

**Better**

> We test whether the state handoff changes acquisition decisions under the same candidate tools and sample budget. The comparison reports prediction error and the selected sampling actions. [Insert observed results.] These results support [the interpretation warranted by that comparison].

A controlled question precedes logistics. Planned outputs remain marked as planned. A lower error alone does not prove why the improvement occurred.

## 7. Do not imply more than the evidence supports

**Weak**

> The method lowers average error, proving that every component is modeled reliably.

**Better**

> The method lowers average error on the evaluated configurations. Per-component results identify where the quality target is met and where it is not.

This separates an aggregate finding from a stronger reliability claim. Add the actual per-component results if available; otherwise do not imply they were measured.

## 8. Punctuation and invented labels

**Weak**

> Our evidence-driven-quality-aware-agent-orchestrated framework selects actions; it revises interfaces; it validates predictors—thereby solving modeling.

**Better**

> The framework selects actions using validation results and interface evidence. It then revises the representation or acquires data, depending on the unresolved problem. Candidate predictors are evaluated against the same quality requirement.

Each sentence has a main job, and the order exposes the mechanism. Conventional expressions such as “white-box model,” “state-of-the-art method,” or a mathematical minus sign remain acceptable. Do not mechanically replace every hyphen with a space or every semicolon with a period.

## 9. Useful versus empty annotations

**Empty**

> Purpose: explain the method. Previous: follows the preceding sentence. Next: leads into the next sentence.

**Useful**

> Focus: an interface that merges distinct responses limits any downstream predictor. Incoming: the preceding example established two configurations with identical summaries but different outcomes. Outgoing: the next sentence asks which additional input would distinguish them. Evidence: the example supports this local ambiguity, not a claim about all configurations.

The annotation identifies the actual conceptual handoff and its evidence scope.

## 10. Repair the highest broken level

**Weak revision**

> Add “however” between an experiment paragraph and a paragraph defining the task, while leaving the task definition after the results.

**Better revision**

> Move the task definition before the experiment, then update the section order and both affected neighbor links. Add a short transition only if the new order still leaves a gap.

A section-order problem cannot be solved by sentence-level polish.
