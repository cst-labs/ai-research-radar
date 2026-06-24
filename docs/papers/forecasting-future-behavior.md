---
title: Forecasting Future Behavior as a Learning Task
...
---

# Forecasting Future Behavior as a Learning Task

**Link:** [https://arxiv.org/abs/2606.11445](https://arxiv.org/abs/2606.11445)

**Authors:** Michael K. Cohen, Sam Toyer, Akbir Khan, Jonas Ch. Peters, David Balduzzi, Vincent Conitzer

**Date:** 2026-06-12

**Type:** `paper`

**Primary Topic:** [Behavior Forecasting](../topics/behavior-forecasting.md)

**Topics:** [LLM Reasoning](../topics/llm-reasoning.md), [World Models](../topics/world-models.md), [Behavior Forecasting](../topics/behavior-forecasting.md)

## Contribution and Significance

The contribution is to separate behavior forecasting from explanation. Rather than asking a model or human to read a chain of thought and infer what it means, the paper trains a forecaster to learn predictive patterns directly from trajectories.

This matters for agent evaluation because many safety and reliability questions are predictive: will the system repeat an answer, change under perturbation, or behave consistently under reruns? Forecasting may be a scalable complement to interpretability.


## Summary

This paper argues that trust in large reasoning models often requires forecasting future behavior, but natural-language explanations and naive readings of reasoning traces are unreliable. Instead of trying to interpret a trajectory directly, the authors formulate behavior forecasting as a supervised learning task. A Behavior Forecaster observes a single reasoning trajectory and predicts behavioral properties of the target model, with labels generated automatically by querying the model itself.

The paper instantiates the idea on two tasks: predicting whether the model will repeat its answer on reruns, and predicting how removing parts of the input changes the answer. Across three reasoning datasets, trained Behavior Forecasters outperform strong frontier models used as naive readers of the same trajectories, at much lower inference cost. The results indicate that reasoning trajectories contain predictive information that is not obvious from surface reading. Important constraints are that the method requires task-specific supervision, end-to-end fine-tuning, and often initialization from the target model family.


## Related Papers

- [Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose](../papers/compositional-skill-routing.md) - 2026-06-22 - The contribution is a concrete formulation of tool use as a compositional routing problem. 
- [Trajectory-Refined Distillation: Enhancing Agents by Learning from Past Experience](../papers/trajectory-refined-distillation.md) - 2026-06-09 - The contribution is a trajectory-level fix for a structural weakness in on-policy distillation. 
- [Building Social World Models with Large Language Models](../papers/social-world-models-llms.md) - 2026-06-12 - The contribution is a concrete benchmark and training recipe for modeling social belief transitions with LLMs. 
- [Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence](../papers/self-revising-discovery-systems.md) - 2026-06-01 - The contribution is a formal model of self-revising discovery: discovery is a verified transition between representational regimes, not just a better answer in the same frame.
