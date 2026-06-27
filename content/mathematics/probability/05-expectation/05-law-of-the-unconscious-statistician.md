---
title: Law of the Unconscious Statistician (LOTUS)
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

# Law of the Unconscious Statistician (LOTUS)

> *Introduction to Probability* — Blitzstein & Hwang

---

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
