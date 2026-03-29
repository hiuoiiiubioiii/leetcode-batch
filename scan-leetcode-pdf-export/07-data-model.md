# Data Model

## Row Representation

Each problem:

{
  id,
  title,
  constraints,
  tags,
  derived_patterns,
  composite_patterns
}

## Relationships

Problem → Pattern (many-to-many)
Pattern → Bucket (many-to-one)

## Pipeline

HTML → Parse → Normalize → Pattern Engine → Buckets → Playbook

## Scaling

Designed for thousands of problems (5000+)
