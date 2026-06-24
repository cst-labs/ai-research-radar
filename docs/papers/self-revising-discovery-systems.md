---
title: 'Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic
  Artificial Intelligence'
---

# Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence

**Link:** [https://arxiv.org/abs/2606.01444](https://arxiv.org/abs/2606.01444)

**Authors:** Edward Lee, Feng-Jen Yang, Varun Manjunatha, Huanzhi Mao, Eric Dash, Haoyang Wen, Matthew Gormley, Marzieh Nabi

**Date:** 2026-06-01

**Type:** `framework`

**Primary Topic:** [Self Improvement](../topics/self-improvement.md)

**Topics:** [Agents](../topics/agents.md), [World Models](../topics/world-models.md), [Self Improvement](../topics/self-improvement.md)

## Contribution and Significance

The contribution is a formal model of self-revising discovery: discovery is a verified transition between representational regimes, not just a better answer in the same frame.

This matters for AI-for-science agents because genuinely useful discovery systems may need to change how they type artifacts, define operations, and validate claims over time.


## Summary

This paper develops a category-theoretic account of agentic scientific discovery. Its core idea is that discovery is not merely generating an answer inside a fixed representation, but revising the representational regime in which evidence, artifacts, operations, and verifiers are typed. In a fixed regime, the system updates typed states and provenance; discovery occurs when a verified transition moves the system into a new regime while preserving and transporting old artifacts, then identifying residual content that cannot be explained by transport alone.

The paper instantiates this abstract framework in two materials-science systems. Builder/Breaker revises a protein-mechanics world model under a Minimum Description Length gate, while CategoryScienceClaw represents typed skills, artifacts, open needs, workflow mutation, gates, stress tests, and discourse as a proof-carrying knowledge-computation graph. The work is mathematically heavy and more framework-building than benchmark-driven, but it provides a rigorous language for distinguishing retrieval, search, and discovery. Its relevance to agentic AI is strongest where agents are expected to revise not only hypotheses but also their schemas, tools, and verification regimes.


## Related Papers

- [AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts](../papers/atomic-facts-memory-llm-agents.md) - 2026-06-23 - The paper's main contribution is to treat agent memory as a representation problem before it is a retrieval problem. 
- [Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose](../papers/compositional-skill-routing.md) - 2026-06-22 - The contribution is a concrete formulation of tool use as a compositional routing problem. 
- [Building Social World Models with Large Language Models](../papers/social-world-models-llms.md) - 2026-06-12 - The contribution is a concrete benchmark and training recipe for modeling social belief transitions with LLMs. 
- [Trajectory-Refined Distillation: Enhancing Agents by Learning from Past Experience](../papers/trajectory-refined-distillation.md) - 2026-06-09 - The contribution is a trajectory-level fix for a structural weakness in on-policy distillation. 
- [Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents](../papers/agentic-clear.md) - 2026-05-28 - The key contribution is a multi-level evaluation pipeline that turns agent traces into actionable diagnostic insight.
