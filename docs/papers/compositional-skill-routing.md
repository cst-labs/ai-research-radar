---
title: 'Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose'
---

# Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose

**Link:** [https://arxiv.org/abs/2606.18051](https://arxiv.org/abs/2606.18051)

**Authors:** Yassir Fathullah, Doug Downey, Tom M. Mitchell, Yu Su

**Date:** 2026-06-22

**Type:** `paper`

**Primary Topic:** [Agent Systems](../topics/agent-systems.md)

**Topics:** [Agents](../topics/agents.md), [Agent Systems](../topics/agent-systems.md), [LLM Reasoning](../topics/llm-reasoning.md)

## Contribution and Significance

The contribution is a concrete formulation of tool use as a compositional routing problem. Instead of assuming an agent can select one tool or stuff every tool into context, the paper shows why decomposition, retrieval, and planning need to be engineered together.

Its significance is strongest for MCP-style ecosystems: as tool libraries grow, agent capability will depend on routing systems that can identify the right subset of skills and preserve task granularity without exhausting the context window.


## Summary

This paper formalizes compositional skill routing for LLM agents: given a complex user query and a large library of reusable skills or tool specifications, the agent must decompose the request into atomic subtasks, retrieve an appropriate skill for each subtask, and compose an executable plan. The proposed SKILLWEAVER framework combines an LLM decomposer, a bi-encoder skill retriever with FAISS indexing, and a dependency-aware planning stage. The evaluation uses COMPSKILLBENCH, a benchmark of 300 compositional queries over 2,209 real MCP server skills across 24 categories.

The most important empirical finding is that decomposition quality is the bottleneck. Standard LLM decomposition has weak step-level category recall, so the paper introduces Iterative Skill-Aware Decomposition, a retrieval-augmented feedback loop that aligns decomposition with the skills actually available. This improves decomposition accuracy substantially in the reported experiments and reduces context-window consumption by more than 99 percent compared with naively loading large tool libraries. The limitations are clear: the benchmark queries are partly synthetic, evaluation is mainly category-level retrieval rather than exact skill execution, and the full compose stage is not yet evaluated end to end with real compatibility annotations and recovery mechanisms.


## Related Papers

- [AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts](../papers/atomic-facts-memory-llm-agents.md) - 2026-06-23 - The paper's main contribution is to treat agent memory as a representation problem before it is a retrieval problem. 
- [Building Social World Models with Large Language Models](../papers/social-world-models-llms.md) - 2026-06-12 - The contribution is a concrete benchmark and training recipe for modeling social belief transitions with LLMs. 
- [Trajectory-Refined Distillation: Enhancing Agents by Learning from Past Experience](../papers/trajectory-refined-distillation.md) - 2026-06-09 - The contribution is a trajectory-level fix for a structural weakness in on-policy distillation. 
- [Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence](../papers/self-revising-discovery-systems.md) - 2026-06-01 - The contribution is a formal model of self-revising discovery: discovery is a verified transition between representational regimes, not just a better answer in the same frame. 
- [Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents](../papers/agentic-clear.md) - 2026-05-28 - The key contribution is a multi-level evaluation pipeline that turns agent traces into actionable diagnostic insight.
