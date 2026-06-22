# AI Research Radar

AI Research Radar is a static GitHub Pages site for tracking and summarizing AI research papers, frameworks, benchmarks, models, and major product releases.

The source of truth is `data/papers.yaml`. Generated Markdown pages live under `docs/` and are built with MkDocs Material.

## Requirements

- Python 3.12
- GitHub Pages enabled for GitHub Actions deployment

## Local Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/generate_site.py
mkdocs serve
```

Open the local MkDocs URL shown by `mkdocs serve`.

## Add Content

Add entries to `data/papers.yaml`:

```yaml
papers:
  - id: example-paper
    title: Example Paper
    url: https://example.com
    authors:
      - Researcher One
    date: 2026-06-22
    type: paper
    primary_topic: agent-evals
    topics:
      - agents
      - agent-evals
    summary: Short summary of the work.
    takeaway: One-line explanation of why it matters.
    status: unread
```

Supported `type` values:

- `paper`
- `framework`
- `benchmark`
- `model`
- `product-release`

Supported `status` values:

- `unread`
- `reviewed`

`primary_topic` controls where the paper is grouped in weekly digests. It must also appear in `topics`.

Current topic slugs:

- `agents`
- `agent-memory`
- `agent-evals`
- `agent-systems`
- `agent-security`
- `multi-agent-systems`
- `llm-reasoning`
- `world-models`
- `behavior-forecasting`
- `self-improvement`
- `data-quality`
- `reinforcement-learning`
- `game-theory`
- `evals`
- `alignment-safety`
- `privacy`
- `model-architecture`
- `ai-infra`
- `open-source-models`
- `product-release`

## Generate Pages

```bash
python scripts/generate_site.py
```

The generator creates:

- Individual paper pages in `docs/papers/`
- Topic pages in `docs/topics/`
- Weekly digest pages in `docs/weekly/`
- MkDocs navigation in `mkdocs.yml`
- Homepage sections for the latest weekly digest, recent papers, and top topics

Weekly digests are generated from the `date` field. The script groups entries by ISO calendar week and writes pages such as `docs/weekly/2026-week-26.md`. Publishing happens when the generated files are committed and pushed to `main`, which triggers the GitHub Pages workflow.

## Build

```bash
mkdocs build --strict
```

## Deployment

The workflow at `.github/workflows/deploy.yml` builds and deploys the site to GitHub Pages on every push to `main`.

Before deploying, update `site_url` and `repo_url` in `mkdocs.yml` to match your GitHub repository.
