# Retail Analytics Copilot — Summary

- Graph design:
  - Router (rule-based DSPy-lite): decides `rag | sql | hybrid`.
  - Retriever: simple TF-IDF over docs/ (agent/rag/retrieval.py).
  - Planner: extract date ranges and KPI mentions from docs (simple heuristics).
  - NL→SQL: template-based SQL generation (in agent/graph_hybrid.py).
  - Executor: SQLite local queries (agent/tools/sqlite_tool.py).
  - Synthesizer: format enforcement + citations.
  - Repair loop: up to 2 retries on SQL failure or invalid output.

- DSPy module optimized:
  - Router (simple rule-based implementation in `agent/dspy_signatures.py`).
  - Metric (tiny test on 6 eval questions): Router increased correct routing from X → Y (replace X/Y with your observed counts after you run the scripts).

- Assumptions:
  - CostOfGoods ≈ 0.7 * UnitPrice when not available.
  - Using canonical Northwind DB (1997) as provided by assignment.
