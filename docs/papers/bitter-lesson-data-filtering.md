---
title: 'A Bitter Lesson for Data Filtering: Even Synthetic Data From Small Models Can Improve
  Efficient Language Models'
---

# A Bitter Lesson for Data Filtering: Even Synthetic Data From Small Models Can Improve Efficient Language Models

**Link:** [https://arxiv.org/abs/2605.19407](https://arxiv.org/abs/2605.19407)

**Authors:** Haozhe Ji, Arjun S. Majumdar, Marzena Karpinska, Jason Phang, Egor Shelomovskiy, Hanna Mazzawi, Devendra S. Chaplot, Yonatan Bisk, Koustuv Sinha, Rajarshi Das, Danqi Chen, Omer Levy

**Date:** 2026-05-24

**Type:** `paper`

**Primary Topic:** [Data Quality](../topics/data-quality.md)

**Topics:** [Data Quality](../topics/data-quality.md), [Model Architecture](../topics/model-architecture.md)

## Contribution and Significance

The contribution is an empirical scaling argument against treating data filtering as a universal good. In some high-compute regimes, broader data may outperform aggressively filtered subsets.

This matters because agent and model builders often inherit assumptions about "quality" data without checking the scaling regime. The paper argues for measuring the tradeoff directly rather than filtering by intuition alone.


## Summary

This paper challenges the assumption that aggressive quality filtering is always essential for language-model pretraining. It studies data filtering in a high-compute, data-scarce regime and finds that sufficiently trained large-parameter models can tolerate, and sometimes benefit from, data that common filters would label low quality or distracting. The striking claim is that with enough compute, the best filter may be no filter.

The paper uses scaling studies around pretraining data selection and injection, including Common Crawl-style data and filtered alternatives. The discussion is careful about the boundaries of the claim: filtering can still matter when compute is limited, the experiments focus on dense transformer pretraining without curricula or post-training, and questions remain about duplicates, AI-generated content, factuality, and other architectures such as MoEs. The practical message is not that filtering is obsolete, but that the value of filtering depends strongly on compute scale and the role low-quality data may play as signal or regularizer.


## Related Papers

No related entries yet.
