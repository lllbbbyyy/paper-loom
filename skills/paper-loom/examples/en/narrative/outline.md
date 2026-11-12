# Paper argument outline

Manuscript: [manuscript.md](../manuscript.md), v1. Reader: a broad researcher who understands prediction but not acquisition policies. Scope: all prose in this miniature proposal, including the abstract. Its short paragraphs demonstrate the records, not the space allocation of a conference paper.

Research question: how should measurements be allocated across response regimes under a limited budget? Central claim CL-01: allocation using unexplained differences may improve prediction, pending evaluation. The current artifact is a proposal, not a demonstrated empirical advantage.

| Need | Challenge | Insight/hypothesis | Design | Evaluation | Evidence and claim |
|---|---|---|---|---|---|
| Repeated configuration comparisons require accurate prediction | CH-01: unequal regime sizes can leave small regimes with few uniformly allocated observations | IN-01: observed differences can guide allocation, a working hypothesis | DS-01: record unexplained differences to guide the next measurements | EX-01: compare uniform sampling with the same initial data, budget, and predictor family | Planned, not measured. Tests CL-01 rather than establishing it. |

Conditional basis: uniform allocation distributes samples over the range, so a smaller region receives fewer samples in expectation. This supports the coverage concern under the stated condition, not the superiority of any adaptive policy.

## Section order

1. [SEC-ABSTRACT](sections/SEC-ABSTRACT.md): Abstract

2. [SEC-INTRO](sections/SEC-INTRO.md): Introduction

3. [SEC-METHOD](sections/SEC-METHOD.md): Method sketch

4. [SEC-EXPERIMENTS](sections/SEC-EXPERIMENTS.md): Evaluation plan

5. [SEC-CONCLUSION](sections/SEC-CONCLUSION.md): Conclusion

## Space and open relationships

Prioritize the need and coverage difficulty in the introduction. The method is a sketch and still requires a concrete allocation rule. Evaluation has not been executed. A full paper needs the rule and results before claiming effectiveness. The abstract is an independent reading path; the remaining sections follow the listed order.
