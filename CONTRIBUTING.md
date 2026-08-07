# Contributing to estravon-backend-benchmarks

This package drives a running `estravon-backend` instance over HTTP (`httpx` only — see
`pyproject.toml`'s `dependencies`); it never imports or requires `estravon-backend`'s own
source. That separation keeps the review bar here focused on **"is this a good comparison?"**
rather than anything about `estravon-backend`'s own internals.

## What kinds of contributions fit here

- New scoring metrics (`score.py`) — TEDS, CER/edit-distance, formula
  metrics — reused from established literature, not invented from scratch.
- Benchmark-harness adapters (`omnidocbench.py` and similar) — mapping a
  standard benchmark's page/document format into `compare()`'s inputs and
  its scorer format.
- Reporting/rendering improvements (`report.py`) — better tables, more useful
  diffs, notebook-friendly output.
- Test-axis additions that reflect a real, documented architectural difference between
  engines — for example: text-layer-present vs. scanned/no-text-layer, formula/table
  density, marginalia (headers/footers/page numbers/footnotes) handling, inline-formatting
  fidelity, numeric/digit accuracy, and language/script coverage.

## Development

This package is authored with [nbdev](https://nbdev.fast.ai/) — the
notebooks under `nbs/` are the source of truth; `estravon_bench/*.py` is
generated from them via `nbdev-export`, not hand-edited. If you're new to
nbdev's workflow (the `#| export`/`#| hide` cell directives, the
edit-notebook-then-`nbdev-export` loop), read nbdev's own docs first — the
audience for this package is exactly the crowd that already values that
workflow, so we lean into it rather than working around it.

```bash
pip install -e ".[dev]"
nbdev-install-hooks   # keeps notebook diffs clean (strips outputs on commit)

# after editing a notebook under nbs/:
nbdev-export           # regenerate estravon_bench/*.py
nbdev-test              # run every notebook's cells as tests
```

nbdev 3.x only ships hyphenated console scripts (`nbdev-export`, not
`nbdev_export`) — if a command isn't found, that's the usual reason.

## Scope reminder

This is an evaluation aid for comparing engines on your own PDFs apples-to-apples, just this, not a
leaderboard. 