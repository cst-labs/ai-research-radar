---
title: 'Boiling the Frog: A Multi-Turn Benchmark for Agentic Safety'
---

# Boiling the Frog: A Multi-Turn Benchmark for Agentic Safety

**Link:** [https://arxiv.org/abs/2605.22643](https://arxiv.org/abs/2605.22643)

**Authors:** Piercosma Bisconti, Matteo Prandi, Federico Pierucci, Federico Sartore, Enrico Panai, Laura Caroli, Yue Zhu, Adam Leon Smith, Luca Nannini, Marcello Galisai, Susanna Cifani, Francesco Giarrusso, Marcantonio Bracale Syrnikov, Daniele Nardi

**Date:** 2026-05-22

**Type:** `benchmark`

**Primary Topic:** [Agent Security](../topics/agent-security.md)

**Topics:** [Agent Evals](../topics/agent-evals.md), [Agent Security](../topics/agent-security.md), [Evals](../topics/evals.md), [Alignment Safety](../topics/alignment-safety.md)

## Contribution and Significance

The contribution is a stateful multi-turn safety benchmark for agents. It captures a failure mode where every individual request may look tolerable, but the sequence gradually produces an unsafe persistent state.

This is significant because agent safety cannot be evaluated only by classifying responses. For tool-using agents, the safety-relevant object is often the artifact, file, workflow, or environment state the agent leaves behind.


## Summary

Boiling the Frog is a benchmark for agentic safety that shifts attention from unsafe text outputs to unsafe state changes caused by tool-using agents. The scenarios are set in corporate and office-like workspaces. Each chain begins with benign workspace edits and later introduces a risk-bearing request, testing whether models can resist incremental attacks that gradually move a persistent workspace toward an unsafe artifact state.

The benchmark uses a three-level operational risk taxonomy grounded in Boiling-the-Frog risks, EU AI Act high-risk contexts, and the Code of Practice on General-Purpose AI. Across a nine-model panel, the paper reports a strict aggregate attack success rate of 44.4 percent, with large differences across models and especially high success in loss-of-control scenarios. Its methodological contribution is artifact-state validation: the benchmark scores whether the final workspace state is unsafe, not merely whether the model said something unsafe. Limitations include one finalized run per chain, a selective model panel, and a sandboxed office environment that does not yet cover browsers, databases, email, identity systems, CI pipelines, cloud dashboards, or human approval workflows.


## Related Papers

- [SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Running AI Agents](../papers/subtlememory.md) - 2026-06-05 - The contribution is a benchmark that makes memory quality more precise: the question is not merely whether an agent remembers something, but whether it remembers how related memories interact. 
- [Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents](../papers/agentic-clear.md) - 2026-05-28 - The key contribution is a multi-level evaluation pipeline that turns agent traces into actionable diagnostic insight. 
- [What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema](../papers/audit-llm-agent-benchmarks.md) - 2026-05-27 - The contribution is to make benchmark reporting itself measurable. 
- [An Empirical Study of Privacy Leakage Chains via Prompt Injection in Black-Box Chatbot Environments](../papers/privacy-leakage-chains-prompt-injection.md) - 2026-05-22 - The contribution is an empirical attack-chain analysis showing how indirect prompt injection can become privacy leakage when agents are allowed to browse and invoke tools.
