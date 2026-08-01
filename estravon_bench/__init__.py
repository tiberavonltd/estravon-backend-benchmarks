"""Apples-to-apples PDF-to-Markdown engine comparison for estravon-backend

Modules:

- `estravon_bench.client`: Thin HTTP client for one `estravon-backend` instance, plus local-subprocess orchestration -- one process per engine, since each running `estravon-backend` instance is pinned to a single engine (see its own docs) and this package is what drives several of them side by side for a comparison.
- `estravon_bench.compare`: Fan out one PDF across N engines and collect a `ComparisonResultList`. Two modes: spawn local pinned instances (Mode A), or point at a pre-existing `{engine: url}` map of already-running instances (Mode B).
- `estravon_bench.overhead`: Separating fixed per-request overhead from real per-page processing time, by measuring at several page counts instead of just one.
- `estravon_bench.saas_probe`: Free-by-default reachability/quota probes for Mistral, Datalab, and Replicate -- for answering "is it them or is it me" before trusting a `compare()` run against an engine that's behaving strangely."""

__version__ = "0.1.0"
