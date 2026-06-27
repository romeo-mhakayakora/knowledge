

## Table of Contents

1. [Why Random Variables?](#why-random-variables)
2. [Definition and Core Insight](#definition-and-core-insight)
3. [Discrete vs Continuous Random Variables](#discrete-vs-continuous-random-variables)
4. [The Support of a Random Variable](#the-support-of-a-random-variable)
5. [The Probability Mass Function (PMF)](#the-probability-mass-function-pmf)
6. [The PMF Pipeline](#the-pmf-pipeline)
7. [Named Distributions](#named-distributions)
   - [Bernoulli](#bernoulli-distribution)
   - [Binomial — Three Lenses](#binomial-distribution)
   - [Hypergeometric](#hypergeometric-distribution)
   - [Discrete Uniform](#discrete-uniform-distribution)
8. [When Things Are NOT Binomial](#when-things-are-not-binomial)
9. [Cumulative Distribution Functions (CDF)](#cumulative-distribution-functions-cdf)
10. [Functions of Random Variables](#functions-of-random-variables)
11. [Independence of Random Variables](#independence-of-random-variables)
12. [Sum of Independent Binomials — Three Proofs](#sum-of-independent-binomials)
13. [Connections Between Binomial and Hypergeometric](#connections-between-binomial-and-hypergeometric)
14. [Big Picture Flowchart](#big-picture-flowchart)
15. [Summary Cheatsheet](#summary-cheatsheet)

---

# Why Random Variables?

Standard probability notation gets unwieldy fast. For example, in the Gambler's Ruin problem, tracking exact amounts using event notation like $A_{jk}$ and $B_{jk}$ becomes a long, tangled string of unions and intersections.

The fix: random variables let us work with *numbers* instead of raw events — unlocking clean algebra and compact notation.

> "Instead of having convoluted notation that obscures how the quantities of interest are related, wouldn't it be nice if we could say something like: Let $X_k$ be the wealth of gambler A after $k$ rounds..."

Random variables also let us simplify a complex sample space. The sample space of an experiment is often incredibly complicated or high-dimensional, and the outcomes $s \in S$ may be non-numeric. A random variable maps those messy outcomes to numbers — so we can do mathematics on them.

---

# Definition and Core Insight

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

# Discrete vs Continuous Random Variables

**Discrete:** X can only take a countable list of values — finite or countably infinite. Most commonly integers.

**Continuous:** X can take any real value in an interval. Between any two values there are infinitely many more — you can never write a complete list.

> **Always ask this first before anything else.** Everything that follows — which tools to use, how to compute probabilities — depends on this answer.

| | Discrete | Continuous |
|--|---------|-----------|
| Values | Countable list | Any value in an interval |
| Primary tool | PMF | PDF (later in course) |
| Universal tool | CDF | CDF |
| Example | Number of bags | Height of a student |
| $P(X = x)$ | Can be positive | Always 0 for any single point |
| Gaps between values? | Yes | No |

> Discrete = you can **count** the possibilities. Continuous = you can **measure** the possibilities.

Hybrid RVs (partly discrete, partly continuous) also exist — if you understand both types separately, you can handle hybrids too.

---

# The Support of a Random Variable

> **Definition:** The *support* of a discrete r.v. $X$ is the set of all values $x$ such that $P(X = x) > 0$.

Formally: $\text{Support of } X = \{x : P(X = x) > 0\}$

Only values where X can actually land with nonzero probability belong to the support. Values outside the support have probability exactly 0 — X can never land there.

> **Your lecturer analogy:** The support is the set of chairs in the room. The lecturer (X) will always sit on one of the chairs. The probability of the lecturer sitting on the ceiling = 0 because the ceiling is not in the support.

A random variable X is **discrete** if its support is a finite or countably infinite list $\{a_1, a_2, \ldots\}$ such that $P(X = a_j \text{ for some } j) = 1$.

---

# The Probability Mass Function (PMF)

> **Definition:** The *probability mass function* (PMF) of a discrete r.v. $X$ is the function $p_X$ given by:
> $$p_X(x) = P(X = x)$$
> This is positive if $x$ is in the support of $X$, and 0 otherwise.

The PMF is the complete blueprint of a discrete random variable. Once you know the PMF, you can answer any probability question about $X$ by summing:

$$P(X \in B) = \sum_{x \in B} p_X(x)$$

### Valid PMF — Two Conditions

Any PMF must satisfy:

1. **Nonnegative:** $p_X(x) > 0$ for $x$ in the support, and $p_X(x) = 0$ otherwise
2. **Sums to 1:** $\sum_j p_X(x_j) = 1$

These follow naturally: probability is always nonnegative, and X must take *some* value — certainty.

> **Practical habit:** Before using a PMF, always: (1) list the valid values of $k$, and (2) verify the sum equals 1. This catches errors early.

### What P(X = x) Really Means

$\{X = x\}$ is an **event** — the set of all outcomes $s$ in $S$ that X maps to $x$:

$$\{X = x\} = \{s \in S : X(s) = x\}$$

This set is a subset of $S$, so it is a legitimate event, and we can take its probability. Multiple different outcomes can map to the same value of $x$ — the event $\{X = x\}$ collects all of them.

> Note: Writing $P(X)$ makes no sense — you can only take the probability of an **event**, not of a random variable itself.

### What "Find the Distribution" Means

When a problem says *find the distribution of $X$*, it means: provide a complete mathematical description of the randomness of $X$. There are two valid answers:

1. **Give the PMF** $P(X = k)$ for all $k$ — works only for discrete RVs, but is usually far easier.
2. **Give the CDF** $F(x) = P(X \leq x)$ — works for any RV.

These are equally valid and carry the same information. In discrete settings, always prefer the PMF unless told otherwise.

---

# The PMF Pipeline

This is the core procedure for finding any PMF. Always follow it step by step.

**Step 0 — Is X discrete or continuous?**
If discrete, continue. Identify what X counts or measures.

**Step 1 — Find the support of X**
List all values x can actually take (where $P(X = x) > 0$).

**Step 2 — For each value x, find the event $\{X = x\}$**
$\{X = x\} = \{s \in S : X(s) = x\}$ — the set of all outcomes mapping to x.

**Step 3 — Calculate the probability of each individual outcome in that event**

**Step 4 — Add them up**
$p_X(x) = \sum_{s \in \{X=x\}} P(s)$

**Step 5 — Finish with:**
$p_X(x) = 0$ for all $x$ outside the support.

### Example — Two Coin Tosses

$X$ = number of Heads, $S = \{HH, HT, TH, TT\}$, each outcome probability $1/4$:

| Event | Outcomes | Calculation | PMF value |
|-------|---------|-------------|-----------|
| $\{X = 0\}$ | $\{TT\}$ | $1/4$ | $p_X(0) = 1/4$ |
| $\{X = 1\}$ | $\{HT, TH\}$ | $1/4 + 1/4$ | $p_X(1) = 1/2$ |
| $\{X = 2\}$ | $\{HH\}$ | $1/4$ | $p_X(2) = 1/4$ |

---

# Named Distributions

Named distributions are specific families with known PMFs and stories. They are not separate from the PMF concept — each one just has a name and parameters that completely determine its PMF.

---

## Bernoulli Distribution

> **Story:** An experiment that results in either success or failure (but not both) is called a Bernoulli trial. $X$ = 1 if success, 0 if failure.

$$X \sim \text{Bern}(p)$$

$$P(X = 1) = p, \qquad P(X = 0) = 1-p$$

$p \in (0,1)$ is the **success probability** — the single parameter that completely determines which Bernoulli distribution you have. There is a whole family indexed by $p$.

**Check — sums to 1:** $p + (1-p) = 1$ ✓

**Indicator random variables:** Every event $A$ has a naturally associated indicator r.v. $I_A$ that equals 1 if $A$ occurs and 0 otherwise. This is always $I_A \sim \text{Bern}(P(A))$. Any yes/no question in probability can be immediately turned into a Bernoulli random variable.

**Special case:** $\text{Bern}(p) = \text{Bin}(1, p)$ — Bernoulli is just Binomial with one trial.

---

## Binomial Distribution

$$X \sim \text{Bin}(n, p)$$

**Parameters:** $n$ (positive integer — number of trials) and $p \in [0,1]$ (success probability per trial).

> Changing $n$ or $p$ gives a *different* distribution. There is no single "the Binomial" — there is a whole **family** of Binomial distributions, one for each valid $(n, p)$ pair.

A high performer doesn't just memorize a formula — they hold **three equivalent views** of the same object and switch between them fluidly. Each view is best for different types of problems.

### Lens 1 — The Story (Most Important)

> Run $n$ **independent** trials. Each trial results in success (with probability $p$) or failure (with probability $1-p = q$). $X$ = total number of successes.

This is why the Binomial matters. Any real-world setting with independent binary outcomes maps here.

**The two non-negotiable conditions:**
1. Trials are **independent**
2. Every trial has the **same** probability of success $p$

Violate either condition → you no longer have a Binomial.

### Lens 2 — Sum of Indicator Random Variables (Elegant)

Decompose a complicated count into a sum of the simplest possible things:

$$X = X_1 + X_2 + \cdots + X_n$$

where each indicator $X_j = 1$ if trial $j$ succeeds, $0$ otherwise. The $X_j$'s are **i.i.d. Bern($p$)**:

- *Independent*: knowing the outcome of trial 3 tells you nothing about trial 7.
- *Identically distributed*: every $X_j$ has the exact same Bern($p$) distribution.

> **Why this lens is powerful:** It breaks a complex RV into a sum of 0/1 bricks. This unlocks easy computation of expectation, variance, and more in later lectures — and is the key to proving the sum of independent Binomials theorem.

### Lens 3 — The PMF

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k \in \{0, 1, \ldots, n\}$$

**Where the formula comes from — two parts:**

- $p^k(1-p)^{n-k}$: probability of one **specific sequence** of $k$ successes and $n-k$ failures. Trials are independent so probabilities multiply.
- $\binom{n}{k}$: number of ways to **choose which $k$ trials** are successes. Once successes are chosen, failures are automatically determined — so you only need $\binom{n}{k}$, not $\binom{n}{k} \times \binom{n-k}{n-k}$. (That second factor equals 1 always.)

**Check — sums to 1:**
$$\sum_{k=0}^{n} \binom{n}{k} p^k (1-p)^{n-k} = (p + (1-p))^n = 1^n = 1 \quad \checkmark$$
This uses the **Binomial Theorem** — and is exactly why the distribution is called "binomial."

**Symmetry:** If $X \sim \text{Bin}(n,p)$ then $n - X \sim \text{Bin}(n, 1-p)$ — counting failures instead of successes. When $p = 1/2$ and $n$ is even, the distribution is symmetric about $n/2$.

---

## When Things Are NOT Binomial

> **Pitfall:** It is tempting to label any count of "successes" as Binomial. Resist this. Check the two conditions every time.

**Example:** Draw 5 cards from a standard 52-card deck. Let $X$ = number of aces.

- Are the trials independent? **No.** If the first card is an ace, there are only 3 aces left in 51 remaining cards — the probability of the next ace has changed.
- Extreme case: if the first 4 cards are all aces, the 5th card *cannot* be an ace. Perfectly dependent.

**Conclusion: $X$ is not Binomial.** Use the Hypergeometric instead.

### PMF via Direct Counting

Since all $\binom{52}{5}$ five-card hands are equally likely:

$$P(X = k) = \frac{\binom{4}{k}\binom{48}{5-k}}{\binom{52}{5}}, \quad k \in \{0, 1, 2, 3, 4\}$$

- $\binom{4}{k}$: choose $k$ aces from the 4 in the deck.
- $\binom{48}{5-k}$: choose the remaining $5-k$ cards from the 48 non-aces.
- $\binom{52}{5}$: total equally likely hands.

> **Pattern recognition (the Elk Problem):** This is *identical* in structure to drawing tagged elk from a population — a group split into two types (aces/non-aces, white/black, tagged/untagged), sample drawn without replacement, count how many from one group you got. Recognizing that this is the *same* problem — not just similar — is a key skill. The formula is the same; only the labels change. This is the Hypergeometric distribution.

---

## Hypergeometric Distribution

> **Story:** A population of $w + b$ objects: $w$ white and $b$ black. Draw $n$ objects **without replacement**. $X$ = number of white objects in the sample.

$$X \sim \text{HGeom}(w, b, n)$$

**PMF:**
$$P(X = k) = \frac{\binom{w}{k}\binom{b}{n-k}}{\binom{w+b}{n}}$$

for integers $k$ satisfying $0 \leq k \leq w$ and $0 \leq n-k \leq b$, and $P(X=k) = 0$ otherwise. By convention $\binom{a}{b} = 0$ when $b < 0$ or $b > a$, so the formula self-zeros outside the valid range.

**Where the formula comes from:**

| Part | Meaning |
|------|---------|
| $\binom{w}{k}$ | Ways to choose $k$ white objects from $w$ white objects |
| $\binom{b}{n-k}$ | Ways to choose $n-k$ black objects from $b$ black objects |
| $\binom{w+b}{n}$ | Total ways to choose $n$ objects from the full population |

**Why $\binom{b}{n-k} \neq 1$:** Unlike Binomial where failures are automatically determined once successes are chosen, here the black balls come from a **separate pool**. There are genuinely multiple ways to choose which black balls you get.

**Check — sums to 1:** $\sum_k \binom{w}{k}\binom{b}{n-k} = \binom{w+b}{n}$ by the **Vandermonde Identity** ✓ — this constitutes a third independent proof of Vandermonde.

**Two-tag interpretation:** Every item in the population gets two labels simultaneously — first tag (white/black) and second tag (sampled/not sampled). $X$ counts items that are **twice-tagged**: white AND sampled. This interpretation generalizes far beyond urns: tagged elk in a forest, aces in a card hand, defective items in batch inspection — all are the same story with different labels.

**Key difference from Binomial:** Sampling without replacement means $p$ changes after each draw — the pool shrinks and probabilities shift. The trials are **dependent**.

**Symmetry:** $\text{HGeom}(w, b, n)$ and $\text{HGeom}(n, w+b-n, w)$ are identical distributions — swapping which tag is "first" counts the same twice-tagged items.

### Hypergeometric vs. Binomial — Full Comparison

| Property | Binomial | Hypergeometric |
|---|---|---|
| Sampling method | With replacement (or independent trials) | Without replacement |
| Trial independence | ✅ Yes | ❌ No |
| Probability of success $p$ | ✅ Constant across trials | ❌ Changes after each draw |
| Parameters | $n$, $p$ | $w$, $b$, $n$ |
| PMF | $\binom{n}{k}p^k(1-p)^{n-k}$ | $\dfrac{\binom{w}{k}\binom{b}{n-k}}{\binom{w+b}{n}}$ |
| Approx. relationship | — | $\approx \text{Bin}\!\left(n,\, \frac{w}{w+b}\right)$ when $w+b \gg n$ |

---

## Discrete Uniform Distribution

> **Story:** Let $C$ be a finite, nonempty set of numbers. Choose one uniformly at random — all values equally likely. Call the chosen number $X$.

$$X \sim \text{DUnif}(C)$$

**PMF:**
$$P(X = x) = \frac{1}{|C|} \quad \text{for } x \in C \quad (0 \text{ otherwise})$$

**Check — sums to 1:** $|C| \times \frac{1}{|C|} = 1$ ✓

**For any subset $A \subseteq C$:**
$$P(X \in A) = \frac{|A|}{|C|}$$

This is exactly the naive definition of probability — DUnif questions always reduce to counting problems.

**Special note on X:** When the sample space $C$ is already numeric, $X$ is the **identity function** — $X(s) = s$ for all $s \in C$. The sample space IS the support of $X$, so naive probability applies directly without the full pipeline.

---

## Worked Example — Slips of Paper (DUnif)

There are 100 slips of paper numbered $1, 2, \ldots, 100$, each number appearing once. Five slips are drawn one at a time.

### Sampling With Replacement

**(a) Distribution of how many drawn slips have value $\geq 80$:**
Each draw independently has probability $\frac{21}{100}$ of landing $\geq 80$. By the Binomial story: $\text{Bin}(5, 21/100)$.

**(b) Distribution of the value of the $j$-th draw:**
By symmetry, $X_j \sim \text{DUnif}(\{1, 2, \ldots, 100\})$ for any $j$.

**(c) $P(\text{number 100 drawn at least once})$:**
$$1 - \left(\frac{99}{100}\right)^5 \approx 0.049$$

### Sampling Without Replacement

**(d) Distribution of how many drawn slips have value $\geq 80$:**
Now $\text{HGeom}(21, 79, 5)$ — pool shrinks, $p$ changes, trials dependent.

**(e) Distribution of the value of the $j$-th draw:**
Still $Y_j \sim \text{DUnif}(\{1, 2, \ldots, 100\})$ by symmetry — each slip equally likely to be in any position when viewed in isolation.

**(f) $P(\text{number 100 is in the sample})$:**
$$\frac{5}{100} = \frac{1}{20} = 0.05$$

> **Key insight:** Sampling with and without replacement give the **same marginal distribution** for any single draw — $\text{DUnif}$ either way. The difference only shows up when looking at *multiple* draws together.

---

## Worked Example — Random Walk

A particle starts at 0. At each step it moves $+1$ or $-1$, each with probability $\frac{1}{2}$, independently. After $n$ steps, let $Y$ be the particle's position.

Let $X$ = number of right steps, so $X \sim \text{Bin}(n, 1/2)$. Net position: $Y = X - (n - X) = 2X - n$.

$$P(Y = k) = P\!\left(X = \frac{n+k}{2}\right) = \binom{n}{\frac{n+k}{2}} \left(\frac{1}{2}\right)^n$$

Valid for $k \in \{-n, -n+2, \ldots, n-2, n\}$ — values where $n+k$ is even.

---

## Worked Example — Distance from Origin

Let $D = |Y|$ = distance from origin after $n$ steps. Since $|k| = |-k|$, this is many-to-one:

$$P(D = 0) = P(Y = 0) = \binom{n}{n/2} \left(\frac{1}{2}\right)^n \quad \text{(only if } n \text{ is even)}$$

$$P(D = k) = 2\binom{n}{\frac{n+k}{2}}\left(\frac{1}{2}\right)^n \quad \text{for } k \geq 1$$

Two $y$ values ($+k$ and $-k$) collapse into one $d$ value ($k$) — a direct application of the many-to-one PMF formula.

---

# Cumulative Distribution Functions (CDF)

> **Definition:** The *cumulative distribution function* (CDF) of an r.v. $X$ is:
> $$F_X(x) = P(X \leq x)$$

Unlike the PMF (discrete only), the CDF is defined for **all** random variables — discrete and continuous. It is the universal tool for describing distributions.

Think of the CDF as a running total — it accumulates all PMF values from $-\infty$ up to $x$.

**Three properties every valid CDF must satisfy:**

**Property 1 — Non-decreasing:**
$$x_1 \leq x_2 \implies F(x_1) \leq F(x_2)$$
$P(X \leq x_2)$ includes everything in $P(X \leq x_1)$ plus more. Probability can only accumulate, never decrease.

**Property 2 — Right-continuous:**
$$F(a) = \lim_{x \to a^+} F(x)$$
For discrete r.v.s, the CDF is completely flat between support values and jumps *at* each support value. The jump size equals the PMF value there.

**Property 3 — Convergence to 0 and 1:**
$$\lim_{x \to -\infty} F(x) = 0 \qquad \text{and} \qquad \lim_{x \to +\infty} F(x) = 1$$

The third property is just the PMF axiom expressed through the CDF — the boundary conditions are the PMF properties in disguise.

### What CDF Graphs Look Like

*Continuous RV* — a smooth, S-shaped curve rising from 0 to 1. No jumps.

```
F(x)
 1 ─────────────────╮
                   /
 0.5             /
               /
 0 ────────╯
           x
```

*Discrete RV* — a **step function** with jumps at each possible value. Flat between values. The function takes the higher value at each jump (right-continuous, consistent with $\leq$).

```
F(x)
 1 ───────────────────o━━━━━
                   ○━╯
 0.6           ○━━╯
 0.3       ○━━╯
 0 ━━━━━○
         0   1   2   3     x
```

**PMF vs CDF:**

| | PMF | CDF |
|---|---|---|
| Formula | $P(X = x)$ | $P(X \leq x)$ |
| What it gives | Probability at one exact point | Accumulated probability up to $x$ |
| Shape (discrete) | Spikes at support values | Staircase — flat then jump |
| Jump size | — | Equals PMF value at that point |
| Defined for | Discrete r.v.s only | All r.v.s |

The CDF and PMF carry the same information — you can always recover one from the other. The jump in the CDF at any point equals the PMF value there: $P(X = x_0) = F(x_0) - F(x_0^-)$.

---

# Functions of Random Variables

If $X$ is a random variable, then any function of $X$ is also a random variable. $X^2$, $e^X$, $\sin(X)$, $g(X)$ — all are random variables. Randomness flows from the original sample space through every transformation.

> **Definition 3.7.1:** For an experiment with sample space $S$, an r.v. $X$, and a function $g : \mathbb{R} \to \mathbb{R}$, $g(X)$ is the r.v. that maps $s$ to $g(X(s))$ for all $s \in S$.

$$s \xrightarrow{X} X(s) \xrightarrow{g} g(X(s))$$

### PMF of g(X) — The Master Formula

$$P(g(X) = y) = \sum_{x \,:\, g(x) = y} P(X = x)$$

Find every $x$ in the support of $X$ that maps to $y$ under $g$, then add up their probabilities.

**One-to-one g:** Only one $x$ maps to each $y$ → probability passes down unchanged:
$$P(Y = g(x)) = P(X = x)$$

**Many-to-one g:** Multiple $x$ values map to the same $y$ → probabilities merge and add up.

> **Key insight:** Probability is born in $S$ and travels down through every function. One-to-one guarantees it arrives unchanged. Many-to-one is the only case where something interesting happens — probabilities of merging inputs add up.

### Two Common Mistakes

**Mistake 1 — Multiplying the PMF to get PMF of $2X$:**

Wrong: $P(2X = y) = 2 \times P(X = x)$. This makes probabilities sum to 2.

Correct: $P(2X = y) = P(X = y/2)$. The PMF of $2X$ is a **horizontal stretch** of the PMF of $X$ — same heights, doubled support values.

**Mistake 2 — Same distribution means always equal:**

Wrong: if $X$ and $Y$ have the same distribution, then $P(X = Y) = 1$.

| Situation | $P(X = Y)$ |
|-----------|------------|
| $X$ and $Y = 1-X$ (coin) | 0 — never equal |
| $X$ and $Z$ (independent flip) | 1/2 — sometimes equal |
| $X$ and itself | 1 — always equal |

All three cases can share the same Bern$(1/2)$ distribution. **Same distribution $\neq$ same r.v.**

---

# Independence of Random Variables

> **Definition:** Random variables $X$ and $Y$ are *independent* if:
> $$P(X \leq x, Y \leq y) = P(X \leq x) P(Y \leq y) \quad \text{for all } x, y \in \mathbb{R}$$

**Discrete equivalent condition:**
$$P(X = x, Y = y) = P(X = x) P(Y = y)$$
for all $x, y$ in the respective supports. Much easier to check in practice.

### Proof — Why the Discrete Condition is Equivalent

**PMF condition $\implies$ CDF condition:**

$$P(X \leq x, Y \leq y) = \sum_{x' \leq x} \sum_{y' \leq y} P(X = x', Y = y') = \sum_{x' \leq x} \sum_{y' \leq y} P(X = x') P(Y = y')$$

$$= \left(\sum_{x' \leq x} P(X = x')\right)\left(\sum_{y' \leq y} P(Y = y')\right) = P(X \leq x) P(Y \leq y) \quad \checkmark$$

**CDF condition $\implies$ PMF condition:**

Recover the joint PMF by taking differences of the CDF at specific values $x_0, y_0$. Since each CDF term factors by assumption, the whole expression factors into $P(X = x_0) \cdot P(Y = y_0)$. $\blacksquare$

**Pairwise vs mutual independence:** Full independence implies pairwise independence, but pairwise independence does NOT imply full independence.

**i.i.d.:** Random variables that are **independent** and **identically distributed**. Two completely different concepts:

| | Independent | Identically distributed |
|--|-------------|------------------------|
| Meaning | Knowing one tells you nothing about the others | Same PMF / distribution |
| i.i.d. | ✅ | ✅ |
| Indep., different dist. | ✅ | ❌ |
| Same dist., dependent | ❌ | ✅ |
| Neither | ❌ | ❌ |

**Example — same dist., dependent:** $X \sim \text{Bin}(n, 1/2)$, $Y = n - X$. Both $\sim \text{Bin}(n, 1/2)$ but $Y = n - X$ so knowing $X$ tells you $Y$ exactly.

**Functions of independent r.v.s:** If $X \perp Y$, then $g(X) \perp h(Y)$ for any functions $g$, $h$.

---

# Sum of Independent Binomials

**Theorem:** If $X \sim \text{Bin}(n,p)$, $Y \sim \text{Bin}(m,p)$, and $X \perp Y$, then:
$$X + Y \sim \text{Bin}(n+m, p)$$

Requires the **same $p$** — if success probabilities differ, the sum is not Binomial.

**Proof 1 — Story (fastest):**
$X$ counts successes in $n$ trials, $Y$ in $m$ additional independent trials, all with the same $p$. Together that is $n+m$ independent trials each with probability $p$ — exactly $\text{Bin}(n+m,p)$ by definition. $\square$

**Proof 2 — Bernoulli indicators (elegant):**
Write $X = X_1 + \cdots + X_n$ and $Y = Y_1 + \cdots + Y_m$ where all $X_i, Y_j \overset{\text{i.i.d.}}{\sim} \text{Bern}(p)$. Since $X \perp Y$, all $n+m$ indicators are mutually independent with the same Bern$(p)$ distribution. A sum of $n+m$ i.i.d. Bern$(p)$ r.v.s is $\text{Bin}(n+m,p)$ by definition. $\square$

**Proof 3 — PMF convolution (most algebraic, most instructive):**

Adding two random variables via their PMFs is called a **convolution**. Condition on $X$ using LOTP:

$$P(X+Y=k) = \sum_{j=0}^{k} P(Y=k-j \mid X=j) P(X=j) = \sum_{j=0}^{k} P(Y=k-j) P(X=j)$$

Independence lets us drop the condition on $X$ when asking about $Y$ — we are not making $P(Y=k-j \mid X=j)$ become 1, we are simply replacing the conditional probability with the unconditional one.

**The dice analogy — building intuition for LOTP:**
The same conditioning technique applies to: what is the probability two dice sum to 8?

$$P(\text{sum} = 8) = \sum_{j=1}^{6} P(\text{die 2} = 8 - j) \cdot P(\text{die 1} = j)$$

For each value die 1 could take, figure out exactly what die 2 needs to be, then weight by how likely die 1 was. The Binomial proof uses exactly the same logic.

Substitute Binomial PMFs and collect powers of $p$ and $q = 1-p$ (they factor out because $p$ is shared — with different $p$'s they would not cancel):

$$P(X+Y=k) = p^k q^{n+m-k} \sum_{j=0}^{k} \binom{n}{j}\binom{m}{k-j}$$

Apply Vandermonde's Identity: $\sum_{j=0}^{k} \binom{n}{j}\binom{m}{k-j} = \binom{n+m}{k}$

$$\therefore \quad P(X+Y=k) = \binom{n+m}{k} p^k q^{n+m-k} \quad \checkmark \quad \square$$

> **Meta-insight:** The convolution proof is also a **second proof of the Vandermonde Identity** — because the story proof already guarantees the result must be $\text{Bin}(n+m,p)$, the algebra *must* produce $\binom{n+m}{k}$. If it didn't, we'd have a contradiction. So either proof validates the other.

**Vandermonde's Identity** — proved three independent ways across the course:
1. Combinatorial story (choose $k$ from $n$ men and $m$ women, split by gender)
2. Binomial convolution (the algebra above)
3. Hypergeometric PMF summing to 1

---

# Connections Between Binomial and Hypergeometric

$$\text{Binomial} \xrightarrow{\text{condition on total}} \text{Hypergeometric}$$
$$\text{Hypergeometric} \xrightarrow{\text{population} \to \infty} \text{Binomial}$$

**Binomial → Hypergeometric by conditioning:**
Start with $X \sim \text{Bin}(n,p)$ and $Y \sim \text{Bin}(m,p)$ independent. Condition on the total $X+Y = K$. Once the total is fixed, the trials are no longer independent — asking for the distribution of $X$ given the total is exactly the Hypergeometric.

**Hypergeometric → Binomial by taking a limit:**
Start with $\text{HGeom}(w, b, n)$. Let $w + b \to \infty$ while keeping $\frac{w}{w+b} = p$ fixed. Drawing without replacement from an effectively infinite population is the same as drawing with replacement — dependence vanishes. In the limit, $\text{HGeom}(w, b, n) \to \text{Bin}(n, p)$.

> **Practical implication:** When sampling $n$ people from a large population $N$ where $n \ll N$, the Hypergeometric can be safely approximated by the Binomial. The approximation improves as $n/N \to 0$.

---

# Big Picture Flowchart

```
Two conditions: independence + constant p
        |
        ├── Both hold → BINOMIAL Bin(n,p)
        │       ├── Lens 1 Story: n indep. Bern(p) trials, count successes
        │       ├── Lens 2 Indicators: X = X₁ + ... + Xₙ, i.i.d. Bern(p)
        │       └── Lens 3 PMF: C(n,k) pᵏ qⁿ⁻ᵏ  [validated by Binomial Theorem]
        │
        └── Sampling without replacement → HYPERGEOMETRIC HGeom(w,b,n)
                ├── Story: draw n from w white + b black, count white
                └── PMF: C(w,k)C(b,n-k) / C(w+b,n)  [validated by Vandermonde]

Adding independent Binomials with same p:
    Bin(n,p) + Bin(m,p) = Bin(n+m,p)
    Proved 3 ways: Story | Indicators | PMF convolution (uses Vandermonde)

Vandermonde Identity: Σⱼ C(n,j)C(m,k-j) = C(n+m,k)
    Proved 3 times across the course:
        1. Story proof (combinatorics)
        2. Binomial convolution (PMF proof above)
        3. Hypergeometric PMF summing to 1

Random Variables: functions X: S → ℝ
    Described by CDF F(x) = P(X ≤ x)  [always]
    or PMF pⱼ = P(X = aⱼ)             [discrete only, usually easier]
```

---

# Summary Cheatsheet

| Concept | Key Formula / Fact |
|---------|-------------------|
| Random variable | Deterministic function $X: S \to \mathbb{R}$; randomness lives in $P$, not $X$ |
| Support | $\{x : P(X=x) > 0\}$ — where probability mass actually lives |
| PMF | $p_X(x) = P(X=x)$; nonneg + sums to 1 |
| PMF pipeline | Support → event $\{X=x\}$ → add outcome probabilities → done |
| "Find the distribution" | Give PMF (discrete, easier) or CDF (universal) — both equally valid |
| Bernoulli | $P(X=1)=p$, $P(X=0)=1-p$; indicator r.v. of any event |
| Binomial — 3 lenses | Story (indep. trials) / Indicators (sum of Bern) / PMF formula |
| Binomial PMF | $\binom{n}{k}p^k(1-p)^{n-k}$; requires independent trials, same $p$ |
| Binomial as sum | $X = X_1 + \cdots + X_n$, $X_i \overset{\text{i.i.d.}}{\sim} \text{Bern}(p)$ |
| Binomial additivity | $\text{Bin}(n,p) + \text{Bin}(m,p) = \text{Bin}(n+m,p)$ (same $p$, independent) |
| NOT Binomial | If sampling without replacement or $p$ changes — use Hypergeometric |
| Hypergeometric PMF | $\frac{\binom{w}{k}\binom{b}{n-k}}{\binom{w+b}{n}}$; without replacement, equally likely |
| Vandermonde Identity | $\sum_{j=0}^k \binom{n}{j}\binom{m}{k-j} = \binom{n+m}{k}$ — proved 3 ways |
| DUnif PMF | $\frac{1}{\vert C \vert}$ for $x \in C$; reduces to counting problems |
| CDF | $F(x) = P(X \leq x)$; non-decreasing, right-continuous, $0 \to 1$ |
| CDF shape | Continuous: smooth S-curve. Discrete: staircase, jumps = PMF values |
| PMF → CDF | $F(x) = \sum_{x' \leq x} p_X(x')$ (running total) |
| CDF → PMF | $P(X=x_0) = F(x_0) - F(x_0^-)$ (size of jump) |
| PMF of $g(X)$ | $P(g(X)=y) = \sum_{x: g(x)=y} P(X=x)$ |
| One-to-one $g$ | Probability passes down unchanged |
| Many-to-one $g$ | Probabilities of merging inputs add up |
| Independence | $P(X \leq x, Y \leq y) = P(X \leq x)P(Y \leq y)$ |
| Discrete independence | $P(X=x, Y=y) = P(X=x)P(Y=y)$ |
| i.i.d. | Independent AND identically distributed — two orthogonal properties |
| HGeom ≈ Binomial | When population $\gg$ sample size ($n/N \to 0$) |
| Convolution meta-insight | PMF proof of Bin additivity is simultaneously a proof of Vandermonde |
