---
title: 'Lecture 8: Binomial, Hypergeometric & Random Variables'
subject: probability
chapter: 04-random-variables
tags:
- probability
- mathematics
date: '2026-06-18'
updated: '2026-06-19'
status: complete
difficulty: intermediate
---
> 🎥 **Source:** [Statistics 110 — Lecture 8 (Harvard, Prof. Joe Blitzstein)](https://youtu.be/k2BB0p8byGA?si=uOHXwDLpX4fPrAhm)

> **Mental Model First:** Anchor this entire lecture in one question — *what happens when you count successes under different sampling regimes?*
> - Trials are **independent** (or sampling with replacement) → **Binomial**
> - Sampling **without replacement** → **Hypergeometric**
>
> Everything else — indicators, convolutions, CDFs, PMFs — is just the mathematical scaffolding that makes these stories precise.

---

## 1. The Binomial Distribution — Three Lenses

$$X \sim \text{Bin}(n, p)$$

**Parameters:** $n$ (positive integer) and $p \in [0,1]$.

> Changing $n$ or $p$ gives a *different* distribution. There is no single "the Binomial" — there is a whole **family** of Binomial distributions, one for each valid $(n, p)$ pair.

A high performer doesn't just memorize a formula — they hold **three equivalent views** of the same object and switch between them fluidly. Each view is best for different types of problems.

---

### Lens 1 — The Story (Most Important)

> Run $n$ **independent** trials. Each trial results in success (with probability $p$) or failure (with probability $1-p = q$). $X$ = total number of successes.

This is why the Binomial matters. Any real-world setting with independent binary outcomes maps here.

**Classic example:** Flip a coin $n$ times; $X$ = number of heads. Success = heads, failure = tails (or define it the other way — the math doesn't care).

**The two non-negotiable conditions:**
1. Trials are **independent**
2. Every trial has the **same** probability of success $p$

Violate either condition → you no longer have a Binomial.

---

### Lens 2 — Sum of Indicator Random Variables

Decompose a complicated count into a sum of the simplest possible things:

$$X = X_1 + X_2 + \cdots + X_n$$

where each **indicator random variable** $X_j$ encodes the $j$-th trial:

$$X_j = \begin{cases} 1 & \text{if trial } j \text{ is a success} \\ 0 & \text{if trial } j \text{ is a failure} \end{cases}$$

Adding 1 for every success and 0 for every failure is exactly how you count — so $X = \sum X_j$ is trivially correct.

The $X_j$'s are **i.i.d. Bernoulli($p$)**:

$$X_j \sim \text{Bern}(p) \quad \Longleftrightarrow \quad P(X_j = 1) = p,\quad P(X_j = 0) = 1-p$$

**i.i.d.** = **Independent** and **Identically Distributed**
- *Independent*: knowing the outcome of trial 3 tells you nothing about trial 7.
- *Identically distributed*: every $X_j$ has the exact same Bern($p$) distribution.

> **Why this lens is powerful:** It breaks a complex RV into a sum of 0/1 bricks. This is one of the most frequently used techniques in the course — it will unlock easy computation of expectation, variance, and more in later lectures.

> ⚠️ **Critical distinction — RV ≠ Distribution:**
> $X_1, X_2, \ldots, X_n$ are *different* random variables (each depends on a different trial). Yet they all *share* the same distribution Bern($p$). Many random variables can have the same distribution. The distribution is the blueprint (what are the probabilities?); the random variable is a specific instance of randomness (what actually happened on trial $j$?).

---

### Lens 3 — The PMF

$$P(X = k) = \binom{n}{k} p^k q^{n-k}, \quad k \in \{0, 1, \ldots, n\}, \quad q = 1-p$$

**Where does this come from?**
- $p^k q^{n-k}$: probability of one specific arrangement with exactly $k$ successes and $n-k$ failures.
- $\binom{n}{k}$: number of ways to choose *which* $k$ of the $n$ trials are the successes.

**Validity check — always verify a PMF sums to 1:**

$$\sum_{k=0}^{n} \binom{n}{k} p^k q^{n-k} = (p + q)^n = 1^n = 1 \quad \checkmark$$

The last step uses the **Binomial Theorem**: $(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^k b^{n-k}$.

This is exactly why the distribution is called "binomial" — its PMF sums to 1 *because* of the binomial theorem.

---

## 2. What "Find the Distribution" Means

When a problem says *find the distribution of $X$*, it means: provide a complete mathematical description of the randomness of $X$. There are two valid answers:

1. **Give the CDF** $F(x) = P(X \leq x)$ — works for any RV.
2. **Give the PMF** $P(X = k)$ for all $k$ — works only for discrete RVs, but is usually far easier.

These are equally valid. In discrete settings, always prefer the PMF unless told otherwise.

---

## 3. Key Property: Sum of Independent Binomials

$$X \sim \text{Bin}(n,p),\quad Y \sim \text{Bin}(m,p),\quad X \perp Y \implies X + Y \sim \text{Bin}(n+m,\, p)$$

> Note: this only works when **both** have the **same** $p$. $\text{Bin}(n, \tfrac{1}{2}) + \text{Bin}(m, \tfrac{1}{3})$ is not Binomial.

### Proof via Lens 1 — Story (Fastest)

$n$ independent trials with prob $p$ of success, then $m$ more independent trials with the same $p$. Together that's $n+m$ independent trials, each with success prob $p$. Counting all successes gives $\text{Bin}(n+m, p)$. $\square$

### Proof via Lens 2 — Indicators (Elegant)

$$X + Y = \underbrace{X_1 + \cdots + X_n}_{n \text{ i.i.d. Bern}(p)} + \underbrace{Y_1 + \cdots + Y_m}_{m \text{ i.i.d. Bern}(p)}$$

Since $X \perp Y$, all $n + m$ indicators are mutually independent, and each is Bern($p$). A sum of $n+m$ i.i.d. Bern($p$) variables *is* $\text{Bin}(n+m, p)$ by definition (Lens 1/2). $\square$

### Proof via Lens 3 — PMF Convolution (Most Work, Most Instructive)

Adding two random variables via their PMFs is called a **convolution** — a word that shares roots with "convoluted" for good reason. This is where things get algebraically heavy *unless* you see the pattern.

**Strategy: wishful thinking + Law of Total Probability.**
We don't know $X+Y$, but if we *knew* $X$, we'd immediately know what $Y$ must equal for the sum to be $k$. So condition on $X$:

$$P(X+Y = k) = \sum_{j=0}^{k} P(X+Y = k \mid X = j)\, P(X = j)$$

*(We sum $j$ from $0$ to $k$ only — if $X > k$, the sum can't equal $k$ since both are non-negative.)*

Substitute $X = j$ into the first factor:

$$= \sum_{j=0}^{k} P(Y = k-j \mid X = j)\, P(X = j)$$

Apply **independence** ($X \perp Y$ means knowing $X$ gives no information about $Y$, so we drop the conditioning):

$$= \sum_{j=0}^{k} P(Y = k-j)\, P(X = j)$$

Now substitute the Binomial PMFs:

$$= \sum_{j=0}^{k} \binom{m}{k-j} p^{k-j} q^{m-k+j} \cdot \binom{n}{j} p^{j} q^{n-j}$$

Collect powers of $p$ and $q$ (they don't depend on $j$, so factor them out):

$$= p^{k}\, q^{m+n-k} \sum_{j=0}^{k} \binom{n}{j}\binom{m}{k-j}$$

Apply the **Vandermonde Identity**:

$$\sum_{j=0}^{k} \binom{n}{j}\binom{m}{k-j} = \binom{n+m}{k}$$

$$\therefore \quad P(X+Y=k) = \binom{n+m}{k} p^k q^{n+m-k} \quad \checkmark$$

This is exactly the $\text{Bin}(n+m, p)$ PMF. $\square$

> **Meta-insight:** The convolution proof is also a **second proof of the Vandermonde Identity** — because the story proof already guarantees the result must be $\text{Bin}(n+m,p)$, the algebra *must* produce $\binom{n+m}{k}$. If it didn't, we'd have a contradiction. So either proof validates the other.

---

## 4. When Things Are NOT Binomial

> **Pitfall:** It's tempting to label any count of "successes" as Binomial. Resist this. Check the two conditions every time.

**Example:** Draw 5 cards from a standard 52-card deck. Let $X$ = number of aces.

- Is each card "a trial"? Yes.
- Are the trials independent? **No.** If the first card is an ace, there are only 3 aces left in 51 remaining cards — the probability of the next ace has changed.
- Extreme case: if the first 4 cards are all aces, the 5th card *cannot* be an ace. Perfectly dependent.

**Conclusion: $X$ is not Binomial.**

### PMF via Direct Counting (Naive Definition)

Since all $\binom{52}{5}$ five-card hands are equally likely:

$$P(X = k) = \frac{\dbinom{4}{k}\dbinom{48}{5-k}}{\dbinom{52}{5}}, \quad k \in \{0, 1, 2, 3, 4\}$$

- $\binom{4}{k}$: choose $k$ aces from the 4 in the deck.
- $\binom{48}{5-k}$: choose the remaining $5-k$ cards from the 48 non-aces.
- $\binom{52}{5}$: total hands.

> **Pattern recognition (the Elk Problem):** This is *identical* in structure to the elk problem — a population split into two groups (tagged/untagged, aces/non-aces, white/black marbles), sample drawn without replacement, count how many from one group you got. Recognizing that this is the same problem — not just similar, but *the same* — is a key skill. The formula is the same; only the labels change.

---

## 5. The Hypergeometric Distribution

### Mental Model

> A jar contains $w$ white marbles and $b$ black marbles. Draw $n$ marbles **without replacement**. $X$ = number of white marbles in the sample.

Equivalent framings: tagged elk in a population, aces in a card hand, defective items in a batch inspection. One story, many costumes.

$$X \sim \text{HGeom}(w,\, b,\, n)$$

$$\boxed{P(X = k) = \frac{\dbinom{w}{k}\dbinom{b}{n-k}}{\dbinom{w+b}{n}}}$$

**Constraints:** $k$ must satisfy $0 \leq k \leq w$ and $0 \leq n-k \leq b$. By convention $\binom{a}{b} = 0$ when $b < 0$ or $b > a$, so the formula self-zeros outside the valid range.

**Validity — PMF sums to 1:**

$$\sum_{k} P(X=k) = \frac{1}{\dbinom{w+b}{n}} \sum_{k} \binom{w}{k}\binom{b}{n-k} = \frac{\dbinom{w+b}{n}}{\dbinom{w+b}{n}} = 1 \quad \checkmark$$

The inner sum is the **Vandermonde Identity** again. This constitutes a **third independent proof** of Vandermonde.

---

### Hypergeometric vs. Binomial — Full Comparison

| Property | Binomial | Hypergeometric |
|---|---|---|
| Sampling method | With replacement (or independent trials) | Without replacement |
| Trial independence | ✅ Yes | ❌ No |
| Probability of success $p$ | ✅ Constant across trials | ❌ Changes after each draw |
| Parameters | $n$, $p$ | $w$, $b$, $n$ |
| PMF | $\binom{n}{k}p^k(1-p)^{n-k}$ | $\dfrac{\binom{w}{k}\binom{b}{n-k}}{\binom{w+b}{n}}$ |
| Approx. relationship | — | $\approx \text{Bin}\!\left(n,\, \frac{w}{w+b}\right)$ when $w+b \gg n$ |

**Why the approximation works:** If the population $w + b$ is enormous relative to the sample $n$, drawing without replacement barely differs from drawing with replacement — you'd almost never draw the same marble twice anyway. So dependence becomes negligible and Hypergeometric $\approx$ Binomial.

---

## 6. Random Variables — Core Concepts

### What Is a Random Variable?

Formally, a **random variable** (RV) $X$ is a **function** mapping each outcome in the sample space $S$ to a real number:

$$X : S \to \mathbb{R}$$

**Pebble world picture:** Each pebble (outcome) gets stamped with a number. The event $\{X = 7\}$ is not an equation to solve — it's the *set of all pebbles stamped with the number 7*. It is a legitimate event, so it has a probability.

This means expressions like $P(X = k)$, $P(X \leq x)$, $P(a < X \leq b)$ are all well-defined probabilities of events.

---

### CDF — Cumulative Distribution Function

Defined for **any** random variable (discrete, continuous, or hybrid):

$$F(x) = P(X \leq x)$$

**Properties:**
- $F$ is **non-decreasing**: larger $x$ → more outcomes qualify → probability can only stay or grow.
- $\lim_{x \to -\infty} F(x) = 0$: it's impossible to be below $-\infty$.
- $\lim_{x \to +\infty} F(x) = 1$: $X$ must take *some* value.
- **Right-continuous**: $F(x) = \lim_{t \downarrow x} F(t)$ (a technicality that matters at jump points).

**Why the CDF matters:** It is a *complete* description of the distribution. Given $F$, you can answer any probability question about $X$ — e.g., $P(a < X \leq b) = F(b) - F(a)$.

**What CDF graphs look like:**

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

*Discrete RV* — a **step function** with jumps at each possible value. Flat between values. Open circles at the bottom of each jump (the function takes the higher value, since we use $\leq$, not $<$).

```
F(x)
 1 ───────────────────o━━━━━
                   ○━╯
 0.6           ○━━╯
 0.3       ○━━╯
 0 ━━━━━○
         0   1   2   3     x
```

> For discrete RVs, the PMF is usually simpler to work with. The CDF exists for both, which is why it's defined this way — it's the universal tool.

---

### PMF — Probability Mass Function (Discrete RVs Only)

A discrete RV takes values in a listable set $\{a_1, a_2, \ldots\}$ (the list may be infinite). The PMF assigns a probability to each:

$$p_j = P(X = a_j)$$

**Two conditions every valid PMF must satisfy:**

$$p_j \geq 0 \quad \text{for all } j \qquad \text{(probabilities are non-negative)}$$

$$\sum_j p_j = 1 \qquad \text{(}X \text{ must equal something)}$$

Conversely, any collection of non-negative numbers summing to 1 defines a valid PMF.

> **Practical habit:** Before using a PMF, always: (1) list the valid values of $k$, and (2) verify the sum equals 1. This catches errors early.

---

### Discrete vs. Continuous RVs

| | Discrete | Continuous |
|---|---|---|
| Possible values | Finite or countably infinite, can be listed | Uncountably infinite (e.g., any real in an interval) |
| Primary tool | PMF | PDF — Probability Density Function (later in course) |
| Universal tool | CDF | CDF |
| $P(X = x)$ | Can be positive | Always 0 for any single point |

Hybrid RVs (partly discrete, partly continuous) also exist — if you understand both types separately, you can handle hybrids too.

---

## 7. Big Picture — Everything in This Lecture

```
Two conditions: independence + constant p
        |
        ├── Both hold → BINOMIAL Bin(n,p)
        │       ├── Story: n indep. Bern(p) trials, count successes
        │       ├── Indicator decomposition: X = X₁ + ... + Xₙ, i.i.d. Bern(p)
        │       └── PMF: C(n,k) pᵏ qⁿ⁻ᵏ  [validated by Binomial Theorem]
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

## 8. Summary Cheatsheet

| Concept | Formula / Fact |
|---|---|
| Binomial PMF | $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$, $k=0,\ldots,n$ |
| Binomial validity | $\sum_{k=0}^n \binom{n}{k}p^k q^{n-k} = (p+q)^n = 1$ (Binomial Theorem) |
| i.i.d. Bernoulli sum | $X_1+\cdots+X_n \sim \text{Bin}(n,p)$ if $X_i \overset{iid}{\sim} \text{Bern}(p)$ |
| Binomial additivity | $\text{Bin}(n,p) + \text{Bin}(m,p) = \text{Bin}(n+m,p)$ (same $p$, independent) |
| Hypergeometric PMF | $P(X=k) = \dfrac{\binom{w}{k}\binom{b}{n-k}}{\binom{w+b}{n}}$ |
| Vandermonde Identity | $\sum_{j=0}^{k}\binom{n}{j}\binom{m}{k-j} = \binom{n+m}{k}$ |
| CDF (universal) | $F(x) = P(X \leq x)$; non-decreasing, right-continuous, $0 \to 1$ |
| PMF validity | $p_j \geq 0$ for all $j$, and $\sum_j p_j = 1$ |
| Convolution strategy | Condition on one variable, use independence, apply known identity |
| HGeom ≈ Binomial when | Population $\gg$ sample size |