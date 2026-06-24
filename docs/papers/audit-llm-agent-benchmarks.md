---
title: 'What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and
  an Open Scoring Schema'
---

# What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema

**Link:** [https://arxiv.org/abs/2605.21404](https://arxiv.org/abs/2605.21404)

**Authors:** Lisa Bukowski, Jordan Martin, Eden Davis, Tom B. Brown, Sarah Chen

**Date:** 2026-05-27

**Type:** `paper`

**Primary Topic:** [Agent Evals](../topics/agent-evals.md)

**Topics:** [Agent Evals](../topics/agent-evals.md), [Evals](../topics/evals.md)

## Contribution and Significance

The contribution is to make benchmark reporting itself measurable. By scoring what papers disclose about harnesses, inference settings, costs, and failures, the work gives the community a lightweight reproducibility checklist.

This matters because agent benchmark results are especially sensitive to scaffolds and environment details. Without disclosure standards, leaderboard numbers can look comparable while hiding materially different evaluation conditions.


## Summary

This pilot audit examines what LLM agent benchmark papers disclose about how their evaluations were actually run. The motivation is a practical reproducibility problem: different papers may report different numbers for the same nominal model and benchmark, but the published artifact often does not reveal whether the discrepancy comes from scaffold differences, inference settings, subsets, evaluator versions, or cost constraints. The authors design a small audit schema covering benchmark identity, harness specification, inference settings, cost reporting, and failure breakdown.

Applying the schema to twelve benchmark papers, the paper reports lower disclosure scores for agent benchmarks than for classical static benchmarks. The largest gaps appear in inference cost and harness specification; none of the audited agent benchmark papers fully disclose a content-addressed container image of the evaluation environment. The paper does not claim that disclosure proves correctness. Instead, it argues that without disclosure, readers cannot interpret or compare results reliably. The contribution is a practical scoring schema and codebook for benchmark transparency rather than a new agent benchmark.


## Related Papers

- [SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Running AI Agents](../papers/subtlememory.md) - 2026-06-05 - The contribution is a benchmark that makes memory quality more precise: the question is not merely whether an agent remembers something, but whether it remembers how related memories interact. 
- [Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents](../papers/agentic-clear.md) - 2026-05-28 - The key contribution is a multi-level evaluation pipeline that turns agent traces into actionable diagnostic insight. 
- [Boiling the Frog: A Multi-Turn Benchmark for Agentic Safety](../papers/boiling-the-frog-agentic-safety.md) - 2026-05-22 - The contribution is a stateful multi-turn safety benchmark for agents.
