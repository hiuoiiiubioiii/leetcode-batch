# Composite Pattern Logic

## Problem

Single-label classification is insufficient.

Most LeetCode problems involve:
- multiple techniques
- layered reasoning

## Solution Model

Each problem has:

Primary Pattern
Secondary Pattern
Auxiliary Structures

## Example

Sliding Window + HashMap:

- window defines range
- hashmap maintains frequency

## Overlap Handling

Instead of forcing exclusivity:

Allow:
Problem ∈ Pattern A
Problem ∈ Pattern B
Problem ∈ Pattern C

## Counting Strategy

Two modes:

1. Non-overlapping count (strict)
2. Overlapping count (true coverage)

## Insight

This is why counts like 3873 vs 5478 diverge.
