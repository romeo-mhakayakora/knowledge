---
title: Conditioning Continued, Law of Total Probability
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
**Source:** [Lecture 5: Conditioning Continued, Law of Total Probability (YouTube)](https://youtu.be/JzDvVgNDxo8)  
**Book chapter(s):** Ch. 2

---

## Core Theme

Statistics is a course in **thinking**. Two master strategies for tackling hard problems:

1. **Try simple and extreme cases** — test the boundaries of a problem to build intuition before solving the general case.
2. **Break the problem into simpler pieces** — decompose a hard problem, solve each piece, then reassemble.

The Law of Total Probability is the mathematical formalisation of strategy 2.

---

## 1. Law of Total Probability (LOTP)

### Setup — Partition of a Sample Space

A collection of events $A_1, A_2, \dots, A_n$ forms a **partition** of the sample space $S$ if:

- **Mutually exclusive (disjoint):** $A_i \cap A_j = \emptyset$ for all $i \neq j$
- **Exhaustive:** $A_1 \cup A_2 \cup \cdots \cup A_n = S$

### Derivation

For any event $B$, decompose it using the partition:

$$B = (B \cap A_1) \cup (B \cap A_2) \cup \cdots \cup (B \cap A_n)$$

Since the pieces $B \cap A_i$ are disjoint, by the addition rule:

$$P(B) = P(B \cap A_1) + P(B \cap A_2) + \cdots + P(B \cap A_n)$$

Applying the multiplication rule $P(B \cap A_i) = P(B \mid A_i)\,P(A_i)$ to each term:

$$\boxed{P(B) = \sum_{i=1}^{n} P(B \mid A_i)\, P(A_i)}$$

> **Intuition:** You cannot compute $P(B)$ directly, but you *can* compute it in each "world" $A_i$ separately. LOTP is the weighted average of those conditional probabilities, weighted by how likely each world is.

---

## 2. Example 1 — Two-Card Hand (Ace Problem)

**Setup:** Deal a random two-card hand from a standard 52-card deck. Compare two subtly different conditions.

### Case A: Given you have *an* Ace

$$P(\text{both Aces} \mid \text{have an Ace}) = \frac{P(\text{both Aces} \cap \text{have an Ace})}{P(\text{have an Ace})}$$

Since having both Aces implies having an Ace, the intersection simplifies:

$$= \frac{P(\text{both Aces})}{P(\text{at least one Ace})}$$

**Numerator** — choose 2 Aces from 4:

$$P(\text{both Aces}) = \frac{\dbinom{4}{2}}{\dbinom{52}{2}}$$

**Denominator** — use the complement (easier than counting directly):

$$P(\text{at least one Ace}) = 1 - P(\text{no Aces}) = 1 - \frac{\dbinom{48}{2}}{\dbinom{52}{2}}$$

**Result:**

$$P(\text{both Aces} \mid \text{have an Ace}) = \frac{\dbinom{4}{2}}{\dbinom{52}{2} - \dbinom{48}{2}} = \frac{6}{1326 - 1128} = \frac{6}{198} = \frac{1}{33} \approx 0.030$$

---

### Case B: Given you have the *Ace of Spades* specifically

Knowing one card is the Ace of Spades, the second card is equally likely to be any of the remaining 51 cards. Three of those 51 cards are Aces.

$$P(\text{both Aces} \mid \text{have Ace of Spades}) = \frac{3}{51} = \frac{1}{17} \approx 0.059$$

### Key Takeaway

$$\frac{1}{17} \approx 0.059 \quad \gg \quad \frac{1}{33} \approx 0.030$$

The probability **nearly doubles** just by specifying *which* Ace you hold. The conditioning event "Ace of Spades" carries strictly more information than "an Ace." This illustrates how **conditional probability is exquisitely sensitive to the exact wording** of the given condition.

---

## 3. Example 2 — Disease Testing (Bayes + LOTP)

A canonical example showing why human intuition systematically fails at probability.

### Setup

| Symbol | Meaning |
|--------|---------|
| $D$ | Patient has the disease |
| $D^c$ | Patient does not have the disease |
| $T$ | Patient tests positive |
| $T^c$ | Patient tests negative |

### Given information

$$P(D) = 0.01 \qquad \text{(disease prevalence: 1\%)}$$

$$P(T \mid D) = 0.95 \qquad \text{(true positive rate / sensitivity)}$$

$$P(T^c \mid D^c) = 0.95 \qquad \text{(true negative rate / specificity)}$$

$$\implies P(T \mid D^c) = 0.05 \qquad \text{(false positive rate)}$$

### Goal

Find $P(D \mid T)$ — the probability the patient is truly sick given a positive result.

### Solution — Bayes' Rule + LOTP

Apply Bayes' Rule:

$$P(D \mid T) = \frac{P(T \mid D)\, P(D)}{P(T)}$$

Expand $P(T)$ in the denominator using LOTP with partition $\{D, D^c\}$:

$$P(T) = P(T \mid D)\,P(D) + P(T \mid D^c)\,P(D^c)$$

Substituting all values:

$$P(D \mid T) = \frac{0.95 \times 0.01}{(0.95 \times 0.01) + (0.05 \times 0.99)}$$

$$= \frac{0.0095}{0.0095 + 0.0495} = \frac{0.0095}{0.0590} \approx 0.161$$

### Takeaway

> Even with a **95% accurate test**, a positive result only means roughly a **16% chance** of actually having the disease.

Most people guess ~95%. The correct answer is ~16%. The gap exists because people focus entirely on the test accuracy and completely ignore the **prior** $P(D) = 0.01$. The base rate is very low, so most positive tests come from the large healthy population generating false positives, not from the small sick population.

---

## 4. "Biohazards" — Three Common Mistakes

### Biohazard 1 — The Prosecutor's Fallacy

Confusing $P(A \mid B)$ with $P(B \mid A)$.

$$P(A \mid B) \neq P(B \mid A) \quad \text{in general}$$

*In court:* the probability of the evidence given innocence $P(E \mid \text{innocent})$ is **not** the same as the probability of innocence given the evidence $P(\text{innocent} \mid E)$.

---

### Biohazard 2 — Confusing Prior with Posterior

Confusing $P(A)$ (the prior) with $P(A \mid B)$ (the posterior).

If a problem tells you "assume event $A$ occurred," you work with the posterior $P(\,\cdot \mid A)$. You do **not** retroactively set $P(A) = 1$.

> Note: it is mathematically true that $P(A \mid A) = 1$, but substituting this back into the prior is a logical error — the prior and posterior live at different stages of reasoning.

---

### Biohazard 3 — Conflating Independence and Conditional Independence

These are **distinct** concepts. Neither implies the other.

---

## 5. Independence vs. Conditional Independence

### Definition — Conditional Independence

Events $A$ and $B$ are **conditionally independent given $C$** if:

$$\boxed{P(A \cap B \mid C) = P(A \mid C)\, P(B \mid C)}$$

Equivalently (when $P(B \mid C) > 0$):

$$P(A \mid B \cap C) = P(A \mid C)$$

That is, once $C$ is known, learning $B$ tells you nothing additional about $A$.

---

### Does conditional independence $\Rightarrow$ unconditional independence? **No.**

**Example — Chess opponent of unknown strength:**

- Let $W_k$ = win game $k$.
- Given the opponent's true skill level $C$, the outcomes $W_1, W_2, \dots$ are independent: $P(W_k \mid C)$ does not depend on other game results.
- **Unconditionally**, they are *dependent*: winning the first 5 games tells you the opponent is weak, which raises $P(W_6)$. Conditioning on the hidden variable $C$ breaks a dependence that exists in the marginal world.

---

### Does unconditional independence $\Rightarrow$ conditional independence? **No.**

**Example — Fire alarm:**

Let:
- $F$ = there is a fire
- $C$ = someone is making popcorn
- $A$ = the fire alarm goes off

Assume $F$ and $C$ are **unconditionally independent** — whether there is a fire has nothing to do with whether someone is making popcorn.

Now condition on the alarm going off ($A$). If you then learn no one is making popcorn ($C^c$), the only remaining explanation for the alarm is a real fire:

$$P(F \mid A,\, C^c) = 1$$

So $F$ and $C$ become **dependent** once you condition on $A$, even though they were independent marginally. This phenomenon is sometimes called **explaining away** — one cause "explains away" the other once you know the effect occurred.

---

## Summary

| Concept | Formula |
|---------|---------|
| Law of Total Probability | $P(B) = \displaystyle\sum_{i=1}^{n} P(B \mid A_i)\,P(A_i)$ |
| Bayes' Rule with LOTP denominator | $P(A_j \mid B) = \dfrac{P(B \mid A_j)\,P(A_j)}{\displaystyle\sum_{i=1}^{n} P(B \mid A_i)\,P(A_i)}$ |
| Conditional independence | $P(A \cap B \mid C) = P(A \mid C)\,P(B \mid C)$ |

---

## Questions to Follow Up

- [ ] Work through more Bayes' Rule examples with different priors to build intuition for base-rate neglect.
- [ ] Explore the full Bayes' Rule with LOTP denominator for $n > 2$ partition pieces.
- [ ] What is "explaining away" more formally — is there a graphical model formulation?
- [ ] How does conditional independence connect to Bayesian networks / causal graphs?