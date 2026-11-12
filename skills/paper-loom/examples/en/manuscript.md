# Planning measurements across response regimes

## Abstract

Repeated model evaluation requires predictions that are inexpensive to query. Building such predictors requires observations of the operating conditions that affect the response. We describe a measurement policy that uses unresolved differences between operating regimes to select the next observations. A planned comparison with uniform sampling will evaluate prediction error under equal measurement budgets.

## Introduction

A response model lets a designer compare operating configurations without repeating every physical measurement. Its predictions must remain accurate across the configurations used in that comparison. Obtaining that accuracy requires observations of the conditions under which the response changes.

Uniform sampling allocates measurements across a chosen configuration range. When distinct response regimes occupy unequal portions of that range, uniform allocation can leave a small regime with few observations. The resulting question is how to allocate a limited budget to differences that the current model has not yet explained.

Our working hypothesis is that observed differences between regimes can guide this allocation. The proposed policy records unresolved differences and uses them to select subsequent measurements. Its value must be tested against a policy with the same measurement budget and access to the same predictors.

## Method sketch

The policy receives the available measurements and a candidate predictor. It groups observed configurations by their declared operating regime and records differences that the predictor does not explain. These records guide the next measurement allocation, after which the predictor is fitted again.

## Evaluation plan

The evaluation will test whether the proposed allocation reduces prediction error relative to uniform sampling. Both policies will use the same initial measurements, total budget, and predictor family. Error will be reported both overall and by regime so that an aggregate improvement does not hide a poorly modeled regime.

## Conclusion

This proposal connects a measurement need to a policy that acts on unresolved response differences. The planned controlled comparison will determine whether that design improves prediction under a fixed budget.
