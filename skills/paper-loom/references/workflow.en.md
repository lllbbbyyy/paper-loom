# Workflow and document contract

## 1. Establish the editing scope

Record the manuscript version, target reader, paper type, language, space constraints, available evidence, and the requested unit of work. Use supplied context and sensible defaults rather than delaying for optional preferences. Preserve the manuscript’s existing format and location. This skill adds a companion `narrative/` directory, not a mandatory conversion to Markdown or a new publication workflow.

For a full paper, inventory all prose sections, including the abstract, limitations or discussion if present, and the conclusion. Annotate substantive captions when they make claims. Treat equations, algorithms, tables, and bibliographic entries as linked artifacts, not artificially segmented sentences. A heading belongs to its section record. An equation’s explanatory prose still needs sentence records.

For a local request, inventory only the requested units. Read sufficient surrounding context to check their incoming and outgoing links. Preserve untouched sections and mark unreviewed links as unreviewed.

## 2. Build an argument map before polishing

The overall outline records:

- The target reader, current problem, why it matters, and central supported claim.
- What the reader needs to know before understanding the gap.
- A traceability table: need/problem → challenge → insight → design response → evaluation question → evidence → claim.
- The intended section order and each section’s contribution.
- Space priorities and unresolved dependencies.

Give concepts stable IDs, for example `CH-01`, `IN-01`, `DS-01`, `EX-01`, and `CL-01`. Link existing evidence by its actual path or source. Use `observed`, `planned`, `missing`, or `not applicable` deliberately. A proposed experiment cannot be cited as a result. If evidence contradicts a claim, narrow the claim, explain the tradeoff, or propose a specific investigation. Do not silently change the comparison or the metric.

For theoretical, qualitative, or other nonexperimental work, use the corresponding proof, analysis, or source-based argument as the evidence step. Do not invent experiments or modules to fit an empirical-paper template.

A correspondence is a reason, not a name match. Explain **how** the design addresses the challenge and **what observation** would support that explanation. Many challenges may share a mechanism, and one experiment may test several claims. Background exposition does not need an artificial experiment link.

## 3. Use separate records, with stable identities

```text
narrative/outline.md
narrative/sections/SEC-ABSTRACT.md
narrative/sections/SEC-INTRO.md
narrative/paragraphs/P-INTRO-01.md
narrative/sentences/S-INTRO-001.md
```

Keep the IDs after moving a unit. Reading order comes from explicit lists, not filename sorting. Each section lists its paragraph IDs in order; each paragraph lists its sentence IDs in order. Every child links to its parent and to the manuscript location. Record the current text or a source excerpt so a later edit can detect drift without relying only on line numbers.

| Level | Required contents |
|---|---|
| Overall | Question, reader, central claim, argument/evidence map, ordered sections, space allocation, open gaps |
| Section | Purpose, main content, incoming reader knowledge, outgoing takeaway/question, neighboring section relationships, ordered paragraph outline, supported claims |
| Paragraph | Purpose, main point, role within section, incoming/outgoing relationships, ordered sentence outline, evidence dependencies |
| Sentence | Exact current text, main emphasis, content, previous/next relationships, given/new information, evidence status, source location and revision state |

A unit can have `START` or `END` as its structural neighbor. Record the reader’s entry context or final takeaway instead of fabricating a neighboring unit. The abstract is a self-contained reading path: its last sentence does not have to transition into the introduction. References are an evidence destination, not a continuation of the conclusion’s narrative.

## 4. Write useful connection annotations

For each incoming connection, answer:

1. Which specific concept or conclusion has the previous unit established?
2. What question, distinction, or missing premise remains?
3. How does this unit advance it?

For each outgoing connection, name the concept or question the next unit will take up. Do not write “provides context” without specifying which context and for what claim. Use a logical relation only when supported. Temporal succession is not causation; a higher score is not proof of the proposed mechanism.

Record intended and observed relationships separately when reviewing an existing draft. Example: “Intended: the interface motivates the method. Observed: the preceding sentence only lists components, so the need for preserving interface information has not been established.” Repair that gap in the prose before marking the link complete.

## 5. Revise at the highest broken level

- Unclear research question: repair the overall argument before polishing transitions.
- A section appears before the reader has its prerequisite: move it or introduce that prerequisite.
- A paragraph alternates among multiple purposes: split or reorganize it.
- A sentence introduces an unexplained concept: define or motivate it where needed.
- A connective implies an unsupported causal link: revise the relation or add a supported premise.

Use the smallest edit that resolves the actual defect. Do not insert a mini-summary after every paragraph or a transition sentence at every boundary if the connection is already clear.

## 6. Keep the map synchronized

A meaning-changing edit triggers this update order:

1. Revise the manuscript and its sentence record together.
2. Update affected sentence neighbors and their paragraph outline.
3. If the paragraph’s purpose changed, update its section outline.
4. If the claim or evidence changed, update the argument map, abstract, and conclusion as appropriate.

For a split, retain one ID and assign a new ID to the new unit. For a merge, retain one ID, remove obsolete links, and record the retired ID in a short revision note. Never leave a card containing a rejected sentence as if it were current. Keep historical versions only when the project requests version history.

Translation can change sentence counts. Preserve the argument and use explicit cross-language mappings, allowing one-to-many links rather than forcing identical syntax.

## 7. Deliver and stop

Deliver a clean draft plus the maintained records. Report substantive repairs, such as a missing premise or a disconnected experiment, rather than counting punctuation changes. Distinguish a complete writing pass from missing research evidence. If evidence is missing, finish the authorized writing with an accurate scoped claim or a clearly marked working placeholder and identify the remaining need. Do not launch experiments or fabricate findings merely to satisfy a story outline.
