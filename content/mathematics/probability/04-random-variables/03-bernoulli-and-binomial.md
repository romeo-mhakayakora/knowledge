---
title: Bernoulli and Binomial Distributions
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

# Bernoulli and Binomial Distributions

> *Introduction to Probability* — Blitzstein & Hwang

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

---

### Lens 1 — The Story (Most Important)

> Run $n$ **independent** trials. Each trial results in success (with probability $p$) or failure (with probability $1-p = q$). $X$ = total number of successes.

This is why the Binomial matters. Any real-world setting with independent binary outcomes maps here.

**The two non-negotiable conditions:**
1. Trials are **independent**
2. Every trial has the **same** probability of success $p$

Violate either condition → you no longer have a Binomial.

---

### Lens 2 — Sum of Indicator Random Variables (Elegant)

Decompose a complicated count into a sum of the simplest possible things:

$$X = X_1 + X_2 + \cdots + X_n$$

where each indicator $X_j = 1$ if trial $j$ succeeds, $0$ otherwise. The $X_j$'s are **i.i.d. Bern($p$)**:

- *Independent*: knowing the outcome of trial 3 tells you nothing about trial 7.
- *Identically distributed*: every $X_j$ has the exact same Bern($p$) distribution.

> **Why this lens is powerful:** It breaks a complex RV into a sum of 0/1 bricks. This unlocks easy computation of expectation, variance, and more in later lectures — and is the key to proving the sum of independent Binomials theorem.

---

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
