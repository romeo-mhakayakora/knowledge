
# Random Variables

> *Introduction to Probability* — Blitzstein & Hwang

---

## Definition and Core Insight

> **Definition 3.1.1** — A *random variable* (r.v.) is a **function** from the sample space $S$ to the real numbers $\mathbb{R}$:
> $$X : S \rightarrow \mathbb{R}, \quad s \mapsto X(s)$$

A random variable assigns a fixed numerical value to every possible outcome. It is **deterministic** — for a given outcome $s$, $X(s)$ is always the same fixed value. The randomness lives in *which outcome gets selected*, not in $X$ itself.

**Pebble world picture:** Each pebble (outcome) in the sample space gets stamped with a number by $X$. The event $\{X = 7\}$ is not an equation to solve — it is the *set of all pebbles stamped with the number 7*. It is a legitimate event, so it has a probability. This means expressions like $P(X = k)$, $P(X \leq x)$, $P(a < X \leq b)$ are all well-defined probabilities of events.

| Component | Role |
|-----------|------|
| Random variable $X$ | Deterministic function — gives each outcome a fixed number |
| Probability function $P$ | Source of randomness — assigns weights to outcomes |

Think of $X$ as a rating machine: it gives each outcome a fixed score. $P$ decides how often each score shows up.

> **The pipeline from your own reasoning:** You have a school with students and bags. $X$ = number of bags is a fully known, deterministic function. The randomness comes from *which student gets picked* — that is where $P$ lives. $X$ just reads off the bag count once the student is selected.

---

### Example 3.1.2 — Two Coin Tosses

Sample space: $S = \{HH, HT, TH, TT\}$

Three random variables defined on this experiment:

| R.V. | Formula | What it measures |
|------|---------|-----------------|
| $X$ | $s_1 + s_2$ | Number of Heads |
| $Y$ | $2 - s_1 - s_2$ | Number of Tails ($Y = 2 - X$) |
| $I$ | $s_1$ | Result of the first flip only |

$I$ is an **indicator random variable** — it equals 1 if the first toss is Heads, 0 otherwise.

> ⚠️ **Critical distinction — RV ≠ Distribution:**
> Multiple random variables (e.g., $X_1, X_2, \ldots, X_n$ for $n$ coin tosses) can be *different* random variables — each depending on a different trial — yet all *share* the same distribution. The distribution is the blueprint (what are the probabilities?); the random variable is a specific instance of randomness (what actually happened on trial $j$?).

---

## Discrete vs Continuous Random Variables

**Discrete:** X can only take a countable list of values — finite or countably infinite. Most commonly integers.

**Continuous:** X can take any real value in an interval. Between any two values there are infinitely many more — you can never write a complete list.

> **Always ask this first before anything else.** Everything that follows — which tools to use, how to compute probabilities — depends on this answer.

| | Discrete | Continuous |
|---|---|---|
| Values | Countable list | Any value in an interval |
| Primary tool | PMF | PDF (later in course) |
| Universal tool | CDF | CDF |
| Example | Number of bags | Height of a student |
| $P(X = x)$ | Can be positive | Always 0 for any single point |
| Gaps between values? | Yes | No |

> Discrete = you can **count** the possibilities. Continuous = you can **measure** the possibilities.

Hybrid RVs (partly discrete, partly continuous) also exist — if you understand both types separately, you can handle hybrids too.

---

## The Support of a Random Variable

> **Definition:** The *support* of a discrete r.v. $X$ is the set of all values $x$ such that $P(X = x) > 0$.

Formally: $\text{Support of } X = \{x : P(X = x) > 0\}$

Only values where X can actually land with nonzero probability belong to the support. Values outside the support have probability exactly 0 — X can never land there.

> **Your lecturer analogy:** The support is the set of chairs in the room. The lecturer (X) will always sit on one of the chairs. The probability of the lecturer sitting on the ceiling = 0 because the ceiling is not in the support.

A random variable X is **discrete** if its support is a finite or countably infinite list $\{a_1, a_2, \ldots\}$ such that $P(X = a_j \text{ for some } j) = 1$.
