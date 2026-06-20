---
title: Expectation, LOTUS, Variance, the Poisson Distribution, and Connections Between
  Poisson and Binomial
subject: probability
chapter: 05-expectation
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

- [Expectation of a Discrete Random Variable](#expectation-of-a-discrete-random-variable)
  - [Why Expectation?](#why-expectation)
  - [The Journey: Arithmetic Mean → Weighted Mean → Expectation](#the-journey-arithmetic-mean--weighted-mean--expectation)
    - [Arithmetic Mean](#1-arithmetic-mean)
    - [Weighted Mean](#2-weighted-mean)
    - [Expectation (Weighted Mean with Probabilities)](#3-expectation-weighted-mean-with-probabilities)
  - [Cleaner Notation](#cleaner-notation)
  - [Special Case: Equally Likely Outcomes](#special-case-equally-likely-outcomes)
  - [Worked Examples](#worked-examples-expectation)
    - [Example 1 — Bernoulli R.V.](#example-1--bernoulli-rv)
    - [Example 2 — Frequentist / Simulation Interpretation](#example-2--frequentist--simulation-interpretation)
  - [When Expectation is Undefined](#when-expectation-is-undefined)
  - [Key Properties and Warnings](#key-properties-and-warnings)
    - [Proposition 4.1.2 — Same Distribution → Same Expectation](#proposition-412--same-distribution--same-expectation)
    - [The Converse is FALSE](#the-converse-is-false)
    - [Warning 4.1.3 — Never Replace an R.V. with Its Expectation](#warning-413--never-replace-an-rv-with-its-expectation)
    - [Notation 4.1.4](#notation-414)
  - [Expectation Summary](#expectation-summary)

- [Law of the Unconscious Statistician (LOTUS)](#law-of-the-unconscious-statistician-lotus)
  - [The Problem LOTUS Solves](#the-problem-lotus-solves)
  - [The Theorem](#the-theorem)
  - [Why "Unconscious Statistician"?](#why-unconscious-statistician)
  - [A Special Case First — Why It's True for X³](#a-special-case-first--why-its-true-for-x3)
  - [The General Proof — Pebbles and Super-Pebbles](#the-general-proof--pebbles-and-super-pebbles)

- [Variance](#variance)
  - [Motivation — Why Variance?](#motivation--why-variance)
  - [Definition](#definition)
  - [Standard Deviation](#standard-deviation)
  - [The Continuous Case and the Gaussian](#the-continuous-case-and-the-gaussian)
  - [Why Squared Deviations?](#why-squared-deviations)
  - [Why Not Use Absolute Value Instead?](#why-not-use-absolute-value-instead)
  - [The Computational Formula for Variance](#the-computational-formula-for-variance)
  - [Properties of Variance](#properties-of-variance)
    - [Property 1 — Shifting](#property-1--shifting)
    - [Property 2 — Scaling](#property-2--scaling)
    - [Property 3 — Additivity for Independent R.V.s](#property-3--additivity-for-independent-rvs)
    - [Property 4 — Non-negativity and the Degenerate Case](#property-4--non-negativity-and-the-degenerate-case)
  - [Variance is NOT Linear](#variance-is-not-linear)
  - [Worked Example — Geometric and Negative Binomial Variance](#worked-example--geometric-and-negative-binomial-variance)
  - [Worked Example — Binomial Variance via Indicators](#worked-example--binomial-variance-via-indicators)
    - [Alternative — Finding E(X²) via Pairs of Trials](#alternative--finding-ex2-via-pairs-of-trials)

- [Poisson Distribution](#poisson-distribution)
  - [Definition](#definition-1)
  - [Validity — Why the PMF Sums to 1](#validity--why-the-pmf-sums-to-1)
    - [The Taylor Series Proof](#the-taylor-series-proof)
    - [What P(X = 0) Looks Like](#what-px--0-looks-like)
  - [Mean and Variance of a Poisson R.V.](#mean-and-variance-of-a-poisson-rv)
    - [Finding E(X) — The Cancellation Trick](#finding-ex--the-cancellation-trick)
    - [Finding Var(X) — The Calculus Method via LOTUS](#finding-varx--the-calculus-method-via-lotus)
    - [The Factorial Moment Method (Alternative)](#the-factorial-moment-method-alternative)
    - [Why Mean = Variance is Remarkable](#why-mean--variance-is-remarkable)
  - [Shape of the Poisson Distribution](#shape-of-the-poisson-distribution)
  - [The Poisson Paradigm (Law of Rare Events)](#the-poisson-paradigm-law-of-rare-events)
    - [What "Rare" Actually Means](#what-rare-actually-means)
    - [The Formal Statement](#the-formal-statement)
    - [Real-World Examples](#real-world-examples)
    - [The Bridge: From Binomial to Poisson](#the-bridge-from-binomial-to-poisson)
    - [The Error Bound — Stein-Chen Method](#the-error-bound--stein-chen-method)
    - [Why the Poisson is Not Exactly Correct](#why-the-poisson-is-not-exactly-correct)
  - [Occupancy Problems](#occupancy-problems)
    - [Setup](#setup)
    - [Expected Number of Empty Boxes — Indicator Method](#expected-number-of-empty-boxes--indicator-method)
    - [Why Indicator Variables Beat Brute Force](#why-indicator-variables-beat-brute-force)
    - [Probability That At Least One Box is Empty — Inclusion-Exclusion](#probability-that-at-least-one-box-is-empty--inclusion-exclusion)
    - [Worked Example — Poisson Approximation for At Least One Empty Box](#worked-example--poisson-approximation-for-at-least-one-empty-box)
  - [Conceptual Clarifications](#conceptual-clarifications)
    - [PMF vs CDF — A Common Confusion](#pmf-vs-cdf--a-common-confusion)
    - [Notation — k vs i as the Summation Index](#notation--k-vs-i-as-the-summation-index)
    - [The Interval Scaling Rule](#the-interval-scaling-rule)
    - [The Core Superpower — You Only Need λ](#the-core-superpower--you-only-need-λ)
    - [When the Poisson Breaks — Occupancy Problems](#when-the-poisson-breaks--occupancy-problems)
    - [Hash Tables — The Computer Science Connection](#hash-tables--the-computer-science-connection)

- [Connections Between Poisson and Binomial](#connections-between-poisson-and-binomial)
  - [The Grand Parallel](#the-grand-parallel)
  - [Sum of Independent Poissons](#sum-of-independent-poissons)
    - [The Intuition — Traffic Story](#the-intuition--traffic-story)
    - [The Proof — Full Derivation](#the-proof--full-derivation)
    - [The Missing Step — How the Binomial Theorem Appears](#the-missing-step--how-the-binomial-theorem-appears)
  - [Poisson Given a Sum of Poissons — Conditioning Gives Binomial](#poisson-given-a-sum-of-poissons--conditioning-gives-binomial)
    - [The Setup](#the-setup)
    - [The Proof — Four Magic Tricks](#the-proof--four-magic-tricks)
      - [Trick 1 — Bayes' Rule Setup](#trick-1--bayes-rule-setup)
      - [Trick 2 — The Great Cancellation](#trick-2--the-great-cancellation)
      - [Trick 3 — Combinatorics Emerge](#trick-3--combinatorics-emerge)
      - [Trick 4 — The Probability p Emerges](#trick-4--the-probability-p-emerges)
    - [The Final Result](#the-final-result)
  - [Poisson Approximation to Binomial — Limit Gives Poisson](#poisson-approximation-to-binomial--limit-gives-poisson)
    - [The Theorem](#the-theorem-1)
    - [The Proof — Four Blocks](#the-proof--four-blocks)
      - [Step 1 — Substitute p = λ/n](#step-1--substitute-p--λn)
      - [Step 2 — Shatter into Four Blocks](#step-2--shatter-into-four-blocks)
      - [Step 3 — Take the Limit on Each Block](#step-3--take-the-limit-on-each-block)
      - [Step 4 — Reassemble](#step-4--reassemble)
    - [The Error Bound](#the-error-bound)
  - [The Full Picture — Switching Tools on the Fly](#the-full-picture--switching-tools-on-the-fly)
  - [The Poisson Splitting Property](#the-poisson-splitting-property)
  - [Worked Example — Poisson Approximation in Practice](#worked-example--poisson-approximation-in-practice)

---

# Expectation of a Discrete Random Variable

## Why Expectation?

A distribution gives you the *full picture* of a random variable — every possible value and its probability. But sometimes that's too much information. Often you just want **one number** that summarizes the r.v.

> "It can be unwieldy to manage so many probabilities — so often we want just one number summarizing the 'average' value of the r.v."

That one-number summary is the **expected value**, also called the **expectation** or **mean**.

> Much of statistics is also about understanding *variability* — how spread out a distribution is. This is formalized with **variance** and **standard deviation**, which are themselves defined in terms of expected values.

---

## The Journey: Arithmetic Mean → Weighted Mean → Expectation

These three concepts are the same idea, progressively generalized.

### 1. Arithmetic Mean

The familiar average — all values treated equally:

$$\bar{x} = \frac{1}{n} \sum_{j=1}^{n} x_j = \frac{x_1 + x_2 + \cdots + x_n}{n}$$

Every data point $x_j$ gets the **same weight**: $\frac{1}{n}$.

---

### 2. Weighted Mean

Used when you already know how much each value should contribute:

$$\text{weighted-mean}(x) = \sum_{j=1}^{n} x_j p_j$$

Where the weights $p_1, \ldots, p_n$ must satisfy:

$$p_j \geq 0 \quad \text{and} \quad \sum_{j=1}^{n} p_j = 1$$

**Key insight:** The arithmetic mean is just a special case of the weighted mean where all weights are equal: $p_j = \frac{1}{n}$ for all $j$.

**Example** — Exam worth 70%, homework worth 30%:
$$\text{weighted mean} = 0.7 \times 80 + 0.3 \times 90 = 83$$
$$\text{arithmetic mean} = \frac{80 + 90}{2} = 85 \quad \leftarrow \text{wrong, ignores weights}$$

---

### 3. Expectation (Weighted Mean with Probabilities)

> "The definition of expectation for a discrete r.v. is inspired by the weighted mean of a list of numbers, with weights given by probabilities."

**Definition 4.1.1:** The *expected value* of a discrete r.v. $X$ with distinct possible values $x_1, x_2, \ldots$ is:

$$E(X) = \sum_{j=1}^{\infty} x_j \cdot P(X = x_j)$$

Same structure as the weighted mean — but now the weights $p_j$ are replaced by **probabilities** $P(X = x_j)$.

| | Arithmetic Mean | Weighted Mean | Expectation |
|---|---|---|---|
| Weight of each $x_j$ | $\frac{1}{n}$ (same for all) | $p_j$ (assigned manually) | $P(X = x_j)$ (from distribution) |
| Weights sum to | $1$ ✓ | $1$ ✓ | $1$ ✓ |
| Number of values | finite | finite | can be infinite |

---

## Cleaner Notation

Instead of indexing with $j$, you can sum directly over the **support** of $X$:

$$E(X) = \sum_{x} x \cdot P(X = x)$$

The **support** is the set of values $X$ can actually take (where the PMF is non-zero).

**Why this works:** For any $x$ not in the support, $P(X = x) = 0$, so:
$$x \cdot P(X = x) = x \cdot 0 = 0$$
Those terms contribute nothing, so it's safe to sum over everything — non-support values vanish automatically.

**The two notations are identical** — same numbers, same arithmetic:
$$\sum_{j=1}^{3} x_j \cdot P(X = x_j) = \sum_{x} x \cdot P(X = x)$$

The index $j$ is just a mechanical counter. The value notation skips the middleman.

**Example** — $X$ has support $\{3, 7, 10\}$ with probabilities $0.2, 0.5, 0.3$:
$$E(X) = 3(0.2) + 7(0.5) + 10(0.3) = 0.6 + 3.5 + 3.0 = 7.1$$

---

## Special Case: Equally Likely Outcomes

When all outcomes are equally likely, $P(X = x_j) = \frac{1}{n}$ for all $j$, so:

$$E(X) = \sum_{j=1}^{n} x_j \cdot \frac{1}{n} = \frac{x_1 + x_2 + \cdots + x_n}{n}$$

This is just the **arithmetic mean** — the average you learned in school.

> The arithmetic mean is a special case of expectation where every outcome is equally probable.

**Die example:** $X \in \{1, 2, 3, 4, 5, 6\}$, each with probability $\frac{1}{6}$:
$$E(X) = 1 \cdot \frac{1}{6} + 2 \cdot \frac{1}{6} + \cdots + 6 \cdot \frac{1}{6} = \frac{21}{6} = 3.5$$

Note: $X$ *never* equals 3.5 — but 3.5 is the long-run average. This is like the average number of children per household being 1.8 — no household actually has 1.8 children.

---

## Worked Examples {#worked-examples-expectation}

### Example 1 — Bernoulli R.V.

Let $X \sim \text{Bern}(p)$, with $q = 1 - p$. Then $X$ takes value 1 (success) with probability $p$ and value 0 (failure) with probability $q$:

$$E(X) = 1 \cdot p + 0 \cdot q = p$$

The expected value of a Bernoulli r.v. is simply $p$ — the probability of success. This makes intuitive sense: $E(X)$ sits between 0 and 1, compromising based on how likely each outcome is.

> Think of it as the balancing point on a seesaw with a pebble of mass $q$ at 0 and a pebble of mass $p$ at 1 — the fulcrum must be at $p$.

---

### Example 2 — Frequentist / Simulation Interpretation

Let $X$ have three possible values $a_1, a_2, a_3$ with probabilities $p_1, p_2, p_3$.

Imagine running $n$ independent draws of $X$. In the long run:
- About $p_1 n$ draws will produce $a_1$
- About $p_2 n$ draws will produce $a_2$
- About $p_3 n$ draws will produce $a_3$

The arithmetic mean of those $n$ simulation results is approximately:

$$\frac{p_1 n \cdot a_1 + p_2 n \cdot a_2 + p_3 n \cdot a_3}{n} = p_1 a_1 + p_2 a_2 + p_3 a_3 = E(X)$$

**Key takeaway:** The formula for $E(X)$ isn't arbitrary — it is exactly what you'd get by running the experiment many times and averaging the results. Expectation *is* the long-run average.

> For the Bernoulli case: writing 1 for "success" and 0 for "failure", the long-run proportion of 1's converges to $p$. The average of a long list of 0's and 1's is just the fraction of 1's — which is $p$.

---

## When Expectation is Undefined

$E(X)$ is only defined when:

$$\sum_{j=1}^{\infty} |x_j| \cdot P(X = x_j) < \infty$$

The sum of **absolute values**, weighted by probabilities, must be finite (must **converge**).

### What does "converge" vs "diverge" mean?

- **Converge** — as you add more and more terms, the sum settles toward a fixed finite number.
  $$\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots = 1 \quad \checkmark$$

- **Diverge** — the sum keeps growing forever, never settling.
  $$1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots = \infty \quad \times$$

### Two problems when $E(X)$ diverges:

1. **The series blows up** — the sum goes to $+\infty$ or $-\infty$. No finite answer.

2. **The answer depends on the order you add terms** — if there are large positive and large negative terms, rearranging them can give different sums (Riemann rearrangement theorem). The expectation wouldn't be well-defined.

Using $|x_j|$ (absolute values) checks that even ignoring signs, the sum stays finite — guaranteeing the answer is stable regardless of ordering.

| Condition | Result |
|---|---|
| $\sum \|x_j\| \cdot P(X = x_j) < \infty$ | $E(X)$ exists, finite, unambiguous ✓ |
| $\sum \|x_j\| \cdot P(X = x_j) = \infty$ | $E(X)$ undefined — diverges or order-dependent ✗ |

> In practice, most textbook distributions have well-defined expectations. But it's important to know it isn't automatically guaranteed.

---

## Key Properties and Warnings

### Proposition 4.1.2 — Same Distribution → Same Expectation

If $X$ and $Y$ are discrete r.v.s with the **same distribution** (same PMF), then:
$$E(X) = E(Y)$$

This follows directly from the definition — expectation is computed purely from the PMF.

### The Converse is FALSE

**Same expectation does NOT mean same distribution.**

$E(X)$ is just one number. It only tells you the "balancing point" — the center. It says nothing about:
- How spread out the values are
- The shape of the distribution
- How likely positive vs negative values are

**Example:** Both distributions below have $E(X) = 5$, but are completely different:

| Distribution A | Distribution B |
|---|---|
| $\{4, 5, 6\}$ equally likely | $\{1, 5, 9\}$ equally likely |
| Narrow spread | Wide spread |

Think of a seesaw — two differently shaped seesaws can still balance at the same point.

---

### Warning 4.1.3 — Never Replace an R.V. with Its Expectation

> "A common mistake is to replace an r.v. by its expectation without justification."

| | $X$ | $E(X)$ |
|---|---|---|
| What it is | A **function** — maps outcomes to values | A **constant** — one fixed number |
| Is it random? | Yes — varies across outcomes | No — completely fixed |

Replacing $X$ with $E(X)$ is wrong:
- **Mathematically** — $X$ is a function, $E(X)$ is a constant. They are different objects.
- **Statistically** — it ignores all the variability and randomness in $X$.

**Only exception:** If $X$ is a constant (e.g., $X = 5$ always with probability 1), then $X = E(X)$. But that's a degenerate r.v. — no randomness at all.

---

### Notation 4.1.4

We often abbreviate $E(X^2)$ to $EX^2$, and $E(X^n)$ to $EX^n$.

> $E(X^2)$ is the expectation of the r.v. $X^2$ — **not** the square of the number $EX$. These are generally different!

---

## Expectation Summary

$$\text{Arithmetic Mean} \longrightarrow \text{Weighted Mean} \longrightarrow \text{Expectation}$$

Each step just generalizes how weights are assigned:

- **Arithmetic mean** — all values weighted equally by $\frac{1}{n}$
- **Weighted mean** — values weighted by manually assigned $p_j$'s that sum to 1
- **Expectation** — values weighted by their probabilities $P(X = x_j)$

> **Core intuition:** $E(X)$ is the *long-run average* value of $X$ over many independent repetitions of the experiment. It is a one-number summary of the center — but does not determine the full distribution.

---

# Law of the Unconscious Statistician (LOTUS)

## The Problem LOTUS Solves

As we saw in the St. Petersburg paradox, $E(g(X))$ does **not** equal $g(E(X))$ in general if $g$ is not linear. So how do we correctly calculate $E(g(X))$?

Since $g(X)$ is itself an r.v., one way is to first find the **distribution of $g(X)$** and then apply the definition of expectation to that distribution. This means computing the PMF of $g(X)$ — which, as we saw in the functions of r.v.s notes, can require grouping many-to-one mappings and adding probabilities together.

Perhaps surprisingly, it turns out to be possible to find $E(g(X))$ **directly using the distribution of $X$**, without ever finding the distribution of $g(X)$. This is done using the **law of the unconscious statistician (LOTUS)**.

---

## The Theorem

**Theorem 4.5.1 (LOTUS):** If $X$ is a discrete r.v. and $g$ is a function from $\mathbb{R}$ to $\mathbb{R}$, then:

$$E(g(X)) = \sum_{x} g(x) P(X = x)$$

where the sum is taken over all possible values of $X$.

This means we can get the expected value of $g(X)$ knowing only $P(X = x)$ — the PMF of $X$. We don't need to know the PMF of $g(X)$ at all.

---

## Why "Unconscious Statistician"?

The name comes from the fact that going from $E(X) = \sum_x x \cdot P(X=x)$ to $E(g(X)) = \sum_x g(x) \cdot P(X=x)$ is tempting to do just by **changing $x$ to $g(x)$** in the definition — a swap that can be done very easily and mechanically, perhaps in a state of unconsciousness.

On second thought, it may sound too good to be true that finding the distribution of $g(X)$ is not needed for this calculation — surely you'd need to know how $g(X)$ is distributed to find its expectation? But LOTUS says it **is** true. The mechanical, "unconscious" shortcut actually works — and the rest of this section explains why.

---

## A Special Case First — Why It's True for $X^3$ {#a-special-case-first--why-its-true-for-x3}

Before proving LOTUS in general, let's see why it is true in a special case.

Let $X$ have support $0, 1, 2, \ldots$ with probabilities $p_0, p_1, p_2, \ldots$, so the PMF is $P(X = n) = p_n$.

Then $X^3$ has support $0^3, 1^3, 2^3, \ldots$ with the **same** probabilities $p_0, p_1, p_2, \ldots$ — because $X = n$ if and only if $X^3 = n^3$ (the cubing function is one-to-one, so each value of $X$ corresponds to exactly one value of $X^3$, with the same probability).

So:

$$E(X) = \sum_{n=0}^{\infty} n \, p_n$$

$$E(X^3) = \sum_{n=0}^{\infty} n^3 \, p_n$$

As claimed by LOTUS, to edit the expression for $E(X)$ into an expression for $E(X^3)$, we can just change the $n$ in front of the $p_n$ to $n^3$ — exactly the mechanical "unconscious" substitution described above.

**Why this case was easy:** This was an easy example because the function $g(x) = x^3$ is **one-to-one**. Recall from the functions of r.v.s notes that for one-to-one $g$, the support just gets relabeled and probabilities pass down unchanged — so $X^3$'s PMF really is "the same $p_n$'s, just attached to $n^3$ instead of $n$."

But LOTUS holds much more generally — even for many-to-one $g$, where the PMF of $g(X)$ is genuinely different from the PMF of $X$ (values collapse together and probabilities add up). The general proof needs a different idea.

---

## The General Proof — Pebbles and Super-Pebbles

The key insight needed for the proof of LOTUS for general $g$ is the **same insight used in the proof of linearity of expectation**: the expectation of $g(X)$ can be written in "ungrouped form" as:

$$E(g(X)) = \sum_{s} g(X(s)) \, P(\{s\})$$

where the sum is over **all the pebbles** in the sample space — every individual outcome $s$, before any grouping by value.

This is just the definition of expectation applied to the r.v. $g(X)$ viewed as a function on the sample space directly: for each outcome $s$, $g(X)$ takes the value $g(X(s))$, and $s$ occurs with probability $P(\{s\})$. Summing $g(X(s)) \cdot P(\{s\})$ over every pebble gives the expectation — this is true by definition, no matter what $g$ is.

**Now group the pebbles into super-pebbles.** We can also group the pebbles into **super-pebbles** according to the value that $X$ assigns to them. A super-pebble labeled $x$ consists of all individual pebbles $s$ such that $X(s) = x$.

**The crucial observation:** Within the super-pebble $X = x$, $g(X)$ always takes on the **same value** $g(x)$ — because every pebble $s$ inside this super-pebble has $X(s) = x$, so $g(X(s)) = g(x)$ for all of them. $g(x)$ can therefore be pulled out as a common factor when summing over that super-pebble.

**The derivation:**

$$E(g(X)) = \sum_{s} g(X(s)) P(\{s\})$$

Group the outer sum by which super-pebble each $s$ belongs to — first sum over all possible values $x$, then within each $x$, sum over all pebbles $s$ with $X(s) = x$:

$$= \sum_{x} \sum_{s : X(s) = x} g(X(s)) P(\{s\})$$

Since $g(X(s)) = g(x)$ for every $s$ in this inner sum (they all belong to the same super-pebble), $g(x)$ is constant with respect to $s$ and factors out:

$$= \sum_{x} g(x) \sum_{s : X(s) = x} P(\{s\})$$

Finally, $\sum_{s : X(s) = x} P(\{s\})$ is just the total weight of all the pebbles in the super-pebble $X = x$ — which is, by definition, $P(X = x)$:

$$= \sum_{x} g(x) P(X = x)$$

This is exactly the LOTUS formula. $\blacksquare$

**The one-line intuition:** $g(X)$ takes the value $g(x)$ on the entire super-pebble $X = x$ — so when computing the expectation, you don't need to know how that super-pebble's probability is split among individual outcomes, or how $g(X)$'s own PMF is structured. You only need to know the *total* probability of the super-pebble, $P(X = x)$, and the *single value* $g(X)$ takes there, $g(x)$. Multiply and sum over super-pebbles — done.

---

# Variance

## Motivation — Why Variance?

One important application of LOTUS is for finding the **variance** of a random variable.

Like expected value, variance is a single-number summary of the distribution of a random variable. While the expected value tells us the **center of mass** of a distribution, the variance tells us **how spread out** the distribution is.

---

## Definition

**Definition 4.6.1 (Variance and standard deviation):** The *variance* of an r.v. $X$ is:

$$\text{Var}(X) = E(X - EX)^2$$

Recall that when we write $E(X-EX)^2$, we mean the expectation of the random variable $(X-EX)^2$ — **not** $(E(X-EX))^2$ (which is 0 by linearity, since $E(X - EX) = EX - EX = 0$ always).

This is exactly where LOTUS comes in: $(X - EX)^2$ is $g(X)$ for $g(x) = (x - EX)^2$, so $\text{Var}(X) = E(g(X))$ can be computed directly from the PMF of $X$ using LOTUS, without first finding the distribution of $(X-EX)^2$.

---

## Standard Deviation

The square root of the variance is called the *standard deviation* (SD):

$$\text{SD}(X) = \sqrt{\text{Var}(X)}$$

We use the standard deviation because it brings the units of spread back into the **original units** of $X$, making it physically intuitive — a deviation of "2 standard deviations" is directly comparable across different distributions in a way that variance alone is not.

---

## The Continuous Case and the Gaussian

Everything above is stated for discrete r.v.s using PMFs and sums, but the same definitions hold for **continuous r.v.s** with a probability density function (PDF) $f(x)$, replacing sums with integrals. The second moment becomes:

$$E(X^2) = \int_{-\infty}^{\infty} x^2 f(x) \, dx$$

and $\text{Var}(X) = E(X^2) - (EX)^2$ exactly as before. The derivation via linearity of expectation (Theorem 4.6.2 below) goes through identically — linearity of $E[\cdot]$ doesn't care whether the underlying sum is discrete or an integral.

**The Gaussian connection:** For a Normal (Gaussian) distribution, roughly **68% of the probability mass lies within $\pm 1$ standard deviation of the mean**. More strikingly, the mean $\mu$ and variance $\sigma^2$ are not just *a* summary of a Gaussian — they **completely and uniquely determine its entire shape**.

This is special to the Gaussian. For most distributions, knowing the mean and variance tells you the center and spread but not the full shape — as the balancing-point example from earlier in this chapter showed, two very different PMFs can share the same mean, and the same logic extends to variance for non-Gaussian distributions.

---

## Why Squared Deviations?

The variance of $X$ measures how far $X$ is from its mean **on average** — but instead of simply taking the average difference between $X$ and its mean $EX$, we take the average **squared** difference.

**Why not just the average difference?** Note that the average deviation from the mean, $E(X - EX)$, **always equals 0** by linearity:

$$E(X - EX) = E(X) - E(EX) = EX - EX = 0$$

Positive and negative deviations cancel each other out exactly, regardless of how spread out the distribution actually is. So $E(X - EX)$ is useless as a measure of spread — it's always 0 no matter what.

**Squaring fixes this:** By squaring the deviations, we ensure that both positive and negative deviations contribute positively to the overall variability. A deviation of $-3$ and a deviation of $+3$ both contribute $9$ to the squared sum — neither cancels the other.

**The units problem:** However, because variance is an average *squared* distance, it has the wrong units. If $X$ is in dollars, $\text{Var}(X)$ is in *squared dollars* — which is hard to interpret directly. To get back to the original units, we take the square root — this gives us the standard deviation, which is in the same units as $X$ itself.

---

## Why Not Use Absolute Value Instead?

One might wonder why variance isn't defined as $E|X - EX|$, which would achieve the goal of counting both positive and negative deviations while maintaining the same units as $X$ (no squared-units problem).

This measure of variability (called the *mean absolute deviation*) isn't nearly as popular as $E(X-EX)^2$, for a variety of reasons. Most notably:

- The **absolute value function isn't differentiable at 0** — this causes problems in calculus-based derivations and optimization.
- The **squaring function is differentiable everywhere** and is central in various fundamental mathematical results, such as the **Pythagorean theorem**.

Squaring connects variance to a rich body of mathematical theory (least-squares methods, orthogonality, the Pythagorean theorem in the context of random variables) that absolute value does not.

---

## The Computational Formula for Variance

An equivalent expression for variance is:

$$\text{Var}(X) = E(X^2) - (EX)^2$$

This formula is often much easier to work with when doing actual calculations. Since this is the variance formula we will use over and over again, we state it as its own theorem.

**Theorem 4.6.2:** For any r.v. $X$:

$$\text{Var}(X) = E(X^2) - (EX)^2$$

**Proof:** Let $\mu = EX$. Expanding $(X - \mu)^2$ and using linearity, the variance of $X$ is:

$$E(X-\mu)^2 = E(X^2 - 2\mu X + \mu^2) = E(X^2) - 2\mu E X + \mu^2 = E(X^2) - 2\mu^2 + \mu^2 = E(X^2) - \mu^2 \qquad \blacksquare$$

Step by step: expand the square $(X-\mu)^2 = X^2 - 2\mu X + \mu^2$. Apply linearity of expectation to each term: $E(X^2) - 2\mu E(X) + E(\mu^2)$. Since $\mu = EX$ is a constant, $E(\mu^2) = \mu^2$ and $E(X) = \mu$, so the middle term becomes $-2\mu \cdot \mu = -2\mu^2$. Combining: $E(X^2) - 2\mu^2 + \mu^2 = E(X^2) - \mu^2 = E(X^2) - (EX)^2$.

---

## Properties of Variance

Variance has the following properties. The first two are easily verified from the definition, the third is addressed in a later chapter (Chapter 7), and the last is proven just after stating it.

### Property 1 — Shifting

$$\text{Var}(X + c) = \text{Var}(X) \quad \text{for any constant } c$$

**Intuition:** If we shift a distribution to the left or right by a constant $c$, that should affect the *center of mass* of the distribution (the mean shifts by $c$ too) but **not** its *spread* — the shape and width of the distribution stay exactly the same. Variance measures spread, so it is unaffected by shifts.

---

### Property 2 — Scaling

$$\text{Var}(cX) = c^2 \text{Var}(X) \quad \text{for any constant } c$$

Unlike shifting, scaling **does** affect spread — and it affects it by the **square** of the scaling factor. This is the first hint that variance is not linear (more on this below).

---

### Property 3 — Additivity for Independent R.V.s

If $X$ and $Y$ are independent, then:

$$\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)$$

We prove this and discuss it more in Chapter 7. **This is not true in general if $X$ and $Y$ are dependent.**

**Example — extreme dependence:** Consider the extreme case where $X$ always equals $Y$ (perfect dependence). Then:

$$\text{Var}(X+Y) = \text{Var}(2X) = 4\text{Var}(X) > 2\text{Var}(X) = \text{Var}(X) + \text{Var}(Y)$$

if $\text{Var}(X) > 0$ (which will be true unless $X$ is a constant, as the next property shows). So when $X$ and $Y$ are perfectly dependent, $\text{Var}(X+Y)$ is **strictly greater** than $\text{Var}(X) + \text{Var}(Y)$ — additivity fails completely. This shows the independence assumption in Property 3 is essential, not just a technical nicety.

---

### Property 4 — Non-negativity and the Degenerate Case

$$\text{Var}(X) \geq 0, \quad \text{with equality if and only if } P(X=a) = 1 \text{ for some constant } a$$

In other words, the only random variables that have zero variance are **constants** (which can be thought of as *degenerate* r.v.s); all other r.v.s have positive variance.

**Proof:**

Note that $\text{Var}(X)$ is the expectation of the **nonnegative** r.v. $(X-EX)^2$ — a square is always $\geq 0$. So $\text{Var}(X) \geq 0$, since the expectation of a nonnegative r.v. cannot be negative.

**Forward direction:** If $P(X=a) = 1$ for some constant $a$, then $E(X) = a$ and $E(X^2) = a^2$ (since $X^2 = a^2$ with probability 1), so $\text{Var}(X) = E(X^2) - (EX)^2 = a^2 - a^2 = 0$.

**Converse direction:** Suppose $\text{Var}(X) = 0$. Then $E(X-EX)^2 = 0$. Since $(X-EX)^2$ is a nonnegative r.v. whose expectation is 0, this shows $(X-EX)^2 = 0$ has probability 1 — because if $(X-EX)^2$ took any positive value with positive probability, its expectation would be strictly positive (a nonnegative r.v. with positive expectation must take a positive value with positive probability). This in turn shows that $X$ equals its mean $EX$ with probability 1 — i.e., $X$ is the constant $EX$. $\blacksquare$

---

## Variance is NOT Linear

**Remark 4.6.3 (Variance is not linear):** Unlike expectation, variance is **not linear**.

- The constant comes out **squared**: $\text{Var}(cX) = c^2 \text{Var}(X)$, not $c \cdot \text{Var}(X)$.
- The variance of the sum of r.v.s may **not** be the sum of their variances if they are dependent.

This is a critical distinction from expectation, where $E(cX) = cE(X)$ and $E(X+Y) = E(X) + E(Y)$ hold **unconditionally**, for any r.v.s. Variance only behaves additively under the **independence** assumption (Property 3) and only scales with the **square** of constants (Property 2).

---

## Worked Example — Geometric and Negative Binomial Variance

**Example 4.6.4 (Geometric and Negative Binomial variance):** In this example we'll use LOTUS to compute the variance of the Geometric distribution.

Let $X \sim \text{Geom}(p)$. We already know $E(X) = q/p$ (from the geometric series derivation in the expectation chapter). By LOTUS:

$$E(X^2) = \sum_{k=0}^{\infty} k^2 P(X=k) = \sum_{k=0}^{\infty} k^2 p q^k = \sum_{k=1}^{\infty} k^2 p q^k$$

(The $k=0$ term vanishes since $0^2 = 0$, so the sum can equivalently start from $k=1$.)

**Strategy:** Find this sum using a tactic similar to how we found the expectation — starting from the geometric series and taking derivatives.

**Step 1 — Start with the geometric series:**

$$\sum_{k=0}^{\infty} q^k = \frac{1}{1-q}$$

**Step 2 — Differentiate once with respect to $q$:**

$$\sum_{k=1}^{\infty} k q^{k-1} = \frac{1}{(1-q)^2}$$

We start the sum from $k=1$ since the $k=0$ term is 0 anyway (differentiating $q^0=1$ gives 0).

If we differentiate again, we'll get $k(k-1)$ instead of $k^2$ as we want — so before differentiating again, let's replenish our supply of $q$'s by multiplying both sides by $q$:

$$\sum_{k=1}^{\infty} k q^k = \frac{q}{(1-q)^2}$$

**Step 3 — Now take another derivative:**

$$\sum_{k=1}^{\infty} k^2 q^{k-1} = \frac{1+q}{(1-q)^3}$$

**Step 4 — Multiply by $q$ and by $p$ to get $E(X^2)$:**

$$E(X^2) = \sum_{k=1}^{\infty} k^2 p q^k = pq \cdot \frac{1+q}{(1-q)^3} = pq \cdot \frac{1+q}{p^3} = \frac{q(1+q)}{p^2}$$

(using $1 - q = p$, so $(1-q)^3 = p^3$, and one factor of $p$ from $pq$ cancels with $p^3$ leaving $p^2$ in the denominator).

**Step 5 — Apply the computational variance formula:**

$$\text{Var}(X) = E(X^2) - (EX)^2 = \frac{q(1+q)}{p^2} - \left(\frac{q}{p}\right)^2 = \frac{q(1+q) - q^2}{p^2} = \frac{q + q^2 - q^2}{p^2} = \frac{q}{p^2}$$

**Result:** For $X \sim \text{Geom}(p)$:

$$\boxed{\text{Var}(X) = \frac{q}{p^2}}$$

**The First Success connection:** This is also the variance of the **First Success** distribution, since shifting by a constant does not affect the variance (Property 1 above) — the First Success distribution is just Geom$(p) + 1$.

**Negative Binomial:** Since an $\text{NBin}(r,p)$ r.v. can be represented as a sum of $r$ i.i.d. $\text{Geom}(p)$ random variables (by the earlier theorem on the Negative Binomial story), and since variance is **additive for independent random variables** (Property 3), it follows that:

$$\text{Var}(\text{NBin}(r,p)) = r \cdot \frac{q}{p^2}$$

Each of the $r$ i.i.d. Geometric pieces contributes $\frac{q}{p^2}$ to the variance, and since they are independent, the variances simply add.

---

## Worked Example — Binomial Variance via Indicators

LOTUS is an all-purpose tool for computing $E(g(X))$ for any $g$, but as it usually leads to complicated sums, it should be used as a last resort. For variance calculations, our trusty **indicator r.v.s** can sometimes be used in place of LOTUS, as in this next example.

**Example 4.6.5 (Binomial variance):** Let's find the variance of $X \sim \text{Bin}(n,p)$ using indicator r.v.s to avoid tedious sums.

Represent $X = I_1 + I_2 + \cdots + I_n$, where $I_j$ is the indicator of the $j$-th trial being a success (this is exactly the Bernoulli decomposition from the independence chapter).

**Step 1 — Find the variance of each indicator $I_j$:**

$$\text{Var}(I_j) = E(I_j^2) - (E(I_j))^2 = p - p^2 = p(1-p)$$

**Why $E(I_j^2) = p$:** Recall that $I_j^2 = I_j$, since an indicator squared is itself ($0^2=0$ and $1^2=1$). So $E(I_j^2) = E(I_j) = p$.

So $\text{Var}(I_j) = p - p^2 = p(1-p) = pq$.

**Step 2 — Use additivity since the $I_j$ are independent:**

Since the $I_j$ are independent (independent trials), we can add their variances to get the variance of their sum:

$$\text{Var}(X) = \text{Var}(I_1) + \cdots + \text{Var}(I_n) = np(1-p)$$

**Result:**

$$\boxed{\text{Var}(\text{Bin}(n,p)) = np(1-p)}$$

This required no LOTUS at all — just the indicator decomposition and additivity of variance for independent r.v.s.

---

### Alternative — Finding $E(X^2)$ via Pairs of Trials

Alternatively, we can find $E(X^2)$ by first finding $E\binom{X}{2}$. The latter sounds more complicated, but actually it is simpler, since $\binom{X}{2}$ is the number of **pairs** of successful trials.

**Why $\binom{X}{2}$ counts pairs of successes:** If $X = k$ trials were successes, the number of ways to choose 2 of those $k$ successful trials is $\binom{k}{2}$ — so $\binom{X}{2}$ literally counts unordered pairs of trials that were both successes.

**Creating an indicator r.v. for each pair of trials:** For each pair of trials, define an indicator that is 1 if *both* trials in the pair were successes. Since trials are independent and each has success probability $p$, the probability that any specific pair are both successes is $p \cdot p = p^2$. There are $\binom{n}{2}$ such pairs, so:

$$E\binom{X}{2} = \binom{n}{2} p^2$$

**Step — Connect $\binom{X}{2}$ to $E(X^2)$ and $E(X)$:**

$$\binom{X}{2} = \frac{X(X-1)}{2} \implies X(X-1) = 2\binom{X}{2}$$

Taking expectations and using linearity:

$$E(X(X-1)) = E(X^2 - X) = E(X^2) - E(X)$$

So:

$$n(n-1)p^2 = E(X(X-1)) = E(X^2) - E(X) = E(X^2) - np$$

Solving for $E(X^2)$:

$$E(X^2) = n(n-1)p^2 + np$$

**Step — Apply the computational variance formula again:**

$$\text{Var}(X) = E(X^2) - (EX)^2 = (n(n-1)p^2 + np) - (np)^2$$

Expanding $(np)^2 = n^2p^2$ and $(n(n-1)p^2 = (n^2-n)p^2 = n^2p^2 - np^2)$:

$$\text{Var}(X) = (n^2p^2 - np^2 + np) - n^2p^2 = np - np^2 = np(1-p)$$

Same result as before: $\text{Var}(X) = np(1-p)$ — confirming the indicator-sum approach via a completely different route.

> **Note:** Exercise 48 uses this pairs-of-trials strategy to find the variance of the Hypergeometric distribution — the same technique generalizes beyond the Binomial.

---

# Poisson Distribution
> *Introduction to Probability* — Blitzstein & Hwang | Chapter 4.7

---

# Definition

**Definition 4.7.1 (Poisson distribution):** An r.v. $X$ has the *Poisson distribution* with parameter $\lambda$, where $\lambda > 0$, if the PMF of $X$ is:

$$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \ldots$$

We write this as $X \sim \text{Pois}(\lambda)$.

**Breaking down the formula:**

- $X$ is the count of events — it can only take discrete non-negative integer values $k = 0, 1, 2, \ldots$
- $\lambda$ (lambda) is the **rate parameter** — the average number of events expected in the interval. The condition $\lambda > 0$ simply means the average rate must be strictly positive.
- $P(X = k)$ gives the exact probability of observing exactly $k$ events given average rate $\lambda$.

**Why the formula is structured the way it is:** The $\lambda^k$ term in the numerator grows as $k$ gets larger (when $\lambda > 1$), but the $k!$ in the denominator grows much faster — eventually crushing the probability toward zero for very large $k$. The $e^{-\lambda}$ term acts as a normalizing constant ensuring all probabilities sum to exactly 1.

---

# Validity — Why the PMF Sums to 1

For any function to be a valid PMF, the sum of all probabilities across every possible outcome must equal exactly 1.

## The Taylor Series Proof

We want to prove:

$$\sum_{k=0}^{\infty} P(X=k) = 1$$

**Step 1 — Set up the sum:**

$$\sum_{k=0}^{\infty} \frac{e^{-\lambda} \lambda^k}{k!}$$

**Step 2 — Factor out the constant $e^{-\lambda}$:**

Since $e^{-\lambda}$ does not depend on $k$, it pulls out of the sum:

$$e^{-\lambda} \left(\sum_{k=0}^{\infty} \frac{\lambda^k}{k!}\right)$$

**Step 3 — Apply the Taylor series for $e^x$:**

The Maclaurin series (Taylor series evaluated at 0) for $e^x$ is defined exactly as:

$$\sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots = e^x$$

Substituting $\lambda$ for $x$, the entire summation collapses to $e^{\lambda}$:

$$e^{-\lambda} \cdot e^{\lambda}$$

**Step 4 — Resolve the exponents:**

$$e^{-\lambda + \lambda} = e^0 = 1 \quad \checkmark$$

The key mechanism: factoring out $e^{-\lambda}$ leaves behind exactly the Taylor series for $e^{\lambda}$, and their product is $e^0 = 1$.

---

## What P(X = 0) Looks Like

When $k = 0$, the PMF gives the probability that exactly zero events occur:

$$P(X = 0) = \frac{e^{-\lambda} \lambda^0}{0!} = \frac{e^{-\lambda} \cdot 1}{1} = e^{-\lambda}$$

Two foundational rules make this work cleanly:
- $\lambda^0 = 1$ (any non-zero number raised to the power 0 is 1)
- $0! = 1$ (zero factorial is defined as 1)

**Intuition of $e^{-\lambda}$:**
- If $\lambda = 100$ (very high rate), then $e^{-100}$ is incredibly tiny — nearly zero. It is highly unlikely you receive zero events when the average is 100.
- If $\lambda = 0.1$ (very low rate), then $e^{-0.1} \approx 0.90$ — a 90% chance of zero events when you only expect a fraction of one.

The fact that $0! = 1$ is the exact mathematical glue that allows the Poisson formula to gracefully handle the case where absolutely nothing happens.

---

# Mean and Variance of a Poisson R.V.

**Example 4.7.2:** Let $X \sim \text{Pois}(\lambda)$. Both the mean and the variance equal $\lambda$.

---

## Finding E(X) — The Cancellation Trick

$$E(X) = e^{-\lambda} \sum_{k=0}^{\infty} \frac{k\lambda^k}{k!}$$

**Step 1 — Drop the $k = 0$ term:**

When $k = 0$, the term is $0 \cdot \frac{\lambda^0}{0!} = 0$. It contributes nothing, so the sum starts from $k = 1$:

$$E(X) = e^{-\lambda} \sum_{k=1}^{\infty} \frac{k\lambda^k}{k!}$$

**Step 2 — Cancel $k$ with the first factor of $k!$:**

For $k \geq 1$: $\frac{k}{k!} = \frac{k}{k \cdot (k-1)!} = \frac{1}{(k-1)!}$

$$E(X) = e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^k}{(k-1)!}$$

**Step 3 — Factor out one $\lambda$:**

$$E(X) = \lambda e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!}$$

**Step 4 — Recognize the Taylor series:**

Let $j = k - 1$. As $k$ runs from 1 to $\infty$, $j$ runs from 0 to $\infty$:

$$\sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!} = \sum_{j=0}^{\infty} \frac{\lambda^j}{j!} = e^{\lambda}$$

**Step 5 — Combine:**

$$E(X) = \lambda e^{-\lambda} \cdot e^{\lambda} = \lambda e^{0} = \lambda \quad \checkmark$$

The $k$ in the numerator perfectly cancels the first factor of $k!$ in the denominator — leaving exactly the Taylor series for $e^{\lambda}$. This is the "magic trick" of the derivation.

$$\boxed{E(X) = \lambda}$$

---

## Finding Var(X) — The Calculus Method via LOTUS

By LOTUS:

$$E(X^2) = e^{-\lambda} \sum_{k=0}^{\infty} \frac{k^2 \lambda^k}{k!}$$

The problem is the $k^2$ in the numerator — it does not cancel as cleanly as $k$ did. The strategy is to use **differentiation** to force powers of $k$ to appear from the exponent, using the fact that $\frac{d}{d\lambda}\lambda^k = k\lambda^{k-1}$.

**Step 1 — Start with the Taylor series:**

$$\sum_{k=0}^{\infty} \frac{\lambda^k}{k!} = e^{\lambda}$$

**Step 2 — Differentiate with respect to $\lambda$:**

Differentiating the left side: the derivative of $\lambda^k$ brings down a factor of $k$.
Differentiating the right side: the derivative of $e^{\lambda}$ is $e^{\lambda}$.

$$\sum_{k=1}^{\infty} \frac{k\lambda^{k-1}}{k!} = e^{\lambda}$$

(The sum starts at $k = 1$ since the $k = 0$ term differentiates to 0.)

**Step 3 — "Replenish" (multiply both sides by $\lambda$):**

Differentiating lowered the exponent from $k$ to $k-1$. We need it back at $k$ to match the LOTUS formula, so multiply both sides by $\lambda$:

$$\sum_{k=1}^{\infty} \frac{k\lambda^k}{k!} = \lambda e^{\lambda}$$

*(If you plug this into the expectation formula you've just re-proved that $E(X) = \lambda$ — a good consistency check.)*

**Step 4 — "Rinse and repeat" (differentiate again):**

We have one factor of $k$. We need $k^2$. Differentiate both sides again:

- Left side: brings down another $k$, giving $k \cdot k = k^2$, and lowers the exponent to $k-1$.
- Right side: differentiate $\lambda e^{\lambda}$ using the **product rule**: $\frac{d}{d\lambda}(\lambda e^{\lambda}) = 1 \cdot e^{\lambda} + \lambda \cdot e^{\lambda} = e^{\lambda}(1 + \lambda)$.

$$\sum_{k=1}^{\infty} \frac{k^2 \lambda^{k-1}}{k!} = e^{\lambda}(1 + \lambda)$$

**Step 5 — Replenish again (multiply by $\lambda$):**

$$\sum_{k=1}^{\infty} \frac{k^2 \lambda^k}{k!} = \lambda e^{\lambda}(1 + \lambda)$$

**Step 6 — Plug back into the LOTUS expression for $E(X^2)$:**

$$E(X^2) = e^{-\lambda} \cdot \lambda e^{\lambda}(1 + \lambda) = \lambda(1 + \lambda)$$

The $e^{-\lambda}$ and $e^{\lambda}$ cancel perfectly, leaving $E(X^2) = \lambda(1 + \lambda)$.

**Step 7 — Apply the computational variance formula:**

$$\text{Var}(X) = E(X^2) - (EX)^2 = \lambda(1+\lambda) - \lambda^2 = \lambda + \lambda^2 - \lambda^2 = \lambda$$

$$\boxed{\text{Var}(X) = \lambda}$$

The mean and variance of a $\text{Pois}(\lambda)$ r.v. are both equal to $\lambda$.

---

## The Factorial Moment Method (Alternative)

Instead of using the calculus/derivative trick above, we can also find $E(X^2)$ using the **factorial moment** $E[X(X-1)]$.

**Why $E[X(X-1)]$ instead of $E[X^2]$:** When you expand $\frac{k^2}{k!}$, the $k$ doesn't cancel $k!$ perfectly — but $\frac{k(k-1)}{k!} = \frac{1}{(k-2)!}$, which cancels cleanly.

**Step 1 — Compute $E[X(X-1)]$:**

$$E[X(X-1)] = \sum_{k=0}^{\infty} k(k-1) \frac{e^{-\lambda}\lambda^k}{k!}$$

The $k=0$ and $k=1$ terms both equal 0 (since $k(k-1) = 0$ for $k \leq 1$), so the sum starts at $k=2$. For $k \geq 2$: $\frac{k(k-1)}{k!} = \frac{1}{(k-2)!}$.

$$E[X(X-1)] = e^{-\lambda} \sum_{k=2}^{\infty} \frac{\lambda^k}{(k-2)!}$$

**Step 2 — Factor out $\lambda^2$ and apply the Taylor series:**

$$E[X(X-1)] = \lambda^2 e^{-\lambda} \sum_{k=2}^{\infty} \frac{\lambda^{k-2}}{(k-2)!} = \lambda^2 e^{-\lambda} \cdot e^{\lambda} = \lambda^2$$

**Step 3 — Connect to $E(X^2)$:**

By expanding and using linearity:
$$E[X(X-1)] = E(X^2 - X) = E(X^2) - E(X)$$

Substituting $E[X(X-1)] = \lambda^2$ and $E(X) = \lambda$:

$$\lambda^2 = E(X^2) - \lambda \implies E(X^2) = \lambda^2 + \lambda$$

**Step 4 — Compute variance:**

$$\text{Var}(X) = E(X^2) - (EX)^2 = (\lambda^2 + \lambda) - \lambda^2 = \lambda \quad \checkmark$$

---

## Why Mean = Variance is Remarkable

In probability theory, having Mean = Variance is the **defining hallmark** of a Poisson process. It means that as events become more frequent, your uncertainty about the exact number grows at the exact same rate.

- $\lambda = 2$: The distribution is tight. Values of 1, 2, or 3 are highly likely. The spread is small.
- $\lambda = 100$: The distribution is much wider. Getting 90 or 110 events is completely normal. The "curve" flattens and widens as $\lambda$ grows.

**Important note:** For the Poisson distribution, $E[X(X-1)]$ and $[E(X)]^2$ both equal $\lambda^2$ — a coincidence specific to this distribution. In general, $E[X(X-1)] \neq [E(X)]^2$. The fact that they cancel each other out is exactly what forces $\text{Var}(X) = \lambda$.

---

# Shape of the Poisson Distribution

Figure 4.7 in the textbook shows the PMF and CDF of $\text{Pois}(2)$ and $\text{Pois}(5)$ from $k = 0$ to $k = 10$.

**Key observations:**

**Center:** The mean of Pois(2) is around 2 and the mean of Pois(5) is around 5 — consistent with $E(X) = \lambda$. Visually, the "center of mass" of the PMF bar chart balances exactly at the $\lambda$ value.

**Skewness for small $\lambda$:** The PMF of Pois(2) is **highly right-skewed**. The Poisson distribution models event counts, meaning the $x$-axis ($k$) can never be negative — there is a hard "wall" at $x = 0$. When $\lambda$ is small, the center of the graph sits right up against this wall. Since values cannot spread left past zero but can stretch arbitrarily far right, the graph is scrunched on the left and stretched on the right — a right-skewed distribution.

**Bell-shaped for larger $\lambda$:** As $\lambda$ grows larger, the skewness is reduced and the PMF becomes more bell-shaped. As $\lambda$ increases, the center walks away from the zero wall and the distribution has room to spread symmetrically in both directions. For sufficiently large $\lambda$, the Poisson distribution approximates a Normal (Gaussian) distribution — this is the Central Limit Theorem taking effect.

---

# The Poisson Paradigm (Law of Rare Events)

## What "Rare" Actually Means

The Poisson paradigm is also called the **law of rare events**. The interpretation of "rare" is crucial and often misunderstood:

> **"Rare" means the $p_j$ are small — not that $\lambda$ is small.**

For example: receiving 50 emails in an hour ($\lambda = 50$) is not a rare event — it happens all the time. But the Poisson paradigm still holds because the probability that any *specific person* emails you in any *specific millisecond* is microscopic. It is a barrage of rare micro-events combining into a very common macro-event.

---

## The Formal Statement

**Theorem (Poisson Paradigm):** Let $A_1, \ldots, A_n$ be events with $p_j = P(A_j)$, where $n$ is large, the $p_j$ are small, and the $A_j$ are independent or weakly dependent. Let:

$$X = \sum_{j=1}^{n} I(A_j)$$

count how many of the $A_j$ occur, where $I(A_j)$ is the indicator r.v. for event $A_j$. Then $X$ is approximately distributed as $\text{Pois}(\lambda)$, with:

$$\lambda = \sum_{j=1}^{n} p_j$$

**Key upgrade over the simplified version:** The $p_j$'s don't have to be identical — they can vary across trials. As long as each individual probability is small, you can simply add them all up to get $\lambda$. This makes the paradigm far more flexible than it might first appear.

**"Weakly dependent":** The paradigm also relaxes the independence assumption. Events that are slightly correlated (e.g., cars driving in packs on a highway) still permit the Poisson approximation, as long as the dependencies are localized. The precise definition of weak dependence and how to verify it are advanced topics (requiring measure theory).

---

## Real-World Examples

The following real-world quantities could follow an approximately Poisson distribution:

**Emails per hour:** There are many people who could potentially email you in that hour, but the probability that any specific person actually emails you in that specific hour is small. Alternatively, subdivide the hour into milliseconds — there are $3.6 \times 10^6$ milliseconds in an hour, but in any specific millisecond it is very unlikely you receive an email. $\lambda \approx 20$ emails per hour.

**Chocolate chips in a cookie:** Subdivide the cookie into small cubes. The probability of a chocolate chip landing in any single cube is small, but the number of cubes is large. $\lambda \approx 10$ chips per cookie.

**Earthquakes per year:** At any given time and location, the probability of an earthquake is small, but there are a large number of possible times and locations. $\lambda \approx 2$ earthquakes per year in a region.

In each case: $\lambda$ is the rate parameter, $k$ is the actual observed count in the interval, and $\lambda = n \cdot p$ where $n$ is the large number of trials and $p$ is the small per-trial probability.

---

## The Bridge: From Binomial to Poisson

The Poisson distribution is the mathematical limiting case of the Binomial when $n$ is very large and $p$ is very small, with $\lambda = np$ held constant.

**Why this matters:** If you tried to calculate exact Binomial probabilities with $n = 10^{12}$ trials, the combinatorial computation ($\binom{n}{k}$) would cause integer overflow on virtually any computer. The Poisson distribution provides a clean closed-form approximation:

$$\text{Bin}(n, p) \approx \text{Pois}(\lambda) \quad \text{when } n \text{ large, } p \text{ small, } \lambda = np$$

**The macro-micro connection you derived:**

$$\lambda = n \cdot p \quad \Leftrightarrow \quad p = \frac{\lambda}{n}$$

The micro-level probability $p$ is just the average rate $\lambda$ divided by the number of trials — exactly the naive definition of probability (number of expected occurrences over total trials). The Poisson distribution rescues us from the microscopic, unusable probability $p$ and lets us work entirely with the stable, observable average $\lambda$.

---

## The Error Bound — Stein-Chen Method

A remarkable theorem gives an upper bound on the error incurred from using a Poisson approximation. If the $A_j$ are independent, $N \sim \text{Pois}(\lambda)$, and $B$ is any set of nonnegative integers, then:

$$|P(X \in B) - P(N \in B)| \leq \min\!\left(1, \frac{1}{\lambda}\right) \sum_{j=1}^{n} p_j^2$$

**What the left side means:** The absolute difference between the true probability (using the exact distribution of $X$) and the Poisson approximation (using $N$), for any possible question $B$ you could ask.

**What the right side means — why squaring small numbers is the key:**

The crucial term is $\sum p_j^2$. Because probabilities are fractions less than 1, squaring them makes them much smaller:
$$0.01^2 = 0.0001 \quad \text{(100 times smaller)}$$

So when all $p_j$ are tiny, $\sum p_j^2$ is crushed to near zero even when summing many terms — making the error bound negligibly small. This is the precise mathematical reason why the Poisson paradigm works only for **rare events** with small $p_j$.

If the events are not rare (e.g., $p = 0.5$ like a coin flip): $\sum p_j^2 = n \cdot (0.5)^2 = 0.25n$, which is huge — the error bound would be massive, telling you that the Poisson approximation is completely invalid.

The $\min(1, 1/\lambda)$ factor acts as a stabilizer: for small $\lambda$ it caps at 1; for large $\lambda$ it shrinks the error further.

**Note:** Proving this bound rigorously requires the **Stein-Chen method**, an advanced graduate-level technique. At this stage, we accept the result and understand *when* to trust the approximation — which is fully captured by the condition that the $p_j$ are small.

---

## Why the Poisson is Not Exactly Correct

The Poisson r.v. has **no upper bound** — $k$ can be any nonnegative integer. But in real applications, the number of events is always bounded by the number of trials $n$. You cannot have more successes than trials, and you cannot physically cram an infinite number of chocolate chips into a cookie.

However, this theoretical mismatch is harmless in practice: the Poisson probability for $k$ far above $\lambda$ is so infinitesimally small that the physical impossibility doesn't corrupt the model. The formula's infinite "tail" is negligible.

The conditions for the Poisson paradigm are also flexible:
- The $n$ trials can have **different** success probabilities $p_j$ (not all equal)
- The trials don't have to be fully independent, only **not very dependent**

This flexibility makes the Poisson a popular starting model for **count data** — any data consisting of nonnegative integers representing how many times something happened (network failures, website clicks, customer arrivals, document typos, etc.).

---

# Occupancy Problems

## Setup

There are $k$ distinguishable balls and $n$ distinguishable boxes. The balls are randomly placed in the boxes, with all $n^k$ possibilities equally likely. Problems in this setting are called **occupancy problems**, and are at the core of many widely used algorithms in computer science (particularly hash tables, where keys are balls and memory buckets are boxes).

---

## Expected Number of Empty Boxes — Indicator Method

**Example 4.7.4(a):** Find the expected number of empty boxes (fully simplified, not as a sum).

**Solution — The Indicator Variable Approach:**

Let $I_j$ be the indicator r.v. for the $j$-th box being empty:
$$I_j = \begin{cases} 1 & \text{if box } j \text{ is completely empty} \\ 0 & \text{if box } j \text{ has at least one ball} \end{cases}$$

The total number of empty boxes is $\sum_{j=1}^{n} I_j$.

**Step 1 — Find $E(I_j)$ for a single box:**

For box $j$ to be empty, all $k$ balls must miss it. Each ball independently has probability $\frac{1}{n}$ of landing in box $j$, so the probability of missing box $j$ is $\left(1 - \frac{1}{n}\right)$.

Since all $k$ throws are independent, the probability that all $k$ balls miss box $j$ is:

$$P(I_j = 1) = \left(1 - \frac{1}{n}\right)^k$$

Since $I_j$ is an indicator, $E(I_j) = P(I_j = 1) = \left(1 - \frac{1}{n}\right)^k$.

**Where this probability comes from, step by step:**
- Ball 1 misses box $j$ with probability $\left(1 - \frac{1}{n}\right)$
- Ball 2 also misses box $j$ with probability $\left(1 - \frac{1}{n}\right)$ (independent)
- For all $k$ balls to miss: multiply $k$ times → $\left(1 - \frac{1}{n}\right)^k$

**Step 2 — Apply Linearity of Expectation:**

Even though the indicator variables are **highly dependent** (if one box is empty, the balls were forced into other boxes, affecting the others), Linearity of Expectation does not care about dependence:

$$E\!\left(\sum_{j=1}^{n} I_j\right) = \sum_{j=1}^{n} E(I_j) = n\left(1 - \frac{1}{n}\right)^k$$

$$\boxed{E(\text{empty boxes}) = n\left(1 - \frac{1}{n}\right)^k}$$

**Poisson connection:** For large $n$, using the fact that $\left(1 - \frac{1}{n}\right)^n \to e^{-1}$:

$$n\left(1 - \frac{1}{n}\right)^k \approx n \cdot e^{-k/n} = n \cdot e^{-\lambda}$$

where $\lambda = k/n$ is the average number of balls per box (the load factor). The expected number of empty boxes is approximately $n \cdot e^{-\lambda}$ — and $e^{-\lambda}$ is exactly $P(\text{Pois}(\lambda) = 0)$, the Poisson probability of a box being empty.

---

## Why Indicator Variables Beat Brute Force

There are two approaches to this problem. Understanding why one is elegant and the other is a nightmare is the real lesson:

**Method 1 — Brute Force (State Space):**

Use $E(X) = \sum_x x \cdot P(X = x)$. You must calculate the exact probability of exactly 0, 1, 2, ..., $n-1$ boxes being empty, then weight and sum. Each of those probabilities requires tracking where all $k$ balls go simultaneously — using the Inclusion-Exclusion Principle and Stirling Numbers of the Second Kind. For large $n$, this is computationally explosive and algebraically miserable.

**Method 2 — Indicator Variables (Perspective Shift):**

Instead of tracking all $k$ balls globally, put blinders on and look at exactly **one box**. Ask a simple binary question: "Is this box empty?" The answer is just the probability that all $k$ balls independently missed this one box. Then use Linearity of Expectation — which works regardless of dependence — to scale the single-box answer up to all $n$ boxes.

The power of the indicator approach: it changes the fundamental unit from "the whole system" to "a single binary switch." The LOE then stitches the macroscopic average back together without ever needing to reason about the joint distribution of all boxes simultaneously.

---

## Probability That At Least One Box is Empty — Inclusion-Exclusion

**Example 4.7.4(b):** Find the probability that at least one box is empty. Express your answer as a sum of at most $n$ terms.

**Why the "1 - P(none empty)" shortcut fails here:**

The natural instinct for "at least one" problems is $1 - P(\text{none})$. But computing $P(\text{all boxes occupied})$ directly is just as hard as the original problem — it requires tracking the complicated joint distribution of all $n$ boxes.

The textbook's hint — "a sum of at most $n$ terms" — points directly to the **Principle of Inclusion-Exclusion (PIE)**.

**Setup:** Let $A_j$ be the event that box $j$ is empty. We want $P(A_1 \cup A_2 \cup \cdots \cup A_n)$ (the probability that box 1 is empty, OR box 2 is empty, OR ...).

**The overcounting problem:** Simply adding $P(A_1) + P(A_2) + \cdots$ double-counts scenarios where multiple boxes are simultaneously empty. PIE fixes this with an alternating "accordion":

- **Add** the single-box probabilities (correct the count for one-empty-box scenarios, but overcount the two-empty scenarios)
- **Subtract** the two-box intersection probabilities (fix the two-empty overcount, but accidentally erase the three-empty scenarios)
- **Add** the three-box intersection probabilities (restore the three-empty scenarios...)
- ...and so on, alternating $+/-$ until all overlaps are counted exactly once.

**Computing the terms:**

- $P(\text{one specific box is empty}) = \left(1 - \frac{1}{n}\right)^k$ (all $k$ balls miss that box)
- $P(\text{two specific boxes are empty}) = \left(1 - \frac{2}{n}\right)^k$ (all $k$ balls land in the remaining $n-2$ boxes)
- $P(\text{j specific boxes are empty}) = \left(1 - \frac{j}{n}\right)^k$
- Number of ways to choose $j$ boxes from $n$: $\binom{n}{j}$

**The final sum (PIE result):**

$$P(\text{at least one empty}) = \sum_{j=1}^{n} (-1)^{j-1} \binom{n}{j} \left(1 - \frac{j}{n}\right)^k$$

This is a sum of exactly $n$ terms. The $(-1)^{j-1}$ term is the master alternating switch: positive for odd $j$ (singles, triples, ...) and negative for even $j$ (doubles, quadruples, ...).

---

## Worked Example — Poisson Approximation for At Least One Empty Box

**Example 4.7.4(c):** Let $n = 1000$, $k = 5806$. The expected number of empty boxes is approximately 3. Find a good approximation as a decimal for the probability that at least one box is empty. The handy fact $e^3 \approx 20$ may help.

**Solution — Using the Poisson Approximation:**

Instead of computing a 1000-term Inclusion-Exclusion sum, we use the Poisson paradigm.

**Step 1 — Define the Poisson approximation:**

Let $X = $ total number of empty boxes. Since $n = 1000$ is large and the probability of any specific box being empty is small, $X$ behaves approximately like a Poisson random variable.

**Step 2 — Identify $\lambda$:**

The textbook tells us the expected number of empty boxes is approximately 3, so:

$$X \approx \text{Pois}(\lambda = 3)$$

*(Verification: $\lambda = n\left(1 - \frac{1}{n}\right)^k = 1000\left(1 - \frac{1}{1000}\right)^{5806} \approx 1000 \cdot e^{-5.806} \approx 3$.)*

**Step 3 — Apply the "at least one" shortcut:**

Now that we are inside the clean Poisson world, we can use the complementary shortcut:

$$P(X \geq 1) = 1 - P(X = 0)$$

**Step 4 — Compute $P(X = 0)$ from the Poisson PMF:**

$$P(X = 0) = \frac{e^{-3} \cdot 3^0}{0!} = e^{-3} = \frac{1}{e^3} \approx \frac{1}{20} = 0.05$$

**Step 5 — Final answer:**

$$P(X \geq 1) \approx 1 - 0.05 = 0.95$$

There is approximately a **95% chance** that at least one box remains completely empty.

**Why this is remarkable:** A problem that naively required a 1000-term alternating sum collapsed to a single arithmetic step: $1 - \frac{1}{20}$. This is the engineering power of the Poisson approximation — it replaces exponentially complex combinatorics with a clean, tractable formula, as long as the events are rare and the average rate $\lambda$ is known.

---

# Conceptual Clarifications

## PMF vs CDF — A Common Confusion

When first working with the Poisson distribution, a common mix-up is between the PMF sum and the CDF.

**What sums to 1 — the PMF:**

$$\sum_{k=0}^{\infty} P(X = k) = 1$$

This is the infinite sum of the individual "slice" probabilities — the probability of exactly 0 events, plus exactly 1 event, plus exactly 2 events, stretching to infinity. This sum must equal 1 for any valid PMF, and we proved it above using the Taylor series.

**What does NOT sum to 1 — the CDF:**

$$P(X \leq k) = \sum_{i=0}^{k} P(X = i)$$

The CDF is a running tally up to a specific value $k$. You do not sum the CDF itself — instead, as $k \to \infty$, the CDF *approaches* 1:

$$\lim_{k \to \infty} P(X \leq k) = 1$$

| | PMF | CDF |
|---|---|---|
| Notation | $P(X = k)$ | $P(X \leq k)$ |
| What it gives | Probability of exactly $k$ events | Running total up to $k$ |
| Sums to 1? | Yes — $\sum_{k=0}^{\infty} P(X=k) = 1$ | No — it approaches 1 as $k \to \infty$ |

In one sentence: the PMF is the individual slice, the CDF is the running tally, and only the *infinite sum of the PMF* equals 1.

---

## Notation — $k$ vs $i$ as the Summation Index

When writing the expectation or any sum over the Poisson PMF, be careful not to use $k$ for two different things at once.

**The clean way to write these:**

$$\sum_{i=0}^{\infty} P(X = i) = 1 \quad \leftarrow \text{sum over all outcomes, counter is } i$$

$$P(X \leq k) = \sum_{i=0}^{k} P(X = i) \quad \leftarrow \text{sum up to a specific } k \text{, counter is } i$$

Here $k$ is the **specific value** you are testing or interested in — a fixed number. The letter $i$ (or $j$ or $n$) is the **counter variable** that runs through the sum. Mixing them up leads to confused notation like "summing from $k = k$ to infinity," which is circular.

---

## The Interval Scaling Rule

$\lambda$ is always defined relative to a **fixed interval** — a specific window of time, space, or volume. Changing the interval changes $\lambda$ proportionally.

**Example:** If you receive an average of 20 emails per hour ($\lambda = 20$), then over 2 hours the rate doubles to $\lambda = 40$, and over 30 minutes it halves to $\lambda = 10$.

This is why defining your interval precisely before setting $\lambda$ is critical. The interval dictates everything else — once you fix it, $\lambda$ is the expected count within that specific container, and $k$ is the actual observed count you want to calculate the probability of.

$$\text{New } \lambda = \text{old } \lambda \times \frac{\text{new interval length}}{\text{old interval length}}$$

---

## The Core Superpower — You Only Need $\lambda$

In the Poisson paradigm, you almost never have access to $n$ (the number of microscopic trials) or $p$ (the per-trial probability) individually. The environment is too complex and the trials are too numerous to count. But that does not matter.

> **As long as you know $\lambda$, you don't need $n$ or $p$.**

$\lambda$ is stable and directly observable from data. You can measure the average rate of emails, earthquakes, or cosmic ray hits empirically without ever knowing how many "millisecond-trials" your system is running or what the per-trial probability is.

The Poisson distribution is the mathematical bridge that lets you ignore the microscopic noise entirely and build your reasoning solely around the macroscopic average $\lambda$. This is the single most important practical fact about the Poisson distribution.

---

## When the Poisson Breaks — Occupancy Problems

Not every occupancy problem can be approximated by a Poisson. The key condition is that the per-box probability must be **small** — i.e., the events must be **rare**.

**Case 1 — Poisson works (large $n$, small $p$):**

$k = 10000$ balls, $n = 10000$ boxes:
$$p = \frac{1}{n} = \frac{1}{10000} = 0.0001 \quad \text{(tiny)} \qquad \lambda = \frac{k}{n} = 1$$

$p$ is microscopic, so squaring it: $p^2 = 0.00000001$ — the Stein-Chen error bound is negligibly small. Poisson works perfectly.

**Case 2 — Poisson breaks (small $n$, large $p$):**

$k = 10000$ balls, $n = 5$ boxes:
$$p = \frac{1}{n} = \frac{1}{5} = 0.2 \quad \text{(not rare)} \qquad \lambda = \frac{k}{n} = 2000$$

$p = 0.2$ is not small. Squaring it: $p^2 = 0.04$ — summing $10000$ of these gives an error bound of $0.04 \times 10000 = 400$, which is enormous. The Poisson approximation is completely invalid here. For this regime (large $\lambda$, large $p$), the correct approximation is the **Normal (Gaussian) distribution**.

**The rule of thumb:**

| Regime | Correct Model |
|---|---|
| Large $n$, small $p$, moderate $\lambda$ | Poisson |
| Large $n$, moderate $p$, large $\lambda$ | Normal (Gaussian) |
| Small $n$, any $p$ | Exact Binomial |

---

## Hash Tables — The Computer Science Connection

The occupancy problem is not just an abstract exercise. It is the mathematical foundation of **hash tables**, one of the most widely used data structures in computer science.

**The mapping:**
- $k$ balls = $k$ keys being inserted into the hash table
- $n$ boxes = $n$ memory buckets in the array
- A **hash collision** occurs when two keys land in the same bucket
- $\lambda = k/n$ is called the **load factor** — the average number of keys per bucket

**Why Poisson applies:** Memory arrays are large ($n$ is huge), so the probability of any key hitting a specific bucket is $p = 1/n$ — microscopic. The Poisson paradigm applies directly.

**What systems architects calculate using Poisson:**

- $P(\text{bucket empty}) = e^{-\lambda}$ — fraction of buckets with no keys (wasted space)
- $P(\text{bucket has exactly 1 key}) = \lambda e^{-\lambda}$ — ideal, no collision
- $P(\text{collision}) = 1 - P(0) - P(1) = 1 - e^{-\lambda}(1 + \lambda)$ — fraction of buckets with 2+ keys

For a load factor of $\lambda = 1$ (equal number of keys and buckets):
$$P(\text{empty}) = e^{-1} \approx 0.368 \quad P(\text{1 key}) \approx 0.368 \quad P(\text{collision}) \approx 0.264$$

About 26% of buckets will have collisions — a key design constraint in building performant hash tables.

The Poisson distribution converts what would otherwise require computing $\binom{n}{k}$ with astronomically large numbers into clean, tractable arithmetic.

---

# Connections Between Poisson and Binomial
> *Introduction to Probability* — Blitzstein & Hwang | Chapter 4.8

---

# The Grand Parallel

The Poisson and Binomial distributions are closely connected, and their relationship is **exactly parallel** to the relationship between the Binomial and Hypergeometric that we examined in the previous chapter:

$$\text{Binomial} \xrightarrow{\text{condition on total}} \text{Hypergeometric}$$
$$\text{Hypergeometric} \xrightarrow{\text{population} \to \infty} \text{Binomial}$$

The same structure holds between Poisson and Binomial:

$$\text{Poisson} \xrightarrow{\text{condition on total}} \text{Binomial}$$
$$\text{Binomial} \xrightarrow{n \to \infty,\, p \to 0,\, np = \lambda} \text{Poisson}$$

You can cross the bridge in two directions:

- **Taking a limit** (Binomial → Poisson): when $n$ is too large to compute with, approximate with Poisson.
- **Conditioning** (Poisson → Binomial): when you suddenly learn the total count of two Poisson processes, their conditional distribution becomes Binomial.

This is the grand unified tool for counting probabilities — understanding both directions lets you switch mathematical frameworks on the fly depending on what information you have.

---

# Sum of Independent Poissons

**Theorem 4.8.1:** If $X \sim \text{Pois}(\lambda_1)$, $Y \sim \text{Pois}(\lambda_2)$, and $X$ is independent of $Y$, then:

$$X + Y \sim \text{Pois}(\lambda_1 + \lambda_2)$$

The Poisson distribution is **closed under addition** — adding two independent Poisson r.v.s gives another Poisson r.v., with rate equal to the sum of the individual rates.

---

## The Intuition — Traffic Story

Think of two types of cars passing a checkpoint:
- Blue cars arrive at rate $\lambda_1 = 3$ per hour
- Red cars arrive at rate $\lambda_2 = 7$ per hour

Both types arrive randomly and independently. If you stop caring about color and just count **total cars**, the underlying mechanics haven't changed — cars still arrive randomly in a continuous time interval. You now just expect $\lambda_1 + \lambda_2 = 10$ cars per hour. The total count perfectly follows $\text{Pois}(10)$.

The rates add because the two independent streams of events simply merge into one combined stream.

---

## The Proof — Full Derivation

**Strategy:** Use the Law of Total Probability. To find $P(X + Y = k)$, condition on every possible value $X$ could take — for each value $j$ that $X$ takes, $Y$ must take $k - j$ to make the total equal $k$.

$$P(X+Y=k) = \sum_{j=0}^{k} P(X+Y=k \mid X=j) \cdot P(X=j)$$

Since $X$ and $Y$ are **independent**, knowing $X = j$ tells us nothing about $Y$:

$$= \sum_{j=0}^{k} P(Y=k-j) \cdot P(X=j)$$

**Plug in the Poisson PMFs:**

$$= \sum_{j=0}^{k} \frac{e^{-\lambda_2}\lambda_2^{k-j}}{(k-j)!} \cdot \frac{e^{-\lambda_1}\lambda_1^j}{j!}$$

**Factor out the $e$ terms** (they don't depend on $j$, so they come out of the sum):

$$= e^{-(\lambda_1+\lambda_2)} \sum_{j=0}^{k} \frac{\lambda_1^j \lambda_2^{k-j}}{j!(k-j)!}$$

---

## The Missing Step — How the Binomial Theorem Appears

This is the step the textbook describes as "using the binomial theorem" without showing the algebra. Here is exactly what happens.

Multiply the expression inside the sum by $\frac{k!}{k!} = 1$ (which changes nothing but reveals hidden structure):

$$= e^{-(\lambda_1+\lambda_2)} \cdot \frac{1}{k!} \sum_{j=0}^{k} \frac{k!}{j!(k-j)!} \lambda_1^j \lambda_2^{k-j}$$

Look at what's inside the sum now: $\frac{k!}{j!(k-j)!}$ is exactly the definition of $\binom{k}{j}$. So:

$$= e^{-(\lambda_1+\lambda_2)} \cdot \frac{1}{k!} \sum_{j=0}^{k} \binom{k}{j} \lambda_1^j \lambda_2^{k-j}$$

The entire summation now matches the **Binomial Theorem** exactly:

$$(a+b)^k = \sum_{j=0}^{k} \binom{k}{j} a^j b^{k-j}$$

with $a = \lambda_1$ and $b = \lambda_2$. So the sum collapses to $(\lambda_1 + \lambda_2)^k$:

$$P(X+Y=k) = e^{-(\lambda_1+\lambda_2)} \cdot \frac{(\lambda_1+\lambda_2)^k}{k!}$$

This is exactly the $\text{Pois}(\lambda_1 + \lambda_2)$ PMF. $\blacksquare$

**What made it work:** The $e^{-\lambda_1}$ and $e^{-\lambda_2}$ terms combined into $e^{-(\lambda_1+\lambda_2)}$ because when you multiply exponentials with the same base, you add the exponents. That combined $e$ term then sat outside the sum, and the clever $\frac{k!}{k!}$ trick forced the Binomial Theorem to appear inside.

---

# Poisson Given a Sum of Poissons — Conditioning Gives Binomial

**Theorem 4.8.2:** If $X \sim \text{Pois}(\lambda_1)$, $Y \sim \text{Pois}(\lambda_2)$, and $X$ is independent of $Y$, then the conditional distribution of $X$ given $X + Y = n$ is:

$$X \mid (X+Y=n) \sim \text{Bin}\!\left(n,\, \frac{\lambda_1}{\lambda_1+\lambda_2}\right)$$

**Intuition:** You have blue cars ($\lambda_1$) and red cars ($\lambda_2$) arriving independently. You are then told the total number of cars that arrived was $n$. Given this new information, what is the distribution of the number of blue cars?

Once you lock in the total $n$, you lose the infinite, boundary-free nature of the Poisson — you now have exactly $n$ "slots" and each car is independently blue with probability $\frac{\lambda_1}{\lambda_1 + \lambda_2}$. That is precisely a Binomial experiment.

---

## The Setup

We want to find $P(X = k \mid X+Y = n)$ for each $k \in \{0, 1, \ldots, n\}$.

By Bayes' rule (conditional probability):

$$P(X=k \mid X+Y=n) = \frac{P(X+Y=n \mid X=k) \cdot P(X=k)}{P(X+Y=n)}$$

Given $X = k$, the total $X + Y = n$ requires $Y = n - k$, so:

$$P(X+Y=n \mid X=k) = P(Y = n-k)$$

By independence of $X$ and $Y$. So:

$$P(X=k \mid X+Y=n) = \frac{P(Y=n-k) \cdot P(X=k)}{P(X+Y=n)}$$

By Theorem 4.8.1, $X + Y \sim \text{Pois}(\lambda_1 + \lambda_2)$, so we know the denominator exactly.

---

## The Proof — Four Magic Tricks

### Trick 1 — Bayes' Rule Setup

Plug in the three Poisson PMFs:

$$P(X=k \mid X+Y=n) = \frac{\dfrac{e^{-\lambda_2}\lambda_2^{n-k}}{(n-k)!} \cdot \dfrac{e^{-\lambda_1}\lambda_1^k}{k!}}{\dfrac{e^{-(\lambda_1+\lambda_2)}(\lambda_1+\lambda_2)^n}{n!}}$$

---

### Trick 2 — The Great Cancellation

Look at the $e$ terms:
- Numerator: $e^{-\lambda_2} \cdot e^{-\lambda_1} = e^{-(\lambda_1+\lambda_2)}$
- Denominator: $e^{-(\lambda_1+\lambda_2)}$

They are **identical** — they cancel completely:

$$\frac{e^{-(\lambda_1+\lambda_2)}}{e^{-(\lambda_1+\lambda_2)}} = 1$$

This is the most critical step in the proof. The $e^{-\lambda}$ term is what gives the Poisson its infinite tail — its ability to take any nonnegative integer value. The moment it cancels out, the distribution is no longer infinite. It is suddenly locked inside a finite box of size $n$.

After cancellation, what remains is:

$$\frac{\dfrac{\lambda_1^k \lambda_2^{n-k}}{k!(n-k)!}}{\dfrac{(\lambda_1+\lambda_2)^n}{n!}}$$

---

### Trick 3 — Combinatorics Emerge

Dividing the numerator fraction by the denominator fraction means multiplying by the reciprocal. The $n!$ from the denominator flips up:

$$= \frac{n!}{k!(n-k)!} \cdot \frac{\lambda_1^k \lambda_2^{n-k}}{(\lambda_1+\lambda_2)^n}$$

The piece $\frac{n!}{k!(n-k)!}$ is exactly $\binom{n}{k}$ — the combinatorial coefficient for choosing $k$ successes from $n$ trials. The system has **automatically generated** the combinatorics needed for a Binomial distribution.

---

### Trick 4 — The Probability p Emerges

Now handle the $\lambda$ terms:

$$\frac{\lambda_1^k \lambda_2^{n-k}}{(\lambda_1+\lambda_2)^n}$$

Split $(\lambda_1+\lambda_2)^n$ into $(\lambda_1+\lambda_2)^k \cdot (\lambda_1+\lambda_2)^{n-k}$ and group:

$$= \left(\frac{\lambda_1}{\lambda_1+\lambda_2}\right)^k \left(\frac{\lambda_2}{\lambda_1+\lambda_2}\right)^{n-k}$$

Let $p = \frac{\lambda_1}{\lambda_1+\lambda_2}$. Then $1 - p = \frac{\lambda_2}{\lambda_1+\lambda_2}$. So this becomes:

$$= p^k (1-p)^{n-k}$$

The **success probability** $p$ is exactly the rate of $X$ divided by the total rate — the fraction of all events that are type $X$. This makes complete sense: given that $n$ total events occurred, each event independently belongs to type $X$ with probability proportional to its rate.

---

## The Final Result

Putting Tricks 3 and 4 together:

$$P(X=k \mid X+Y=n) = \binom{n}{k} p^k (1-p)^{n-k}, \quad p = \frac{\lambda_1}{\lambda_1+\lambda_2}$$

This is exactly the $\text{Bin}\!\left(n, \frac{\lambda_1}{\lambda_1+\lambda_2}\right)$ PMF. $\blacksquare$

**Summary of what conditioning did:** Starting with two unbounded Poisson r.v.s (each can take any nonnegative integer value), the moment we condition on their sum being $n$, three things happen automatically:
1. The infinite $e^{-\lambda}$ tails cancel — the distribution becomes finite
2. The factorials rearrange into $\binom{n}{k}$ — combinatorics appear
3. The $\lambda$ ratios become success/failure probabilities — the Binomial structure emerges

The Poissons are completely eradicated. You are left holding the pure Binomial PMF.

---

# Poisson Approximation to Binomial — Limit Gives Poisson

## The Theorem

**Theorem 4.8.3 (Poisson approximation to Binomial):** If $X \sim \text{Bin}(n, p)$ and we let $n \to \infty$ and $p \to 0$ such that $\lambda = np$ remains fixed, then the PMF of $X$ converges to the $\text{Pois}(\lambda)$ PMF:

$$P(X = k) \to \frac{e^{-\lambda}\lambda^k}{k!}$$

More generally, the same conclusion holds if $n \to \infty$ and $p \to 0$ in such a way that $np$ converges to a constant $\lambda$.

This is a special case of the Poisson paradigm where the $A_j$ are independent with the same probabilities. In this special case we can prove the approximation works by directly taking a limit of the Binomial PMF.

---

## The Proof — Four Blocks

### Step 1 — Substitute p = λ/n

Start with the Binomial PMF and eliminate $p$ by substituting $p = \frac{\lambda}{n}$ (since $\lambda = np$ is fixed):

$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$

Expand $\binom{n}{k} = \frac{n(n-1)\cdots(n-k+1)}{k!}$ and substitute $p = \frac{\lambda}{n}$:

$$= \frac{n(n-1)\cdots(n-k+1)}{k!} \cdot \left(\frac{\lambda}{n}\right)^k \cdot \left(1 - \frac{\lambda}{n}\right)^{n-k}$$

---

### Step 2 — Shatter into Four Blocks

Reorganize by pulling $\frac{\lambda^k}{k!}$ to the front, sliding $n^k$ underneath the numerator expansion, and splitting the last exponent:

$$P(X=k) = \underbrace{\frac{\lambda^k}{k!}}_{\text{Block 1}} \cdot \underbrace{\frac{n(n-1)\cdots(n-k+1)}{n^k}}_{\text{Block 2}} \cdot \underbrace{\left(1-\frac{\lambda}{n}\right)^n}_{\text{Block 3}} \cdot \underbrace{\left(1-\frac{\lambda}{n}\right)^{-k}}_{\text{Block 4}}$$

---

### Step 3 — Take the Limit on Each Block

Now let $n \to \infty$ with $k$ held fixed and watch what happens to each block:

**Block 1 — $\frac{\lambda^k}{k!}$:**

No $n$ appears here. This block is completely immune to the limit — it sits perfectly preserved.

$$\frac{\lambda^k}{k!} \to \frac{\lambda^k}{k!}$$

**Block 2 — $\frac{n(n-1)\cdots(n-k+1)}{n^k}$:**

There are exactly $k$ terms in the numerator and $k$ copies of $n$ in the denominator. Pair them up:

$$\frac{n}{n} \cdot \frac{n-1}{n} \cdot \frac{n-2}{n} \cdots \frac{n-k+1}{n}$$

As $n \to \infty$, subtracting any fixed number from $n$ becomes negligible — each fraction approaches 1. So the entire block approaches 1:

$$\frac{n(n-1)\cdots(n-k+1)}{n^k} \to 1$$

**Block 3 — $\left(1 - \frac{\lambda}{n}\right)^n$:**

This is one of the most famous limits in mathematics — the **compound interest formula** / definition of $e$:

$$\lim_{n\to\infty}\left(1 + \frac{x}{n}\right)^n = e^x$$

With $x = -\lambda$:

$$\left(1 - \frac{\lambda}{n}\right)^n \to e^{-\lambda}$$

This is where the $e^{-\lambda}$ normalizing constant of the Poisson PMF comes from — it is born from the compound interest formula as $n \to \infty$.

**Block 4 — $\left(1 - \frac{\lambda}{n}\right)^{-k}$:**

As $n \to \infty$, $\frac{\lambda}{n} \to 0$, so this becomes $(1 - 0)^{-k} = 1^{-k} = 1$:

$$\left(1-\frac{\lambda}{n}\right)^{-k} \to 1$$

---

### Step 4 — Reassemble

Multiply the limits of all four blocks together:

$$P(X=k) \to \frac{\lambda^k}{k!} \cdot 1 \cdot e^{-\lambda} \cdot 1 = \frac{e^{-\lambda}\lambda^k}{k!}$$

This is exactly the $\text{Pois}(\lambda)$ PMF. $\blacksquare$

**What happened physically:** The Binomial framework completely burned away in the limit. Block 2 (the combinatorial ratio) collapsed to 1 — the factorial structure of the Binomial dissolved. Block 3 (the failure probability taken to a large power) crystallized into $e^{-\lambda}$ — the Poisson's normalizing constant. Blocks 1 and 4 stayed clean. The four pieces reassembled into the pure Poisson formula.

---

## The Error Bound

In the real world, $n$ is never truly infinity and $p$ is never truly zero. The theorem gives us a practical guarantee:

If $X \sim \text{Bin}(n,p)$ and $N \sim \text{Pois}(np)$, then for any set $B$ of nonnegative integers:

$$|P(X \in B) - P(N \in B)| \leq \min(p,\, np^2)$$

**Reading this bound:**

- The error is controlled by $\min(p, np^2)$
- As $p \to 0$ (events become rarer), $p$ itself shrinks — the approximation improves
- As $p \to 0$ with fixed $\lambda = np$, $np^2 = \lambda p \to 0$ as well — the error vanishes
- **Only $p$ matters:** even if $n$ is enormous, if $p$ isn't small enough, squaring it won't crush the error

This connects directly back to the Stein-Chen error bound from the Poisson paradigm section. In the special case where all $p_j = p$ are equal, the general bound $\sum p_j^2 = np^2$ reduces to this cleaner form.

**The ultimate engineering rule of thumb:** Use the Poisson approximation when $n$ is large and $p$ is small. The condition that actually matters is that $p$ is small — $n$ just needs to be large enough that $np$ is a meaningful average rate.

---

# The Full Picture — Switching Tools on the Fly

$$\boxed{\text{Binomial} \underset{n\to\infty,\, p\to 0}{\xrightarrow{\hspace{2cm}}} \text{Poisson} \underset{\text{condition on total}}{\xrightarrow{\hspace{2cm}}} \text{Binomial}}$$

| Direction | Operation | When to use |
|---|---|---|
| Binomial → Poisson | Take limit $n\to\infty$, $p\to 0$, $np=\lambda$ | $n$ too large to compute $\binom{n}{k}$ |
| Poisson → Binomial | Condition on total $X+Y=n$ | You learn the combined count of two Poisson streams |
| Poisson + Poisson | Add rates | Two independent Poisson processes merge |

**The key insight across all three theorems:**

- **Sum of Poissons:** rates add. Two independent streams merge into one with combined rate.
- **Conditioning on the sum:** the $e^{-\lambda}$ tails cancel, the infinite domain collapses to $\{0,\ldots,n\}$, and the rates become Binomial probabilities.
- **Limit of Binomial:** the combinatorial Block 2 collapses to 1, Block 3 becomes $e^{-\lambda}$ via compound interest, and the Poisson emerges naturally.

All three results reinforce the same underlying truth: the Poisson and Binomial are not separate objects — they are the same counting story viewed through different lenses of information and scale.

---

# The Poisson Splitting Property

This is the **reverse** of the sum theorem. Whereas the sum theorem says two independent Poisson streams merge into one, the splitting property says one Poisson stream can be split into two independent Poisson streams.

**Theorem:** Let $X \sim \text{Pois}(\lambda)$. Suppose each event is independently classified as type 1 with probability $p$ and type 2 with probability $1-p$. Let $X_1$ = number of type 1 events and $X_2$ = number of type 2 events. Then:

$$X_1 \sim \text{Pois}(\lambda p), \quad X_2 \sim \text{Pois}(\lambda(1-p)), \quad X_1 \perp X_2$$

**Three remarkable facts in one theorem:**
1. $X_1$ is Poisson with rate $\lambda p$ — the original rate scaled by the fraction that are type 1
2. $X_2$ is Poisson with rate $\lambda(1-p)$ — the original rate scaled by the fraction that are type 2
3. $X_1$ and $X_2$ are **independent** — even though they sum to $X$, knowing one tells you nothing about the other

**Why independence is surprising:** You might expect $X_1$ and $X_2$ to be dependent — after all, $X_1 + X_2 = X$ is fixed by $X$. But $X$ itself is random, so fixing $X_1 = k_1$ does not force $X_2$ to be $k - k_1$ for any fixed $k$. The randomness in $X$ absorbs the constraint and the two counts remain independent.

**Connection to Theorem 4.8.2:** The splitting property and the conditioning theorem are two sides of the same coin:
- **Splitting:** start with one Pois$(\lambda)$, classify events → get two independent Poissons
- **Conditioning:** start with two independent Poissons, learn the total → get a Binomial

The success probability in the resulting Binomial is exactly $p = \frac{\lambda_1}{\lambda_1 + \lambda_2}$ — the same fraction that appears in the splitting property. This is not a coincidence.

**Intuition:** Think of cars arriving at rate $\lambda$ per hour. Each car is independently red with probability $p$ and blue with probability $1-p$. The red cars form their own Poisson process at rate $\lambda p$, the blue cars form their own at rate $\lambda(1-p)$, and — crucially — whether a red car just arrived tells you nothing about when the next blue car will arrive. The two streams are completely decoupled.

**Consistency check with the sum theorem:** If you split $\text{Pois}(\lambda)$ into $\text{Pois}(\lambda p)$ and $\text{Pois}(\lambda(1-p))$, and then add them back together, you get $\text{Pois}(\lambda p + \lambda(1-p)) = \text{Pois}(\lambda)$. The sum theorem and splitting property are perfectly consistent — they are inverses of each other.

---

# Worked Example — Poisson Approximation in Practice

**Example 4.8.4:** This example illustrates using the Poisson approximation to avoid computing a tedious exact Binomial sum, and also demonstrates the Poisson approximation to the sum of non-identically distributed indicators (the full Poisson paradigm, not just the special case where all $p_j$ are equal).

**Setup:** There are $n$ people at a party, and the birthday of each person is equally likely to be any of the 365 days of the year, independently. Find the expected number of birthday matches (pairs of people with the same birthday), and approximate the probability of at least one match.

**Step 1 — Define indicator r.v.s:**

For each pair $(i, j)$ with $i < j$, let $I_{ij}$ be the indicator that persons $i$ and $j$ share a birthday. There are $\binom{n}{2}$ such pairs.

$$P(I_{ij} = 1) = \frac{1}{365} \quad \text{(given person } i\text{'s birthday, person }j\text{ matches with prob }\frac{1}{365})$$

**Step 2 — Expected number of matches by linearity:**

$$E\!\left(\sum_{i<j} I_{ij}\right) = \binom{n}{2} \cdot \frac{1}{365} = \frac{n(n-1)}{2 \cdot 365}$$

For $n = 23$: $E = \frac{23 \cdot 22}{730} = \frac{506}{730} \approx 0.693$.

**Step 3 — Poisson approximation:**

Let $X = \sum_{i<j} I_{ij}$ = total number of birthday matches. The $I_{ij}$ are not independent (three people $i, j, k$ have correlated match indicators since if $i$ matches $j$ and $j$ matches $k$, then $i$ matches $k$). However, they are **weakly dependent** — any two pairs share at most one person. By the Poisson paradigm:

$$X \approx \text{Pois}(\lambda), \quad \lambda = \binom{n}{2} \cdot \frac{1}{365}$$

**Step 4 — Probability of at least one match:**

$$P(X \geq 1) \approx 1 - P(X = 0) = 1 - e^{-\lambda}$$

For $n = 23$, $\lambda \approx 0.693$:

$$P(X \geq 1) \approx 1 - e^{-0.693} \approx 1 - \frac{1}{2} = 0.5$$

So with just 23 people there is approximately a 50% chance of at least one birthday match — the famous **Birthday Problem** result. The Poisson approximation gives the right answer cleanly without computing any large Binomial sums.

**Why this example matters:** This is the Poisson paradigm in its most general form — the indicators $I_{ij}$ are not i.i.d. (they have different dependencies) and we are not summing Binomial trials. Yet the Poisson approximation still works because the dependencies are weak. The expected value $\lambda = \sum_{i<j} p_{ij}$ is all you need.

**The key technique chain demonstrated:**
1. Define indicator r.v.s for each event of interest
2. Use linearity of expectation to find $\lambda$
3. Invoke the Poisson paradigm to approximate $X \sim \text{Pois}(\lambda)$
4. Use $P(X \geq 1) = 1 - e^{-\lambda}$ to get the final probability

This four-step chain is one of the most powerful problem-solving patterns in probability.