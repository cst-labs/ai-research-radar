---
title: 'From Model Scaling to System Scaling: Scaling the Harness in Agentic AI'
---

# From Model Scaling to System Scaling: Scaling the Harness in Agentic AI

**Link:** [https://arxiv.org/abs/2605.26112](https://arxiv.org/abs/2605.26112)

**Authors:** Theodora Worledge, Albert Jiang, Karthik Narasimhan, Ofir Press

**Date:** 2026-05-28

**Type:** `paper`

**Primary Topic:** [Agent Systems](../topics/agent-systems.md)

**Topics:** [Agents](../topics/agents.md), [Agent Systems](../topics/agent-systems.md), [AI Infra](../topics/ai-infra.md)

## Contribution and Significance

The paper's contribution is the argument that agent progress should be evaluated at the system level, not just at the model level. It makes the harness an explicit object of scaling, optimization, and governance.

This is significant for the radar because many recent agent papers, including memory, routing, evaluation, and self-improvement work, can be seen as different pieces of harness scaling.


## Summary

This position/framework paper argues that the next bottleneck in agentic AI is system scaling rather than only model scaling. It defines the "harness" as the structured execution layer around the model: memory, context construction, skill routing, orchestration, verification, governance, and interaction with tools or subagents. The paper's central claim is that long-horizon agent behavior emerges from the interaction between the foundation model and this harness, so model-centric evaluation misses much of what determines practical capability.

The paper organizes the research agenda around context governance, trustworthy memory, dynamic skill routing, orchestration, and verification/governance. It uses Claude Code, OpenClaw, and CheetahClaws as concrete points of comparison to make harness-level design choices visible. Its value is conceptual and architectural: it provides vocabulary for treating agent scaffolds as first-class objects of design and evaluation. The limitation is that the paper is primarily a framework and research agenda rather than a controlled empirical comparison; the claims should be read as a call to measure harness components more systematically.


## Related Papers

- [AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts](../papers/atomic-facts-memory-llm-agents.md) - 2026-06-23 - The paper's main contribution is to treat agent memory as a representation problem before it is a retrieval problem. 
- [Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose](../papers/compositional-skill-routing.md) - 2026-06-22 - The contribution is a concrete formulation of tool use as a compositional routing problem. 
- [Building Social World Models with Large Language Models](../papers/social-world-models-llms.md) - 2026-06-12 - The contribution is a concrete benchmark and training recipe for modeling social belief transitions with LLMs. 
- [Trajectory-Refined Distillation: Enhancing Agents by Learning from Past Experience](../papers/trajectory-refined-distillation.md) - 2026-06-09 - The contribution is a trajectory-level fix for a structural weakness in on-policy distillation. 
- [Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence](../papers/self-revising-discovery-systems.md) - 2026-06-01 - The contribution is a formal model of self-revising discovery: discovery is a verified transition between representational regimes, not just a better answer in the same frame.
