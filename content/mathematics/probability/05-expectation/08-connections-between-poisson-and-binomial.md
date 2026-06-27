---
title: Connections Between Poisson and Binomial
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

# Connections Between Poisson and Binomial

> *Introduction to Probability* — Blitzstein & Hwang | Chapter 4.8

---

## The Grand Parallel

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

## Sum of Independent Poissons

**Theorem 4.8.1:** If $X \sim \text{Pois}(\lambda_1)$, $Y \sim \text{Pois}(\lambda_2)$, and $X$ is independent of $Y$, then:

$$X + Y \sim \text{Pois}(\lambda_1 + \lambda_2)$$

The Poisson distribution is **closed under addition** — adding two independent Poisson r.v.s gives another Poisson r.v., with rate equal to the sum of the individual rates.

---

### The Intuition — Traffic Story

Think of two types of cars passing a checkpoint:
- Blue cars arrive at rate $\lambda_1 = 3$ per hour
- Red cars arrive at rate $\lambda_2 = 7$ per hour

Both types arrive randomly and independently. If you stop caring about color and just count **total cars**, the underlying mechanics haven't changed — cars still arrive randomly in a continuous time interval. You now just expect $\lambda_1 + \lambda_2 = 10$ cars per hour. The total count perfectly follows $\text{Pois}(10)$.

The rates add because the two independent streams of events simply merge into one combined stream.

---

### The Proof — Full Derivation

**Strategy:** Use the Law of Total Probability. To find $P(X + Y = k)$, condition on every possible value $X$ could take — for each value $j$ that $X$ takes, $Y$ must take $k - j$ to make the total equal $k$.

$$P(X+Y=k) = \sum_{j=0}^{k} P(X+Y=k \mid X=j) \cdot P(X=j)$$

Since $X$ and $Y$ are **independent**, knowing $X = j$ tells us nothing about $Y$:

$$= \sum_{j=0}^{k} P(Y=k-j) \cdot P(X=j)$$

**Plug in the Poisson PMFs:**

$$= \sum_{j=0}^{k} \frac{e^{-\lambda_2}\lambda_2^{k-j}}{(k-j)!} \cdot \frac{e^{-\lambda_1}\lambda_1^j}{j!}$$

**Factor out the $e$ terms** (they don't depend on $j$, so they come out of the sum):

$$= e^{-(\lambda_1+\lambda_2)} \sum_{j=0}^{k} \frac{\lambda_1^j \lambda_2^{k-j}}{j!(k-j)!}$$

---

### The Missing Step — How the Binomial Theorem Appears

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

## Poisson Given a Sum of Poissons — Conditioning Gives Binomial

**Theorem 4.8.2:** If $X \sim \text{Pois}(\lambda_1)$, $Y \sim \text{Pois}(\lambda_2)$, and $X$ is independent of $Y$, then the conditional distribution of $X$ given $X + Y = n$ is:

$$X \mid (X+Y=n) \sim \text{Bin}\!\left(n,\, \frac{\lambda_1}{\lambda_1+\lambda_2}\right)$$

**Intuition:** You have blue cars ($\lambda_1$) and red cars ($\lambda_2$) arriving independently. You are then told the total number of cars that arrived was $n$. Given this new information, what is the distribution of the number of blue cars?

Once you lock in the total $n$, you lose the infinite, boundary-free nature of the Poisson — you now have exactly $n$ "slots" and each car is independently blue with probability $\frac{\lambda_1}{\lambda_1 + \lambda_2}$. That is precisely a Binomial experiment.

---

### The Setup

We want to find $P(X = k \mid X+Y = n)$ for each $k \in \{0, 1, \ldots, n\}$.

By Bayes' rule (conditional probability):

$$P(X=k \mid X+Y=n) = \frac{P(X+Y=n \mid X=k) \cdot P(X=k)}{P(X+Y=n)}$$

Given $X = k$, the total $X + Y = n$ requires $Y = n - k$, so:

$$P(X+Y=n \mid X=k) = P(Y = n-k)$$

By independence of $X$ and $Y$. So:

$$P(X=k \mid X+Y=n) = \frac{P(Y=n-k) \cdot P(X=k)}{P(X+Y=n)}$$

By Theorem 4.8.1, $X + Y \sim \text{Pois}(\lambda_1 + \lambda_2)$, so we know the denominator exactly.

---

### The Proof — Four Magic Tricks

#### Trick 1 — Bayes' Rule Setup

Plug in the three Poisson PMFs:

$$P(X=k \mid X+Y=n) = \frac{\dfrac{e^{-\lambda_2}\lambda_2^{n-k}}{(n-k)!} \cdot \dfrac{e^{-\lambda_1}\lambda_1^k}{k!}}{\dfrac{e^{-(\lambda_1+\lambda_2)}(\lambda_1+\lambda_2)^n}{n!}}$$

---

#### Trick 2 — The Great Cancellation

Look at the $e$ terms:
- Numerator: $e^{-\lambda_2} \cdot e^{-\lambda_1} = e^{-(\lambda_1+\lambda_2)}$
- Denominator: $e^{-(\lambda_1+\lambda_2)}$

They are **identical** — they cancel completely:

$$\frac{e^{-(\lambda_1+\lambda_2)}}{e^{-(\lambda_1+\lambda_2)}} = 1$$

This is the most critical step in the proof. The $e^{-\lambda}$ term is what gives the Poisson its infinite tail — its ability to take any nonnegative integer value. The moment it cancels out, the distribution is no longer infinite. It is suddenly locked inside a finite box of size $n$.

After cancellation, what remains is:

$$\frac{\dfrac{\lambda_1^k \lambda_2^{n-k}}{k!(n-k)!}}{\dfrac{(\lambda_1+\lambda_2)^n}{n!}}$$

---

#### Trick 3 — Combinatorics Emerge

Dividing the numerator fraction by the denominator fraction means multiplying by the reciprocal. The $n!$ from the denominator flips up:

$$= \frac{n!}{k!(n-k)!} \cdot \frac{\lambda_1^k \lambda_2^{n-k}}{(\lambda_1+\lambda_2)^n}$$

The piece $\frac{n!}{k!(n-k)!}$ is exactly $\binom{n}{k}$ — the combinatorial coefficient for choosing $k$ successes from $n$ trials. The system has **automatically generated** the combinatorics needed for a Binomial distribution.

---

#### Trick 4 — The Probability p Emerges

Now handle the $\lambda$ terms:

$$\frac{\lambda_1^k \lambda_2^{n-k}}{(\lambda_1+\lambda_2)^n}$$

Split $(\lambda_1+\lambda_2)^n$ into $(\lambda_1+\lambda_2)^k \cdot (\lambda_1+\lambda_2)^{n-k}$ and group:

$$= \left(\frac{\lambda_1}{\lambda_1+\lambda_2}\right)^k \left(\frac{\lambda_2}{\lambda_1+\lambda_2}\right)^{n-k}$$

Let $p = \frac{\lambda_1}{\lambda_1+\lambda_2}$. Then $1 - p = \frac{\lambda_2}{\lambda_1+\lambda_2}$. So this becomes:

$$= p^k (1-p)^{n-k}$$

The **success probability** $p$ is exactly the rate of $X$ divided by the total rate — the fraction of all events that are type $X$. This makes complete sense: given that $n$ total events occurred, each event independently belongs to type $X$ with probability proportional to its rate.

---

### The Final Result

Putting Tricks 3 and 4 together:

$$P(X=k \mid X+Y=n) = \binom{n}{k} p^k (1-p)^{n-k}, \quad p = \frac{\lambda_1}{\lambda_1+\lambda_2}$$

This is exactly the $\text{Bin}\!\left(n, \frac{\lambda_1}{\lambda_1+\lambda_2}\right)$ PMF. $\blacksquare$

**Summary of what conditioning did:** Starting with two unbounded Poisson r.v.s (each can take any nonnegative integer value), the moment we condition on their sum being $n$, three things happen automatically:
1. The infinite $e^{-\lambda}$ tails cancel — the distribution becomes finite
2. The factorials rearrange into $\binom{n}{k}$ — combinatorics appear
3. The $\lambda$ ratios become success/failure probabilities — the Binomial structure emerges

The Poissons are completely eradicated. You are left holding the pure Binomial PMF.

---

## Poisson Approximation to Binomial — Limit Gives Poisson

### The Theorem

**Theorem 4.8.3 (Poisson approximation to Binomial):** If $X \sim \text{Bin}(n, p)$ and we let $n \to \infty$ and $p \to 0$ such that $\lambda = np$ remains fixed, then the PMF of $X$ converges to the $\text{Pois}(\lambda)$ PMF:

$$P(X = k) \to \frac{e^{-\lambda}\lambda^k}{k!}$$

More generally, the same conclusion holds if $n \to \infty$ and $p \to 0$ in such a way that $np$ converges to a constant $\lambda$.

This is a special case of the Poisson paradigm where the $A_j$ are independent with the same probabilities. In this special case we can prove the approximation works by directly taking a limit of the Binomial PMF.

---

### The Proof — Four Blocks

#### Step 1 — Substitute p = λ/n

Start with the Binomial PMF and eliminate $p$ by substituting $p = \frac{\lambda}{n}$ (since $\lambda = np$ is fixed):

$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$

Expand $\binom{n}{k} = \frac{n(n-1)\cdots(n-k+1)}{k!}$ and substitute $p = \frac{\lambda}{n}$:

$$= \frac{n(n-1)\cdots(n-k+1)}{k!} \cdot \left(\frac{\lambda}{n}\right)^k \cdot \left(1 - \frac{\lambda}{n}\right)^{n-k}$$

---

#### Step 2 — Shatter into Four Blocks

Reorganize by pulling $\frac{\lambda^k}{k!}$ to the front, sliding $n^k$ underneath the numerator expansion, and splitting the last exponent:

$$P(X=k) = \underbrace{\frac{\lambda^k}{k!}}_{\text{Block 1}} \cdot \underbrace{\frac{n(n-1)\cdots(n-k+1)}{n^k}}_{\text{Block 2}} \cdot \underbrace{\left(1-\frac{\lambda}{n}\right)^n}_{\text{Block 3}} \cdot \underbrace{\left(1-\frac{\lambda}{n}\right)^{-k}}_{\text{Block 4}}$$

---

#### Step 3 — Take the Limit on Each Block

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

#### Step 4 — Reassemble

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

## The Full Picture — Switching Tools on the Fly

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

## The Poisson Splitting Property

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

## Worked Example — Poisson Approximation in Practice

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
