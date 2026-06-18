# Welcome to Knowledge Base

A unified repository for lifelong learning across multiple domains.

## 🎯 Purpose

This knowledge base is designed to:
- **Organize learning** across 10+ domains systematically
- **Build connections** between concepts through wikilinks
- **Enable discovery** with full-text search and tags
- **Scale sustainably** as learning continues 5+ years

## 📚 Domains

### [Mathematics](domains/mathematics.md)
Probability, linear algebra, optimization, analysis, statistics

### [Computer Science](domains/computer-science.md)
Algorithms, operating systems, distributed systems, databases, networks

### [AI & Machine Learning](domains/ai.md)
Deep learning, NLP, computer vision, reinforcement learning, LLMs

### [Economics](domains/economics.md)
Microeconomics, macroeconomics, econometrics

### [Physics](domains/physics.md)
Classical mechanics, quantum mechanics, thermodynamics

### [Systems](domains/systems.md)
Complex systems, network science, emergence

### [Business](domains/business.md)
Strategy, finance, management, organization

## 🔍 Navigation

- **Search** — Type `/` to search across all concepts
- **Wikilinks** — Click concepts to explore related ideas
- **Tags** — Browse by topic across domains
- **Domains** — Start from a high-level area

## 📝 How to Use

### For Learning
1. Pick a domain that interests you
2. Explore subject by subject
3. Follow wikilinks to deepen understanding
4. Use search to find specific concepts

### For Contributing
1. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
2. Follow the frontmatter template
3. Use wikilinks liberally
4. Push to GitHub — GitHub Actions will build automatically

## 🏗️ Architecture

This repository is built with:
- **MkDocs Material** for beautiful, responsive documentation
- **GitHub Pages** for free static hosting
- **GitHub Actions** for automated deployment
- **Markdown + YAML** for version-controlled content

See [ARCHITECTURE.md](ARCHITECTURE.md) for design philosophy and technical details.

## 📋 Quick Facts

| Metric | Value |
|--------|-------|
| **Domains** | 7 |
| **Framework** | MkDocs Material |
| **Hosting** | GitHub Pages |
| **Deployment** | Automated via GitHub Actions |
| **Content Format** | Markdown + YAML frontmatter |
| **Building Block** | One concept per file |
| **Scale Target** | 1000+ notes |
| **Maintenance** | Quarterly reviews, annual audits |

## 🚀 Getting Started

### Local Development
```bash
# Clone repository
git clone https://github.com/romeo-mhakayakora/knowledge.git
cd knowledge

# Setup environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Preview locally
mkdocs serve
```

### Add Your First Note
```bash
# Create file in appropriate domain/subject/chapter
content/mathematics/probability/01-fundamentals/bayes-theorem.md

# Add frontmatter and content following CONTRIBUTING.md

# Push to GitHub
git add .
git commit -m "feat: add bayes theorem note"
git push
```

## 📖 Standards

| Aspect | Standard |
|--------|----------|
| **File naming** | `kebab-case.md` |
| **Concepts per file** | One concept only |
| **Organization** | domain/subject/01-chapter/concept.md |
| **Linking** | Wikilinks: `[[concept-name]]` |
| **Metadata** | YAML frontmatter required |

## 🔗 Useful Links

- [ARCHITECTURE.md](ARCHITECTURE.md) — System design and principles
- [CONTRIBUTING.md](CONTRIBUTING.md) — How to add content
- [GOVERNANCE.md](GOVERNANCE.md) — Standards and review process
- [GitHub Repository](https://github.com/romeo-mhakayakora/knowledge)

---

**Last updated:** June 18, 2026
