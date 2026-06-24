---
title: 'SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Running
  AI Agents'
---

# SubtleMemory: A Benchmark for Fine-Grained Relational Memory Discrimination in Long-Running AI Agents

**Link:** [https://arxiv.org/abs/2606.05761](https://arxiv.org/abs/2606.05761)

**Authors:** Kevin Qinghong Lin, Haiyang Yu, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun

**Date:** 2026-06-05

**Type:** `benchmark`

**Primary Topic:** [Agent Memory](../topics/agent-memory.md)

**Topics:** [Agent Memory](../topics/agent-memory.md), [Agent Evals](../topics/agent-evals.md), [Evals](../topics/evals.md)

## Contribution and Significance

The contribution is a benchmark that makes memory quality more precise: the question is not merely whether an agent remembers something, but whether it remembers how related memories interact.

Its significance is that realistic agent memory will involve conflicts, refinements, and context-dependent relations. Systems that pass simple recall tests may still fail when asked to reason over subtly different or contradictory memories.


## Summary

SubtleMemory is a benchmark for evaluating whether long-running agents can preserve and use fine-grained relations among memories. The paper argues that persistent assistants do not only need to recall isolated facts; they must understand when memories are complementary, nuanced variants, or direct contradictions. To test this, the benchmark constructs relation-controlled latent semantic artifacts, embeds variants into realistic user-agent histories, and asks later queries that require recovering distributed relational structure.

The benchmark contains 1,522 evaluation instances over 10 long histories, grounded in 1,090 relation-controlled memory-variant sets. The evaluation covers standalone memory systems, Claw-style agents with native memory, and Claw-style agents with plugin memory modules. The reported finding is that current systems remain weak at fine-grained relational discrimination, and diagnostic protocols separate preservation, retrieval, and downstream reasoning failure modes. The limitations are that it is text-only, uses a controlled relation taxonomy, and relies on selected answer-generation and judging models; future work needs multimodal, multilingual, domain-specific, and more human-validated settings.


## Related Papers

- [AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts](../papers/atomic-facts-memory-llm-agents.md) - 2026-06-23 - The paper's main contribution is to treat agent memory as a representation problem before it is a retrieval problem. 
- [Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents](../papers/agentic-clear.md) - 2026-05-28 - The key contribution is a multi-level evaluation pipeline that turns agent traces into actionable diagnostic insight. 
- [What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema](../papers/audit-llm-agent-benchmarks.md) - 2026-05-27 - The contribution is to make benchmark reporting itself measurable. 
- [Boiling the Frog: A Multi-Turn Benchmark for Agentic Safety](../papers/boiling-the-frog-agentic-safety.md) - 2026-05-22 - The contribution is a stateful multi-turn safety benchmark for agents.
