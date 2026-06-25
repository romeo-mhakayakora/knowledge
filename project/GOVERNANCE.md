# Governance & Standards

## Content Standards

### File Organization

**Rule**: One concept per markdown file, numbered chapters.

```
subject/
├── 01-chapter-name/
│   ├── concept-1.md
│   ├── concept-2.md
│   └── README.md
├── 02-chapter-name/
│   ├── concept-3.md
│   ├── concept-4.md
│   └── README.md
```

### Naming Conventions

| Item | Rule | Example |
|------|------|---------|
| Files | kebab-case | `bayes-theorem.md` |
| Folders | kebab-case or numbered | `01-fundamentals` |
| Metadata | underscore prefix | `_subject.yml` |
| Links | wikilink format | `[[concept-name]]` |

### Frontmatter Requirements

**Mandatory fields:**
- `title` — Clear, descriptive page title
- `subject` — Subject slug (lowercase, kebab-case)
- `chapter` — Chapter folder name
- `tags` — Array of searchable keywords
- `date` — Creation date (ISO 8601)
- `updated` — Last update date (ISO 8601)
- `status` — One of: draft, in-progress, complete, review
- `difficulty` — One of: beginner, intermediate, advanced

**Recommended fields:**
- `prerequisites` — Array of prerequisite concepts
- `related` — Array of related concepts
- `references` — Array of source citations

## Content Quality

### Completeness Status

| Status | Meaning | When |
|--------|---------|------|
| `draft` | Skeleton written | Initial creation |
| `in-progress` | Content being written | Active development |
| `complete` | Ready for others | Finished and proofread |
| `review` | Awaiting feedback | Ready for peer review |

### Difficulty Levels

| Level | Audience | Prerequisites |
|-------|----------|---|
| `beginner` | Anyone | None, foundational |
| `intermediate` | Domain familiar | Domain basics required |
| `advanced` | Deep practitioners | Significant domain knowledge |

## Review Process

### Pull Request Checklist

- [ ] Frontmatter complete (title, subject, tags, status)
- [ ] Content is clear and well-structured
- [ ] Wikilinks to related concepts included
- [ ] References cited where applicable
- [ ] No broken links to other concepts
- [ ] File in correct location (`content/domain/subject/chapter/`)
- [ ] File name is kebab-case
- [ ] One concept per file

### Acceptance Criteria

- Content is original or properly attributed
- Writing is clear and accessible
- Metadata is complete
- No duplicate concepts across repository
- Links are valid

## Maintenance Schedule

### Weekly
- Review PRs and merged changes
- Check for broken links (GitHub Actions)
- Update tags if needed

### Monthly
- Audit frontmatter completeness
- Update file dates where relevant
- Validate cross-references

### Quarterly
- Archive outdated chapters
- Review learning outcomes
- Assess domain coverage gaps
- Update statistics

### Annually
- Full repository audit
- Update framework documentation
- Plan next year's learning goals
- Assess tool effectiveness

## Validation Rules

### Automatic Checks (GitHub Actions)

- [ ] Frontmatter syntax valid YAML
- [ ] Required fields present
- [ ] Wikilinks reference valid files
- [ ] File naming conventions followed
- [ ] Directory structure valid
- [ ] No duplicate concept names

### Manual Review

- Content clarity and accuracy
- Alignment with subject learning outcomes
- Quality of examples and explanations
- Proper citation of sources

## Domain Definitions

### Domains

| Domain | Purpose | Key Subjects |
|--------|---------|---|
| **Mathematics** | Foundational mathematical thinking | Probability, linear algebra, optimization |
| **Computer Science** | Computing fundamentals | Algorithms, systems, databases |
| **AI** | Artificial intelligence & ML | Deep learning, NLP, computer vision |
| **Economics** | Economic principles | Micro, macro, econometrics |
| **Systems** | Complex adaptive systems | Networks, emergence, chaos |


Each domain:
- Has its own folder under `content/`
- Contains a `_domain.yml` metadata file
- Has a `README.md` overview
- Organizes knowledge into subjects
- Maintains independent taxonomy

### Subject Structure

Each subject:
- Lives in `content/[domain]/[subject]/`
- Has `_subject.yml` metadata
- Has `README.md` overview
- Organizes chapters sequentially
- Defines learning outcomes
- Lists prerequisites and resources

## Cross-Domain Linking

### Concepts Folder

Truly cross-domain concepts live in `content/_concepts/`:
- `information-theory.md` — Relevant to AI, CS, Economics
- `optimization.md` — Used in multiple domains
- `graph-theory.md` — Foundation for CS, Networks, AI
- `time-series.md` — Economics, Systems

### Linking Strategy

**Within domain:**
```markdown
[[related-concept-in-same-subject]]
```

**Across domain:**
```markdown
[[concept-name-in-concepts]] (see _concepts)
```

**External:**
```markdown
[Link text](https://example.com)
```

## Version Control

### Commit Messages

Format: `type: brief description`

Types:
- `feat:` — New concept or feature
- `fix:` — Correction or broken link fix
- `docs:` — Documentation updates
- `refactor:` — Reorganization
- `chore:` — Maintenance tasks

Examples:
```
feat: add bayes theorem note
fix: correct probability definition link
docs: update contributing guide
```

### Branching

- `main` — Deployed content
- `develop` — Work in progress
- Feature branches: `feature/domain-subject` — Specific additions

## Governance Review

This governance document is reviewed:
- Quarterly for policy changes
- Annually for framework updates
- As needed for new domains

Suggestions and feedback welcome via issues.
