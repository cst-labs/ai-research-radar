---
title: An Empirical Study of Privacy Leakage Chains via Prompt Injection in Black-Box Chatbot
  Environments
...
---

# An Empirical Study of Privacy Leakage Chains via Prompt Injection in Black-Box Chatbot Environments

**Link:** [https://arxiv.org/abs/2605.18133](https://arxiv.org/abs/2605.18133)

**Authors:** Leyang Cui, Sairun Huang, Che-Yu Chen, Wenzhe Gao, Uri Gal, Lili Mou, Huan Liu, Yong Li

**Date:** 2026-05-22

**Type:** `paper`

**Primary Topic:** [Agent Security](../topics/agent-security.md)

**Topics:** [Agent Security](../topics/agent-security.md), [Alignment Safety](../topics/alignment-safety.md), [Privacy](../topics/privacy.md)

## Contribution and Significance

The contribution is an empirical attack-chain analysis showing how indirect prompt injection can become privacy leakage when agents are allowed to browse and invoke tools. The paper is less about a single jailbreak trick and more about how individually familiar weaknesses compose into a practical exfiltration path.

Its significance is that agent security needs end-to-end controls: instruction-data separation, tool-use policies, URL and network restrictions, and monitoring of multi-step behavior all matter.


## Summary

This paper studies privacy leakage chains in black-box chatbot agents that combine natural-language reasoning with external tools such as web browsing. The threat model is intentionally practical: the attacker does not know the model weights, system prompt, or implementation details, but controls external content that the agent may retrieve. The paper analyzes how indirect prompt injection can hijack the user's intended task and redirect the agent toward an attacker-defined objective.

A central contribution is the "exemplification" prompt-injection technique, which reframes the user prompt and benign beginning of the retrieved page as examples before appending the malicious objective. The paper compares exemplification with fake completion and reports higher attack success in the single-injection experiment. It then demonstrates a proof-of-concept data-exfiltration chain using fictitious personal information and URL query parameters in a controlled setting. The work is important because it treats privacy leakage as a chain spanning external content, instruction steering, jailbreak-like behavior, and tool invocation, rather than as a single unsafe response. Its scope is still limited to controlled experiments and a particular class of black-box chatbot/tool behavior.


## Related Papers

- [Boiling the Frog: A Multi-Turn Benchmark for Agentic Safety](../papers/boiling-the-frog-agentic-safety.md) - 2026-05-22 - The contribution is a stateful multi-turn safety benchmark for agents.
