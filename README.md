# Personal Learning & Education Wiki

A unified personal repository for lifelong learning and course notes across multiple academic domains. This is an **educational notes wiki**, not a software project. The notes are written in Markdown, cross-linked using wiki-style links, and compiled into a static website using **MkDocs Material** and deployed via **GitHub Pages**.

**Live Interactive Wiki:** [https://romeo-mhakayakora.github.io/knowledge/](https://romeo-mhakayakora.github.io/knowledge/)

---

## 📚 Course Shortcuts

Use the links below to navigate directly to the course notes inside the repository:

### 1. Mathematics
*   [**Probability Theory**](content/mathematics/probability/) — Comprehensive study of probability spaces, random variables, expectations, named distributions, limit theorems, Markov chains, and Poisson processes.
*   [**Linear Algebra for ML & Quantum**](content/mathematics/linear-algebra-ml-qc/) — Vector spaces, projections, SVD, PCA, Markov transitions, and quantum computing foundations.

### 2. Computer Science
*   [**Distributed Systems**](content/computer-science/distributed-systems/) — P2P networks (Napster/Gnutella), DHTs (Chord/Pastry), logical clocks, election algorithms, consistency models, CAP theorem, Paxos/Raft consensus, and Bitcoin/blockchains.

### 3. Economics
*   [**Game Theory**](content/economics/game-theory/) — Strategic interaction models, game theory proofs, Nash equilibria, and decision science.

---

## 🛠️ Previewing the Wiki Locally

If you want to view or preview the wiki on your local machine, follow these steps:

### Prerequisites
*   Python 3.9+
*   Git

### Setup and Start Server
```bash
# Clone the repository
git clone https://github.com/romeo-mhakayakora/knowledge.git
cd knowledge

# Create and activate a Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install MkDocs and dependencies
pip install -r requirements.txt

# Run the local preview server
mkdocs serve
```

Once the server is running, visit [**http://localhost:8000**](http://localhost:8000) in your web browser.

---

## 🗂️ Repository Structure

```
knowledge/
├── content/                 # All learning content (Markdown files)
│   ├── mathematics/        # Probability, Linear Algebra
│   ├── computer-science/   # Distributed Systems
│   ├── economics/          # Game Theory
│   ├── systems/            # Complex Systems notes
│   └── _concepts/          # Cross-domain concept index files
├── config/                 # YAML Configuration files
├── tools/                  # Build, validation, and automation scripts
├── .github/                # GitHub workflows (automated deployment to Pages)
└── styles/                 # Custom CSS and JS stylesheets
```

---

## ✍️ Contribution & Standards

For details on note standards, file naming rules, and cross-linking using wikilinks `[[concept]]`:
*   See [ARCHITECTURE.md](ARCHITECTURE.md) for the design philosophy.
*   See [GOVERNANCE.md](GOVERNANCE.md) for style and writing standards.
*   See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on formatting.

---

## 📄 License

All content consists of personal learning materials and study notes.
