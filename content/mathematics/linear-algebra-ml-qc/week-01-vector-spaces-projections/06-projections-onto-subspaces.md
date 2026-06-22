# 06 — Projections onto Subspaces

**MIT Lecture:** 15 — Projections onto Subspaces
**Maps to:** IIT Indore Week 1, Topic 5 — Projections and the linear least-squares problem
**Builds on:** Note 05 (orthogonality, left null space, the normal equation $A^TA\hat{x}=A^Tb$) — this lecture *re-derives* that same equation from a completely different starting point: pure geometry instead of "closest point in the left null space"
**Sets up:** Note 07 — the numerical least-squares example (line-fitting), which this lecture sets up but doesn't finish

---

## Big picture first

Note 05 already derived $A^TA\hat{x}=A^Tb$ by reasoning about the left null space. This lecture arrives at the *exact same equation* a second way — by literally asking "what's the closest point in a subspace to a given vector?" and turning that geometry into algebra. Seeing the same destination reached from two different starting points is the best confirmation that the formula isn't a trick — it's forced by the geometry no matter which door you walk in through.

The plan: solve the simplest possible version first (projecting onto a *line*), get clean formulas, then generalize to projecting onto any subspace.

---

## 1. Projecting onto a line

**Setup:** a line through the origin, spanned by a single vector $a$. Given some vector $b$ not on that line, find the point $p$ *on the line* closest to $b$.

> **💡 Clarification: What do we mean by "shortest distance"?**
> When dealing with vectors, "distance" can mean a few things. Here is how the geometry breaks down:
> 1. **Point to a Line (Orthogonal Projection):** This is what we are doing here. The shortest distance from vector $b$ to the line spanned by $a$ is the straight perpendicular drop (the error vector $e$).
> 2. **Between Two Lines (Skew Lines in 3D):** The shortest path connecting two non-intersecting lines is a segment parallel to their cross product ($n = d_1 \times d_2$), making it mutually perpendicular to both.
> 3. **Tip to Tip (Euclidean Distance):** This is just $\|b - a\|$, the straight line connecting the vector tips, which is not necessarily perpendicular to anything unless it forms a right triangle.

### Why orthogonality has to be the key fact

Because $p$ is on the line, it's some multiple of $a$: $p = \hat{x}a$ for a scalar $\hat{x}$ we need to find. The error is $e = b - \hat{x}a$. The one geometric fact that pins down "closest point on a line" is that the shortest distance from $b$ to the line is along the *perpendicular* — so $e$ must be orthogonal to $a$:

$$
a^T(b - \hat{x}a) = 0
$$

> **🔍 Deep Dive: The Machine Learning Connection**
> This geometric truth is the fundamental engine driving optimization algorithms. When building Ordinary Least Squares (OLS) regression or designing loss functions for neural networks, minimizing the error means finding the shortest "distance" between the model's predictions and the actual data. The mathematical guarantee that you have hit the absolute lowest point in your loss is achieved precisely when the error vector is perfectly orthogonal to the subspace spanned by your data features. The math is literally just finding that perpendicular drop.

### Solving for $\hat{x}$, $p$, and the projection matrix

Expand and isolate $\hat{x}$:

$$
a^Tb - \hat{x}\,a^Ta = 0 \;\;\Longrightarrow\;\; \hat{x} = \frac{a^Tb}{a^Ta}
$$

So the projection point is:

$$
p = \hat{x}a = \frac{a^Tb}{a^Ta}\,a
$$

### Sanity checks (the *why* behind the formula, not just the formula)

- **Double $b$:** $\hat{x}$ doubles, so $p$ doubles. Makes sense — push the target twice as far out, the shadow it casts on the line moves twice as far too.

> **🔍 Proof for Doubling $b$:**
> $$\hat{x}_{\text{new}} = \frac{a^T(2b)}{a^Ta} = 2\left(\frac{a^Tb}{a^Ta}\right) = 2\hat{x}$$
> $$p_{\text{new}} = (2\hat{x})a = 2(\hat{x}a) = 2p$$

- **Double $a$ (or flip its sign):** $\hat{x}$ gets cut in half ($a^Ta$ in the denominator quadruples while $a^Tb$ only doubles), and $p = \hat{x}a$ ends up exactly the same as before. This makes sense too — doubling $a$ doesn't change the *line*, just how it's labeled, so the projection point shouldn't move at all.

> **🔍 Proof for Doubling $a$:**
> $$\hat{x}_{\text{new}} = \frac{(2a)^Tb}{(2a)^T(2a)} = \frac{2(a^Tb)}{4(a^Ta)} = \frac{1}{2}\hat{x}$$
> $$p_{\text{new}} = \left(\frac{1}{2}\hat{x}\right)(2a) = 1 \cdot (\hat{x}a) = p$$
>
> **🔍 Proof for Flipping the sign of $a$ ($-a$):**
> $$\hat{x}_{\text{new}} = \frac{(-a)^Tb}{(-a)^T(-a)} = \frac{-(a^Tb)}{(-1)^2(a^Ta)} = -\hat{x}$$
> $$p_{\text{new}} = (-\hat{x})(-a) = \hat{x}a = p$$

### The projection matrix

Rewrite $p$ as a matrix acting on $b$:

$$
p = \underbrace{\frac{aa^T}{a^Ta}}_{P}\,b
$$

> **🔍 Deep Dive: Dimensional Analysis (Why $P$ is an $n \times n$ matrix)**
> We start with $p = a\hat{x}$. Substitute the formula for the scalar $\hat{x}$: 
> $$p = a \left( \frac{a^Tb}{a^Ta} \right)$$
> Slide the scalar denominator out: $p = \frac{1}{a^Ta} a(a^Tb)$. Because matrix multiplication is associative, we can regroup the numerator: $p = \frac{1}{a^Ta} (aa^T)b$. 
> 
> Look at the dimensions if $a$ is an $n \times 1$ column vector:
> * **Denominator ($a^Ta$):** Dot product $(1 \times n) \times (n \times 1) \rightarrow \mathbf{1 \times 1}$ (Scalar).
> * **Numerator ($aa^T$):** Outer product $(n \times 1) \times (1 \times n) \rightarrow \mathbf{n \times n}$ (Matrix).
> Because the numerator is an $n \times n$ matrix and the denominator is a scalar, $P$ expands into a full $n \times n$ square matrix.

$P$ is a genuine $n\times n$ matrix (a column $a$ times a row $a^T$ divided by a number), not just a leftover scalar — and it has three properties worth checking *because they'll define what a projection matrix has to look like* in any dimension:

- **Rank 1.** $aa^T$ is a column times a row — the column space of $P$ is just the line through $a$ itself, dimension 1. Multiplying any $b$ by $P$ always lands you back on that line, by construction.
  * *Geometric meaning:* No matter what wild, high-dimensional vector $b$ you multiply by $P$, the matrix strips away all other dimensions and forces the output to land exactly on the 1D line defined by $a$. It acts as a rigid dimensional bottleneck.
- **Symmetric.** $P^T = \left(\frac{aa^T}{a^Ta}\right)^T = \frac{aa^T}{a^Ta} = P$, since transposing a column-times-row swaps it with itself and the denominator is just a number.
  * *Geometric meaning:* If $P$ were not symmetric, projecting $b$ onto $a$ would cast a "shadow" at a skewed angle (an oblique projection). The symmetry mathematically locks in that perfectly perpendicular 90° shortest-distance drop.
- **Idempotent: $P^2 = P$.** Projecting a point that's *already on the line* doesn't move it — so applying $P$ a second time has to give back the same answer as the first time. This is true of any projection onto any subspace, not just a line — it's the algebraic signature of "closest point" being a stable, settled answer.
  * *Algebraic Proof:* $P^2 = \left(\frac{aa^T}{a^Ta}\right)\left(\frac{aa^T}{a^Ta}\right) = \frac{a(a^Ta)a^T}{(a^Ta)(a^Ta)}$. The inner $(a^Ta)$ in the numerator is a scalar dot product, which perfectly cancels with one $(a^Ta)$ in the denominator, leaving $\frac{aa^T}{a^Ta} = P$.

### Worked example

Let $a = (1, 2)$, $b = (4, 3)$.

$$
\hat{x} = \frac{a^Tb}{a^Ta} = \frac{(1)(4)+(2)(3)}{1^2+2^2} = \frac{10}{5} = 2
$$
$$
p = \hat{x}a = (2, 4)
$$

Check orthogonality: $e = b - p = (2, -1)$, and $e^Ta = (2)(1)+(-1)(2) = 0$ ✓.

Projection matrix: $P = \dfrac{aa^T}{a^Ta} = \dfrac{1}{5}\begin{pmatrix}1&2\\2&4\end{pmatrix} = \begin{pmatrix}0.2&0.4\\0.4&0.8\end{pmatrix}$.

Check: $Pb = (0.2(4)+0.4(3),\; 0.4(4)+0.8(3)) = (2,4) = p$ ✓. And $P^2 = P$ — multiply it out and every entry matches.

---

## 2. Why bother projecting? (The motivation, restated)

Same problem as note 05: $Ax=b$ has no exact solution whenever $b$ isn't in the column space of $A$ — the typical case once there are more equations (rows) than unknowns (columns), with any real-world noise. The fix is to stop demanding $Ax=b$ exactly, and instead solve $A\hat{x} = p$, where $p$ is the closest point to $b$ that *is* reachable — the projection of $b$ onto the column space of $A$. This lecture is entirely about finding $p$ in general, not just for a single line.

---

## 3. Projecting onto a subspace (the general case)

**Setup:** a subspace described by a matrix $A$ whose columns $a_1, \dots, a_n$ form a basis for it (they don't need to be perpendicular to each other — just independent). Given $b$, find the closest point $p$ in that subspace.

> **💡 Clarification: The 1D vs nD Shift**
> In the 1D case, we stretched a single vector $a$ by a single scalar multiplier $\hat{x}$. Now, because our surface is built from multiple columns (basis vectors $a_1, a_2, \dots, a_n$), $\hat{x}$ upgrades from a scalar to a full vector $\hat{x}$. It contains the individual weights applied to each column of $A$ to reach the exact projection point ($p = A\hat{x}$).

### Setting up the equation

Since $p$ is in the column space, it's some combination of the columns: $p = A\hat{x}$ for a vector $\hat{x}$ to be found. The error is $e = b - A\hat{x}$, and the geometric requirement is that $e$ is perpendicular to the *entire* subspace — which means perpendicular to every column that spans it:

$$
a_1^T(b - A\hat{x}) = 0, \qquad a_2^T(b-A\hat{x}) = 0, \qquad \dots
$$

Stack these into one matrix equation — the rows of $A^T$ are exactly $a_1^T, a_2^T, \dots$ — and the whole system collapses to:

$$
A^T(b - A\hat{x}) = 0
$$

### The tie back to notes 04 and 05

This is worth pausing on. The equation says $A^Te = 0$ — by definition, that means $e$ is in the **left null space** of $A$ (note 04). And note 05 already proved that the left null space is the orthogonal complement of the column space. So this single line of algebra is silently re-confirming the exact geometric fact we just used to set the problem up: $e$ is perpendicular to the column space precisely because it's in the left null space, and those are the same statement viewed from two different definitions. The theory built in notes 04–05 and the fresh geometric derivation here land on identical ground.

### Solving

Expand:

$$
A^Tb - A^TA\hat{x} = 0 \;\;\Longrightarrow\;\; A^TA\,\hat{x} = A^Tb
$$

The normal equation, again — this time arrived at by "drop a perpendicular onto a subspace" rather than "the error has to live in the left null space." Solve for $\hat{x}$:

$$
\hat{x} = (A^TA)^{-1}A^Tb
$$

And since $p = A\hat{x}$:

$$
p = A(A^TA)^{-1}A^Tb
$$

so the **projection matrix** for a general subspace is:

$$
P = A(A^TA)^{-1}A^T
$$

Compare this to the line case: $P = \dfrac{aa^T}{a^Ta}$ is *exactly* this formula with $A$ replaced by the single column $a$ — the general formula isn't a different idea, it's the same one written so it survives more than one column.

> **🔍 Deep Dive: Why does $(A^TA)^{-1}$ replace division by $a^Ta$?**
> In the vector case, the denominator $a^Ta$ is a scalar, so it sits neatly underneath the fraction. But for a matrix, $A^TA$ is a full matrix containing all the dot products between the columns of $A$. Because matrix division is undefined, we "divide" by bringing its inverse into the product. 
> 
> Furthermore, $AA^T$ alone does not project correctly unless the columns of $A$ are orthonormal. $(A^TA)^{-1}$ acts as the crucial correction factor that accounts for the columns of $A$ possibly having different lengths and not being perpendicular. It "undoes" those interactions so the projection lands correctly.

### Why you can't simplify $P$ down to the identity

It's tempting to use $(AB)^{-1} = B^{-1}A^{-1}$ and write $(A^TA)^{-1} = A^{-1}(A^T)^{-1}$, which would make $P = AA^{-1}(A^T)^{-1}A^T = I$. **This is only legal when $A$ itself is square and invertible** — and in the normal use case here, $A$ is tall ($m>n$) with no inverse at all, so that splitting step doesn't exist. The formula has to stay in its "messier" combined form $A(A^TA)^{-1}A^T$ precisely because $A$ alone can't be inverted.

> **🔍 Deep Dive: The Algebraic Trap of Tall Matrices**
> The algebraic order swap rule $(AB)^{-1} = B^{-1}A^{-1}$ is mathematically correct, but applying it here is a "crime" of dimensions. In optimization and projection problems, $A$ is typically a "tall" matrix (e.g., 1000 rows for data points, 3 columns for features). A rectangular matrix does not have an inverse. The symbols $A^{-1}$ and $(A^T)^{-1}$ *literally do not exist*. 
>
> However, multiplying a tall matrix by its transpose ($A^TA$) results in a neat, small $n \times n$ square matrix (e.g., $3 \times 3$). As long as the columns are independent, this new square matrix *does* have an inverse. You cannot shatter the valid $(A^TA)^{-1}$ into invalid rectangular pieces.

That said, the degenerate case is a useful sanity check: if $A$ *is* square and invertible, its column space is all of $\mathbb{R}^n$ — every vector is already reachable, so the "best approximation" should just be $b$ itself, i.e. $P$ should be the identity. And indeed, in that one special case the splitting trick is legal, and it correctly produces $P=I$ — confirming the general formula behaves exactly the way the geometry demands at the boundary case.

> **💡 Clarification: When $P=I$, Projection is Pointless**
> If $A$ is square and invertible, its independent columns form a basis that spans the entire $n$-dimensional space. Since the column space is the entire universe, any vector $b$ you can imagine already lives perfectly inside it. The error is zero. You don't need a projection formula because the standard algebra $Ax = b$ already has a perfect, exact solution ($x = A^{-1}b$).

### Properties of $P$ in general

Both properties from the 1-D case carry over, by essentially the same algebra:

- **Symmetric:** $P^T = (A(A^TA)^{-1}A^T)^T = A((A^TA)^{-1})^TA^T = A(A^TA)^{-1}A^T = P$, since $(A^TA)$ is already symmetric (note 05) and the inverse of a symmetric matrix is symmetric.
- **Idempotent ($P^2=P$):** geometrically forced — the first projection lands you on the subspace, and projecting a point that's already there can't move it. Algebraically, $P^2 = A(A^TA)^{-1}\underbrace{A^TA}_{\text{cancels with its inverse}}(A^TA)^{-1}A^T = A(A^TA)^{-1}A^T = P$.

> **🔍 Deep Dive: Outer Products and Rank**
> In the 1D case, the numerator of $P$ is an outer product $uv^T$. A single outer product of two non-zero vectors ALWAYS produces a matrix of Rank 1. 
> 
> However, in the $n$D case, the numerator $AA^T$ is a perfectly calculable matrix, but it is *not* a single outer product. It is a **sum** of outer products: $AA^T = a_1a_1^T + a_2a_2^T + \dots + a_na_n^T$. 
> 
> This is a crucial distinction: while a single outer product is Rank 1, a sum of $r$ independent outer products can have Rank $r$. This is why the general projection matrix can project onto a multi-dimensional subspace rather than collapsing everything down to a 1D line.

### Worked examples

**Easy case — orthonormal basis.** Let $a_1=(1,0,0)$, $a_2=(0,1,0)$ (the $xy$-plane in $\mathbb{R}^3$), and $b=(2,3,5)$.

Because the basis is already orthonormal, $A^TA = I$, and the formula collapses to $\hat{x}=A^Tb = (2,3)$, so $p = (2,3,0)$ and $e=(0,0,5)$. This matches pure intuition — projecting onto the $xy$-plane just zeroes out the $z$-component, and the error is exactly the part that stuck out of the plane. *(This is also a preview of why building an orthonormal basis — Gram-Schmidt, Week 2 — is worth the effort: it turns the messy $(A^TA)^{-1}$ into a free identity matrix.)*

**General case — non-orthogonal basis.** Let $a_1=(1,0,1)$, $a_2=(0,1,1)$, $b=(1,2,4)$.

$$
A^TA = \begin{pmatrix}2&1\\1&2\end{pmatrix}, \qquad A^Tb = \begin{pmatrix}5\\6\end{pmatrix}
$$

Solving $\begin{pmatrix}2&1\\1&2\end{pmatrix}\hat{x} = \begin{pmatrix}5\\6\end{pmatrix}$ gives $\hat{x} = \left(\frac{4}{3}, \frac{7}{3}\right)$, so:

$$
p = \tfrac{4}{3}(1,0,1) + \tfrac{7}{3}(0,1,1) = \left(\tfrac{4}{3}, \tfrac{7}{3}, \tfrac{11}{3}\right), \qquad e = b-p = \left(-\tfrac{1}{3},-\tfrac{1}{3},\tfrac{1}{3}\right)
$$

Check: $e \cdot a_1 = -\tfrac13(1) + 0 + \tfrac13(1) = 0$, and $e\cdot a_2 = 0 -\tfrac13(1)+\tfrac13(1)=0$ — perpendicular to both columns, exactly as required.

---

## Where this is heading: line-fitting (completed in note 07)

The whole point of building this machinery is data that's *almost* linear but not quite. Suppose you have three data points and want the best straight line $b = C + Dt$ through them — say $(t,b) = (1,2), (2,3), (3,5)$. Plugging each point into $C+Dt=b$ gives three equations in only two unknowns:

$$
C + D = 2, \qquad C+2D = 3, \qquad C+3D = 5
$$

In matrix form, $Ax=b$ with $A=\begin{pmatrix}1&1\\1&2\\1&3\end{pmatrix}$, $x=\begin{pmatrix}C\\D\end{pmatrix}$, $b=\begin{pmatrix}2\\3\\5\end{pmatrix}$ — and since the three points clearly aren't collinear (the jumps are $+1$ then $+2$, not equal steps), there's no exact solution. This is precisely the unsolvable system Section 2 described, and it gets resolved exactly the way Section 3 lays out: solve $A^TA\hat{x}=A^Tb$ instead, and out comes the best-fit line. The full numeric solve — actually computing $C$ and $D$ — is note 07's job.

---

## Where this shows up later

- **Note 07 (Lecture 16):** finishes the numeric line-fitting example above and generalizes to fitting any number of data points with any polynomial degree.
- **Week 2, Gram-Schmidt/QR:** the "easy case" worked example above is the entire motivation for Gram-Schmidt — building a basis where $A^TA$ collapses to $I$ turns every projection formula in this note into trivial matrix-vector multiplication.
- **Week 2, symmetric matrices:** the proof that $P$ is symmetric here is a direct preview of why $A^TA$ (and projection matrices generally) always have real eigenvalues and orthogonal eigenvectors.

## Questions / things to revisit

- Re-derive $P=A(A^TA)^{-1}A^T$ from scratch starting only from "$p=A\hat{x}$ and $e\perp$ every column" — this is the cleanest single derivation to have memorized cold.
- Make sure the "$e$ is in the left null space" connection (Section 3) feels obvious, not just noted in passing — it's the single clearest link between notes 04, 05, and this one.
- Practice explaining out loud *why* you can't simplify $A(A^TA)^{-1}A^T$ to $I$ in general, and *why* it's allowed in the one special case where $A$ is square and invertible.
