# Markov Chains — Notes (Lecture + Worked Discussion)

*Stat 110-style notes, reorganized with extra "why" and "how" added where the lecture moved fast — now merged with follow-up clarifications.*

**Lecture source:** https://youtu.be/8AJPs3gvNlY?si=F0QJIo963_FGgz-m

---

## 1. What Is a Markov Chain?

A **stochastic process** is a sequence of random variables evolving over an index (usually time): $X_0, X_1, X_2, \dots$

- If the $X_i$ are i.i.d., each step is a fresh independent draw — no memory at all.
- If we allow *arbitrary* dependence between all the $X_i$, the math becomes intractable almost immediately.
- A **Markov chain** is the compromise: one step beyond i.i.d. The next state depends on the past, but *only through the current state*.

**Why this matters:** it's the simplest way to add "memory" to a process without losing the ability to compute anything. Every formula below depends on this restriction.

We restrict to **discrete time** ($n = 0, 1, 2, \dots$) and a **discrete, finite state space** $\{1, 2, \dots, M\}$.

> **Takeaway:** Markov chains are dependent, but only *loosely* — just enough structure to be useful, just enough simplicity to actually compute.

---

## 2. The Markov Property

For any states $i, j$ and any history $i_0, i_1, \dots, i_{n-1}$:

$$
P(X_{n+1} = j \mid X_n = i,\ X_{n-1} = i_{n-1},\ \dots,\ X_0 = i_0) \;=\; P(X_{n+1} = j \mid X_n = i)
$$

**Intuition:** *past and future are conditionally independent given the present.* If you know where you are right now, knowing how you got there gives you zero extra information about where you're going next.

### 2.1 What "conditionally independent" actually means

Start from the baseline: in most real sequences, the past and future genuinely *are* dependent — knowing where you were yesterday is useful for guessing where you'll be tomorrow.

"Conditional independence" means that once you're handed one specific piece of information — the *condition* — that dependence gets severed. In a Markov chain, the condition is *"knowing the present state."*

**GPS analogy:**
- *Without* knowing your current location: knowing you left New York two days ago and were in Ohio yesterday is genuinely useful for guessing where you'll be in five minutes.
- *Given* your exact current GPS coordinates, heading, and speed: where you started two days ago adds nothing. Your past is now irrelevant once the present is known. That's conditional independence — the past and future become independent *conditional on* the present being fully known.

So: the present is not just "relevant" — it's a complete informational bottleneck. All the predictive value of the past is *already contained in* the present state, so there's nothing left for the older history to add.

### 2.2 How accurate is this assumption, really?

In practice: **almost never perfectly accurate.** It's a modeling idealization, and its accuracy depends entirely on how completely you've defined "the present."

**Where it holds well — physics with full state info.** Modeling a billiard ball's future position: if your present state captures exact position, velocity, spin, and table friction, that's a complete description. Knowing the ball bounced off three cushions five seconds ago adds nothing once you know its exact state right now.

**Where it breaks — hidden variables / partial observability.** If your "present state" leaves out something that actually drives the system, the past sneaks back in as a proxy for what you can't observe. Example: modeling a stock using *only* today's closing price. A stock that's been falling for six straight days carries information (momentum, panic) that today's isolated price doesn't capture — so the past still matters, meaning this state definition isn't truly Markovian.

**The engineering fix — expand the state, don't abandon the model.** If the past matters, fold the needed history directly into the definition of "the present":

- Not Markovian: state = *current speed* (can't tell if accelerating or braking)
- Markovian: state = *(speed at $t{-}2$, speed at $t{-}1$, speed at $t$)*

This is also how "higher-order" Markov chains (next state depends on the last $k$ states) reduce back to the first-order case: bundle the last $k$ values into a single redefined "state."

---

## 3. Homogeneity

A chain is **time-homogeneous** if the transition probability

$$
p_{ij} \;=\; P(X_{n+1} = j \mid X_n = i)
$$

does **not depend on $n$**. The value is determined by which state you're in, not by what time step you're at.

**Key subtlety:** homogeneity does *not* mean every transition shares the same probability $c$. Different pairs $(i,j)$ can have different probabilities — e.g. $p_{12} = 0.3$, $p_{13} = 0.7$, $p_{21} = 0.5$. Homogeneity just means whatever $p_{ij}$ is, it's **constant in $n$**.

**Non-homogeneous contrast example:** if $P(X_2 = \text{rain} \mid X_1 = \text{rain}) = 0.6$ but $P(X_3 = \text{rain} \mid X_2 = \text{rain}) = 0.8$, the transition probability itself depends on $n$, breaking homogeneity.

### 3.1 "But real-world conditions change over time" — reconciling this

This is a fair objection: a self-driving car's safe-braking probability genuinely differs between 2 PM (dry, sunny) and 8 PM (dark, wet). If the transition probabilities visibly shift as the clock ticks, the system *looks* time-inhomogeneous.

**The fix is the same move as in Section 2.1: expand the state, not the time-dependence.** Take whatever is actually changing (weather, lighting) and bake it directly into the state definition, rather than letting it live silently as a function of $n$.

- **Flawed (time-inhomogeneous) state:** $[\text{speed}=50,\ \text{action}=\text{brake}]$
  At $n=10$ (sunny): $P(\text{stop safely}) = 0.99$. At $n=50$ (raining): $P(\text{stop safely}) = 0.60$. The probability is implicitly a function of $n$ — not homogeneous.

- **Fixed (time-homogeneous) state:** $[\text{speed}=50,\ \text{action}=\text{brake},\ \text{road}=\text{wet},\ \text{lighting}=\text{dark}]$
  Now we don't ask "what's $P(\text{stop safely})$ at $n=50$?" — we ask "what's $P(\text{stop safely} \mid \text{wet}, \text{dark})$?" That number (say, 0.60) is now a fixed physical fact, true today, tomorrow, or ten years from now.

**The core distinction:**
- The *environment* is allowed to change (it can start raining).
- The *state* is allowed to change (you transition from a "dry" state to a "wet" state).
- The *rules* — the transition probabilities themselves — are **not** allowed to change.

Time-homogeneity just means the underlying physics/rules don't spontaneously rewrite themselves at 3 PM. As long as the state definition includes every variable that actually affects the odds, the transition matrix stays fixed and the math holds.

---

## 4. The Transition Matrix

Collect all $p_{ij}$ into an $M \times M$ matrix $Q$, where $Q_{ij} = p_{ij}$. Example (4 states, from lecture):

$$
Q =
\begin{bmatrix}
1/3 & 2/3 & 0 & 0 \\
1/2 & 0 & 1/2 & 0 \\
0 & 0 & 0 & 1 \\
1/2 & 0 & 1/4 & 1/4
\end{bmatrix}
$$

**Row $i$ of $Q$ is the PMF of $X_{n+1}$ given $X_n = i$.**

**Properties:**

$$
Q_{ij} \geq 0 \quad \text{for all } i,j
\qquad\qquad
\sum_{j=1}^{M} Q_{ij} = 1 \quad \text{for all } i
$$

**Why rows sum to 1 but columns don't have to:** row $i$ answers "if I'm at state $i$, where could I end up, and with what probability?" — since you must go *somewhere*, this is a full PMF over $j$, so it sums to 1. Column $j$ answers a different question — "who might arrive at $j$, and from where?" — which has no such constraint.

### 4.1 The row's PMF is of *which* random variable, exactly?

To be precise: row $i$ is the PMF of the **conditional random variable** $(X_{n+1} \mid X_n = i)$ — informally, "my next location, given I am certainly at $i$ right now."

$$
\text{Row } i = \Big(\, P(X_{n+1}=1 \mid X_n = i),\ P(X_{n+1}=2 \mid X_n = i),\ \dots,\ P(X_{n+1}=M \mid X_n = i)\,\Big)
$$

So: random variable = *future location*; the conditioning ("given $X_n = i$") is what locks you into a specific row.

### 4.2 Reading a single cell vs. reading a whole row vs. summing — when do you sum?

This trips people up, so it's worth separating cleanly:

**Case A — You know your current state with certainty (you're locked into row $i$).**
No summing is involved anywhere in finding a transition probability.
- One specific cell $Q_{ij}$ = the exact probability of jumping from $i$ straight to $j$. You just index it.
- The whole row $i$ = the complete menu of where you could go next and the exact odds for each — i.e., the PMF from Section 4.1.
- The *only* sum here is checking that the row adds to 1, since you must land somewhere.

**Case B — You're uncertain which state you're starting from** (e.g., you only know a distribution $\pi_n$ over states).
*Now* you need to sum — this is the Law of Total Probability, covered fully in Section 6:

$$
P(X_{n+1} = j) = \sum_i P(X_n = i) \cdot Q_{ij}
$$

**The takeaway:** "summing over all the ways to reach $x$" only enters once your *starting point* itself is uncertain. If you already know exactly where you are, you don't sum probabilities of competing paths to get there — you just read straight across (or into) the relevant row.

**Reverse direction:** any matrix satisfying $Q_{ij} \geq 0$ and $\sum_j Q_{ij} = 1$ is a valid transition matrix for some Markov chain.

---

## 5. Multi-Step Transitions: Why Powers of $Q$ Work

Goal: find $P(X_{n+2} = j \mid X_n = i)$.

**Condition on the missing intermediate state** $X_{n+1} = k$, summing over all possible $k$ (law of total probability):

$$
P(X_{n+2} = j \mid X_n = i) = \sum_{k=1}^{M} P(X_{n+2} = j \mid X_{n+1} = k,\, X_n = i) \cdot P(X_{n+1} = k \mid X_n = i)
$$

By the Markov property, the first factor drops its conditioning on $X_n$:

$$
= \sum_{k=1}^{M} P(X_{n+2} = j \mid X_{n+1} = k) \cdot P(X_{n+1} = k \mid X_n = i)
= \sum_{k=1}^{M} q_{ik}\, q_{kj}
$$

### 5.1 Plain-English reading: "I'm at $i$, I'll hand you $P(k)$; $k$ hands you $P(j)$"

Split the equation into its two factors, in order:

- **"I am $i$, I'll give you $P(k)$":** $P(X_{n+1}=k \mid X_n=i)$ — starting at $i$, the probability of taking one step to an intermediate "middleman" state $k$.
- **"$k$ will give you $P(j)$":** $P(X_{n+2}=j \mid X_{n+1}=k)$ — starting fresh at $k$, the probability of taking the next step to $j$. (Originally this term would also condition on having come from $i$, but the Markov property lets us drop that — once you're at $k$, your history is irrelevant.)

Multiplying these two gives the probability of one specific two-step path, $i \to k \to j$. Since $k$ could be *any* state, you sum over every possible middleman to get the total probability — this is what the $\sum_{k=1}^M$ is doing.

### 5.2 Why is $P(X_n = i)$ missing from the left-hand side?

Notice the left side is $P(X_{n+2}=j \mid X_n=i)$ — there's no separate factor for "probability of starting at $i$." That's because the conditioning bar ($\mid$) already locks in $X_n = i$ with **certainty**. Formally you could write the whole right-hand side multiplied by $P(X_n=i) = 1.0$, but multiplying by 1 changes nothing, so it's dropped.

Contrast this with Section 4.2's "Case B": if you *weren't* certain you started at $i$ (no conditioning bar — you only have a distribution over starting states), then $P(X_n = i)$ would **not** be 1, and you'd be back to the full Law of Total Probability from Section 6, which explicitly keeps that factor.

### 5.3 "All roads" — the flight-layover analogy

The sum over $k$ literally means: *add up every possible road that leads from $i$ to $j$ through some layover.*

Imagine flying from New York ($i$) to Los Angeles ($j$) with exactly one layover, choosing among three possible layover cities (the states $k$): Chicago, Dallas, Denver.

$$
\text{Total} = \underbrace{P(\text{NY}\to\text{Chi})\cdot P(\text{Chi}\to\text{LA})}_{\text{Road via Chicago}} + \underbrace{P(\text{NY}\to\text{Dal})\cdot P(\text{Dal}\to\text{LA})}_{\text{Road via Dallas}} + \underbrace{P(\text{NY}\to\text{Den})\cdot P(\text{Den}\to\text{LA})}_{\text{Road via Denver}}
$$

**Why this is exactly matrix multiplication:** a sum of products of matched indices, $\sum_k q_{ik} q_{kj}$, is precisely the definition of the $(i,j)$ entry of $Q \times Q = Q^2$.

### 5.4 The mechanics: matrix multiplication as a "zipper"

To compute the $(i,j)$ entry of $Q^2$, take **row $i$** of the first $Q$ and **column $j$** of the second $Q$. The index $k$ acts like a zipper: it moves across row $i$ (the step *to* middleman $k$) and simultaneously down column $j$ (the step *from* middleman $k$ to $j$), multiplying the paired entries and summing the results.

$$
\left(Q^2\right)_{ij} = \sum_{k=1}^M Q_{ik} \cdot Q_{kj}
$$

**General result (Chapman–Kolmogorov equation):**

$$
P(X_{n+m} = j \mid X_n = i) \;=\; \left(Q^m\right)_{ij}
$$

### 5.5 Worked Example — the Zipper Method with numbers

Take a 3-state chain with transition matrix:

$$
Q = \begin{bmatrix} 0.2 & 0.5 & 0.3 \\ 0.6 & 0.1 & 0.3 \\ 0.4 & 0.4 & 0.2 \end{bmatrix}
$$

**Goal:** find $P(X_{n+2} = 3 \mid X_n = 1)$ — starting in State 1, the probability of landing in State 3 exactly two steps later.

$$
P(X_{n+2}=3 \mid X_n=1) = \sum_{k=1}^{3} Q_{1k}\cdot Q_{k3}
$$

**Setup:** highlight **Row 1** of $Q$ (we're certain we start at State 1) and **Column 3** of $Q$ (State 3 is the destination):

- Row 1 (start at State 1): $\ Q_{11}=0.2,\ \ Q_{12}=0.5,\ \ Q_{13}=0.3$
- Column 3 (end at State 3): $\ Q_{13}=0.3,\ \ Q_{23}=0.3,\ \ Q_{33}=0.2$

**Zip across, one $k$ at a time:**

| Middleman $k$ | Step 1: $1 \to k$ | Step 2: $k \to 3$ | Path probability |
|---|---|---|---|
| $k=1$ | $Q_{11}=0.2$ | $Q_{13}=0.3$ | $0.2 \times 0.3 = 0.06$ |
| $k=2$ | $Q_{12}=0.5$ | $Q_{23}=0.3$ | $0.5 \times 0.3 = 0.15$ |
| $k=3$ | $Q_{13}=0.3$ | $Q_{33}=0.2$ | $0.3 \times 0.2 = 0.06$ |

**Sum all three roads:**

$$
P(X_{n+2}=3 \mid X_n=1) = 0.06 + 0.15 + 0.06 = \mathbf{0.27}
$$

**Conclusion:** starting in State 1, there's a **27% chance** of being in State 3 exactly two steps later. That $0.27$ is exactly the $(1,3)$ entry of $Q^2$.

**How to use it generally:** to find the probability of being at $j$ exactly $m$ steps after starting at $i$, compute $Q^m$ and read off entry $(i,j)$ — no need to re-derive the conditioning argument each time.

---

## 6. Evolving a Distribution Over Time

Let $\pi_n$ be the row vector of the distribution of $X_n$:

$$
\pi_n = \big(\, P(X_n = 1),\ P(X_n = 2),\ \dots,\ P(X_n = M)\,\big), \qquad \sum_j \pi_n(j) = 1,\ \ \pi_n \geq 0
$$

This is exactly **Case B** from Section 4.2: you're *not* certain which state you're in, only the odds. Same law-of-total-probability argument as Section 5 gives:

$$
\pi_{n+1}(j) = \sum_{i=1}^{M} \pi_n(i)\, q_{ij}
$$

which is exactly the vector–matrix product:

$$
\pi_{n+1} = \pi_n Q
$$

**Why this is the same idea as Section 5:** Section 5 fixed the starting state (a degenerate distribution with probability 1 on state $i$, i.e. $P(X_n=i)=1$ as in Section 5.2); this generalizes to *any* starting distribution $\pi_n$. The underlying computation — a sum of products of matched indices — is identical.

Iterating:

$$
\pi_n = \pi_0\, Q^n
$$

**How to use it:** given a starting distribution $\pi_0$ and a target time $n$, compute one matrix power $Q^n$ and one vector–matrix product, rather than simulating step by step.

---

## 7. Stationary Distribution (preview)

A probability vector $\pi$ (i.e. $\pi \geq 0$, $\sum_j \pi(j) = 1$) is a **stationary distribution** of the chain if:

$$
\pi Q = \pi
$$

**Why it's called "stationary":** from Section 6, if the chain starts with distribution $\pi$, then one step later the distribution is $\pi Q = \pi$ — unchanged. Apply $Q$ again: still $\pi$. So once reached, the distribution is a fixed point of the chain's dynamics:

$$
\pi Q^n = \pi \quad \text{for all } n \geq 0
$$

**Eigenvector connection:** transposing both sides gives $Q^\top \pi^\top = \pi^\top$ — exactly an eigenvalue/eigenvector equation for $Q^\top$ with eigenvalue $1$.

**Open questions flagged in lecture (resolved next time, under mild conditions):**

1. **Existence:** does a solution $\pi$ to $\pi Q = \pi$ with $\pi \geq 0,\ \sum_j \pi(j)=1$ always exist?
2. **Uniqueness:** is it the only such solution?
3. **Convergence:** does $\pi_n \to \pi$ as $n \to \infty$, regardless of $\pi_0$?
4. **Computability:** can $\pi$ be found efficiently, without solving an $M$-variable linear system by brute force?

---

## 8. Two Different Ways Markov Chains Get Used

- **As a literal model** of a real system (weather, stock prices, text generation) — whether the Markov assumption is reasonable is an empirical question (see Section 2.2).
- **Markov Chain Monte Carlo (MCMC):** construct a synthetic chain on purpose, engineered so its stationary distribution $\pi$ equals some complicated target distribution of interest. Running the chain long enough on a computer lets you sample from (or approximate) $\pi$ — useful when direct computation is intractable.

---

## 9. Quick Reference Cheat Sheet

| Want | Formula |
|---|---|
| One-step transition probability | $q_{ij} = P(X_{n+1}=j \mid X_n=i)$ |
| $m$-step transition probability | $\left(Q^m\right)_{ij}$ |
| Distribution one step later | $\pi_{n+1} = \pi_n Q$ |
| Distribution $n$ steps from start | $\pi_n = \pi_0 Q^n$ |
| Stationary distribution | $\pi$ such that $\pi Q = \pi$ |
| Row sum of $Q$ | $\sum_j Q_{ij} = 1$ |
| Homogeneity condition | $q_{ij}$ independent of $n$ |
| Certain state → single transition | read cell $Q_{ij}$ directly, no summing |
| Uncertain state → marginal probability | sum over starting states (Law of Total Probability) |

---

## 10. Open Threads for Next Lecture

- Existence/uniqueness/convergence proofs for stationary distributions
- Efficient computation tricks (some chains don't need matrix algebra at all)
- Worked examples
