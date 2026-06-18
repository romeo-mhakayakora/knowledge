# Contributing Guide

## Workflow

### 1. Create Note

Create a markdown file in the appropriate location:

```
content/[domain]/[subject]/[chapter]/note-title.md
```

Example:
```
content/mathematics/probability/01-fundamentals/bayes-theorem.md
```

### 2. Add Frontmatter

Every note must start with YAML frontmatter:

```yaml
---
title: Bayes' Theorem
subject: probability
chapter: 01-fundamentals
tags: [conditional-probability, theorem, fundamental]
date: 2026-01-15
updated: 2026-06-18
status: complete
difficulty: intermediate
prerequisites: [conditional-probability, basic-probability]
related: [conditional-probability-definition, theorem-proof, applications]
references:
  - author: "Sheldon Ross"
    title: "A First Course in Probability"
    year: 2014
---
```

### 3. Write Content

- Use clear, hierarchical headings
- Include examples and intuitions
- Add wikilinks to related concepts: `[[concept-name]]`
- Format equations with LaTeX when needed

### 4. Use Wikilinks

Reference other notes using double brackets:

```markdown
This builds on [[conditional-probability]] and relates to [[bayes-rule]].
```

### 5. Commit and Push

```bash
git add content/
git commit -m "feat: add note on bayes theorem"
git push origin main
```

GitHub Actions will build automatically.

## File Naming

- Use **kebab-case**: `bayes-theorem.md`, not `Bayes' Theorem.md`
- One concept per file
- Descriptive but concise

## Metadata Reference

| Field | Type | Required | Example |
|-------|------|----------|---------|
| `title` | string | ✅ | "Bayes' Theorem" |
| `subject` | string | ✅ | "probability" |
| `chapter` | string | ✅ | "01-fundamentals" |
| `tags` | array | ✅ | `["theorem", "conditional"]` |
| `date` | ISO 8601 | ✅ | "2026-01-15" |
| `updated` | ISO 8601 | ✅ | "2026-06-18" |
| `status` | enum | ✅ | "complete" |
| `difficulty` | enum | ✅ | "intermediate" |
| `prerequisites` | array | ⚠️ | `["concept1", "concept2"]` |
| `related` | array | ⚠️ | `["concept1", "concept2"]` |
| `references` | array | ⚠️ | See example |
| `hide` | boolean | | `false` |

### Status Values
- `draft` — Work in progress, not ready to publish
- `in-progress` — Being actively worked on
- `complete` — Finished and reviewed
- `review` — Ready for peer review

### Difficulty Levels
- `beginner` — No prerequisites, foundational
- `intermediate` — Requires domain basics
- `advanced` — Requires deep domain knowledge

## Directory Structure Rules

### Subject Level
```
content/[domain]/[subject]/
├── README.md                      # Subject overview
├── _subject.yml                   # Subject metadata
├── 01-chapter-name/              # Ordered chapter folder
│   ├── README.md                 # Chapter overview
│   ├── _chapter.yml              # Chapter metadata
│   ├── concept1.md               # Individual concept
│   └── concept2.md               # Individual concept
├── 02-another-chapter/
└── concepts/                      # Optional: subject-specific index
    └── README.md
```

### Naming Convention
- Chapter folders: `01-name`, `02-name` (enforces ordering)
- Metadata files: `_subject.yml`, `_chapter.yml` (groups and hides from nav)
- Content files: `kebab-case.md` (clear, searchable)

## Templates

### Note Template

```yaml
---
title: [Your Title]
subject: [subject-slug]
chapter: [01-chapter-name]
tags: [tag1, tag2, tag3]
date: 2026-06-18
updated: 2026-06-18
status: draft
difficulty: intermediate
prerequisites: []
related: []
references: []
---

# [Your Title]

## Overview

[Brief introduction]

## Key Concepts

[Main content]

### Example

[Worked example]

## Related

- [[linked-concept-1]]
- [[linked-concept-2]]

## References

[Full reference list]
```

### Chapter Overview Template

```markdown
---
title: Chapter Name
subject: subject-slug
---

# Chapter Name

[Chapter overview and learning objectives]

## Contents

1. [[concept-1]]
2. [[concept-2]]
3. [[concept-3]]

## Learning Outcomes

- [ ] Outcome 1
- [ ] Outcome 2
```

## Best Practices

1. **One concept per file** — Don't cram multiple concepts into one file
2. **Link liberally** — Use wikilinks to create knowledge network
3. **Include examples** — Concrete examples aid understanding
4. **Write clearly** — Assume reader has domain basics but not specific topic knowledge
5. **Update dates** — Keep `updated` field current
6. **Build locally first** — Test with `mkdocs serve` before pushing
7. **Tag thoughtfully** — Tags enable cross-domain discovery
8. **Reference sources** — Always cite sources in references section

## Local Testing

```bash
# Activate venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Serve locally
mkdocs serve

# Build site
mkdocs build
```

Visit `http://localhost:8000` to preview changes before committing.

## Troubleshooting

### Build fails
```bash
# Rebuild dependencies
pip install -r requirements.txt --upgrade
```

### Broken links
Check the GitHub Actions build log for broken wikilinks.

### Search not working
Clear browser cache and rebuild:
```bash
mkdocs build --clean
```

## Questions?

See [ARCHITECTURE.md](ARCHITECTURE.md) for system design details.
