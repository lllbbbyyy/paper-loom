# Organizing sections around reader questions

## Abstract: compress the chain, not just the word count

A useful chain is **setting and need → existing options and unresolved difficulty → approach and distinguishing mechanism → supported result and meaning**. A short abstract may combine functions in one sentence. Preserve enough context for readers outside the narrow specialty to understand why the method is needed.

When space is tight, remove tool names, parameter settings, procedural counts, and secondary metrics before deleting the reason the problem is hard. Match each number to its reference and metric. If results are not available, mark a working placeholder or omit the empirical claim. Do not turn a planned comparison into a finding. Define the logical roles before selecting a word budget for each sentence.

## Introduction: build a research story

The introduction should answer a sequence of reader questions. The following is a menu of functions, not a mandatory eight-paragraph template.

| Function | Reader question | Typical outgoing connection |
|---|---|---|
| Broad setting | What important activity or objective is involved? | That activity requires a particular capability. |
| Specific need | Why is the existing way of supplying it costly or difficult? | Different approaches address that need. |
| State of the art | What approaches or assumptions organize current solutions? | Their tradeoffs leave a task-specific problem. |
| Gap | What remains unresolved, under what conditions? | Solving it requires overcoming identifiable challenges. |
| Challenges | Why is the gap difficult, rather than merely unimplemented? | A useful observation suggests how to address it. |
| Insight | What relationship changes the way we should formulate the problem? | That relationship motivates particular design choices. |
| Approach | How do those choices work together? | Specific contributions and evidence can now be stated. |
| Contributions | What new capability or understanding does the work establish? | The body explains the mechanism and tests its claims. |

Give each paragraph a topic sentence stating its main point. The remaining sentences establish, qualify, or develop that point. A paragraph ending should leave a concept or question that the next paragraph genuinely takes up. Do not manufacture suspense, use fictional scenarios as the default opening, or make the reader wait for the research problem.

### Classifying related work

Choose a common dimension that explains the problem: information used, modeling assumption, optimization objective, level of decomposition, or another relevant property. Avoid mixing a model family, application field, and publication date as if they were parallel categories. Name categories at a level understandable to the intended broad audience before listing representative systems.

For each relevant category, explain what it handles well, what condition creates a remaining difficulty, and why that difficulty matters here. Back each characterization with the source. A concise transition can synthesize the remaining difficulty across several categories; a hostile “however, all these methods fail” after every citation is unnecessary and often inaccurate.

A good taxonomy covers the main alternatives relevant to the task and explains overlap or excluded scope where necessary. It need not be mutually exclusive or globally exhaustive. Map categories to challenges when the connection is substantive, allowing many-to-many relations. Do not invent a third challenge just because there are three categories.

### Challenges and insight

A challenge is a reason the desired capability is hard. “We need a data module” is a task list item. “Labels are expensive, while uniform sampling misses rare failure regimes” explains a difficulty that motivates a data strategy.

An insight is a supported observation or argued relationship that changes a design decision. “We propose a framework” names a contribution but supplies no insight. Distinguish a hypothesis from an observation established by a motivation experiment. Explain the link from insight to mechanism before naming modules.

## Method: purpose before machinery

Begin with task inputs, outputs, assumptions, and a high-level view of how the parts interact. For each major mechanism, explain:

1. Which challenge it addresses.
2. What design decision it makes.
3. Why that decision should address the challenge.
4. What information it receives and produces.
5. Which details are necessary to understand, implement, or evaluate it.

Name a module only when its role is understandable. Use a diagram or short algorithm when it clarifies control or data flow. Keep key objectives, decision rules, interfaces, and operating conditions in the paper. Put configuration inventories, prompts, and repetitive parameter lists in companion material when the venue allows it. Readability is not a reason to hide the mechanism.

## Experiments: answer questions with evidence

Plan the claim-to-experiment map before running additional experiments. Common questions include overall effectiveness, the source of improvement, generalization within a stated scope, and operational tradeoffs. Select those required by the paper’s actual claims; this is not a checklist requiring all four.

For each experiment record: the claim under test, the question, baseline or control, shared conditions, metric, result status, and the interpretation the comparison would permit. An ablation supports a mechanism claim only insofar as other relevant conditions are controlled. A case study can illustrate behavior without establishing a universal advantage.

In the prose, use **question → essential comparison → result → interpretation**. Explain whether errors, costs, or speedups are better when larger or smaller and what they are relative to. Report uncertainty or contrary results when they change the conclusion. Keep execution logs, file counts, and low-level tuning details outside the main narrative unless central to the claim.

## Discussion and conclusion

Discussion explains when the demonstrated mechanism is useful, which tradeoffs matter, and what assumptions affect interpretation. State important scope once where it is needed rather than repeating generic disclaimers.

The conclusion returns to the research problem, states the established capability or finding, and explains its significance within the evaluated scope. It must not introduce new mechanisms, results, or stronger claims than the paper supports. Its final sentence can close the argument without setting up another section.
