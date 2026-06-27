---
title: Poisson Distribution
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

# Poisson Distribution

> *Introduction to Probability* — Blitzstein & Hwang | Chapter 4.7

---

## Definition

**Definition 4.7.1 (Poisson distribution):** An r.v. $X$ has the *Poisson distribution* with parameter $\lambda$, where $\lambda > 0$, if the PMF of $X$ is:

$$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k = 0, 1, 2, \ldots$$

We write this as $X \sim \text{Pois}(\lambda)$.

**Breaking down the formula:**

- $X$ is the count of events — it can only take discrete non-negative integer values $k = 0, 1, 2, \ldots$
- $\lambda$ (lambda) is the **rate parameter** — the average number of events expected in the interval. The condition $\lambda > 0$ simply means the average rate must be strictly positive.
- $P(X = k)$ gives the exact probability of observing exactly $k$ events given average rate $\lambda$.

**Why the formula is structured the way it is:** The $\lambda^k$ term in the numerator grows as $k$ gets larger (when $\lambda > 1$), but the $k!$ in the denominator grows much faster — eventually crushing the probability toward zero for very large $k$. The $e^{-\lambda}$ term acts as a normalizing constant ensuring all probabilities sum to exactly 1.

---

## Validity — Why the PMF Sums to 1

For any function to be a valid PMF, the sum of all probabilities across every possible outcome must equal exactly 1.

### The Taylor Series Proof

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

### What P(X = 0) Looks Like

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

## Mean and Variance of a Poisson R.V.

**Example 4.7.2:** Let $X \sim \text{Pois}(\lambda)$. Both the mean and the variance equal $\lambda$.

---

### Finding E(X) — The Cancellation Trick

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

### Finding Var(X) — The Calculus Method via LOTUS

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

### The Factorial Moment Method (Alternative)

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

### Why Mean = Variance is Remarkable

In probability theory, having Mean = Variance is the **defining hallmark** of a Poisson process. It means that as events become more frequent, your uncertainty about the exact number grows at the exact same rate.

- $\lambda = 2$: The distribution is tight. Values of 1, 2, or 3 are highly likely. The spread is small.
- $\lambda = 100$: The distribution is much wider. Getting 90 or 110 events is completely normal. The "curve" flattens and widens as $\lambda$ grows.

**Important note:** For the Poisson distribution, $E[X(X-1)]$ and $[E(X)]^2$ both equal $\lambda^2$ — a coincidence specific to this distribution. In general, $E[X(X-1)] \neq [E(X)]^2$. The fact that they cancel each other out is exactly what forces $\text{Var}(X) = \lambda$.

---

## Shape of the Poisson Distribution

Figure 4.7 in the textbook shows the PMF and CDF of $\text{Pois}(2)$ and $\text{Pois}(5)$ from $k = 0$ to $k = 10$.

**Key observations:**

**Center:** The mean of Pois(2) is around 2 and the mean of Pois(5) is around 5 — consistent with $E(X) = \lambda$. Visually, the "center of mass" of the PMF bar chart balances exactly at the $\lambda$ value.

**Skewness for small $\lambda$:** The PMF of Pois(2) is **highly right-skewed**. The Poisson distribution models event counts, meaning the $x$-axis ($k$) can never be negative — there is a hard "wall" at $x = 0$. When $\lambda$ is small, the center of the graph sits right up against this wall. Since values cannot spread left past zero but can stretch arbitrarily far right, the graph is scrunched on the left and stretched on the right — a right-skewed distribution.

**Bell-shaped for larger $\lambda$:** As $\lambda$ grows larger, the skewness is reduced and the PMF becomes more bell-shaped. As $\lambda$ increases, the center walks away from the zero wall and the distribution has room to spread symmetrically in both directions. For sufficiently large $\lambda$, the Poisson distribution approximates a Normal (Gaussian) distribution — this is the Central Limit Theorem taking effect.

---

## The Poisson Paradigm (Law of Rare Events)

### What "Rare" Actually Means

The Poisson paradigm is also called the **law of rare events**. The interpretation of "rare" is crucial and often misunderstood:

> **"Rare" means the $p_j$ are small — not that $\lambda$ is small.**

For example: receiving 50 emails in an hour ($\lambda = 50$) is not a rare event — it happens all the time. But the Poisson paradigm still holds because the probability that any *specific person* emails you in any *specific millisecond* is microscopic. It is a barrage of rare micro-events combining into a very common macro-event.

---

### The Formal Statement

**Theorem (Poisson Paradigm):** Let $A_1, \ldots, A_n$ be events with $p_j = P(A_j)$, where $n$ is large, the $p_j$ are small, and the $A_j$ are independent or weakly dependent. Let:

$$X = \sum_{j=1}^{n} I(A_j)$$

count how many of the $A_j$ occur, where $I(A_j)$ is the indicator r.v. for event $A_j$. Then $X$ is approximately distributed as $\text{Pois}(\lambda)$, with:

$$\lambda = \sum_{j=1}^{n} p_j$$

**Key upgrade over the simplified version:** The $p_j$'s don't have to be identical — they can vary across trials. As long as each individual probability is small, you can simply add them all up to get $\lambda$. This makes the paradigm far more flexible than it might first appear.

**"Weakly dependent":** The paradigm also relaxes the independence assumption. Events that are slightly correlated (e.g., cars driving in packs on a highway) still permit the Poisson approximation, as long as the dependencies are localized. The precise definition of weak dependence and how to verify it are advanced topics (requiring measure theory).

---

### Real-World Examples

The following real-world quantities could follow an approximately Poisson distribution:

**Emails per hour:** There are many people who could potentially email you in that hour, but the probability that any specific person actually emails you in that specific hour is small. Alternatively, subdivide the hour into milliseconds — there are $3.6 \times 10^6$ milliseconds in an hour, but in any specific millisecond it is very unlikely you receive an email. $\lambda \approx 20$ emails per hour.

**Chocolate chips in a cookie:** Subdivide the cookie into small cubes. The probability of a chocolate chip landing in any single cube is small, but the number of cubes is large. $\lambda \approx 10$ chips per cookie.

**Earthquakes per year:** At any given time and location, the probability of an earthquake is small, but there are a large number of possible times and locations. $\lambda \approx 2$ earthquakes per year in a region.

In each case: $\lambda$ is the rate parameter, $k$ is the actual observed count in the interval, and $\lambda = n \cdot p$ where $n$ is the large number of trials and $p$ is the small per-trial probability.

---

### The Bridge: From Binomial to Poisson

The Poisson distribution is the mathematical limiting case of the Binomial when $n$ is very large and $p$ is very small, with $\lambda = np$ held constant.

**Why this matters:** If you tried to calculate exact Binomial probabilities with $n = 10^{12}$ trials, the combinatorial computation ($\binom{n}{k}$) would cause integer overflow on virtually any computer. The Poisson distribution provides a clean closed-form approximation:

$$\text{Bin}(n, p) \approx \text{Pois}(\lambda) \quad \text{when } n \text{ large, } p \text{ small, } \lambda = np$$

**The macro-micro connection you derived:**

$$\lambda = n \cdot p \quad \Leftrightarrow \quad p = \frac{\lambda}{n}$$

The micro-level probability $p$ is just the average rate $\lambda$ divided by the number of trials — exactly the naive definition of probability (number of expected occurrences over total trials). The Poisson distribution rescues us from the microscopic, unusable probability $p$ and lets us work entirely with the stable, observable average $\lambda$.

---

### The Error Bound — Stein-Chen Method

A remarkable theorem gives an upper bound on the error incurred from using a Poisson approximation. If the $A_j$ are independent, $N \sim \text{Pois}(\lambda)$, and $B$ is any set of nonnegative integers, then:

$$|P(X \in B) - P(N \in B)| \leq \min\!\left(1, \frac{1}{\lambda}\right) \sum_{j=1}^{n} p_j^2$$

**What the left side means:** The absolute difference between the true probability (using the exact distribution of $X$) and the Poisson approximation (using $N$), for any possible question $B$ you could ask.

**What the right side means — why squaring small numbers is the key:**

The crucial term is $\sum p_j^2$. Because probabilities are fractions less than 1, squaring them makes them much smaller:
$$0.01^2 = 0.0001 \quad \text{(100 times smaller)}$$

So when all $p_j$ are tiny, $\sum p_j^2$ is crushed to near zero even when summing many terms — making the error bound negligibly small. This is the precise mathematical reason why the Poisson paradigm works only for **rare events** with small $p_j$.

If the events are not rare (e.g., $p = 0.5$ like a coin flip): $\sum p_j^2 = n \cdot (0.5)^2 = 0.25n$, which is huge — the error bound would be massive, telling you that the Poisson approximation is completely invalid here.

The $\min(1, 1/\lambda)$ factor acts as a stabilizer: for small $\lambda$ it caps at 1; for large $\lambda$ it shrinks the error further.

**Note:** Proving this bound rigorously requires the **Stein-Chen method**, an advanced graduate-level technique. At this stage, we accept the result and understand *when* to trust the approximation — which is fully captured by the condition that the $p_j$ are small.

---

### Why the Poisson is Not Exactly Correct

The Poisson r.v. has **no upper bound** — $k$ can be any nonnegative integer. But in real applications, the number of events is always bounded by the number of trials $n$. You cannot have more successes than trials, and you cannot physically cram an infinite number of chocolate chips into a cookie.

However, this theoretical mismatch is harmless in practice: the Poisson probability for $k$ far above $\lambda$ is so infinitesimally small that the physical impossibility doesn't corrupt the model. The formula's infinite "tail" is negligible.

The conditions for the Poisson paradigm are also flexible:
- The $n$ trials can have **different** success probabilities $p_j$ (not all equal)
- The trials don't have to be fully independent, only **not very dependent**

This flexibility makes the Poisson a popular starting model for **count data** — any data consisting of nonnegative integers representing how many times something happened (network failures, website clicks, customer arrivals, document typos, etc.).

---

## Occupancy Problems

### Setup

There are $k$ distinguishable balls and $n$ distinguishable boxes. The balls are randomly placed in the boxes, with all $n^k$ possibilities equally likely. Problems in this setting are called **occupancy problems**, and are at the core of many widely used algorithms in computer science (particularly hash tables, where keys are balls and memory buckets are boxes).

---

### Expected Number of Empty Boxes — Indicator Method

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

### Why Indicator Variables Beat Brute Force

There are two approaches to this problem. Understanding why one is elegant and the other is a nightmare is the real lesson:

**Method 1 — Brute Force (State Space):**

Use $E(X) = \sum_x x \cdot P(X = x)$. You must calculate the exact probability of exactly 0, 1, 2, ..., $n-1$ boxes being empty, then weight and sum. Each of those probabilities requires tracking where all $k$ balls go simultaneously — using the Inclusion-Exclusion Principle and Stirling Numbers of the Second Kind. For large $n$, this is computationally explosive and algebraically miserable.

**Method 2 — Indicator Variables (Perspective Shift):**

Instead of tracking all $k$ balls globally, put blinders on and look at exactly **one box**. Ask a simple binary question: "Is this box empty?" The answer is just the probability that all $k$ balls independently missed this one box. Then use Linearity of Expectation — which works regardless of dependence — to scale the single-box answer up to all $n$ boxes.

The power of the indicator approach: it changes the fundamental unit from "the whole system" to "a single binary switch." The LOE then stitches the macroscopic average back together without ever needing to reason about the joint distribution of all boxes simultaneously.

---

### Probability That At Least One Box is Empty — Inclusion-Exclusion

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

### Worked Example — Poisson Approximation for At Least One Empty Box

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
