#!/usr/bin/env python3
"""Generate AI Research Radar pages from data/papers.yaml."""

from __future__ import annotations

import datetime as dt
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "papers.yaml"
DOCS_DIR = ROOT / "docs"
PAPERS_DIR = DOCS_DIR / "papers"
TOPICS_DIR = DOCS_DIR / "topics"
WEEKLY_DIR = DOCS_DIR / "weekly"
MKDOCS_FILE = ROOT / "mkdocs.yml"

TAXONOMY = [
    "agents",
    "llm-reasoning",
    "evals",
    "alignment-safety",
    "medical-ai",
    "multimodal",
    "vision",
    "rag",
    "code-agents",
    "inference",
    "model-architecture",
    "ai-infra",
    "open-source-models",
    "product-release",
]


def main() -> None:
    papers = load_papers()
    clean_generated_dirs()
    generate_paper_pages(papers)
    generate_topic_pages(papers)
    weekly_pages = generate_weekly_pages(papers)
    update_homepage(papers, weekly_pages)
    update_mkdocs_nav(papers, weekly_pages)
    print(f"Generated {len(papers)} paper pages, {len(weekly_pages)} weekly digests, and topic pages.")


def load_papers() -> list[dict[str, Any]]:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Missing data file: {DATA_FILE}")

    payload = yaml.safe_load(DATA_FILE.read_text(encoding="utf-8")) or {}
    papers = payload.get("papers", [])
    if not isinstance(papers, list):
        raise ValueError("data/papers.yaml must contain a top-level 'papers' list")

    seen: set[str] = set()
    for paper in papers:
        validate_paper(paper, seen)
        paper["date"] = parse_date(paper["date"])
        paper["topics"] = sorted(set(paper["topics"]), key=lambda topic: TAXONOMY.index(topic) if topic in TAXONOMY else 999)

    return sorted(papers, key=lambda item: item["date"], reverse=True)


def validate_paper(paper: dict[str, Any], seen: set[str]) -> None:
    required = {"id", "title", "url", "authors", "date", "type", "topics", "summary", "takeaway", "status"}
    missing = required - set(paper)
    if missing:
        raise ValueError(f"Paper entry is missing fields {sorted(missing)}: {paper!r}")

    if paper["id"] in seen:
        raise ValueError(f"Duplicate paper id: {paper['id']}")
    seen.add(paper["id"])

    if paper["type"] not in {"paper", "framework", "benchmark", "model", "product-release"}:
        raise ValueError(f"Invalid type for {paper['id']}: {paper['type']}")
    if paper["status"] not in {"unread", "reviewed"}:
        raise ValueError(f"Invalid status for {paper['id']}: {paper['status']}")
    if not isinstance(paper["authors"], list) or not paper["authors"]:
        raise ValueError(f"authors must be a non-empty list for {paper['id']}")
    if not isinstance(paper["topics"], list) or not paper["topics"]:
        raise ValueError(f"topics must be a non-empty list for {paper['id']}")


def parse_date(value: Any) -> dt.date:
    if isinstance(value, dt.date):
        return value
    return dt.date.fromisoformat(str(value))


def clean_generated_dirs() -> None:
    for directory in (PAPERS_DIR, TOPICS_DIR, WEEKLY_DIR):
        if directory.exists():
            shutil.rmtree(directory)
        directory.mkdir(parents=True, exist_ok=True)


def generate_paper_pages(papers: list[dict[str, Any]]) -> None:
    by_topic = index_by_topic(papers)
    for paper in papers:
        related = [
            candidate
            for topic in paper["topics"]
            for candidate in by_topic[topic]
            if candidate["id"] != paper["id"]
        ]
        deduped_related = unique_by_id(related)[:5]
        body = [
            f"---\ntitle: {yaml.safe_dump(paper['title']).strip()}\n---",
            f"# {paper['title']}",
            f"**Link:** [{paper['url']}]({paper['url']})",
            f"**Authors:** {', '.join(paper['authors'])}",
            f"**Date:** {paper['date'].isoformat()}",
            f"**Type:** `{paper['type']}`",
            f"**Status:** `{paper['status']}`",
            f"**Topics:** {topic_links(paper['topics'])}",
            "## Takeaway",
            paper["takeaway"],
            "## Summary",
            paper["summary"],
            "## Related Papers",
        paper_list(deduped_related) if deduped_related else "No related entries yet.",
        ]
        write_page(PAPERS_DIR / f"{paper['id']}.md", "\n\n".join(body))


def generate_topic_pages(papers: list[dict[str, Any]]) -> None:
    by_topic = index_by_topic(papers)
    for topic in TAXONOMY:
        topic_papers = by_topic.get(topic, [])
        body = [
            f"---\ntitle: {titleize(topic)}\n---",
            f"# {titleize(topic)}",
            f"{len(topic_papers)} tracked entr{'y' if len(topic_papers) == 1 else 'ies'} for this topic.",
            "## Entries",
            paper_list(topic_papers) if topic_papers else "No entries yet.",
        ]
        write_page(TOPICS_DIR / f"{topic}.md", "\n\n".join(body))


def generate_weekly_pages(papers: list[dict[str, Any]]) -> list[dict[str, str]]:
    by_week: dict[tuple[int, int], list[dict[str, Any]]] = defaultdict(list)
    for paper in papers:
        iso = paper["date"].isocalendar()
        by_week[(iso.year, iso.week)].append(paper)

    weekly_pages: list[dict[str, str]] = []
    for (year, week), week_papers in sorted(by_week.items(), reverse=True):
        slug = f"{year}-week-{week:02d}"
        grouped = group_by_primary_topic(week_papers)
        topic_counts = Counter(topic for paper in week_papers for topic in paper["topics"])
        trends = [
            f"- **{titleize(topic)}:** {count} entr{'y' if count == 1 else 'ies'}"
            for topic, count in topic_counts.most_common(5)
        ]
        sections = []
        for topic, topic_papers in grouped.items():
            sections.extend([f"### {titleize(topic)}", paper_list(topic_papers)])

        body = [
            f"---\ntitle: {year} Week {week:02d}\n---",
            f"# {year} Week {week:02d}",
            "## Key Trends",
            "\n".join(trends) if trends else "No trend data yet.",
            "## Papers Published This Week",
            "\n\n".join(sections) if sections else "No entries for this week.",
        ]
        write_page(WEEKLY_DIR / f"{slug}.md", "\n\n".join(body))
        weekly_pages.append({"title": f"{year} Week {week:02d}", "path": f"weekly/{slug}.md", "slug": slug})

    return weekly_pages


def update_homepage(papers: list[dict[str, Any]], weekly_pages: list[dict[str, str]]) -> None:
    recent = papers[:5]
    topic_counts = Counter(topic for paper in papers for topic in paper["topics"])
    latest_week = weekly_pages[0] if weekly_pages else None
    body = [
        "---\ntitle: AI Research Radar\n---",
        "# AI Research Radar",
        "Track and summarize AI research papers, frameworks, benchmarks, models, and major product releases from a YAML source of truth.",
        "## Latest Weekly Digest",
        f"[{latest_week['title']}]({latest_week['path']})" if latest_week else "No weekly digest generated yet.",
        "## Search",
        "Use the search field in the site header to find papers, topics, authors, summaries, and takeaways.",
        "## Recent Papers",
        paper_list(recent, link_prefix="papers"),
        "## Top Topics",
        "\n".join(
            f"- [{titleize(topic)}](topics/{topic}.md) ({count})"
            for topic, count in topic_counts.most_common(8)
        ),
    ]
    write_page(DOCS_DIR / "index.md", "\n\n".join(body))


def update_mkdocs_nav(papers: list[dict[str, Any]], weekly_pages: list[dict[str, str]]) -> None:
    text = MKDOCS_FILE.read_text(encoding="utf-8")
    nav = ["nav:", "  - Home: index.md"]
    if weekly_pages:
        nav.append("  - Weekly Digests:")
        for page in weekly_pages:
            nav.append(f"      - {page['title']}: {page['path']}")
    nav.append("  - Papers:")
    for paper in papers:
        nav.append(f"      - {quote_nav_title(paper['title'])}: papers/{paper['id']}.md")
    nav.append("  - Topics:")
    for topic in TAXONOMY:
        nav.append(f"      - {titleize(topic)}: topics/{topic}.md")

    generated = "# BEGIN GENERATED NAV\n" + "\n".join(nav) + "\n# END GENERATED NAV"
    updated = re.sub(
        r"# BEGIN GENERATED NAV\n.*?\n# END GENERATED NAV",
        generated,
        text,
        flags=re.DOTALL,
    )
    if updated == text and "# BEGIN GENERATED NAV" not in text:
        updated = text.rstrip() + "\n\n" + generated + "\n"
    MKDOCS_FILE.write_text(updated, encoding="utf-8")


def index_by_topic(papers: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    by_topic: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for paper in papers:
        for topic in paper["topics"]:
            by_topic[topic].append(paper)
    return by_topic


def group_by_primary_topic(papers: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for paper in sorted(papers, key=lambda item: item["date"], reverse=True):
        grouped[paper["topics"][0]].append(paper)
    return dict(sorted(grouped.items(), key=lambda item: TAXONOMY.index(item[0]) if item[0] in TAXONOMY else 999))


def unique_by_id(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    unique: list[dict[str, Any]] = []
    for paper in papers:
        if paper["id"] not in seen:
            unique.append(paper)
            seen.add(paper["id"])
    return unique


def paper_list(papers: list[dict[str, Any]], link_prefix: str = "../papers") -> str:
    return "\n".join(
        f"- [{paper['title']}]({link_prefix}/{paper['id']}.md) - {paper['date'].isoformat()} - {paper['takeaway']}"
        for paper in papers
    )


def topic_links(topics: list[str]) -> str:
    return ", ".join(f"[{titleize(topic)}](../topics/{topic}.md)" for topic in topics)


def titleize(slug: str) -> str:
    return slug.replace("-", " ").title().replace("Ai", "AI").replace("Llm", "LLM").replace("Rag", "RAG")


def quote_nav_title(title: str) -> str:
    return yaml.safe_dump(title, default_style='"').strip()


def write_page(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
