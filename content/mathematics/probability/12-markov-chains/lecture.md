# Markov Chains — Notes (Lecture + Worked Discussion)

*Stat 110-style notes, reorganized with extra "why" and "how" added where the lecture moved fast.*

**Lecture source:** https://youtu.be/8AJPs3gvNlY?si=F0QJIo963_FGgz-m

---

## 1. What Is a Markov Chain?

A **stochastic process** is a sequence of random variables evolving over an index (usually time): $X_0, X_1, X_2, \dots$

- If the $X_i$ are i.i.d., each step is a fresh independent draw — no memory at all.
- If we allow *arbitrary* dependence between all the $X_i$, the math becomes intractable almost immediately.
- A **Markov chain** is the compromise: one step beyond i.i.d. The next state depends on the past, but *only through the current state*.

**Why this matters:** it's the simplest way to add "memory" to a process without losing the ability to compute anything. Every formula below depends on this restriction.

We restrict to **discrete time** ($n = 0, 1, 2, \dots$) and a **discrete, finite state space** $\{1, 2, \dots, M\}$.

---

## 2. The Markov Property

For any states $i, j$ and any history $i_0, i_1, \dots, i_{n-1}$:

$$
P(X_{n+1} = j \mid X_n = i,\ X_{n-1} = i_{n-1},\ \dots,\ X_0 = i_0) \;=\; P(X_{n+1} = j \mid X_n = i)
$$

**Intuition:** *past and future are conditionally independent given the present.* If you know where you are right now, knowing how you got there gives you zero extra information about where you're going next.

**Why this is so useful:** without it, predicting the future requires conditioning on an entire growing history — a probability table that grows combinatorially with $n$. The Markov property collapses that to a single lookup: "what state am I in right now?"

**A subtlety:** this is *conditional* independence — it does **not** mean the past and future are unconditionally independent. Drop the conditioning on $X_n$ and the past matters again.

**Why it's less restrictive than it looks:** "higher-order" chains (next state depends on the last $k$ states) can be built by redefining the state as a bundle of the last $k$ values, reducing back to the first-order case above.

---

## 3. Homogeneity

A chain is **time-homogeneous** if the transition probability

$$
p_{ij} \;=\; P(X_{n+1} = j \mid X_n = i)
$$

does **not depend on $n$**. The value is determined by which state you're in, not by what time step you're at.

**Key subtlety:** homogeneity does *not* mean every transition shares the same probability $c$. Different pairs $(i,j)$ can have different probabilities — e.g. $p_{12} = 0.3$, $p_{13} = 0.7$, $p_{21} = 0.5$. Homogeneity just means whatever $p_{ij}$ is, it's **constant in $n$**:

$$
P(X_{n+1} = j \mid X_n = i) = p_{ij} \quad \text{for all } n
$$

**Non-homogeneous contrast example:** if $P(X_2 = \text{rain} \mid X_1 = \text{rain}) = 0.6$ but $P(X_3 = \text{rain} \mid X_2 = \text{rain}) = 0.8$, the transition probability itself depends on $n$, breaking homogeneity.

**Why we restrict to homogeneous chains:** it allows one fixed matrix $Q$ to describe the entire chain, instead of a different matrix $Q_n$ for every $n$.

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

**Why rows sum to 1 but columns don't have to:** row $i$ answers "if I'm at state $i$, where could I end up, and with what probability?" — since you must go *somewhere*, this is a full PMF over $j$, so it sums to 1. Column $j$ answers a different question — "who might arrive at $j$, and from where?" — which has no such constraint; some states are easy to reach from many places, others nearly unreachable.

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

**Why this is exactly matrix multiplication:** a sum of products of matched indices, $\sum_k q_{ik} q_{kj}$, is precisely the definition of the $(i,j)$ entry of $Q \times Q = Q^2$. The algebra of matrix multiplication performs the "sum over all intermediate paths" automatically.

**General result (Chapman–Kolmogorov equation):**

$$
P(X_{n+m} = j \mid X_n = i) \;=\; \left(Q^m\right)_{ij}
$$

**How to use it:** to find the probability of being at $j$ exactly $m$ steps after starting at $i$, compute $Q^m$ and read off entry $(i,j)$ — no need to re-derive the conditioning argument each time.

---

## 6. Evolving a Distribution Over Time

Let $\pi_n$ be the row vector of the distribution of $X_n$:

$$
\pi_n = \big(\, P(X_n = 1),\ P(X_n = 2),\ \dots,\ P(X_n = M)\,\big), \qquad \pi_n \mathbf{1}^\top = 1,\ \ \pi_n \geq 0
$$

Same law-of-total-probability argument as Section 5 gives:

$$
\pi_{n+1}(j) = \sum_{i=1}^{M} \pi_n(i)\, q_{ij}
$$

which is exactly the vector–matrix product:

$$
\pi_{n+1} = \pi_n Q
$$

**Why this is the same idea as Section 5:** Section 5 fixed the starting state (a degenerate distribution with probability 1 on state $i$); this generalizes to *any* starting distribution $\pi_n$. The underlying computation — a sum of products of matched indices — is identical.

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

- **As a literal model** of a real system (weather, stock prices, text generation) — whether the Markov assumption is reasonable is an empirical question.
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

---

## 10. Open Threads for Next Lecture

- Existence/uniqueness/convergence proofs for stationary distributions
- Efficient computation tricks (some chains don't need matrix algebra at all)
- Worked examples
