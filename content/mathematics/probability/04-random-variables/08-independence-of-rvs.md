---
title: Independence of Random Variables
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

# Independence of Random Variables

> *Introduction to Probability* — Blitzstein & Hwang

---

## Independence of Random Variables

> **Definition:** Random variables $X$ and $Y$ are *independent* if:
> $$P(X \leq x, Y \leq y) = P(X \leq x) P(Y \leq y) \quad \text{for all } x, y \in \mathbb{R}$$

Knowing $X$'s value gives no information about $Y$, and vice versa.

**Discrete equivalent condition:**
$$P(X = x, Y = y) = P(X = x) P(Y = y)$$
for all $x, y$ in the respective supports. Much easier to check in practice.

---

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

---

### Independence of many r.v.s

$$P(X_1 \leq x_1, \ldots, X_n \leq x_n) = P(X_1 \leq x_1) \cdots P(X_n \leq x_n)$$

For infinitely many r.v.s: every finite subset must be independent.

**Pairwise vs mutual independence:** Full independence implies pairwise independence (let all other variables go to $\infty$), but pairwise independence does NOT imply full independence. Full independence is strictly stronger.

**i.i.d.:** Random variables that are **independent** and **identically distributed**. Two completely different concepts — each can hold or fail regardless of the other.

**Four cases to fully understand the distinction:**

* **Case 1 — Independent AND identically distributed (i.i.d.):**
  Let $X$ = result of a die roll, $Y$ = result of a second independent die roll. Both $X, Y \sim \text{DUnif}(\{1,\ldots,6\})$ and independent — one roll tells you nothing about the other. This is the i.i.d. case.

* **Case 2 — Independent but NOT identically distributed:**
  Let $X$ = result of a die roll, $Y$ = closing price of the Dow Jones stock index a month from now. $X$ and $Y$ are independent (a die roll tells you nothing about the stock market), but they clearly do not have the same distribution.

* **Case 3 — Identically distributed but NOT independent:**
  Let $X$ = number of Heads in $n$ coin tosses, $Y$ = number of Tails in those same $n$ tosses. Both $X, Y \sim \text{Bin}(n, 1/2)$ — same distribution — but $Y = n - X$ so knowing $X$ tells you $Y$ exactly. Completely dependent: $P(Y = n - X) = 1$.

* **Case 4 — Dependent AND not identically distributed:**
  Let $X$ = indicator of whether the majority party retains control of the House after the next election, $Y$ = average favorability rating of the majority party in polls taken within a month of the election. $X$ and $Y$ are dependent (poll ratings and election outcomes are related) and do not share the same distribution.

> **The core distinction:** Same distribution describes how a single r.v. behaves in isolation — what values it takes and with what probabilities. Independence describes how two r.v.s relate to each other — whether one gives information about the other. These are completely orthogonal properties.

| | Independent | Identically distributed |
|---|---|---|
| Meaning | Knowing one tells you nothing about the others | Same PMF / distribution |
| Case 1 i.i.d. | ✅ | ✅ |
| Case 2 | ✅ | ❌ |
| Case 3 | ❌ | ✅ |
| Case 4 | ❌ | ❌ |

**Functions of independent r.v.s:** If $X \perp Y$, then $g(X) \perp h(Y)$ for any functions $g$, $h$. Knowing $g(X)$ can only reveal information about $X$ — and since $X$ tells you nothing about $Y$, it tells you nothing about $h(Y)$ either.

---

## Sum of Independent Binomials

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
