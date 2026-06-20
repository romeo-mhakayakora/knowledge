---
title: Conditional Probability
subject: probability
chapter: 03-conditional-probability
tags:
- probability
- mathematics
date: '2026-06-18'
updated: '2026-06-19'
status: complete
difficulty: intermediate
---
**Course:** Harvard Statistics 110 — Probability  
**Source:** [Lecture 4: Conditional Probability (YouTube)](https://youtu.be/P7NE4WF8j-Q?si=JCrkzbz44S-3lsiI)  
**Timestamp covered:** 32:00 onwards  
**Book chapter(s):** Ch. 2

---

## Core Theme

The central idea of this half of the lecture is **belief updating**: how do you revise your probability estimate for an event once you receive new evidence? This sequential updating process is foundational to science, statistics, and reasoning under uncertainty.

---

## 1. Conditional Probability — Definition

### Notation

$$P(A \mid B)$$

Read as: *"the probability that event $A$ occurs, **given** that event $B$ has occurred."*

### Formula

$$\boxed{P(A \mid B) = \frac{P(A \cap B)}{P(B)}}$$

### Constraint

This definition requires $P(B) > 0$. Conditioning on an event of probability zero is undefined (no division by zero).

---

## 2. Intuition 1 — Pebble World

Think of the sample space $\Omega$ as a collection of **pebbles**, where each pebble $\omega_i$ has a mass $m_i \geq 0$ and the total mass sums to 1:

$$\sum_{i} m_i = 1$$

**Step-by-step reasoning for $P(A \mid B)$:**

1. **Restrict the universe.** You are told $B$ occurred. Any pebble outside $B$ is now irrelevant — discard $B^c$.

2. **Find the intersection.** The event $A$ can only occur via pebbles in both $A$ *and* $B$, i.e. pebbles in $A \cap B$.

3. **Renormalise.** After discarding $B^c$, the remaining pebbles have total mass $P(B) \leq 1$, not necessarily 1. Dividing by $P(B)$ rescales the masses so the restricted universe sums to 1 again:

$$P(A \mid B) = \frac{\text{mass of } A \cap B}{\text{mass of } B} = \frac{P(A \cap B)}{P(B)}$$

This is exactly why the denominator is $P(B)$ — it is a **renormalisation constant**.

---

## 3. Intuition 2 — Frequentist World

Interpret probability as a long-run frequency over many repeated trials.

1. Run the experiment $N$ times (where $N$ is very large).
2. **Circle only the trials where $B$ occurred.** Suppose there are $n_B$ such trials.
3. Among those $n_B$ trials, count how many also had $A$ occur. Call this $n_{AB}$.

Then:

$$P(A \mid B) \approx \frac{n_{AB}}{n_B} = \frac{n_{AB}/N}{n_B/N} \xrightarrow{N \to \infty} \frac{P(A \cap B)}{P(B)}$$

The same formula falls out naturally — you are simply asking *"of the times $B$ happened, how often did $A$ also happen?"*

---

## 4. Theorem 1 — Multiplication Rule (Two Events)

**Derivation:** Multiply both sides of the conditional probability definition by $P(B)$:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} \implies P(A \cap B) = P(A \mid B) \cdot P(B)$$

Since $A \cap B = B \cap A$, we can swap the roles of $A$ and $B$:

$$\boxed{P(A \cap B) = P(A \mid B) \cdot P(B) = P(B \mid A) \cdot P(A)}$$

### Connection to Independence

If $A$ and $B$ are **independent**, conditioning on $B$ gives no new information about $A$:

$$P(A \mid B) = P(A)$$

Substituting into Theorem 1:

$$P(A \cap B) = P(A) \cdot P(B)$$

This recovers the standard definition of independence — it is not an axiom, it is a consequence of $P(A \mid B) = P(A)$.

---

## 5. Theorem 2 — General Multiplication Rule ($n$ Events)

For events $A_1, A_2, \dots, A_n$:

$$\boxed{P\!\left(\bigcap_{i=1}^{n} A_i\right) = P(A_1)\cdot P(A_2 \mid A_1)\cdot P(A_3 \mid A_1 \cap A_2) \cdots P(A_n \mid A_1 \cap A_2 \cap \cdots \cap A_{n-1})}$$

Written more compactly:

$$P\!\left(\bigcap_{i=1}^{n} A_i\right) = \prod_{k=1}^{n} P\!\left(A_k \;\Bigg|\; \bigcap_{j=1}^{k-1} A_j\right)$$

where by convention the $k=1$ term is just $P(A_1)$ (empty intersection = $\Omega$).

### Key remark — ordering

Because $\bigcap_{i=1}^n A_i$ is symmetric in the $A_i$'s, there are exactly $n!$ valid orderings you can choose to write the expansion. Picking a clever ordering often makes a problem significantly easier to compute.

---

## 6. Theorem 3 — Bayes' Rule

### Derivation

Start from Theorem 1 (swap labels):

$$P(A \cap B) = P(B \mid A) \cdot P(A)$$

Substitute this into the numerator of the definition $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$:

$$\boxed{P(A \mid B) = \frac{P(B \mid A)\cdot P(A)}{P(B)}}$$

### Named terms

| Term | Expression | Meaning |
|------|-----------|---------|
| **Prior** | $P(A)$ | Belief in $A$ *before* observing $B$ |
| **Likelihood** | $P(B \mid A)$ | How probable $B$ is *if* $A$ is true |
| **Marginal** | $P(B)$ | Overall probability of $B$ (normalising constant) |
| **Posterior** | $P(A \mid B)$ | Updated belief in $A$ *after* observing $B$ |

### Why it matters

The proof is a single line of algebra, yet Bayes' Rule (Thomas Bayes, 1760s) is one of the most consequential results in all of mathematics. It tells you precisely how to **go from $P(B \mid A)$ to $P(A \mid B)$** — from the probability of observing the evidence given a hypothesis, to the probability of the hypothesis given the evidence. This "inversion" of conditioning is the foundation of all of **Bayesian statistics**.

---

## Summary

| Result | Formula |
|--------|---------|
| Conditional probability | $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$ |
| Multiplication rule (2 events) | $P(A \cap B) = P(A \mid B)\cdot P(B)$ |
| Multiplication rule ($n$ events) | $P\!\left(\bigcap_{i=1}^n A_i\right) = P(A_1)\cdot P(A_2\mid A_1)\cdots P(A_n \mid \bigcap_{j<n} A_j)$ |
| Bayes' Rule | $P(A \mid B) = \dfrac{P(B \mid A)\cdot P(A)}{P(B)}$ |

---

## Questions to Follow Up

- [ ] How is $P(B)$ expanded using the Law of Total Probability (covered later)?
- [ ] What happens in the continuous case — is the formula the same?
- [ ] Work through a concrete Bayes' Rule example (e.g. medical testing).