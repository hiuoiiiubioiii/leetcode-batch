# Implementation Plan

## Objective

Turn the LeetCode master artifact into a machine-usable dataset and then classify each row into:
- raw tags
- derived patterns
- composite patterns
- strategy buckets

## Pipeline

1. Source acquisition
   - read `master.html`
   - preserve original row structure

2. Parsing
   - detect tables, cards, or repeated row-like blocks
   - normalize headers
   - emit JSONL / JSON rows

3. Feature extraction
   - title
   - difficulty
   - text tags
   - inferred signals from statements and constraints

4. Pattern inference
   - primary pattern
   - secondary pattern
   - auxiliary structures
   - composite pattern(s)

5. Validation
   - row counts
   - missing columns
   - duplicate IDs / titles
   - overlap counting modes

6. Export
   - normalized JSON
   - bucket summaries
   - playbook-ready grouped outputs
