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
    topics:
      - agents
      - evals
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

## Build

```bash
mkdocs build --strict
```

## Deployment

The workflow at `.github/workflows/deploy.yml` builds and deploys the site to GitHub Pages on every push to `main`.

Before deploying, update `site_url` and `repo_url` in `mkdocs.yml` to match your GitHub repository.
