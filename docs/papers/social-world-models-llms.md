---
title: Building Social World Models with Large Language Models
...
---

# Building Social World Models with Large Language Models

**Link:** [https://arxiv.org/abs/2606.11482](https://arxiv.org/abs/2606.11482)

**Authors:** Jonathan S. Morrow, Mingyu Choi, James A. Evans

**Date:** 2026-06-12

**Type:** `paper`

**Primary Topic:** [World Models](../topics/world-models.md)

**Topics:** [Agents](../topics/agents.md), [World Models](../topics/world-models.md)

## Contribution and Significance

The contribution is a concrete benchmark and training recipe for modeling social belief transitions with LLMs. It broadens "world models" from physical or simulated environments to social and institutional dynamics.

This is important for agentic AI because agents operating in real societies will need to reason about how beliefs, markets, and groups respond to events, but the same capability creates manipulation and governance risks.


## Summary

This paper introduces Social World Models, LLM-based models that predict how collective beliefs evolve in response to events. Instead of relying on explicit human annotations linking events to belief shifts, the method mines temporal patterns in social data and trains state-transition functions over social belief states. The evaluation benchmark, SWM-Bench, is derived from real-world prediction markets such as Kalshi and Polymarket and includes more than 12,000 data points across domains including politics, finance, and cryptocurrency.

The reported results show strong performance on Kalshi and competitive performance on Polymarket, with the added benefit that the model can provide interpretable signals about social belief dynamics. The paper's significance is that it reframes world modeling for social systems: rather than modeling physical dynamics, the target is how populations update beliefs after events. The impact statement also flags serious risks: such models could be used defensively to detect inorganic belief shifts, but also maliciously to optimize disinformation or manipulate public opinion; prediction-market feedback loops are another concern.


## Related Papers

- [AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts](../papers/atomic-facts-memory-llm-agents.md) - 2026-06-23 - The paper's main contribution is to treat agent memory as a representation problem before it is a retrieval problem. 
- [Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose](../papers/compositional-skill-routing.md) - 2026-06-22 - The contribution is a concrete formulation of tool use as a compositional routing problem. 
- [Trajectory-Refined Distillation: Enhancing Agents by Learning from Past Experience](../papers/trajectory-refined-distillation.md) - 2026-06-09 - The contribution is a trajectory-level fix for a structural weakness in on-policy distillation. 
- [Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence](../papers/self-revising-discovery-systems.md) - 2026-06-01 - The contribution is a formal model of self-revising discovery: discovery is a verified transition between representational regimes, not just a better answer in the same frame. 
- [Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents](../papers/agentic-clear.md) - 2026-05-28 - The key contribution is a multi-level evaluation pipeline that turns agent traces into actionable diagnostic insight.
