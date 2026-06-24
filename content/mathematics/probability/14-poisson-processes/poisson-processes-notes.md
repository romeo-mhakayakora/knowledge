# Markov Property and Transition Matrix

*Source: Introduction to Probability, Blitzstein & Hwang*

---

## Table of Contents

- [What Is a Markov Chain?](#what-is-a-markov-chain)
- [Why Markov Chains Matter](#why-markov-chains-matter)
- [State Space](#state-space)
- [Time-Homogeneous Markov Chains](#time-homogeneous-markov-chains)
- [The Markov Property](#the-markov-property)
- [The Transition Matrix Q](#the-transition-matrix-q)
- [How to Read Q in Plain English](#how-to-read-q-in-plain-english)
- [The n-Step Transition Matrix Qⁿ](#the-n-step-transition-matrix-qn)
  - [Theorem: Entries of Qⁿ Are n-Step Transition Probabilities](#theorem-entries-of-qn-are-n-step-transition-probabilities)
- [The Chapman-Kolmogorov Equation](#the-chapman-kolmogorov-equation)
- [Connection to Matrix Multiplication](#connection-to-matrix-multiplication)
- [Alternative Derivations of Chapman-Kolmogorov](#alternative-derivations-of-chapman-kolmogorov)
- [Worked Example — Computing Q² and 2-Step Probabilities](#worked-example--computing-q-and-2-step-probabilities)
- [Common Mistakes](#common-mistakes)
- [Looking Ahead](#looking-ahead)

---

## What Is a Markov Chain?

A **Markov chain** is a sequence of random variables

$$X_0, X_1, X_2, X_3, \ldots$$

whose future evolution depends only on the present state.

Successive random variables are often dependent, but dependence itself is **not** the defining property. The defining property is the **Markov property**, which we state formally below.

&gt; **Core Rule:** The future is conditionally independent of the past, given the present.

Think of a Markov chain as a system with **absolute amnesia**. No matter how you arrived at your current state, only your current state matters for predicting the next step. The path used to arrive at the current state becomes irrelevant once the current state is known.

**Physical meaning:** If you are in State 4 of the Coupon Collector game (you have 4 unique toys), your odds of getting a new toy are exactly $\frac{6}{10}$ — regardless of whether you bought 4 meals to get there, or 500 meals and were horribly unlucky. The history is completely irrelevant.

&gt; **Critical warning:** If a system requires you to look at its **history** to predict its next move, it is **not** a Markov chain. For example, if the probability of rain tomorrow depended on whether it rained today *and* yesterday, the weather process would not be a Markov chain in its current state space. You would need to expand the state space to include pairs of days to recover the Markov property.

---

## Why Markov Chains Matter

Many systems evolve through time:

- Weather systems
- Search engines
- Communication networks
- Population models
- Queueing systems
- Reinforcement learning environments

A major challenge in modeling these systems is that the amount of historical information grows forever. After:

- 10 steps, there are 10 previous states
- 100 steps, there are 100 previous states
- 1,000,000 steps, there are 1,000,000 previous states

Tracking the entire history becomes impractical.

The Markov property provides a remarkable simplification:

&gt; The current state contains all information needed to predict the future.

Instead of remembering an infinitely growing history, we only need to remember the present state. This compression of information is what makes Markov chains mathematically tractable.

**Why this matters for computation:** If we needed the full history, predicting step $n+1$ would require storing $n+1$ values. With the Markov property, we store exactly 1 value: $X_n$. This reduces memory from $O(n)$ to $O(1)$ and makes matrix-power methods possible.

---

## State Space

The set of all possible states of a Markov chain is called the **state space**. We usually denote it by $S$.

### Examples

**Example 1:** $S = \{1, 2, 3\}$ — a chain with three numerical states.

**Example 2:** $S = \{\text{Sunny}, \text{Cloudy}, \text{Rainy}\}$ — a weather model.

**Example 3:** $S = \{0, 1, 2, \ldots, 10\}$ — the Coupon Collector problem where state $i$ means we currently possess $i$ unique toys.

Every random variable $X_n$ takes values from the state space. Without a state space, the chain has nowhere to live.

### Why This Definition Exists

The state space forces us to be explicit about what the chain can and cannot be. It defines the **support** of every $X_n$. Without it, we cannot write transition probabilities because we would not know what values $i$ and $j$ range over.

### What Would Break Without It?

If we refused to specify $S$, the transition matrix $Q$ would have undefined dimensions. We could not write $q_{ij}$ because we would not know the valid indices $i$ and $j$.

### What Would Change for Infinite State Spaces?

**Countably infinite chains** ($S = \{0, 1, 2, \ldots\}$ or $S = \mathbb{Z}$) still exist and are widely used (queueing theory, random walks). However:

- The transition "matrix" becomes an infinite-dimensional operator
- Matrix multiplication requires convergence of infinite series
- Some finite-state theorems stop being true (e.g., an irreducible infinite chain may have all states transient — the simple random walk on $\mathbb{Z}^3$ is transient, whereas every irreducible finite chain is recurrent)

**Uncountable state spaces** require measure-theoretic machinery (transition kernels instead of matrices, integration instead of summation). The elegant matrix-power theory collapses entirely.

&gt; **The finite state space is what makes $Q$ an actual matrix that we can raise to powers.** This is the computational engine of the entire chapter.

---

## Time-Homogeneous Markov Chains

Throughout these notes we assume the chain is **time-homogeneous**. This means:

$$q_{ij} = P(X_{n+1} = j \mid X_n = i)$$

does **not** depend on time $n$. The transition probabilities remain constant.

For example:
- Today: State A → State B = 0.3
- Tomorrow: State A → State B = 0.3
- Next Week: State A → State B = 0.3

The rule never changes.

### Why This Assumption Exists

Without time-homogeneity, we would need a different transition matrix at every step:

$$Q_0, Q_1, Q_2, \ldots, Q_{n-1}$$

The probability of moving from $i$ to $j$ in $n$ steps would become:

$$P(X_n = j \mid X_0 = i) = \sum_{k_1, k_2, \ldots, k_{n-1}} (Q_0)_{ik_1} (Q_1)_{k_1 k_2} \cdots (Q_{n-1})_{k_{n-1} j}$$

This is a **product of distinct matrices**, not a power of one matrix. The elegant theory of $Q^n$ — eigenvalue decomposition, spectral convergence, simple matrix exponentiation — collapses completely.

### What Breaks Without It?

The formula $Q^n$ is replaced by:

$$Q_0 Q_1 Q_2 \cdots Q_{n-1}$$

This product:
- Cannot be computed by repeated squaring ($Q^{2^k}$)
- Has no simple eigenvalue characterization
- Requires storing $n$ distinct matrices instead of 1
- Makes stationary distributions impossible to define in the same form (the equation $sQ = s$ requires a single $Q$)

**Concrete example:** Suppose $Q_n = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ for even $n$ and $Q_n = I$ for odd $n$. Then the 2-step transition probability from State 1 to State 1 depends on whether you start at an even or odd step. There is no universal $Q^2$ matrix.

---

## The Markov Property

For all states $i_0, i_1, \ldots, i_{n-1}, i, j$, the **Markov property** states:

$$P(X_{n+1} = j \mid X_n = i, X_{n-1} = i_{n-1}, \ldots, X_0 = i_0) = P(X_{n+1} = j \mid X_n = i)$$

### Reading the Formula in English

"The probability of moving to state $j$ at the next step, given the entire history of the process, is exactly the same as the probability of moving to state $j$ given only the current state."

Everything before the present becomes irrelevant once the present is known.

### Why This Definition Exists

Suppose we attempted to predict the future without the Markov property. We would need:

$$P(X_{n+1} \mid X_n, X_{n-1}, X_{n-2}, \ldots, X_0)$$

As time grows, the amount of information we must store grows forever. The Markov property compresses all relevant information into a single state $X_n$. Instead of remembering an infinitely growing history, we remember only the current state.

This compression is the fundamental reason Markov chains are useful. It is also why we can build a transition matrix: $Q$ has one row per **current state**, not one row per **history of states**. If histories mattered, $Q$ would need infinitely many rows (one per possible history), and matrix multiplication would be undefined.

### What Breaks Without It?

Consider a weather model where:

- If it rained yesterday **and** today, tomorrow rains with probability 0.9
- If it **only** rained today, tomorrow rains with probability 0.5

Then knowing today's weather is **not enough**. We need:

$$P(X_{n+1} \mid X_n, X_{n-1})$$

rather than $P(X_{n+1} \mid X_n)$. The present state no longer contains all relevant information.

**What fails mathematically:**
- The transition matrix $Q$ is insufficient; we need a transition tensor or expanded state space
- Matrix powers $Q^n$ do not encode multi-step probabilities because the factorization $P(X_n = k \mid X_0 = i) \cdot P(X_{n+1} = j \mid X_n = k)$ fails — the second probability depends on how we reached $k$
- Chapman-Kolmogorov collapses because the intermediate state is not a sufficient summary

**Recovery method:** Expand the state space to pairs $(X_{n-1}, X_n)$. The new "state" contains yesterday and today. This recovered Markov property comes at the cost of a larger state space ($M^2$ states instead of $M$).

### Dependency Chain

Markov Property → (Justifies one-step dependence only) → Transition Matrix Q (one row per state, not per history) → Matrix Powers Qⁿ (encode multi-step probabilities) → Chapman-Kolmogorov (factorization via intermediate states) → Long-Run Analysis (stationary distributions, convergence)

---

## The Transition Matrix Q

The **transition matrix** $Q = (q_{ij})$ collects all one-step transition probabilities:

$$q_{ij} = P(X_{n+1} = j \mid X_n = i)$$

Rows correspond to the **current state**. Columns correspond to the **next state**.

### Example

$$Q = \begin{pmatrix} 0.5 & 0.4 & 0.1 \\ 0.3 & 0.2 & 0.5 \\ 0.2 & 0.3 & 0.5 \end{pmatrix}$$

Row 1 describes movement from State 1. Row 2 from State 2. Row 3 from State 3.

### Why Rows Sum to 1

Fix a state $i$. After one step the chain must move somewhere. The possible destinations are $1, 2, \ldots, M$. These outcomes are:

1. **Mutually exclusive:** The chain cannot be in two states simultaneously
2. **Collectively exhaustive:** The chain must be in some state

Therefore:

$$\sum_{j=1}^{M} q_{ij} = 1$$

for every row. Each row is a complete probability distribution.

### What Would Break if Rows Did Not Sum to 1?

**Case 1: Row sums to 0.8**

Then 20% of the probability mass has disappeared. The chain "leaks" — there is a 20% chance of entering an unmodeled "void" state. When we compute $Q^n$, this missing mass compounds exponentially: $(0.8)^n \to 0$. The "probabilities" in $Q^n$ no longer sum to 1, violating probability axioms.

**Case 2: Row sums to 1.3**

Then we have assigned 130% probability. This violates the axioms of probability (no event can have probability greater than 1). If we naively compute $Q^n$, entries explode: $(1.3)^n \to \infty$. The matrix no longer represents any stochastic process.

**Case 3: Different rows sum to different values**

Then $Q^n$ becomes a mess where some states lose mass and others gain it arbitrarily. The semigroup property $Q^{m+n} = Q^m Q^n$ still holds algebraically, but the probabilistic interpretation is destroyed. We can no longer read rows as probability distributions.

&gt; **The stochastic condition (non-negative entries, rows sum to 1) is what makes $Q$ a probability operator rather than an arbitrary matrix.**

---

## How to Read Q in Plain English

Using the language of conditional probability, the $i$-th row of $Q$ is the **conditional PMF** of the next state given $X_0 = i$.

**Example:** If we start in State 3, only Row 3 matters: $[0.2, 0.3, 0.5]$.

This means:
- 20% chance of moving to State 1
- 30% chance of moving to State 2
- 50% chance of remaining in State 3

Rows 1 and 2 describe **alternate universes** where the chain started elsewhere. They are irrelevant for this specific prediction.

&gt; **The vertical bar $\mid$ in $P(X_n = j \mid X_0 = i)$ is universally read as "given that" or "conditioned on."** It acts as a mathematical filter.

**Notation warning:** The symbol $Q$ is standard for the transition matrix. Some texts use $P$, but we reserve $P$ for probability and use $Q$ to avoid confusion. Both notations are equivalent: $Q_{ij}$ is the probability of moving from $i$ to $j$ in one step. When you see $P_{ij}$ in another text, it means exactly the same thing as $Q_{ij}$ here.

**Row-vector convention:** We write distributions as row vectors and multiply on the right: $\mathbf{p}^{(n+1)} = \mathbf{p}^{(n)} Q$. If we used column vectors, we would write $\mathbf{p}_{\text{col}}^{(n+1)} = Q^T \mathbf{p}_{\text{col}}^{(n)}$. Both conventions exist; do not mix them in the same calculation.

---

## The n-Step Transition Matrix Qⁿ

The matrix $Q^n$ contains transition probabilities over $n$ steps. Its entries are:

$$q_{ij}^{(n)} = P(X_n = j \mid X_0 = i)$$

The $i$-th row gives the complete conditional probability distribution after $n$ steps, assuming the chain started in state $i$.

Think of:
- $Q$ as the one-step future
- $Q^2$ as the two-step future
- $Q^n$ as the $n$-step future

But this interpretation requires proof. We cannot simply assume that matrix powers encode multi-step probabilities.

---

### Theorem: Entries of Qⁿ Are n-Step Transition Probabilities

**Statement:** For every $n \geq 1$ and all states $i, j$:

$$(Q^n)_{ij} = P(X_n = j \mid X_0 = i)$$

**Why it matters:** This theorem is the bridge between linear algebra (matrix powers) and probability theory (multi-step transition probabilities). Without it, $Q^n$ is just a matrix computation with no probabilistic meaning.

---

#### Full Induction Proof

We proceed by induction on $n$.

**Base case ($n = 1$):** By definition, $(Q^1)_{ij} = Q_{ij} = P(X_1 = j \mid X_0 = i)$. This holds by the definition of the transition matrix.

**Inductive step:** Assume that $(Q^n)_{ij} = P(X_n = j \mid X_0 = i)$ for all $i, j$. We want to show that $(Q^{n+1})_{ij} = P(X_{n+1} = j \mid X_0 = i)$.

By the definition of matrix multiplication:

$$(Q^{n+1})_{ij} = (Q^n \cdot Q)_{ij} = \sum_{k=1}^{M} (Q^n)_{ik} Q_{kj}$$

Now interpret this sum probabilistically. To go from $i$ to $j$ in $n+1$ steps, the chain must be in some intermediate state $k$ after $n$ steps, and then move from $k$ to $j$ in one final step.

By the **Law of Total Probability**, conditioning on the intermediate state $X_n$:

$$P(X_{n+1} = j \mid X_0 = i) = \sum_{k=1}^{M} P(X_{n+1} = j, X_n = k \mid X_0 = i)$$

By the **multiplication rule** for conditional probability:

$$P(X_{n+1} = j, X_n = k \mid X_0 = i) = P(X_{n+1} = j \mid X_n = k, X_0 = i) \cdot P(X_n = k \mid X_0 = i)$$

By the **Markov property**, the future depends only on the present:

$$P(X_{n+1} = j \mid X_n = k, X_0 = i) = P(X_{n+1} = j \mid X_n = k) = q_{kj}$$

By the **time-homogeneity** assumption, this one-step probability is exactly $Q_{kj}$ regardless of when we are.

By the **inductive hypothesis**:

$$P(X_n = k \mid X_0 = i) = (Q^n)_{ik}$$

Substituting all of these:

$$P(X_{n+1} = j \mid X_0 = i) = \sum_{k=1}^{M} (Q^n)_{ik} Q_{kj} = (Q^{n+1})_{ij}$$

This completes the induction. ∎

---

#### What Breaks Without the Markov Property?

If the chain's future depended on its entire history, then:

$$P(X_{n+1} = j \mid X_n = k, X_0 = i) \neq P(X_{n+1} = j \mid X_n = k)$$

The factorization in the proof fails. The sum $\sum_k (Q^n)_{ik} Q_{kj}$ would no longer equal the true $(n+1)$-step probability because $Q_{kj}$ is the wrong conditional probability — it ignores the path from $i$ to $k$.

Matrix powers would not encode multi-step probabilities. The entire computational shortcut of raising $Q$ to a power would collapse.

#### What Breaks Without Time-Homogeneity?

The step where we wrote:

$$P(X_{n+1} = j \mid X_n = k) = q_{kj}$$

would become:

$$P(X_{n+1} = j \mid X_n = k) = (Q_n)_{kj}$$

which depends on $n$. The inductive hypothesis would need to track which step we are on, and the clean formula $(Q^n)_{ij}$ would be replaced by a product of distinct matrices. Matrix powers lose all meaning.

---

## The Chapman-Kolmogorov Equation

### Statement

For any nonnegative integers $m$ and $n$:

$$q_{ij}^{(m+n)} = \sum_{k=1}^{M} q_{ik}^{(m)} q_{kj}^{(n)}$$

This gives the probability of traveling from state $i$ to state $j$ in exactly $m+n$ steps.

### Why It Is True

To reach state $j$ after $m+n$ steps:
1. Reach some intermediate state $k$ after $m$ steps
2. Then move from $k$ to $j$ during the next $n$ steps

Every possible intermediate state contributes to the total probability. Adding all possibilities gives the final answer.

### Full Proof

**Step 1: Partition the sample space.**

At time $m$, the chain must occupy exactly one state. The events $\{X_m = 1\}, \{X_m = 2\}, \ldots, \{X_m = M\}$ are mutually exclusive and collectively exhaustive. They form a partition of the sample space.

By the **Law of Total Probability**, conditioning on this partition:

$$P(X_{m+n} = j \mid X_0 = i) = \sum_{k=1}^{M} P(X_{m+n} = j, X_m = k \mid X_0 = i)$$

**Step 2: Apply the multiplication rule.**

Recall: $P(A \cap B) = P(A \mid B) P(B)$. Let $A = \{X_{m+n} = j\}$ and $B = \{X_m = k\}$. Then:

$$P(X_{m+n} = j, X_m = k \mid X_0 = i) = P(X_{m+n} = j \mid X_m = k, X_0 = i) \cdot P(X_m = k \mid X_0 = i)$$

**Step 3: Apply the Markov property.**

By the Markov property, the future depends only on the present:

$$P(X_{m+n} = j \mid X_m = k, X_0 = i) = P(X_{m+n} = j \mid X_m = k)$$

**Step 4: Apply time-homogeneity.**

Because the chain is time-homogeneous, the probability of moving from $k$ to $j$ in $n$ steps does not depend on when we start:

$$P(X_{m+n} = j \mid X_m = k) = q_{kj}^{(n)}$$

Also, by definition:

$$P(X_m = k \mid X_0 = i) = q_{ik}^{(m)}$$

**Step 5: Substitute and conclude.**

$$q_{ij}^{(m+n)} = P(X_{m+n} = j \mid X_0 = i) = \sum_{k=1}^{M} q_{ik}^{(m)} q_{kj}^{(n)}$$

∎

---

### Why Time-Homogeneity Appears in the Proof

Look carefully at Step 4. We wrote:

$$P(X_{m+n} = j \mid X_m = k) = q_{kj}^{(n)}$$

This is only valid because the transition probabilities do not depend on time. Without time-homogeneity, we would need:

$$P(X_{m+n} = j \mid X_m = k) = (Q_m^{(n)})_{kj}$$

a notation so cumbersome that most texts abandon matrix powers entirely for time-inhomogeneous chains. The clean formula $q_{kj}^{(n)}$ requires that $n$-step probabilities be the same regardless of starting time.

---

## Connection to Matrix Multiplication

The formula

$$q_{ij}^{(2)} = \sum_{k=1}^{M} q_{ik} q_{kj}$$

is exactly the formula for the $(i,j)$-entry of the matrix product:

$$Q^2 = Q \times Q$$

Thus:
- **Probability theory** says: sum over all intermediate states
- **Linear algebra** says: multiply matrices

These are two descriptions of the same phenomenon.

More generally, the Chapman-Kolmogorov equation is the probabilistic reason that matrix powers work for Markov chains:

$$Q^{m+n} = Q^m \cdot Q^n$$

The semigroup property of matrix multiplication reflects the semigroup property of time evolution.

---

## Alternative Derivations of Chapman-Kolmogorov

### Probability-First Derivation

**When useful:** Building intuition, verifying model assumptions, teaching the underlying random process.

Begin with the sample space partition, apply LOTP, use the multiplication rule, invoke Markov property and time-homogeneity. This is the proof we gave above.

**Advantage:** Shows exactly where each assumption enters. If someone questions whether your model is Markov, this proof pinpoints which equality fails.

**Disadvantage:** Verbose. For computing $Q^{100}$, you do not want to think about partitions and conditional probabilities.

### Linear-Algebra-First Derivation

**When useful:** Computational efficiency, generalizing to infinite state spaces via operator theory, spectral analysis.

Begin with the definition of matrix multiplication:

$$(Q^{m+n})_{ij} = (Q^m \cdot Q^n)_{ij} = \sum_{k=1}^{M} (Q^m)_{ik} (Q^n)_{kj}$$

By the theorem we proved above, $(Q^m)_{ik} = q_{ik}^{(m)}$ and $(Q^n)_{kj} = q_{kj}^{(n)}$. Substituting:

$$q_{ij}^{(m+n)} = \sum_{k=1}^{M} q_{ik}^{(m)} q_{kj}^{(n)}$$

**Advantage:** Immediate. Matrix multiplication is associative, so $Q^{m+n} = Q^m Q^n$ is automatic. This is why we can compute $Q^{100}$ by repeated squaring instead of 99 matrix multiplications.

**Disadvantage:** Hides the probabilistic assumptions. Someone might apply $Q^{100}$ without checking that their process is actually Markov and time-homogeneous.

&gt; **Use probability-first when building or validating a model. Use linear-algebra-first when computing or analyzing convergence.**

---

## Worked Example — Computing Q² and 2-Step Probabilities

Consider:

$$Q = \begin{pmatrix} 0.5 & 0.4 & 0.1 \\ 0.3 & 0.2 & 0.5 \\ 0.2 & 0.3 & 0.5 \end{pmatrix}$$

### Computing Q² Explicitly (Entry by Entry)

**Entry (1,1):** Row 1 of $Q$ dot Column 1 of $Q$

$$(Q^2)_{11} = (0.5)(0.5) + (0.4)(0.3) + (0.1)(0.2) = 0.25 + 0.12 + 0.02 = 0.39$$

**Entry (1,2):** Row 1 of $Q$ dot Column 2 of $Q$

$$(Q^2)_{12} = (0.5)(0.4) + (0.4)(0.2) + (0.1)(0.3) = 0.20 + 0.08 + 0.03 = 0.31$$

**Entry (1,3):** Row 1 of $Q$ dot Column 3 of $Q$

$$(Q^2)_{13} = (0.5)(0.1) + (0.4)(0.5) + (0.1)(0.5) = 0.05 + 0.20 + 0.05 = 0.30$$

**Entry (2,1):** Row 2 of $Q$ dot Column 1 of $Q$

$$(Q^2)_{21} = (0.3)(0.5) + (0.2)(0.3) + (0.5)(0.2) = 0.15 + 0.06 + 0.10 = 0.31$$

**Entry (2,2):** Row 2 of $Q$ dot Column 2 of $Q$

$$(Q^2)_{22} = (0.3)(0.4) + (0.2)(0.2) + (0.5)(0.3) = 0.12 + 0.04 + 0.15 = 0.31$$

**Entry (2,3):** Row 2 of $Q$ dot Column 3 of $Q$

$$(Q^2)_{23} = (0.3)(0.1) + (0.2)(0.5) + (0.5)(0.5) = 0.03 + 0.10 + 0.25 = 0.38$$

**Entry (3,1):** Row 3 of $Q$ dot Column 1 of $Q$

$$(Q^2)_{31} = (0.2)(0.5) + (0.3)(0.3) + (0.5)(0.2) = 0.10 + 0.09 + 0.10 = 0.29$$

**Entry (3,2):** Row 3 of $Q$ dot Column 2 of $Q$

$$(Q^2)_{32} = (0.2)(0.4) + (0.3)(0.2) + (0.5)(0.3) = 0.08 + 0.06 + 0.15 = 0.29$$

**Entry (3,3):** Row 3 of $Q$ dot Column 3 of $Q$

$$(Q^2)_{33} = (0.2)(0.1) + (0.3)(0.5) + (0.5)(0.5) = 0.02 + 0.15 + 0.25 = 0.42$$

**Final matrix:**

$$Q^2 = \begin{pmatrix} 0.39 & 0.31 & 0.30 \\ 0.31 & 0.31 & 0.38 \\ 0.29 & 0.29 & 0.42 \end{pmatrix}$$

**Verification:** Each row sums to 1.0 (stochastic property preserved).

---

### Scenario A: Starting from State 1, Reach State 3 in 2 Steps

We want $P(X_2 = 3 \mid X_0 = 1) = (Q^2)_{13} = 0.30$.

By Chapman-Kolmogorov, enumerating all paths:

$$q_{13}^{(2)} = q_{11}q_{13} + q_{12}q_{23} + q_{13}q_{33}$$

$$= (0.5)(0.1) + (0.4)(0.5) + (0.1)(0.5)$$

$$= 0.05 + 0.20 + 0.05 = 0.30$$

Path breakdown:
- Via State 1: $1 \to 1 \to 3$, probability $0.05$
- Via State 2: $1 \to 2 \to 3$, probability $0.20$ (most likely)
- Via State 3: $1 \to 3 \to 3$, probability $0.05$

&gt; The most likely path is bouncing through State 2 first, because $q_{12} = 0.4$ and $q_{23} = 0.5$ are relatively strong connections.

---

### Scenario B: Starting from State 2, Reach State 3 in 2 Steps

We want $P(X_2 = 3 \mid X_0 = 2) = (Q^2)_{23} = 0.38$.

By Chapman-Kolmogorov:

$$q_{23}^{(2)} = q_{21}q_{13} + q_{22}q_{23} + q_{23}q_{33}$$

$$= (0.3)(0.1) + (0.2)(0.5) + (0.5)(0.5)$$

$$= 0.03 + 0.10 + 0.25 = 0.38$$

Path breakdown:
- Via State 1: $2 \to 1 \to 3$, probability $0.03$
- Via State 2: $2 \to 2 \to 3$, probability $0.10$
- Via State 3: $2 \to 3 \to 3$, probability $0.25$ (most likely)

&gt; Starting in State 2 gives a higher probability (38%) of reaching State 3 in two steps than starting in State 1 (30%). This is because State 2 has a strong direct connection to State 3 ($q_{23} = 0.5$) and a high self-loop probability ($q_{33} = 0.5$).

---

## Common Mistakes

### Mistake 1: Markov ≠ Independent

**False belief:** "Markov means the future is independent of everything."

**Truth:** Most Markov chains are highly dependent. The future usually depends strongly on the present. The Markov property only removes dependence on states *further* in the past. It does not remove dependence on the present.

**Counterexample:** In $Q = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, $X_{n+1}$ is completely determined by $X_n$ (perfect dependence), yet the chain is Markov.

---

### Mistake 2: Rows ≠ Columns

**False belief:** Switching rows and columns gives an equivalent interpretation.

**Truth:** Rows represent the **current** state. Columns represent the **next** state. Switching them changes the meaning completely.

If you transpose $Q$, you are computing $P(X_n = i \mid X_{n+1} = j)$ — a *backward* probability, not a forward transition. For non-symmetric $Q$, these are different.

**Concrete error:** Using Column 1 instead of Row 1 gives $[0.5, 0.3, 0.2]^T$, which is the distribution of *previous* states given that you are now in State 1 — exactly the wrong direction.

---

### Mistake 3: Qⁿ ≠ nQ

**False belief:** $Q^n$ means multiplying each entry by $n$.

**Truth:** $Q^n$ means repeated matrix multiplication: $Q \cdot Q \cdot \ldots \cdot Q$ ($n$ times).

**Counterexample:** For $Q = \begin{pmatrix} 0.5 & 0.5 \\ 0.5 & 0.5 \end{pmatrix}$, we have $Q^2 = Q$ (idempotent). But $2Q = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, which is not even stochastic.

---

### Mistake 4: Future Independent of Past ≠ Future Independent of Present

**False belief:** "The Markov property says the future doesn't depend on anything."

**Truth:** The future often depends heavily on the present. The Markov property only removes dependence on states *before* the present.

**Precise statement:** $P(X_{n+1} \mid X_n, X_{n-1}, \ldots, X_0) = P(X_{n+1} \mid X_n)$. The future is **conditionally independent of the past given the present** — not unconditionally independent of everything.

---

## Looking Ahead

The transition matrix $Q$ tells us how the chain moves in one step. The matrix $Q^n$ tells us how the chain moves in $n$ steps.

However, many practical questions are not conditional questions such as $P(X_n = j \mid X_0 = i)$. Instead we want **unconditional probabilities**:

$$P(X_n = j)$$

To answer those questions we combine an **initial distribution** $\mathbf{t}$ with $Q^n$. This leads naturally to the next topic:

**Marginal Distributions** (Section 11.1.6)

The marginal distribution of $X_n$ is given by $\mathbf{t}Q^n$, where $t_i = P(X_0 = i)$. This is the weighted average over all possible starting states, using the Law of Total Probability.

Later, marginal distributions will lead us to **stationary distributions** and the long-run behavior of Markov chains.
