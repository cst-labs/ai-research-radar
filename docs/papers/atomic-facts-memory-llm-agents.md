---
title: 'AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts'
---

# AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts

**Link:** [https://arxiv.org/abs/2606.19847](https://arxiv.org/abs/2606.19847)

**Authors:** Haopeng Wang, Tushar Muralidharan, Andrew Lee, Zhiruo Wang, Weili Nie, Samyam Rajbhandari, Yizhong Wang, Yejin Choi, Eric P. Xing, Silvio Savarese, Huan Wang

**Date:** 2026-06-23

**Type:** `paper`

**Primary Topic:** [Agent Memory](../topics/agent-memory.md)

**Topics:** [Agents](../topics/agents.md), [Agent Memory](../topics/agent-memory.md)

## Contribution and Significance

The paper's main contribution is to treat agent memory as a representation problem before it is a retrieval problem. By converting interactions into compact atomic facts and then structuring them into events, profiles, and associations, AtomMem offers a concrete recipe for memory systems that are cheaper, cleaner, and more stable than storing long transcripts.

Its significance for AI Research Radar is that it points toward a practical design principle for persistent agents: memory quality should be engineered explicitly, not left as an emergent property of long-context prompting or vector search over raw logs.


## Summary

AtomMem addresses a core limitation of long-running LLM agents: useful information accumulates across sessions, but raw dialogue logs are noisy, redundant, and expensive to retrieve from. The paper proposes turning interactions into "atomic facts," then organizing those facts into event memories, temporal profile memories, and an associative memory graph. This gives the agent a more value-dense memory substrate than unstructured chat history while preserving enough structure to recover episodic context and changing user attributes.

The empirical focus is the LoCoMo benchmark, where AtomMem is evaluated across reasoning tasks that require long-term personalized recall. The reported results suggest that high-quality memory representation matters at least as much as retrieval sophistication: even a simplified flat variant performs strongly, supporting the paper's claim that clean fact construction is a powerful foundation for agent memory. Important caveats are that several stages depend on the underlying LLM's generation quality, the current system is text-only, and further work is needed to optimize token efficiency and extend the approach to multimodal memories.


## Related Papers

- [Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose](../papers/compositional-skill-routing.md) - 2026-06-22 - The contribution is a concrete formulation of tool use as a compositional routing problem. 
- [Building Social World Models with Large Language Models](../papers/social-world-models-llms.md) - 2026-06-12 - The contribution is a concrete benchmark and training recipe for modeling social belief transitions with LLMs. 
- [Trajectory-Refined Distillation: Enhancing Agents by Learning from Past Experience](../papers/trajectory-refined-distillation.md) - 2026-06-09 - The contribution is a trajectory-level fix for a structural weakness in on-policy distillation. 
- [Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence](../papers/self-revising-discovery-systems.md) - 2026-06-01 - The contribution is a formal model of self-revising discovery: discovery is a verified transition between representational regimes, not just a better answer in the same frame. 
- [Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents](../papers/agentic-clear.md) - 2026-05-28 - The key contribution is a multi-level evaluation pipeline that turns agent traces into actionable diagnostic insight.
