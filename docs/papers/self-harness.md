---
title: 'Self-Harness: Harnesses That Improve Themselves'
---

# Self-Harness: Harnesses That Improve Themselves

**Link:** [https://arxiv.org/abs/2606.09498](https://arxiv.org/abs/2606.09498)

**Authors:** David Balduzzi, Tenavi Nakamura, Martin Buchheit, Kevin R. McKee, Akbir Khan, Michael K. Cohen

**Date:** 2026-06-10

**Type:** `framework`

**Primary Topic:** [Self Improvement](../topics/self-improvement.md)

**Topics:** [Agent Systems](../topics/agent-systems.md), [Self Improvement](../topics/self-improvement.md), [AI Infra](../topics/ai-infra.md)

## Contribution and Significance

The contribution is a disciplined self-improvement loop for harnesses: propose changes from trace evidence, validate them empirically, and promote only non-regressive edits.

Its significance is that it treats the agent scaffold as something that can evolve through recorded, testable, and reversible changes, moving beyond manual prompt/harness engineering while avoiding unconstrained self-modification.


## Summary

Self-Harness asks whether a fixed language model can improve the harness that governs its own agent behavior. The proposed loop has three stages: weakness mining from execution traces, harness proposal that turns failure patterns into bounded modifications, and proposal validation through regression testing. The model and evaluator stay fixed, so improvements can be attributed to changes in the harness rather than a stronger underlying model.

The experiments instantiate the method on Terminal-Bench-2.0 with a minimal initial harness and three different base models. Reported held-out pass rates improve for all three, and qualitative analysis suggests the accepted changes are model-specific executable harness edits rather than generic instruction stuffing. The paper is careful about limits: it studies bounded harness edits under fixed benchmarks, not open-ended recursive self-improvement. Accepted edits may overfit benchmark-specific failures, verifier quality matters, and higher-stakes settings would need stricter acceptance gates than pass-rate non-regression.


## Related Papers

- [Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose](../papers/compositional-skill-routing.md) - 2026-06-22 - The contribution is a concrete formulation of tool use as a compositional routing problem. 
- [Self Improving AI with Harness & Weight Updates](../papers/self-improving-ai-harness-weight-updates.md) - 2026-05-29 - The contribution is to treat self-improvement as a two-lever process: change the scaffold and change the weights. 
- [From Model Scaling to System Scaling: Scaling the Harness in Agentic AI](../papers/scaling-the-harness-agentic-ai.md) - 2026-05-28 - The paper's contribution is the argument that agent progress should be evaluated at the system level, not just at the model level. 
- [Trajectory-Refined Distillation: Enhancing Agents by Learning from Past Experience](../papers/trajectory-refined-distillation.md) - 2026-06-09 - The contribution is a trajectory-level fix for a structural weakness in on-policy distillation. 
- [Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence](../papers/self-revising-discovery-systems.md) - 2026-06-01 - The contribution is a formal model of self-revising discovery: discovery is a verified transition between representational regimes, not just a better answer in the same frame.
