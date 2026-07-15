# The Rayleigh Quotient

*Written in the "symbol → English → example → why" style: every formula is paired with a plain-language meaning, a concrete check, and the specific property that makes it true.*

---

## 1. Definition

For a symmetric matrix $A \in \mathbb{R}^{n\times n}$ (meaning $A = A^T$) and any nonzero vector $x \in \mathbb{R}^n$:

$$Q_A(x) = \frac{x^TAx}{x^Tx}$$

**In English:** it's a single number that measures how much $A$ stretches $x$, relative to the size of $x$ itself.

**Why symmetric matters:** symmetric matrices guarantee an orthonormal eigenbasis (Section 2) — a property ordinary matrices don't have. That guarantee is what makes the whole theory clean, and everything below leans on it.

### 1.1 Scale invariance

Replacing $x \to cx$ for any scalar $c \neq 0$ leaves $Q_A(x)$ unchanged:

$$Q_A(cx) = \frac{(cx)^TA(cx)}{(cx)^T(cx)} = \frac{c^2\, x^TAx}{c^2\, x^Tx} = Q_A(x)$$

**Why this matters:** $Q_A$ only sees the *direction* of $x$, never its length. So $x$ can always be normalized to a unit vector ($x^Tx = 1$) without losing information, simplifying the formula to $Q_A(x) = x^TAx$.

---

## 2. Orthogonal Diagonalization (Spectral Theorem)

> **Spectral Theorem.** Every symmetric matrix $A$ has $n$ orthonormal eigenvectors $v_1, v_2, \dots, v_n$ — mutually perpendicular, each of unit length — with real eigenvalues $\lambda_1, \dots, \lambda_n$.

**Convention used throughout:** eigenvalues sorted **decreasing**:
$$\lambda_1 \ge \lambda_2 \ge \lambda_3 \ge \cdots \ge \lambda_n$$
so **$\lambda_1 = \lambda_{\max}$** and **$\lambda_n = \lambda_{\min}$**.

**Orthonormal, concretely.** A set is orthonormal if:
- **Orthogonal:** $v_i \cdot v_j = 0$ for $i \neq j$
- **Normal:** $\|v_i\| = 1$ for every $i$

**Why orthonormality matters:** because $\{v_i\}$ is a basis, *any* $x\in\mathbb{R}^n$ decomposes as a linear combination of eigenvectors:
$$x = \alpha_1v_1 + \alpha_2v_2 + \cdots + \alpha_nv_n, \qquad \alpha_i = v_i^Tx$$

### 2.1 Matrix form of the decomposition

- Let $V = \begin{pmatrix}v_1 & v_2 & \cdots & v_n\end{pmatrix}$ (eigenvectors as **columns**).
- Let $\alpha = (\alpha_1, \dots, \alpha_n)^T$.
- Then $x = V\alpha$.

**Denominator:**
$$x^Tx = (V\alpha)^T(V\alpha) = \alpha^TV^TV\alpha = \alpha^TI\alpha = \sum_{i=1}^n\alpha_i^2$$
**Why $V^TV=I$:** the columns of $V$ are orthonormal — that's precisely what orthonormality gives in matrix form.

**Numerator:**
$$x^TAx = \alpha^TV^TAV\alpha = \alpha^TD\alpha = \sum_{i=1}^n\lambda_i\alpha_i^2$$
where $D = \mathrm{diag}(\lambda_1,\dots,\lambda_n)$, using the diagonalization identity $V^TAV=D$.

So the two governing formulas are:
$$x^TAx = \sum_i\lambda_i\alpha_i^2, \qquad x^Tx = \sum_i\alpha_i^2$$

**Why this matters:** every fact below is just algebra on these two sums.

---

## 3. Theorem: Max/Min Characterization

Let $A$ be symmetric $n\times n$ with $\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_n$.

**Part A.**
$$\lambda_1 = \max_{x\neq0}\frac{x^TAx}{x^Tx} = \max_{\|x\|=1}x^TAx$$

**Part B.**
$$\lambda_n = \min_{x\neq0}\frac{x^TAx}{x^Tx} = \min_{\|x\|=1}x^TAx$$

**Part C (structural result).** If $x^TAx = \lambda_1\,x^Tx$ — i.e. $x$ *achieves* the maximum — then
$$Ax = \lambda_1x$$
meaning $x$ is not just *some* vector achieving the right value, it is forced to be an **eigenvector** corresponding to $\lambda_1$.

---

## 4. Proof of Parts A & B — The Quotient is Trapped

### 4.1 Upper bound (Part A)

Starting from $x^TAx = \sum_i\lambda_i\alpha_i^2$: since $\lambda_1$ is the **largest** eigenvalue, replacing every $\lambda_i$ in the sum with $\lambda_1$ can only make the sum bigger (or equal):
$$x^TAx = \sum_i\lambda_i\alpha_i^2 \;\le\; \sum_i\lambda_1\alpha_i^2 = \lambda_1\sum_i\alpha_i^2 = \lambda_1\cdot x^Tx$$

**Why the inequality direction holds:** it needs *two* facts simultaneously — $\lambda_i \le \lambda_1$ for all $i$ (the ordering), **and** $\alpha_i^2 \ge 0$ (so multiplying by a bigger number can't decrease anything). Drop either fact and the inequality could flip.

So $Q_A(x) \le \lambda_1$ for every nonzero $x$ — $\lambda_1$ is an upper bound on the ratio.

**Is the bound actually attained?** Check by direct substitution: let $x = v_1$.
$$v_1^TAv_1 = v_1^T(\lambda_1v_1) = \lambda_1(v_1^Tv_1) = \lambda_1\cdot1 = \lambda_1$$
Yes — equality happens at $x=v_1$. Combined with the upper bound, this proves Part A:
$$\lambda_1 = \max_{x\neq0}\frac{x^TAx}{x^Tx}$$

### 4.2 Lower bound (Part B)

Mirror argument. Since $\lambda_n$ is the **smallest** eigenvalue, $\lambda_i \ge \lambda_n$ for all $i$, so:
$$x^TAx = \sum_i\lambda_i\alpha_i^2 \;\ge\; \sum_i\lambda_n\alpha_i^2 = \lambda_n\cdot x^Tx$$
giving $Q_A(x) \ge \lambda_n$ for all $x$. Substituting $x=v_n$ gives equality, exactly as before. This proves Part B:
$$\lambda_n = \min_{x\neq0}\frac{x^TAx}{x^Tx}$$

### 4.3 The one-sentence intuition

> *A weighted average can't beat its own biggest ingredient or fall under its own smallest.* $Q_A(x) = \dfrac{\sum_i\lambda_i\alpha_i^2}{\sum_i\alpha_i^2}$ is exactly such an average — of eigenvalues, weighted by how aligned $x$ is with each eigenvector — so it's automatically trapped between $\lambda_{\min}$ and $\lambda_{\max}$.

**Analogy:** think of $\lambda_i$ as exam scores and $\alpha_i^2$ as the credit-weight of each exam. A GPA can never top the best score or dip below the worst, no matter how the weights are distributed.

---

## 5. Proof of Part C: The Maximizer Must *Be* an Eigenvector

This is a **stronger** claim than Section 4 — not just that the *value* $\lambda_1$ is attainable, but that *any* vector attaining it is forced to be an eigenvector.

### 5.1 Handling repeated eigenvalues (multiplicity)

Suppose $\lambda_1$ has **algebraic multiplicity $k$** — the largest value repeats $k$ times:
$$\lambda_1 = \lambda_2 = \cdots = \lambda_k, \qquad \lambda_{k+1} < \lambda_1 \text{ strictly}$$
(so from position $k+1$ onward, every eigenvalue is *strictly* smaller than $\lambda_1$).

**Why handle this case explicitly:** distinct eigenvalues are a special case, not the general one. Real symmetric matrices routinely have repeated eigenvalues, so a complete proof has to survive that.

### 5.2 The proof, step by step

**Start from the hypothesis**, expanded using the identity from Section 2.1:
$$x^TAx = \sum_{i=1}^n\lambda_i\alpha_i^2, \qquad \lambda_1\,x^Tx = \lambda_1\sum_{i=1}^n\alpha_i^2$$
Setting them equal (the equality hypothesis) and moving everything to one side:
$$\sum_{i=1}^n\lambda_i\alpha_i^2 = \lambda_1\sum_{i=1}^n\alpha_i^2 \quad\Longrightarrow\quad \sum_{i=k+1}^n(\lambda_1-\lambda_i)\,\alpha_i^2 = 0$$
(The terms $i=1,\dots,k$ cancel automatically since $\lambda_i=\lambda_1$ there — only the "strictly smaller" tail survives.)

**Why every remaining term must individually vanish:** for every $i>k$, $(\lambda_1-\lambda_i)>0$ strictly, and $\alpha_i^2\ge0$ always. A sum where *every term is a strictly-positive number times a non-negative number* can only equal zero if **each term is zero on its own** — a positive coefficient can't be cancelled by anything else in the sum. Since $\lambda_1-\lambda_i\neq0$, this forces:
$$\alpha_{k+1}=\alpha_{k+2}=\cdots=\alpha_n=0$$

**Consequence:** $x$ has **zero component** along any eigenvector outside the $\lambda_1$-eigenspace:
$$x = \alpha_1v_1+\alpha_2v_2+\cdots+\alpha_kv_k$$
(no need to write further terms — they're all zero).

**Finishing the proof — apply $A$:**
$$Ax = \alpha_1(Av_1)+\cdots+\alpha_k(Av_k) = \alpha_1\lambda_1v_1+\cdots+\alpha_k\lambda_1v_k = \lambda_1(\alpha_1v_1+\cdots+\alpha_kv_k) = \lambda_1x$$
**Why this last step works:** every $v_i$ for $i\le k$ shares the *same* eigenvalue $\lambda_1$ (that's what multiplicity $k$ means), so $\lambda_1$ factors out of the whole sum uniformly — and what's left inside the parentheses is just $x$ itself, by the decomposition above.

$$\boxed{Ax = \lambda_1x} \qquad\blacksquare$$

This proves $x$ is indeed an eigenvector corresponding to the largest eigenvalue.

### 5.3 Why this matters

Equality in a weighted average is only possible when **all the weight sits on the top value(s)** — any leakage into a smaller-eigenvalue direction would strictly pull the average down, breaking the equality. So a maximizer of $Q_A$ isn't just "some vector that happens to score $\lambda_1$" — it's *structurally confined* to the eigenspace of $\lambda_1$, with zero freedom to point anywhere else.

---

## 6. Applications

| Use | How the Rayleigh quotient helps |
|---|---|
| **Eigenvalue estimation** | Plug an approximate eigenvector into $Q_A(x)$ → very accurate eigenvalue estimate (the quotient is stationary near eigenvectors, so small vector errors barely affect it). |
| **Rayleigh quotient iteration** | Refines a guessed eigenvector using $Q_A$ as feedback; converges cubically fast. |
| **Power iteration / optimization** | Maximizing/minimizing $Q_A(x)$ directly finds $\lambda_{\max}/\lambda_{\min}$ — turns an algebra problem into an optimization problem. |
| **Mechanical vibration** | $Q_A(x)$ = ratio of potential to kinetic energy for a mode shape; minimizing it gives the fundamental frequency. |
| **Quantum mechanics** | With $A$ = Hamiltonian, $Q_A(x)$ estimates energy of a trial wavefunction; minimizing approximates ground-state energy (variational method). |
| **Spectral graph theory** | Rayleigh quotient of a graph Laplacian's second-smallest eigenvalue (Fiedler value) measures how easily a graph splits — used in spectral clustering, image segmentation. |
| **PCA** | Maximizing the Rayleigh quotient of the covariance matrix finds the direction of maximum variance — the first principal component. |

**The common thread:** whenever an extreme value (energy, variance, frequency, connectivity) is shaped by a quadratic form under a matrix, the Rayleigh quotient turns "find the extreme value" into an eigenvalue problem — and the extremizing vector comes for free as the eigenvector.

---

## 7. Self-Check Questions

1. Why does scale-invariance let us restrict to unit vectors?
2. Why does symmetry of $A$ guarantee an orthonormal eigenbasis exists (name the theorem)?
3. In the matrix bookkeeping ($x=V\alpha$), why does $V^TV=I$, and what property of the eigenvectors makes that true?
4. In $Q_A(x) = \sum\lambda_i\alpha_i^2 / \sum\alpha_i^2$, why are there no cross terms $\alpha_i\alpha_j$ ($i\ne j$)?
5. Why can't a weighted average exceed its largest ingredient — and why does this immediately give Part A of the theorem?
6. In the Part C proof, why does $(\lambda_1-\lambda_i)\alpha_i^2 \ge 0$ for every term with $i>k$, and why does that force each such term to be exactly zero when their sum is zero?
7. Why does the multiplicity $k$ specifically matter for the final step $Ax=\lambda_1x$ — what would break if the $v_i$ for $i\le k$ had *different* eigenvalues?
