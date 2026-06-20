---
title: Discrete Uniform, CDF, and Functions of R.V.s
subject: probability
chapter: 06-continuous-random-variables
tags:
- probability
- mathematics
date: '2026-06-18'
updated: '2026-06-19'
status: complete
difficulty: intermediate
---
> *Introduction to Probability* — Blitzstein & Hwang

---

## Table of Contents

- [Discrete Uniform Distribution](#discrete-uniform-distribution)
  - [Definition](#definition)
  - [PMF](#pmf)
  - [Examples of C](#examples-of-c)
  - [Probability of a Subset](#probability-of-a-subset)
  - [Reduces to Counting Problems](#reduces-to-counting-problems)
  - [What is X Here? The Identity Function](#what-is-x-here-the-identity-function)
  - [Worked Example — Slips of Paper](#worked-example--slips-of-paper)
  - [Summary](#summary-discrete-uniform)

- [Cumulative Distribution Functions](#cumulative-distribution-functions)
  - [Why the CDF?](#why-the-cdf)
  - [Definition](#definition-cdf)
  - [From PMF to CDF and Back](#from-pmf-to-cdf-and-back)
  - [Valid CDFs — Three Properties](#valid-cdfs--three-properties)
  - [PMF vs CDF — Side by Side](#pmf-vs-cdf--side-by-side)
  - [Summary](#summary-cdf)

- [Functions of Random Variables](#functions-of-random-variables)
  - [Core Idea](#core-idea)
  - [Definition](#definition-functions)
  - [The Pebble World View](#the-pebble-world-view)
  - [g Uses X's Output as Its Input](#g-uses-xs-output-as-its-input)
  - [Basketball Example](#basketball-example)
  - [Finding the PMF of Y = g(X)](#finding-the-pmf-of-y--gx)
  - [One-to-One vs Many-to-One](#one-to-one-vs-many-to-one)
  - [Worked Examples](#worked-examples)
  - [Two Common Mistakes — Sympathetic Magic](#two-common-mistakes--sympathetic-magic)
  - [Summary](#summary-functions)

---

# Discrete Uniform Distribution

## Definition

> **Story** — Let $C$ be a finite, nonempty set of numbers. Choose one of these numbers uniformly at random (i.e., all values in $C$ are equally likely). Call the chosen number $X$. Then $X$ is said to have the **Discrete Uniform distribution** with parameter $C$, written $X \sim \text{DUnif}(C)$.

---

## PMF

$$P(X = x) = \frac{1}{|C|} \quad \text{for } x \in C \quad (\text{and } 0 \text{ otherwise})$$

$|C|$ is just the **size** (number of elements) of the set $C$. Since a PMF must sum to 1, and there are $|C|$ values each getting equal probability, each gets exactly $\frac{1}{|C|}$.

**Check — sums to 1:**
$$|C| \text{ values} \times \frac{1}{|C|} = 1 \quad \checkmark$$

---

## Examples of $C$

| $C$ | Meaning | $X$ |
|---|---|---|
| $\{1,2,3,4,5,6\}$ | Fair die | The number that lands |
| $\{1,2,\ldots,n\}$ | Any integer from 1 to $n$ | The specific integer selected |
| $\{0,1\}$ | Coin flip (coded) | $1 =$ Heads, $0 =$ Tails |

Note: $\{H, T\}$ is not numeric, so for a coin flip you would define $X = 1$ if Heads, $X = 0$ if Tails — which is just a Bernoulli r.v. in disguise.

---

## Probability of a Subset

For any $A \subseteq C$:

$$P(X \in A) = \frac{|A|}{|C|}$$

Number of favorable values divided by total values — **exactly the naive definition of probability!**

**Example — fair die:**

$C = \{1,2,3,4,5,6\}$, $A = \{2,4,6\}$ (even numbers), $|A| = 3$, $|C| = 6$:
$$P(X \in A) = \frac{3}{6} = \frac{1}{2} \quad \checkmark$$

---

## Reduces to Counting Problems

> "As with questions based on the naive definition of probability, questions based on a Discrete Uniform distribution reduce to counting problems."

Because all values are equally likely, any probability question just becomes:
$$\frac{\text{count of favorable outcomes}}{\text{total outcomes}}$$

No complicated PMF machinery needed — just count. This is the same structure as the naive definition of probability from Chapter 1, now expressed through the language of random variables.

---

## What is $X$ Here? The Identity Function

In previous examples, the sample space was non-numeric (e.g. $\{HH, HT, TH, TT\}$) and $X$ had to *map* outcomes to numbers — a non-trivial function. Here, the sample space $C$ is **already numeric**, so $X$ is the **identity function**:

$$X(s) = s \quad \text{for all } s \in C$$

$X$ just returns whatever value was picked. It is still a deterministic function on the sample space — just a trivial one:

$$X(1) = 1, \quad X(2) = 2, \quad X(3) = 3, \quad \ldots$$

| | Non-numeric sample space | Numeric sample space (DUnif) |
|---|---|---|
| Sample space | $\{HH, HT, TH, TT\}$ | $C = \{1,2,\ldots,6\}$ |
| What $X$ does | Maps outcomes to numbers | Returns the number itself |
| Type of $X$ | Non-trivial function | Identity function |

**Key consequence:** When $X$ is the identity, the sample space IS the support of $X$. So naive probability applies directly — no need for the full pipeline of mapping outcomes through $X$ first. This is exactly why DUnif questions reduce to counting problems.

---

## Worked Example — Slips of Paper

There are 100 slips of paper numbered $1, 2, \ldots, 100$, each number appearing once. Five slips are drawn one at a time.

### Random Sampling With Replacement (equal probabilities)

**(a) Distribution of how many drawn slips have value $\geq 80$:**

Each draw independently has probability $\frac{21}{100}$ of landing $\geq 80$ (the values 80 through 100). By the Binomial story, the count follows $\text{Bin}(5, 21/100)$.

**(b) Distribution of the value of the $j$-th draw:**

By symmetry, every slip is equally likely to be drawn at any position. So $X_j \sim \text{DUnif}(1, 2, \ldots, 100)$ for any $j$.

**(c) $P(\text{number 100 drawn at least once})$:**

Using complements — it is easier to find the probability that 100 is *never* drawn:
$$1 - P(X_1 \neq 100, \ldots, X_5 \neq 100) = 1 - \left(\frac{99}{100}\right)^5 \approx 0.049$$

### Random Sampling Without Replacement

**(d) Distribution of how many drawn slips have value $\geq 80$:**

Now drawing without replacement — the count follows the **Hypergeometric** distribution (sampling without replacement from a population with two types).

**(e) Distribution of the value of the $j$-th draw:**

Still $Y_j \sim \text{DUnif}(1, 2, \ldots, 100)$ by symmetry — even without replacement, each slip is equally likely to end up in any particular position when viewed in isolation.

**(f) $P(\text{number 100 is in the sample})$:**

$$P(Y_1 = 100 \text{ or } Y_2 = 100 \text{ or } \cdots \text{ or } Y_5 = 100) = \frac{5}{100} = \frac{1}{20} = 0.05$$

This can also be seen directly: by symmetry, the probability that slip 100 is among the 5 chosen is just $\frac{5}{100}$.

> **Key insight:** Sampling with and without replacement give the **same marginal distribution** for any single draw — $Y_j \sim \text{DUnif}$ either way. The difference only shows up when looking at *multiple* draws together, where without-replacement draws are dependent (knowing one slip was drawn affects the others) while with-replacement draws are independent.

---

## Summary {#summary-discrete-uniform}

- $X \sim \text{DUnif}(C)$ means every value in $C$ is equally likely, each with probability $\frac{1}{|C|}$.
- $P(X \in A) = \frac{|A|}{|C|}$ — reduces directly to counting.
- $X$ is the identity function when the sample space is already numeric — the trivial case.
- When $X$ is trivial, naive probability applies directly without needing the full mapping pipeline.
- Discrete Uniform is the simplest distribution — **every probability question is just a counting problem.**

---

# Cumulative Distribution Functions

## Why the CDF? {#why-the-cdf}

The PMF gives you the probability at each *exact* point. The distribution gives you the full picture. But sometimes you want just one accumulated value — the probability that $X$ lands *anywhere up to* a certain threshold. That is what the CDF does.

> "Another function that describes the distribution of an r.v. is the cumulative distribution function (CDF). Unlike the PMF, which only discrete r.v.s possess, the CDF is defined for all r.v.s."

The CDF is more universal than the PMF — it works for both discrete and continuous random variables, making it a fundamental tool throughout the rest of probability and statistics.

---

## Definition {#definition-cdf}

**Definition:** The *cumulative distribution function* (CDF) of an r.v. $X$ is the function $F_X$ given by:

$$F_X(x) = P(X \leq x)$$

When there is no risk of ambiguity, we drop the subscript and just write $F$.

Think of the CDF as a **running total** — it accumulates all the PMF values from $-\infty$ up to $x$. As $x$ increases, $F(x)$ can only stay the same or grow — it never decreases.

---

## From PMF to CDF and Back

**Example:** Let $X \sim \text{Bin}(4, 1/2)$.

- **PMF → CDF:** To find $F(1.5)$, add up all PMF values at points $\leq 1.5$:
$$F(1.5) = P(X \leq 1.5) = P(X = 0) + P(X = 1)$$

- **CDF → PMF:** The jump in the CDF at any point equals the PMF value there:
$$P(X = 2) = F(2) - F(1.5)$$
The size of the jump at $x = 2$ is exactly $P(X = 2)$.

Since $X$ is integer-valued and can never land between 1 and 2:
$$P(X \leq 1.5) = P(X \leq 1) \quad \checkmark$$

The CDF and PMF carry the **same information** — you can always recover one from the other.

---

## Valid CDFs — Three Properties

**Theorem:** Any CDF $F$ must satisfy all three of the following properties.

### Property 1 — Increasing

$$x_1 \leq x_2 \implies F(x_1) \leq F(x_2)$$

This makes complete sense: $P(X \leq x_2)$ includes everything in $P(X \leq x_1)$ plus potentially more. A larger $x$ means you are accumulating over a larger set of outcomes, so the probability can only stay the same or go up. The CDF **can never decrease** as $x$ increases.

---

### Property 2 — Right-Continuous

Wherever there is a jump, the CDF is **continuous from the right**:

$$F(a) = \lim_{x \to a^+} F(x)$$

For discrete r.v.s, the CDF is completely flat between support values and jumps *at* each support value. The jump size at any point equals the PMF value there.

**Right-continuous means:** $F(a)$ includes the probability at point $a$ itself — i.e., $P(X \leq a)$ includes $P(X = a)$. The jump happens *at* the support value, not just after it.

**Visualizing (integer-valued $X$):**

```
F(x)
|              ___________
|         ____|
|    ____|
|___|
|_________________________ x
   0    1    2    3    4
```

Flat between integers → jumps AT integers.

**For integer-valued $X$, right-continuity is even stronger than required:**

$F(a + b) = F(a)$ for any $b > 0$ small enough that $a + b < a + 1$ (i.e., there is no integer between $a$ and $a+b$).

For example, with $a = 4.9$: this holds for any $0 < b < 0.1$, since no integer exists in the interval $(4.9, 4.95)$. The CDF is not just right-continuous — it is **literally constant** on the right until the next integer value.

The only place right-continuity is ever interesting is exactly *at* integer values in the support:
- Just to the right of 4: $F(4.0001) = F(4)$ ✓ — includes the jump at 4
- Just to the left of 4: $F(3.9999) = F(3)$ ← does not include the jump at 4, so it is different

---

### Property 3 — Convergence to 0 and 1

$$\lim_{x \to -\infty} F(x) = 0 \qquad \text{and} \qquad \lim_{x \to \infty} F(x) = 1$$

**Why $F \to 0$:** As $x \to -\infty$, there are no values of $X$ that are $\leq x$, so $P(X \leq x) = 0$.

**Why $F \to 1$:** As $x \to \infty$, ALL values of $X$ are eventually $\leq x$, so $P(X \leq x) = 1$.

**Formally (for non-negative integer-valued $X$, e.g. $X \in \{0, 1, 2, \ldots\}$):**

For the lower boundary: $F(x) = 0$ for all $x < 0$, since $X$ can never be negative — $P(X \leq x) = 0$ for any $x < 0$. ✓

For the upper boundary:
$$\lim_{x \to \infty} F(x) = \lim_{x \to \infty} P(X \leq x) = \lim_{x \to \infty} \sum_{n=0}^{x} P(X = n) = \sum_{n=0}^{\infty} P(X = n) = 1$$

The last step follows directly because the PMF must sum to 1 over all its values. So the third property is just the PMF axiom expressed through the CDF lens — **the two boundary conditions are the PMF properties in disguise.**

> The beautiful circle: a valid PMF sums to 1 → the CDF accumulates all of it → the CDF reaches 1 at infinity → third criterion satisfied ✓

---

## PMF vs CDF — Side by Side

| | PMF | CDF |
|---|---|---|
| Formula | $P(X = x)$ | $P(X \leq x)$ |
| What it gives | Probability at one exact point | Accumulated probability up to $x$ |
| Sums / reaches | Sums to 1 over all support | Reaches 1 as $x \to \infty$ |
| Shape (discrete) | Spikes at support values | Staircase — flat then jump |
| At each support value | Spike height = probability | Jump size = PMF value there |
| Defined for | Discrete r.v.s only | All r.v.s (discrete and continuous) |

Think of the PMF as telling you the probability at each individual step, and the CDF as the running bank balance — only goes up, never decreases, starts at 0 and ends at 1.

---

## Summary {#summary-cdf}

- The CDF $F(x) = P(X \leq x)$ accumulates probability from left to right.
- It is a **staircase function** for discrete r.v.s — flat between support values, jumping at each one.
- Three must-have properties: **increasing**, **right-continuous**, **converges to 0 and 1**.
- The boundary properties (converging to 0 and 1) are just the PMF axiom in disguise.
- CDF and PMF carry the same information — you can always recover one from the other.
- The CDF is more general than the PMF — it is defined for all r.v.s, not just discrete ones.

---

# Functions of Random Variables

## Core Idea

If $X$ is a random variable, then **any function of $X$ is also a random variable**.

$X^2$, $e^X$, $\sin(X)$, $g(X)$ for any $g : \mathbb{R} \to \mathbb{R}$ — all are random variables.

**Why?** A random variable is a deterministic function on a random input (the sample space). If you apply another deterministic function on top of that output, the result is still a deterministic function on a random input — and that is exactly the definition of a random variable. Randomness flows from the original sample space through every transformation, no matter how many layers deep.

---

## Definition {#definition-functions}

**Definition:** For an experiment with sample space $S$, an r.v. $X$, and a function $g : \mathbb{R} \to \mathbb{R}$, $g(X)$ is the r.v. that maps $s$ to $g(X(s))$ for all $s \in S$.

$$s \xrightarrow{X} X(s) \xrightarrow{g} g(X(s))$$

This is just **function composition**: $g(X) = g \circ X$. First apply $X$ to the sample outcome, then apply $g$ to the result.

> "If $X$ crystallizes to 4, then $g(X)$ crystallizes to 2." (for $g(x) = \sqrt{x}$)

"Crystallizes" is the book's term for taking on a specific value in a particular outcome — a useful word for saying the r.v. has landed on a number.

---

## The Pebble World View

Remember: each sample outcome $s$ is a pebble with a probability. $X$ labels each pebble with a number. Applying $g$ to $X$ just **relabels every pebble** with a new number — creating a new mapping from sample outcomes to real numbers, which is exactly the definition of a new random variable.

| Pebble | $X(s)$ | $g(X(s))$ |
|---|---|---|
| $s_1$ | $X(s_1)$ | $g(X(s_1))$ |
| $s_2$ | $X(s_2)$ | $g(X(s_2))$ |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $s_6$ | $X(s_6)$ | $g(X(s_6))$ |

$g(X)$ never touches the sample space directly — it only transforms the outputs of $X$. But since those outputs came from a random input (the original sample space), $g(X)$ is still random.

**The full pipeline:**

$$S \xrightarrow{X} \{X(s_1), \ldots, X(s_6)\} \xrightarrow{g} \{g(X(s_1)), \ldots, g(X(s_6))\}$$

All randomness originates in $S$ and travels down through every function applied on top. No function in the chain introduces or removes randomness — it all flows from the original experiment.

---

## g Uses X's Output as Its Input

A natural question: if $X$ was a function from $S$ to numbers, and $g$ takes numbers as input — isn't $g$ effectively treating $X$'s outputs as its own "sample space"?

Yes — in a sense. The chain is:

| Function | Input | Output |
|---|---|---|
| $X$ | Original sample space $S$ | Numbers $\{X(s_1), \ldots, X(s_6)\}$ |
| $g$ | $X$'s outputs as its input | New numbers $\{g(X(s_1)), \ldots, g(X(s_6))\}$ |

But crucially, $g(X)$ is still ultimately a function of the **original sample space** $S$, because $X(s)$ came from $S$. The randomness always traces back to which pebble $s$ gets picked. This is function composition:

$$g(X(s)) = (g \circ X)(s)$$

Just two functions chained together — still one deterministic function on the original random input $S$.

---

## Basketball Example

Let $X$ = number of wins for team A in a seven-game series, with $X \sim \text{Bin}(7, 1/2)$ (teams evenly matched, games independent).

Define two functions:
- $g(x) = 7 - x$ → $g(X) = 7 - X$ = wins for team B (the complement)
- $h(x) = 1$ if $x \geq 4$, $h(x) = 0$ if $x < 4$ → $h(X)$ = indicator of team A winning the majority

| $X$ (team A wins) | $g(X) = 7 - X$ (team B wins) | $h(X)$ (team A majority?) |
|---|---|---|
| 0 | 7 | 0 |
| 1 | 6 | 0 |
| 2 | 5 | 0 |
| 3 | 4 | 0 |
| 4 | 3 | 1 |
| 5 | 2 | 1 |
| 6 | 1 | 1 |
| 7 | 0 | 1 |

Both $g(X)$ and $h(X)$ are r.v.s. Since $X$ is an r.v., every function of $X$ is automatically also an r.v. $h(X)$ is an **indicator random variable** — it equals 1 or 0 depending on whether team A wins, making $h(X) \sim \text{Bern}(p)$ for some $p$.

---

## Finding the PMF of $Y = g(X)$

### The Master Formula

Let $X$ be a discrete r.v. and $g : \mathbb{R} \to \mathbb{R}$. The **support of $g(X)$** is the set of all $y$ such that $g(x) = y$ for at least one $x$ in the support of $X$ — in other words, only values actually reachable from $X$'s support through $g$.

The PMF of $g(X)$ is:

$$P(g(X) = y) = \sum_{x \,:\, g(x) = y} P(X = x)$$

for all $y$ in the support of $g(X)$.

**In plain terms:** find every $x$ value in $X$'s support that maps to $y$ under $g$, then add up all their probabilities. The summation automatically handles all cases — one-to-one and many-to-one — with the same formula.

---

## One-to-One vs Many-to-One

### One-to-One $g$ — Trivial Case

Different inputs always give different outputs: $g(x_1) \neq g(x_2)$ whenever $x_1 \neq x_2$.

Only one $x$ maps to each $y$ → the sum has exactly one term → **probability passes down unchanged:**

$$P(Y = g(x)) = P(X = x)$$

The support just gets relabeled with new values; probabilities are inherited directly and unchanged.

**Why this makes sense:** Since random variables are deterministic, all randomness lives in the original sample space. With one-to-one $g$, there is a perfect correspondence between each old value and each new value — so the probability just travels down unchanged through the chain.

**Example** — $g(x) = \sqrt{x}$, $X$ support $= \{1, 4, 9\}$, each equally likely:

| $x$ | $P(X=x)$ | $g(x) = \sqrt{x}$ | $P(Y = g(x))$ |
|---|---|---|---|
| 1 | $1/3$ | 1 | $1/3$ |
| 4 | $1/3$ | 2 | $1/3$ |
| 9 | $1/3$ | 3 | $1/3$ |

Probabilities carry over directly ✓ — the support changed from $\{1,4,9\}$ to $\{1,2,3\}$ but the probabilities stayed $1/3$ each.

---

### Many-to-One $g$ — The Only Interesting Case

Multiple $x$ values map to the same $y$ → those probabilities **merge and add up:**

$$P(Y = y) = \sum_{\{x \,:\, g(x) = y\}} P(X = x)$$

This is the only case requiring real work. For one-to-one $g$, the probabilities just pass down — trivial. For many-to-one $g$, you must identify which $x$ values collapse together and sum their probabilities.

**Example** — $g(x) = x^2$, $X$ support $= \{-2,-1,0,1,2\}$, each with probability $1/5$:

| $y$ | $x$ values where $g(x) = y$ | Calculation | $P(Y = y)$ |
|---|---|---|---|
| 0 | $\{0\}$ | $1/5$ | $1/5$ |
| 1 | $\{-1, 1\}$ | $1/5 + 1/5$ | $2/5$ |
| 4 | $\{-2, 2\}$ | $1/5 + 1/5$ | $2/5$ |

Note: the support of $Y$ is $\{0, 1, 4\}$, which is smaller than the support of $X$ because $g$ collapsed pairs together. The probabilities still sum to $1/5 + 2/5 + 2/5 = 1$ ✓.

The general formula unifies both cases — one-to-one is just a special case where every sum has exactly one term.

> **Key insight:** Since random variables are deterministic, probability is born in $S$ and travels down through every function applied on top. One-to-one mapping guarantees it arrives unchanged. Many-to-one is the only case where something interesting happens — probabilities of merging inputs add up.

---

## Worked Examples

### Example — Random Walk

A particle starts at 0. At each step it moves $+1$ (right) or $-1$ (left), each with probability $\frac{1}{2}$, independently. After $n$ steps, let $Y$ be the particle's position.

**Setting up $Y$ as a function of a Binomial:**

Think of each step as a Bernoulli trial — right is success, left is failure. Let $X$ = number of right steps, so $X \sim \text{Bin}(n, 1/2)$.

- Number of right steps: $X$
- Number of left steps: $n - X$
- Net position: $Y = X - (n - X) = 2X - n$

So $Y = g(X)$ where $g(x) = 2x - n$. Since $g$ is one-to-one (linear with non-zero slope), probability passes down unchanged:

$$P(Y = k) = P(2X - n = k) = P\!\left(X = \frac{n+k}{2}\right) = \binom{n}{\frac{n+k}{2}} \left(\frac{1}{2}\right)^n$$

This is valid for $k \in \{-n, -n+2, \ldots, n-2, n\}$ — values of $k$ such that $n+k$ is even (otherwise $\frac{n+k}{2}$ is not an integer and the probability is 0). $Y$ can only take even-spaced values because each step changes position by 2 (either $+1$ or $-1$ from both sides).

---

### Example — Distance from Origin

Continuing the random walk above: let $D = |Y|$ = the particle's distance from the origin after $n$ steps.

$D = |2X - n|$ — this is **not** one-to-one since $|k| = |-k|$. Both $Y = k$ and $Y = -k$ give $D = k$. So the event $\{D = k\}$ is the same as $\{Y = k\} \cup \{Y = -k\}$, and these two events are disjoint (since $k \neq -k$ for $k \geq 1$).

We can write $D = |Y|$ as $D = h(Y)$ where $h(y) = |y|$ — a many-to-one function for $y \neq 0$. Using the master formula:

$$P(D = 0) = P(Y = 0) = \binom{n}{n/2} \left(\frac{1}{2}\right)^n \quad \text{(only possible if } n \text{ is even)}$$

$$P(D = k) = P(Y = k) + P(Y = -k) = 2\binom{n}{\frac{n+k}{2}}\left(\frac{1}{2}\right)^n \quad \text{for } k \geq 1$$

This is a direct application of the many-to-one formula: two $y$ values ($+k$ and $-k$) collapse into one $d$ value ($k$), so their probabilities add.

---

## Two Common Mistakes — "Sympathetic Magic"

The book uses the term "sympathetic magic" for mistakes that *look* like valid manipulations but are logically wrong — they follow a superficial pattern without understanding the actual definition.

### Mistake 1 — Multiplying the PMF to get PMF of $2X$

**Wrong:** $P(2X = y) = 2 \times P(X = x)$

The reasoning behind this mistake: "I multiplied $X$ by 2, so I multiply the PMF by 2." This is sympathetic magic — scaling $X$ by 2 does not scale probabilities by 2.

**Why it fails:** Multiplying all probabilities by 2 would make them sum to 2, not 1 — violating the fundamental axiom of probability.

**Correct approach — use the definition:**

$$P(2X = y) = \sum_{x \,:\, 2x = y} P(X = x) = P\!\left(X = \frac{y}{2}\right)$$

Since $g(x) = 2x$ is one-to-one, only one $x$ maps to each $y$ (namely $x = y/2$). Probability passes down unchanged — the support stretches horizontally but probabilities stay the same.

**Example** — $X$ with support $\{0,1,2,3,4\}$:

| $X$ support | $P(X=x)$ | $2X$ support | $P(2X = y)$ |
|---|---|---|---|
| 0 | $p_0$ | 0 | $p_0$ |
| 1 | $p_1$ | 2 | $p_1$ |
| 2 | $p_2$ | 4 | $p_2$ |
| 3 | $p_3$ | 6 | $p_3$ |
| 4 | $p_4$ | 8 | $p_4$ |

The PMF of $2X$ is a **horizontal stretch** of the PMF of $X$ — same heights (probabilities), new positions (support values doubled). It is not a vertical stretch. Note also that $X$ can take odd values, but $2X$ is necessarily even.

---

### Mistake 2 — Same Distribution Means Always Equal

**Wrong:** If $X$ and $Y$ have the same distribution, then $P(X = Y) = 1$.

The reasoning behind this mistake: "same distribution means they behave the same, so they must always be equal." This confuses probability *behaviour* with the actual *function* on the sample space.

**Why it fails:** Same distribution means same PMF — same probability of each value. But two r.v.s can have identical PMFs while mapping individual sample outcomes to completely different numbers.

**Three levels of relationship, illustrated with coin flips:**

**Case 1 — $X$ and $Y = 1 - X$:**

$X$ = indicator of Heads on a fair coin → $X \sim \text{Bern}(1/2)$

$Y = 1 - X$ = indicator of Tails → $Y \sim \text{Bern}(1/2)$

Same distribution! But:
- When $X = 1$ (Heads), $Y = 1 - 1 = 0$ — they are different
- When $X = 0$ (Tails), $Y = 1 - 0 = 1$ — they are different

$X = Y$ is impossible. $P(X = Y) = 0$. They have the same PMF but are *never* equal.

**Case 2 — $X$ and $Z$ from independent flips:**

$X$ = indicator of Heads on flip 1 → $X \sim \text{Bern}(1/2)$

$Z$ = indicator of Heads on flip 2 (independent) → $Z \sim \text{Bern}(1/2)$

Same distribution! But:
$$P(Z = X) = P(HH \text{ or } TT) = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}$$

They are equal *sometimes* — half the time.

**Case 3 — $X$ compared to itself:**

$P(X = X) = 1$ — trivially always equal.

| Situation | $P(X = Y)$ | Interpretation |
|---|---|---|
| $X$ and $Y = 1-X$ | $0$ | Never equal — perfectly anti-correlated |
| $X$ and $Z$ (independent) | $1/2$ | Sometimes equal |
| $X$ and itself | $1$ | Always equal |

All three cases have the same Bern$(1/2)$ distribution. Yet their equality probabilities span the full range from 0 to 1.

> **The core distinction:** The **PMF** describes the probability behaviour of an r.v. — what values it takes and how often. The **r.v. itself** is a function on the sample space — a specific mapping from outcomes to numbers. Two functions can have identical PMFs while mapping individual sample outcomes to completely different numbers. Same distribution $\neq$ same r.v.

---

## Summary {#summary-functions}

- A function of an r.v. is still an r.v. — randomness flows from $S$ through every transformation in the chain.
- $g(X)$ is formally the composition $g \circ X$, mapping each sample outcome $s \mapsto g(X(s))$.
- $g$ effectively uses $X$'s output as its input, but the randomness always traces back to the original $S$.
- **PMF of $g(X)$:** for each $y$ in the support, find all $x$ values mapping to $y$ and add their probabilities.
- **One-to-one $g$:** trivial — probabilities pass down unchanged, support gets relabeled.
- **Many-to-one $g$:** the only interesting case — probabilities of inputs collapsing to the same output add up.
- Multiplying the PMF by a constant is wrong — it breaks the rule that probabilities sum to 1.
- Same distribution $\neq$ same r.v. — same PMF but possibly entirely different functions on the sample space.