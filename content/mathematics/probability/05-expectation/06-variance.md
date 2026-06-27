---
title: Variance
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

# Variance

> *Introduction to Probability* — Blitzstein & Hwang

---

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
