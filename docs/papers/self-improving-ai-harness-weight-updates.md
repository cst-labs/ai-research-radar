---
title: Self Improving AI with Harness & Weight Updates
...
---

# Self Improving AI with Harness & Weight Updates

**Link:** [https://arxiv.org/abs/2605.27276](https://arxiv.org/abs/2605.27276)

**Authors:** Tenavi Nakamura, Michael K. Cohen, David Balduzzi, Vincent Conitzer, Akbir Khan

**Date:** 2026-05-29

**Type:** `paper`

**Primary Topic:** [Self Improvement](../topics/self-improvement.md)

**Topics:** [Agent Systems](../topics/agent-systems.md), [Self Improvement](../topics/self-improvement.md), [AI Infra](../topics/ai-infra.md)

## Contribution and Significance

The contribution is to treat self-improvement as a two-lever process: change the scaffold and change the weights. This is more ambitious than harness-only self-improvement and more agentic than a fixed training pipeline.

Its significance is that future self-improving systems may need to reason about how scaffolds and weights co-evolve. The paper also usefully surfaces the stability risks of optimizing both against the same verifier.


## Summary

This paper proposes SIA, a self-improving loop in which a Feedback-Agent updates both the harness and the weights of a task-specific agent. It explicitly connects two research lines that are often separate: harness-update systems, where prompts/tools/retry logic/search procedures change while weights stay fixed, and test-time training systems, where model weights adapt while the harness stays fixed. The paper argues that both levers matter because harnesses shape how the model searches and acts, while weight updates build domain-specific intuition that scaffolding alone cannot provide.

The evaluation spans three different domains: Chinese legal charge classification, GPU kernel optimization, and single-cell RNA denoising. The reported combined harness-and-weight system outperforms scaffold iteration alone and prior state of the art in all three settings. The limitations section highlights a coupled Goodhart problem: harness search and RL weight updates optimize against the same verifier, and each changes the distribution seen by the other. This can create strong verifier performance while remaining fragile under perturbations to either component. Future work includes learning the meta-policy that chooses between harness and weight updates and using more interleaved update schedules.


## Related Papers

- [Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose](../papers/compositional-skill-routing.md) - 2026-06-22 - The contribution is a concrete formulation of tool use as a compositional routing problem. 
- [Self-Harness: Harnesses That Improve Themselves](../papers/self-harness.md) - 2026-06-10 - The contribution is a disciplined self-improvement loop for harnesses: propose changes from trace evidence, validate them empirically, and promote only non-regressive edits. 
- [From Model Scaling to System Scaling: Scaling the Harness in Agentic AI](../papers/scaling-the-harness-agentic-ai.md) - 2026-05-28 - The paper's contribution is the argument that agent progress should be evaluated at the system level, not just at the model level. 
- [Trajectory-Refined Distillation: Enhancing Agents by Learning from Past Experience](../papers/trajectory-refined-distillation.md) - 2026-06-09 - The contribution is a trajectory-level fix for a structural weakness in on-policy distillation. 
- [Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence](../papers/self-revising-discovery-systems.md) - 2026-06-01 - The contribution is a formal model of self-revising discovery: discovery is a verified transition between representational regimes, not just a better answer in the same frame.
