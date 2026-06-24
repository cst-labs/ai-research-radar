---
title: 'Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents'
---

# Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents

**Link:** [https://arxiv.org/abs/2605.22608](https://arxiv.org/abs/2605.22608)

**Authors:** Difei Gao, Pedro Rodriguez, Yu Su

**Date:** 2026-05-28

**Type:** `framework`

**Primary Topic:** [Agent Evals](../topics/agent-evals.md)

**Topics:** [Agents](../topics/agents.md), [Agent Evals](../topics/agent-evals.md), [Evals](../topics/evals.md)

## Contribution and Significance

The key contribution is a multi-level evaluation pipeline that turns agent traces into actionable diagnostic insight. It moves agent evaluation from "did the task pass?" toward "which recurring behaviors explain success or failure?"

This matters because scalable agent development needs feedback loops that can compare configurations, identify failure modes, and support debugging without requiring humans to inspect every trajectory manually.


## Summary

Agentic CLEAR is an evaluation framework designed to sit above the observability layer and turn execution traces into structured textual feedback. It evaluates agent behavior at three granularities: system-level insights, trace-level judgments, and node-level feedback. The motivation is that agent failures are often distributed across planning, tool use, retrieval, and environment interaction, so static hand-authored taxonomies or final-answer metrics are not enough to explain what went wrong.

The framework uses judge models to generate dynamic criteria and insights from trace data, then links those insights back to specific parts of the execution. Experiments span four benchmarks, seven agentic configurations, and tens of thousands of LLM calls. The paper reports alignment with human-annotated errors and predictive signal for task success. Its practical contribution is not just another benchmark score, but a way to produce operational feedback that developers can use to iterate on agent systems. The limitations are the usual but important ones for judge-based evaluation: reliability depends on judge quality, coverage across domains remains an open problem, and future work is needed to include system execution details alongside reasoning and planning traces.


## Related Papers

- [AtomMem: Building Simple and Effective Memory System for LLM Agents via Atomic Facts](../papers/atomic-facts-memory-llm-agents.md) - 2026-06-23 - The paper's main contribution is to treat agent memory as a representation problem before it is a retrieval problem. 
- [Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose](../papers/compositional-skill-routing.md) - 2026-06-22 - The contribution is a concrete formulation of tool use as a compositional routing problem. 
- [Building Social World Models with Large Language Models](../papers/social-world-models-llms.md) - 2026-06-12 - The contribution is a concrete benchmark and training recipe for modeling social belief transitions with LLMs. 
- [Trajectory-Refined Distillation: Enhancing Agents by Learning from Past Experience](../papers/trajectory-refined-distillation.md) - 2026-06-09 - The contribution is a trajectory-level fix for a structural weakness in on-policy distillation. 
- [Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence](../papers/self-revising-discovery-systems.md) - 2026-06-01 - The contribution is a formal model of self-revising discovery: discovery is a verified transition between representational regimes, not just a better answer in the same frame.
