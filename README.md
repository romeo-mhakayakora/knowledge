# Knowledge Management System

A unified repository for lifelong learning across multiple domains. Built with MkDocs Material and GitHub Pages.

**Live Site:** https://romeo-mhakayakora.github.io/knowledge/

## Quick Start

### Prerequisites
- Python 3.9+
- Git

### Setup

```bash
# Clone and navigate
git clone https://github.com/romeo-mhakayakora/knowledge.git
cd knowledge

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Preview locally
mkdocs serve
```

Visit `http://localhost:8000` to preview.

## Directory Structure

```
knowledge/
├── content/                 # All learning content (markdown files)
│   ├── mathematics/        # Domain
│   ├── computer-science/   # Domain
│   ├── ai/                 # Domain
│   └── _concepts/          # Cross-domain concepts
├── docs/                   # GitHub Pages source
├── config/                 # Configuration files
├── tools/                  # Build and automation scripts
├── .github/                # GitHub workflows and templates
└── styles/                 # Custom CSS/JS
```

## Adding Content

1. **Create note in appropriate location:**
   ```bash
   content/[domain]/[subject]/[chapter]/note-name.md
   ```

2. **Add frontmatter:**
   ```yaml
   ---
   title: Note Title
   subject: subject-slug
   chapter: 01-chapter-name
   tags: [tag1, tag2]
   date: 2026-01-15
   updated: 2026-06-18
   status: complete
   difficulty: intermediate
   ---
   ```

3. **Write content and use wikilinks:**
   ```markdown
   This relates to [[concept-name]] and [[another-concept]].
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "feat: add note on [topic]"
   git push
   ```

GitHub Actions will automatically build and deploy.

## Domains

- **Mathematics:** Probability, linear algebra, optimization, analysis, statistics
- **Computer Science:** Algorithms, operating systems, distributed systems, databases, networks
- **AI:** Deep learning, NLP, computer vision, reinforcement learning, LLMs
- **Economics:** Microeconomics, macroeconomics, econometrics
- **Physics:** Classical mechanics, quantum mechanics, thermodynamics
- **Systems:** Complex systems, network science
- **Business:** Strategy, finance, organization

## Standards

| Item | Standard |
|------|----------|
| File naming | `kebab-case.md` |
| Concepts per file | One concept per file |
| Metadata | YAML frontmatter required |
| Cross-linking | Use wikilinks `[[concept]]` |
| Chapter folders | Numbered: `01-name`, `02-name` |
| Metadata files | Prefixed: `_subject.yml`, `_chapter.yml` |

## Maintenance

| Frequency | Task |
|-----------|------|
| Weekly | Review PRs, check broken links |
| Monthly | Audit files, update index |
| Quarterly | Archive chapters, review outcomes |
| Annually | Full audit, update framework |

## License

All content is personal learning material.

## See Also

- [ARCHITECTURE.md](ARCHITECTURE.md) — System design and philosophy
- [CONTRIBUTING.md](CONTRIBUTING.md) — Detailed contribution guide
- [GOVERNANCE.md](GOVERNANCE.md) — Policies and standards
