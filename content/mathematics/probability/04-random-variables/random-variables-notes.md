---
title: Random Variables and Their Distributions
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
> Notes from *Introduction to Probability* — Blitzstein & Hwang | Full Chapter 3 + Lecture 8

---

## Table of Contents

1. [Why Random Variables?](#why-random-variables)
2. [Definition and Core Insight](#definition-and-core-insight)
3. [Discrete vs Continuous Random Variables](#discrete-vs-continuous-random-variables)
4. [The Support of a Random Variable](#the-support-of-a-random-variable)
5. [The Probability Mass Function (PMF)](#the-probability-mass-function-pmf)
6. [The PMF Pipeline](#the-pmf-pipeline)
7. [Named Distributions](#named-distributions)
   - [Bernoulli](#bernoulli-distribution)
   - [Binomial](#binomial-distribution)
   - [Hypergeometric](#hypergeometric-distribution)
   - [Discrete Uniform](#discrete-uniform-distribution)
8. [Cumulative Distribution Functions (CDF)](#cumulative-distribution-functions-cdf)
9. [Functions of Random Variables](#functions-of-random-variables)
10. [Independence of Random Variables](#independence-of-random-variables)
11. [Sum of Independent Binomials — Three Proofs](#sum-of-independent-binomials)
12. [Connections Between Binomial and Hypergeometric](#connections-between-binomial-and-hypergeometric)
13. [Summary Cheatsheet](#summary-cheatsheet)

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
| Gaps between values? | Yes | No |

> Discrete = you can **count** the possibilities. Continuous = you can **measure** the possibilities.

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

### What P(X = x) Really Means

$\{X = x\}$ is an **event** — the set of all outcomes $s$ in $S$ that X maps to $x$:

$$\{X = x\} = \{s \in S : X(s) = x\}$$

This set is a subset of $S$, so it is a legitimate event, and we can take its probability. Multiple different outcomes can map to the same value of $x$ — the event $\{X = x\}$ collects all of them.

> Note: Writing $P(X)$ makes no sense — you can only take the probability of an **event**, not of a random variable itself.

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

> **Story:** Perform $n$ **independent** Bernoulli trials, each with the same success probability $p$. $X$ = number of successes.

$$X \sim \text{Bin}(n, p)$$

**Parameters:** $n$ (positive integer — number of trials) and $p \in (0,1)$ (success probability per trial).

**PMF:**
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k \in \{0, 1, \ldots, n\}$$

**Where the formula comes from — two parts:**

- $p^k(1-p)^{n-k}$: probability of one **specific sequence** of $k$ successes and $n-k$ failures. Trials are independent so probabilities multiply. $k$ successes contribute $p^k$, the $n-k$ failures contribute $(1-p)^{n-k}$.

- $\binom{n}{k}$: number of ways to **choose which $k$ trials** are successes. Once successes are chosen, failures are automatically determined — so you only need $\binom{n}{k}$, not $\binom{n}{k} \times \binom{n-k}{n-k}$. (That second factor equals 1 always.)

**Check — sums to 1:** $\sum_{k=0}^n \binom{n}{k} p^k (1-p)^{n-k} = (p + (1-p))^n = 1$ ✓ (Binomial Theorem)

**Two non-negotiable conditions for Binomial:**
1. Trials are **independent** — constant $p$ across all trials
2. Same $p$ every trial — *identically distributed*

If $p$ changes between trials (e.g., sampling without replacement from a finite pool), it is no longer Binomial.

**Sum representation:** $X = X_1 + X_2 + \cdots + X_n$ where $X_i \overset{\text{i.i.d.}}{\sim} \text{Bern}(p)$ — the Binomial is literally the sum of independent, identically distributed Bernoullis.

**Symmetry:** If $X \sim \text{Bin}(n,p)$ then $n - X \sim \text{Bin}(n, 1-p)$ — counting failures instead of successes. When $p = 1/2$ and $n$ is even, the distribution is symmetric about $n/2$: $P(X = n/2 + j) = P(X = n/2 - j)$ for all nonneg. integers $j$.

---

## Hypergeometric Distribution

> **Story:** A population of $w + b$ objects: $w$ white and $b$ black. Draw $n$ objects **without replacement**. $X$ = number of white objects in the sample.

$$X \sim \text{HGeom}(w, b, n)$$

**PMF:**
$$P(X = k) = \frac{\binom{w}{k}\binom{b}{n-k}}{\binom{w+b}{n}}$$

for integers $k$ satisfying $0 \leq k \leq w$ and $0 \leq n-k \leq b$, and $P(X=k) = 0$ otherwise.

**Where the formula comes from:**

| Part | Meaning |
|------|---------|
| $\binom{w}{k}$ | Ways to choose $k$ white objects from $w$ white objects |
| $\binom{b}{n-k}$ | Ways to choose $n-k$ black objects from $b$ black objects |
| $\binom{w+b}{n}$ | Total ways to choose $n$ objects from the full population |

Multiply numerator by multiplication rule (two independent choices). Divide by total equally likely outcomes. This uses the **naive definition of probability** — only valid because all samples are equally likely.

**Why $\binom{b}{n-k} \neq 1$:** Unlike Binomial where failures are automatically determined once successes are chosen, here the black balls come from a **separate pool**. There are genuinely multiple ways to choose which black balls you get.

**Check — sums to 1:** $\sum_k \binom{w}{k}\binom{b}{n-k} = \binom{w+b}{n}$ by the **Vandermonde Identity** ✓

**Two-tag interpretation:** Every item in the population gets two labels simultaneously — first tag (white/black) and second tag (sampled/not sampled). $X$ counts items that are **twice-tagged**: white AND sampled. At least one set of tags is assigned completely at random (the sampling). This interpretation generalizes far beyond urns: tagged elk in a forest, aces in a card hand, defective items in batch inspection — all are the same story with different labels.

**Key difference from Binomial:** Sampling without replacement means $p$ changes after each draw — the pool shrinks and probabilities shift. The trials are **dependent**. This is why the formula looks different.

**Symmetry:** $\text{HGeom}(w, b, n)$ and $\text{HGeom}(n, w+b-n, w)$ are identical distributions — swapping which tag is "first" counts the same twice-tagged items.

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

**Special note on X:** When the sample space $C$ is already numeric, $X$ is the **identity function** — $X(s) = s$ for all $s \in C$. It just returns whatever value was picked. The sample space IS the support of $X$, so naive probability applies directly without the full pipeline.

---

## Worked Example — Slips of Paper (DUnif)

There are 100 slips of paper numbered $1, 2, \ldots, 100$, each number appearing once. Five slips are drawn one at a time.

### Sampling With Replacement

**(a) Distribution of how many drawn slips have value $\geq 80$:**

Each draw independently has probability $\frac{21}{100}$ of landing $\geq 80$ (the values 80 through 100). By the Binomial story, the count follows $\text{Bin}(5, 21/100)$.

**(b) Distribution of the value of the $j$-th draw:**

By symmetry, every slip is equally likely to be drawn at any position. So $X_j \sim \text{DUnif}(\{1, 2, \ldots, 100\})$ for any $j$.

**(c) $P(\text{number 100 drawn at least once})$:**

Use complements — easier to find the probability that 100 is *never* drawn:
$$1 - P(X_1 \neq 100, \ldots, X_5 \neq 100) = 1 - \left(\frac{99}{100}\right)^5 \approx 0.049$$

### Sampling Without Replacement

**(d) Distribution of how many drawn slips have value $\geq 80$:**

Now drawing without replacement — the count follows the **Hypergeometric** distribution. The pool shrinks after each draw, $p$ is no longer constant, trials are dependent.

**(e) Distribution of the value of the $j$-th draw:**

Still $Y_j \sim \text{DUnif}(\{1, 2, \ldots, 100\})$ by symmetry — even without replacement, each slip is equally likely to end up in any particular position when viewed in isolation.

**(f) $P(\text{number 100 is in the sample})$:**

$$P(Y_1 = 100 \text{ or } \cdots \text{ or } Y_5 = 100) = \frac{5}{100} = \frac{1}{20} = 0.05$$

By symmetry, the probability that slip 100 is among the 5 chosen is just $\frac{5}{100}$.

> **Key insight:** Sampling with and without replacement give the **same marginal distribution** for any single draw — $\text{DUnif}$ either way. The difference only shows up when looking at *multiple* draws together: without-replacement draws are dependent, with-replacement draws are independent.

---

## Worked Example — Random Walk

A particle starts at 0. At each step it moves $+1$ (right) or $-1$ (left), each with probability $\frac{1}{2}$, independently. After $n$ steps, let $Y$ be the particle's position.

**Setting up $Y$ as a function of a Binomial:**

Think of each step as a Bernoulli trial — right is success, left is failure. Let $X$ = number of right steps, so $X \sim \text{Bin}(n, 1/2)$.

- Number of right steps: $X$
- Number of left steps: $n - X$
- Net position: $Y = X - (n - X) = 2X - n$

So $Y = g(X)$ where $g(x) = 2x - n$. Since $g$ is one-to-one (linear with nonzero slope), probability passes down unchanged:

$$P(Y = k) = P(2X - n = k) = P\!\left(X = \frac{n+k}{2}\right) = \binom{n}{\frac{n+k}{2}} \left(\frac{1}{2}\right)^n$$

Valid for $k \in \{-n, -n+2, \ldots, n-2, n\}$ — values where $n+k$ is even (otherwise $\frac{n+k}{2}$ is not an integer and the probability is 0). $Y$ can only take even-spaced values because each step changes position by 2 (either $+1$ or $-1$ from both sides).

---

## Worked Example — Distance from Origin

Continuing the random walk: let $D = |Y|$ = the particle's distance from the origin after $n$ steps.

$D = |2X - n|$ — this is **not** one-to-one since $|k| = |-k|$. Both $Y = k$ and $Y = -k$ give $D = k$. The event $\{D = k\}$ is the same as $\{Y = k\} \cup \{Y = -k\}$, and these two events are disjoint for $k \geq 1$.

Using the master formula (many-to-one):

$$P(D = 0) = P(Y = 0) = \binom{n}{n/2} \left(\frac{1}{2}\right)^n \quad \text{(only possible if } n \text{ is even)}$$

$$P(D = k) = P(Y = k) + P(Y = -k) = 2\binom{n}{\frac{n+k}{2}}\left(\frac{1}{2}\right)^n \quad \text{for } k \geq 1$$

Two $y$ values ($+k$ and $-k$) collapse into one $d$ value ($k$), so their probabilities add — a direct application of the many-to-one PMF formula.

---

# Cumulative Distribution Functions (CDF)

> **Definition:** The *cumulative distribution function* (CDF) of an r.v. $X$ is:
> $$F_X(x) = P(X \leq x)$$

Unlike the PMF (discrete only), the CDF is defined for **all** random variables — discrete and continuous. It is the universal tool for describing distributions.

Think of the CDF as a running total — it accumulates all PMF values from $-\infty$ up to $x$.

**Three properties every valid CDF must satisfy:**

**Property 1 — Increasing:**
$$x_1 \leq x_2 \implies F(x_1) \leq F(x_2)$$
$P(X \leq x_2)$ includes everything in $P(X \leq x_1)$ plus more. Probability can only accumulate, never decrease.

**Property 2 — Right-continuous:**
$$F(a) = \lim_{x \to a^+} F(x)$$
For discrete r.v.s, the CDF is completely flat between support values and jumps *at* each support value. The jump size equals the PMF value there. For integer-valued X this is even stronger — $F$ is literally constant between integers, not just right-continuous.

```
F(x)
|              ___________
|         ____|
|    ____|
|___|
|_________________________ x
   0    1    2    3    4
```

**Property 3 — Convergence to 0 and 1:**
$$\lim_{x \to -\infty} F(x) = 0 \qquad \text{and} \qquad \lim_{x \to +\infty} F(x) = 1$$

As $x \to -\infty$: no values of $X$ are $\leq x$, so probability = 0.
As $x \to +\infty$: all values of $X$ are $\leq x$, so:
$$\lim_{x \to \infty} F(x) = \lim_{x \to \infty} \sum_{n=0}^{x} P(X=n) = \sum_{n=0}^{\infty} P(X=n) = 1$$

The third property is just the PMF axiom expressed through the CDF — the boundary conditions are the PMF properties in disguise.

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

If $X$ is a random variable, then any function of $X$ is also a random variable.

$X^2$, $e^X$, $\sin(X)$, $g(X)$ for any $g : \mathbb{R} \to \mathbb{R}$ — all are random variables. Why? A random variable is a deterministic function on a random input. Applying another deterministic function on top still gives a deterministic function on a random input — still a random variable. Randomness flows from the original sample space through every transformation.

> **Definition 3.7.1:** For an experiment with sample space $S$, an r.v. $X$, and a function $g : \mathbb{R} \to \mathbb{R}$, $g(X)$ is the r.v. that maps $s$ to $g(X(s))$ for all $s \in S$.

$$s \xrightarrow{X} X(s) \xrightarrow{g} g(X(s))$$

This is function composition: $g(X) = g \circ X$. $g$ uses $X$'s output set as its own input — but the randomness always traces back to $S$.

### PMF of g(X) — The Master Formula

$$P(g(X) = y) = \sum_{x \,:\, g(x) = y} P(X = x)$$

Find every $x$ in the support of $X$ that maps to $y$ under $g$, then add up their probabilities.

**One-to-one g:** Only one $x$ maps to each $y$ → probability passes down unchanged:
$$P(Y = g(x)) = P(X = x)$$
The support just gets relabeled; probabilities are inherited directly.

**Many-to-one g:** Multiple $x$ values map to the same $y$ → probabilities merge and add up. This is the only interesting case requiring real work.

The formula handles both cases with one expression — one-to-one is just a special case where every sum has exactly one term.

> **Key insight:** Since random variables are deterministic, probability is born in $S$ and travels down through every function. One-to-one guarantees it arrives unchanged. Many-to-one is the only case where something interesting happens — probabilities of merging inputs add up.

### Two Common Mistakes

**Mistake 1 — Multiplying the PMF to get PMF of $2X$:**

Wrong: $P(2X = y) = 2 \times P(X = x)$. This makes probabilities sum to 2, violating the axiom.

Correct: $P(2X = y) = P(X = y/2)$. Since $g(x) = 2x$ is one-to-one, probability passes down unchanged. The PMF of $2X$ is a **horizontal stretch** of the PMF of $X$ — same heights, doubled support values. Not a vertical stretch.

**Mistake 2 — Same distribution means always equal:**

Wrong: if $X$ and $Y$ have the same distribution, then $P(X = Y) = 1$.

The PMF describes probability behaviour. Two r.v.s can have identical PMFs while mapping individual sample outcomes to completely different numbers.

| Situation | $P(X = Y)$ |
|-----------|------------|
| $X$ and $Y = 1-X$ (coin) | 0 — never equal |
| $X$ and $Z$ (independent flip) | 1/2 — sometimes equal |
| $X$ and itself | 1 — always equal |

All three cases can share the same Bern$(1/2)$ distribution. Same distribution $\neq$ same r.v.

---

# Independence of Random Variables

> **Definition:** Random variables $X$ and $Y$ are *independent* if:
> $$P(X \leq x, Y \leq y) = P(X \leq x) P(Y \leq y) \quad \text{for all } x, y \in \mathbb{R}$$

Knowing $X$'s value gives no information about $Y$, and vice versa.

**Discrete equivalent condition:**
$$P(X = x, Y = y) = P(X = x) P(Y = y)$$
for all $x, y$ in the respective supports. Much easier to check in practice.

### Proof — Why the Discrete Condition is Equivalent

We need to show that for discrete r.v.s, the CDF factoring condition is equivalent to the PMF factoring condition.

**PMF condition $\implies$ CDF condition:**

If $P(X = x, Y = y) = P(X = x)P(Y = y)$ for all $x, y$ in the supports, then for any $x, y$:

$$P(X \leq x, Y \leq y) = \sum_{x' \leq x} \sum_{y' \leq y} P(X = x', Y = y')$$

$$= \sum_{x' \leq x} \sum_{y' \leq y} P(X = x') P(Y = y')$$

$$= \left(\sum_{x' \leq x} P(X = x')\right)\left(\sum_{y' \leq y} P(Y = y')\right) = P(X \leq x) P(Y \leq y) \quad \checkmark$$

The double sum factors because each term already factors — summing over products of separate quantities gives the product of the sums.

**CDF condition $\implies$ PMF condition:**

If $P(X \leq x, Y \leq y) = P(X \leq x)P(Y \leq y)$ for all $x, y$, we recover the joint PMF by taking differences of the CDF at specific values $x_0, y_0$:

$$P(X = x_0, Y = y_0) = P(X \leq x_0, Y \leq y_0) - P(X \leq x_0^-, Y \leq y_0) - P(X \leq x_0, Y \leq y_0^-) + P(X \leq x_0^-, Y \leq y_0^-)$$

where $x_0^-$ means the largest support value strictly less than $x_0$. Since each CDF term factors by assumption, the whole expression factors into $P(X = x_0) \cdot P(Y = y_0)$. $\blacksquare$

**Independence of many r.v.s:**
$$P(X_1 \leq x_1, \ldots, X_n \leq x_n) = P(X_1 \leq x_1) \cdots P(X_n \leq x_n)$$

For infinitely many r.v.s: every finite subset must be independent.

**Pairwise vs mutual independence:** Full independence implies pairwise independence (let all other variables go to $\infty$), but pairwise independence does NOT imply full independence. Full independence is strictly stronger.

**i.i.d.:** Random variables that are **independent** and **identically distributed**. Two completely different concepts — each can hold or fail regardless of the other.

**Four cases to fully understand the distinction:**

**Case 1 — Independent AND identically distributed (i.i.d.):**
Let $X$ = result of a die roll, $Y$ = result of a second independent die roll. Both $X, Y \sim \text{DUnif}(\{1,\ldots,6\})$ and independent — one roll tells you nothing about the other. This is the i.i.d. case.

**Case 2 — Independent but NOT identically distributed:**
Let $X$ = result of a die roll, $Y$ = closing price of the Dow Jones stock index a month from now. $X$ and $Y$ are independent (a die roll tells you nothing about the stock market), but they clearly do not have the same distribution.

**Case 3 — Identically distributed but NOT independent:**
Let $X$ = number of Heads in $n$ coin tosses, $Y$ = number of Tails in those same $n$ tosses. Both $X, Y \sim \text{Bin}(n, 1/2)$ — same distribution — but $Y = n - X$ so knowing $X$ tells you $Y$ exactly. Completely dependent: $P(Y = n - X) = 1$.

**Case 4 — Dependent AND not identically distributed:**
Let $X$ = indicator of whether the majority party retains control of the House after the next election, $Y$ = average favorability rating of the majority party in polls taken within a month of the election. $X$ and $Y$ are dependent (poll ratings and election outcomes are related) and do not share the same distribution.

> **The core distinction:** Same distribution describes how a single r.v. behaves in isolation — what values it takes and with what probabilities. Independence describes how two r.v.s relate to each other — whether one gives information about the other. These are completely orthogonal properties.

| | Independent | Identically distributed |
|--|-------------|------------------------|
| Meaning | Knowing one tells you nothing about the others | Same PMF / distribution |
| Case 1 i.i.d. | ✅ | ✅ |
| Case 2 | ✅ | ❌ |
| Case 3 | ❌ | ✅ |
| Case 4 | ❌ | ❌ |

**Functions of independent r.v.s:** If $X \perp Y$, then $g(X) \perp h(Y)$ for any functions $g$, $h$. Knowing $g(X)$ can only reveal information about $X$ — and since $X$ tells you nothing about $Y$, it tells you nothing about $h(Y)$ either.

---

# Sum of Independent Binomials

**Theorem:** If $X \sim \text{Bin}(n,p)$, $Y \sim \text{Bin}(m,p)$, and $X \perp Y$, then:
$$X + Y \sim \text{Bin}(n+m, p)$$

Requires the **same $p$** — if success probabilities differ, the sum is not Binomial.

Three proofs, each using a different technique:

**Proof 1 — Story (fastest):**
$X$ counts successes in $n$ trials, $Y$ in $m$ additional independent trials, all with the same $p$. Together that is $n+m$ independent trials each with probability $p$ — exactly $\text{Bin}(n+m,p)$ by definition. $\square$

**Proof 2 — Bernoulli indicators (elegant):**
Write $X = X_1 + \cdots + X_n$ and $Y = Y_1 + \cdots + Y_m$ where all $X_i, Y_j \overset{\text{i.i.d.}}{\sim} \text{Bern}(p)$. Since $X \perp Y$, all $n+m$ indicators are mutually independent with the same Bern$(p)$ distribution. A sum of $n+m$ i.i.d. Bern$(p)$ r.v.s is $\text{Bin}(n+m,p)$ by definition. $\square$

**Proof 3 — PMF convolution (most algebraic, most instructive):**

Condition on $X$ using LOTP:
$$P(X+Y=k) = \sum_{j=0}^{k} P(Y=k-j \mid X=j) P(X=j) = \sum_{j=0}^{k} P(Y=k-j) P(X=j)$$

(Independence lets us drop the condition on $X$ when asking about $Y$. We are not making $P(Y=k-j \mid X=j)$ become 1 — we are simply using independence to replace the conditional probability with the unconditional one.)

**The dice analogy for LOTP — building intuition:**

The same conditioning technique applies to a simpler question first: what is the probability two dice sum to 8?

$$P(\text{sum} = 8) = \sum_{j=1}^{6} P(\text{die 2} = 8 - j) \cdot P(\text{die 1} = j)$$

For each value die 1 could take, figure out exactly what die 2 needs to be, then weight by how likely die 1 was. $P(D_2 = 7) = 0$ since a die cannot show 7, so the $j=1$ term vanishes. The valid terms give:

$$= \frac{1}{6} \cdot \frac{1}{6} + \frac{1}{6} \cdot \frac{1}{6} + \frac{1}{6} \cdot \frac{1}{6} + \frac{1}{6} \cdot \frac{1}{6} + \frac{1}{6} \cdot \frac{1}{6} = \frac{5}{36}$$

You are just breaking the event $\{\text{sum} = 8\}$ into all the ways it could happen, finding the probability of each way, and adding them up. The Binomial proof uses exactly the same logic — just with Binomial PMFs instead of uniform ones.

Substitute Binomial PMFs and collect powers of $p$ and $q = 1-p$:
$$P(X+Y=k) = p^k q^{n+m-k} \sum_{j=0}^{k} \binom{n}{j}\binom{m}{k-j}$$

The $j$'s cancel in the exponents **because $p$ is shared** — with different $p$'s they would not cancel and the sum could not be factored out. Apply Vandermonde's Identity:

$$\sum_{j=0}^{k} \binom{n}{j}\binom{m}{k-j} = \binom{n+m}{k}$$

Result: $P(X+Y=k) = \binom{n+m}{k} p^k q^{n+m-k}$ — exactly $\text{Bin}(n+m,p)$ PMF. $\square$

**Vandermonde's Identity** — proved three ways across the course:
1. Combinatorial story (choose $k$ from $n$ men and $m$ women, split by gender)
2. Binomial convolution (the algebra above)
3. Hypergeometric PMF summing to 1

---

# Connections Between Binomial and Hypergeometric

$$\text{Binomial} \xrightarrow{\text{condition on total}} \text{Hypergeometric}$$
$$\text{Hypergeometric} \xrightarrow{\text{population} \to \infty} \text{Binomial}$$

**Binomial → Hypergeometric by conditioning:**

Start with $X \sim \text{Bin}(n,p)$ and $Y \sim \text{Bin}(m,p)$ independent. Condition on the total $X+Y = K$. Once the total is fixed, the trials are no longer independent — knowing the total constrains the counts. Asking for the distribution of $X$ given the total is exactly the Hypergeometric: draw $n$ from a population of $n+m$ objects ($K$ successes, $n+m-K$ failures) without replacement. Conditioning removes independence and produces the Hypergeometric.

**Hypergeometric → Binomial by taking a limit:**

Start with $\text{HGeom}(w, b, n)$. Let the population $w + b \to \infty$ while keeping $\frac{w}{w+b} = p$ fixed. As the population grows infinitely large, removing one object barely changes the composition of what remains. Drawing without replacement from an effectively infinite population is the same as drawing with replacement — the dependence vanishes. In the limit, $\text{HGeom}(w, b, n) \to \text{Bin}(n, p)$.

> **Practical implication:** When sampling $n$ people from a large population $N$ where $n \ll N$, the Hypergeometric can be safely approximated by the Binomial. The approximation improves as $n/N \to 0$.

---

# Summary Cheatsheet

| Concept | Key Formula / Fact |
|---------|-------------------|
| Random variable | Deterministic function $X: S \to \mathbb{R}$; randomness lives in $P$, not $X$ |
| Support | $\{x : P(X=x) > 0\}$ — where probability mass actually lives |
| PMF | $p_X(x) = P(X=x)$; nonneg + sums to 1 |
| PMF pipeline | Support → event $\{X=x\}$ → add outcome probabilities → done |
| Bernoulli | $P(X=1)=p$, $P(X=0)=1-p$; indicator r.v. of any event |
| Binomial PMF | $\binom{n}{k}p^k(1-p)^{n-k}$; requires independent trials, same $p$ |
| Binomial as sum | $X = X_1 + \cdots + X_n$, $X_i \overset{\text{i.i.d.}}{\sim} \text{Bern}(p)$ |
| Binomial additivity | $\text{Bin}(n,p) + \text{Bin}(m,p) = \text{Bin}(n+m,p)$ (same $p$, independent) |
| Hypergeometric PMF | $\frac{\binom{w}{k}\binom{b}{n-k}}{\binom{w+b}{n}}$; without replacement, equally likely |
| Vandermonde Identity | $\sum_{j=0}^k \binom{n}{j}\binom{m}{k-j} = \binom{n+m}{k}$ |
| DUnif PMF | $\frac{1}{\vert C \vert}$ for $x \in C$; reduces to counting problems |
| CDF | $F(x) = P(X \leq x)$; nondecreasing, right-continuous, $0 \to 1$ |
| PMF → CDF | $F(x) = \sum_{x' \leq x} p_X(x')$ (running total) |
| CDF → PMF | $P(X=x_0) = F(x_0) - F(x_0^-)$ (size of jump) |
| PMF of $g(X)$ | $P(g(X)=y) = \sum_{x: g(x)=y} P(X=x)$ |
| One-to-one $g$ | Probability passes down unchanged |
| Many-to-one $g$ | Probabilities of merging inputs add up |
| Independence | $P(X \leq x, Y \leq y) = P(X \leq x)P(Y \leq y)$ |
| Discrete independence | $P(X=x, Y=y) = P(X=x)P(Y=y)$ |
| i.i.d. | Independent AND identically distributed |
| HGeom ≈ Binomial | When population $\gg$ sample size |