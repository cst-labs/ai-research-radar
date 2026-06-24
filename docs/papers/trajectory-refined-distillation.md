---
title: 'Trajectory-Refined Distillation: Enhancing Agents by Learning from Past Experience'
---

# Trajectory-Refined Distillation: Enhancing Agents by Learning from Past Experience

**Link:** [https://arxiv.org/abs/2606.08432](https://arxiv.org/abs/2606.08432)

**Authors:** Dennis Metz, Dominik Hönig, Hugo Mohammadi, Patrick Schramowski, Kristian Kersting

**Date:** 2026-06-09

**Type:** `paper`

**Primary Topic:** [Self Improvement](../topics/self-improvement.md)

**Topics:** [Agents](../topics/agents.md), [LLM Reasoning](../topics/llm-reasoning.md), [Self Improvement](../topics/self-improvement.md)

## Contribution and Significance

The contribution is a trajectory-level fix for a structural weakness in on-policy distillation. Instead of only changing token losses, TRD repairs the path the student is learning from.

Its significance is that agent and reasoning traces are becoming training objects in their own right. Improving models from experience may require editing or refining whole trajectories, not just scoring final answers.


## Summary

Trajectory-Refined Distillation studies a failure mode in on-policy distillation for reasoning models. In standard on-policy distillation, the student generates rollouts and receives dense per-token teacher supervision along those rollouts. The paper identifies "prefix failure": early problematic prefixes can cause teacher supervision to become fragmented or bimodal, and token-level truncation or reweighting does not fix the structural problem.

The proposed TRD method performs trajectory-level correction. A teacher-guided refinement revises the student's rollout while keeping it close to the on-policy support, and the refined trajectory is used for distillation. The method can also be applied to on-policy self-distillation with privileged information. Across several competition-math benchmarks and Qwen model scales, TRD improves single-attempt accuracy and reasoning coverage over baselines. The main limitations are the extra sampling budget needed to construct refined trajectories and dependence on a teacher that can guide refinement without pushing trajectories too far from the student's distribution.


## Related Papers

- [AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts](../papers/atomic-facts-memory-llm-agents.md) - 2026-06-23 - The paper's main contribution is to treat agent memory as a representation problem before it is a retrieval problem. 
- [Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose](../papers/compositional-skill-routing.md) - 2026-06-22 - The contribution is a concrete formulation of tool use as a compositional routing problem. 
- [Building Social World Models with Large Language Models](../papers/social-world-models-llms.md) - 2026-06-12 - The contribution is a concrete benchmark and training recipe for modeling social belief transitions with LLMs. 
- [Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence](../papers/self-revising-discovery-systems.md) - 2026-06-01 - The contribution is a formal model of self-revising discovery: discovery is a verified transition between representational regimes, not just a better answer in the same frame. 
- [Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents](../papers/agentic-clear.md) - 2026-05-28 - The key contribution is a multi-level evaluation pipeline that turns agent traces into actionable diagnostic insight.
