# 05 — Orthogonal Vectors and Subspaces (Complete)

**MIT Lecture:** 14 — Orthogonal Vectors and Subspaces
**Builds on:** Lecture 10 — Four Fundamental Subspaces (recapped below so this note is self-contained; full depth in note 04)
**Maps to:** IIT Indore Week 1, Topic 4 — Inner products, norms, and orthogonality (extends into Topic 3 and Topic 5)
**Also covers:** Left inverse, right inverse, pseudoinverse — foreshadows SVD (Week 2)

---

## 0. Quick recap: the four fundamental subspaces

Let $A$ be $m \times n$ with rank $r$ — the number of genuinely independent directions among its rows or columns.

**Input domain $\mathbb{R}^n$:**

| Subspace | Definition | Dimension |
|---|---|---|
| Row space | span of $A$'s rows | $r$ |
| Null space | all $x$ with $Ax=0$ | $n-r$ |

$$r + (n-r) = n \quad \text{(Rank-Nullity Theorem)}$$

**Output domain $\mathbb{R}^m$:**

| Subspace | Definition | Dimension |
|---|---|---|
| Column space | span of $A$'s columns | $r$ |
| Left null space | all $y$ with $A^Ty=0$ | $m-r$ |

$$r + (m-r) = m$$

**Why "left"?** Transpose $A^Ty=0$ to get $y^TA = 0^T$ — $y^T$ multiplies $A$ from the left. There are two equivalent ways to read that equation, and both are worth holding onto:

- **By columns:** each entry of $y^TA$ is $y$ dotted with one column of $A$, so the whole product is zero exactly when $y$ is orthogonal to *every column* — i.e. orthogonal to the entire column space.
- **By rows:** $y^TA=0^T$ is literally asking, "what combination of the rows of $A$, weighted by $y$, adds up to a row of all zeros?" — the same question the ordinary null space asks of columns, just mirrored.

If the column space is everywhere $A$ *can* reach in the output space, the left null space is exactly the set of directions in the output space that $A$ *cannot* reach.

### The completeness property: $b = p + e$

This is the output-space mirror of the $x = x_{\text{row}} + x_{\text{null}}$ decomposition from Section 3a. Because the column space and left null space are orthogonal complements (proved in Section 4, but stated here since it belongs with the setup), *any* vector $b$ in $\mathbb{R}^m$ — reachable by $A$ or not — splits cleanly and uniquely into

$$
b = p + e, \qquad p \in \text{column space}, \;\; e \in \text{left null space}
$$

$p$ is the part of $b$ that $A$ can actually produce; $e$ is the part it fundamentally can't. This single decomposition is what makes least squares possible at all (Section 5) — without it, "the closest reachable point to $b$" wouldn't even be a well-defined idea.

### The "dimensional real estate" picture

Treat $\mathbb{R}^n$ as having exactly $n$ dimensions of usable space, which the row space and null space must divide between them completely — no more, no less. This framing makes two special cases fall out immediately, without recomputing anything:

**Full column rank ($r=n$, matrix is tall or square):**
- The row space claims all $n$ dimensions, so the null space gets $n-n=0$ — it shrinks to $\{0\}$.
- *Physical meaning:* the null space measures redundancy — it's literally the size of the set of distinct inputs that all get crushed down onto the same output. If it has dimension zero, no two different inputs ever collide on the same output: every column pulls the result in a genuinely new, necessary direction, none of them can combine to cancel each other to zero, and no information from the input is ever lost or compressed away. The map is **injective**.
- *Solving $Ax=b$:* there are no free variables left to scale, so you never get infinitely many solutions. For any target $b$, there's either **exactly one** solution (if $b$ happens to land inside the column space) or **zero** exact solutions (if it doesn't — the everyday case once there's any noise, which is exactly what Section 5 is built to handle).

**Full row rank ($r=m$, matrix is wide or square):**
- The column space claims all $m$ dimensions of the output, so the left null space gets $m-m=0$.
- *Physical meaning:* if a zero null space means "no information lost," a zero left null space means "no unreachable space." The columns span the *entire* output space, so some combination of them can hit absolutely any target $b$ — the map is **surjective**.
- *Solving $Ax=b$:* because there's no unreachable space, you're guaranteed at least one exact solution for *any* $b$ you could name — you never even need least squares here, since $b$ is already inside the column space by construction. But the input-space null space is non-trivial whenever $n>m$, so that one solution is never alone — you get **1 or infinitely many** solutions, never zero.

**Full rank, square ($r=m=n$):** both shrink to $\{0\}$ at once — bijective, invertible, **exactly one** solution, always.

| Condition | Null space | Left null space | Behavior | Solutions to $Ax=b$ |
|---|---|---|---|---|
| Full column rank | $\{0\}$ | $\dim = m-n$ | Injective | 0 or 1 |
| Full row rank | $\dim = n-m$ | $\{0\}$ | Surjective | 1 or ∞ |
| Full rank, square | $\{0\}$ | $\{0\}$ | Bijective | exactly 1 |

**Why a tall, full-column-rank matrix is forced to have dependent rows:** this feels like a contradiction the first time you see it — "independent columns" sounds like it should mean "independent everything." It doesn't, for a purely dimensional reason. Each row has $n$ entries, so every row lives in $\mathbb{R}^n$ — and you can't fit more than $n$ linearly independent vectors into an $n$-dimensional space (you can't have 5 independent directions crammed into 3-D space, for instance). If $A$ is tall ($m>n$) with full column rank, it has $m$ rows squeezed into that $n$-dimensional space with $m>n$, so **at least $m-n$ of those rows are guaranteed to be combinations of the others** — not approximately, not usually, but as a matter of dimension-counting necessity. This isn't a flaw; it's the literal structural reason least squares exists — see Section 5.

*(This section is a compressed recap. Full derivations and more worked dimension examples live in note 04 — read that first if any of the above feels unfamiliar.)*

---

## 1. Orthogonal vectors — proving the dot-product test

**Definition.** Two vectors are orthogonal if the angle between them is $90^\circ$.

**Test.** $x$ and $y$ are orthogonal exactly when $x^Ty = 0$.

### Why the dot product is the right test

In one line, without algebra: a right angle means the two short sides squared add up to *exactly* the long side squared (Pythagoras) — nothing more. When you expand the long side $\|x+y\|^2$ algebraically, it naturally splits into $\|x\|^2 + \|y\|^2$ plus one extra leftover piece, $2x^Ty$. For the Pythagorean equality to hold *exactly*, that leftover piece has nowhere to go but zero. So $x^Ty=0$ isn't a separate rule — it's the only way the geometry can balance.

In full algebra: picture a triangle with sides $x$, $y$, and hypotenuse $x+y$. The triangle has a right angle exactly when

$$
\|x\|^2 + \|y\|^2 = \|x+y\|^2
$$

Expand the right side using $\|v\|^2 = v^Tv$:

$$
\|x+y\|^2 = (x+y)^T(x+y) = x^Tx + x^Ty + y^Tx + y^Ty
$$

Since $x^Ty = y^Tx$ for real vectors, this becomes $\|x\|^2 + \|y\|^2 + 2x^Ty$. Plug back into the Pythagorean equation:

$$
\|x\|^2 + \|y\|^2 = \|x\|^2 + \|y\|^2 + 2x^Ty \;\;\Longrightarrow\;\; x^Ty = 0
$$

Everything cancels except the cross term — Pythagoras *is* the dot-product test, just multiplied out.

**Edge case:** the zero vector is orthogonal to everything, since $0^Ty=0$ always. "Angle" is meaningless for the zero vector, but the algebra still passes, which keeps later definitions (orthogonal subspaces, complements) consistent.

### Worked example

$x = (3, 1, -2)$, $y = (1, -1, 1)$:

$$
x^Ty = 3 - 1 - 2 = 0 \quad \checkmark
$$
$$
\|x\|^2 = 14, \;\; \|y\|^2 = 3, \;\; x+y=(4,0,-1), \;\; \|x+y\|^2 = 17 = 14+3 \quad \checkmark
$$

---

## 2. Orthogonal subspaces — why "doesn't intersect" isn't enough

**Definition.** $S$ is orthogonal to $T$ if *every* vector in $S$ is orthogonal to *every* vector in $T$.

The natural guess — "two subspaces are orthogonal if they only meet at the origin" — is **necessary but not sufficient**. Two examples make this concrete:

- **In the plane:** draw two lines crossing at a shallow $15^\circ$ angle. They're both 1-D subspaces, and they only intersect at the origin — yet they're obviously nowhere near $90^\circ$. No shared "seam," and the test still fails.
- **In 3-D, the wall and floor of a room:** these intersect along a whole line (the corner seam), so they fail even more directly — any vector on that seam belongs to both planes, so it would have to be orthogonal to itself, which is impossible unless it's zero. And even ignoring the seam, a $45^\circ$ vector on the wall and a vector along the floor aren't at $90^\circ$ to each other anyway.

### Quick check in $\mathbb{R}^2$

| $S$ | $T$ | Orthogonal? |
|---|---|---|
| Line | $\{0\}$ | Always (vacuously) |
| Line | Whole plane | Never (line is *inside* the plane) |
| Line | A different line | Only if literally perpendicular |

So "orthogonal subspaces" is a much stricter condition than "different subspaces."

---

## 3. The main result: row space ⊥ null space

**Claim:** every vector in the null space of $A$ is orthogonal to every vector in the row space of $A$.

### Why

$x$ in the null space means $Ax=0$. Written row by row, each entry of that equation is literally a dot product: $\text{row}_i \cdot x = 0$ for every row. So $x$ is automatically orthogonal to every individual row — that fact was hiding inside $Ax=0$ the whole time.

But the row *space* is more than the rows themselves — it's every combination of them. That extends for free, by linearity of the dot product: if $\text{row}_1 \cdot x = 0$ and $\text{row}_2 \cdot x = 0$, then for any scalars,

$$
(c_1\,\text{row}_1 + c_2\,\text{row}_2)\cdot x = c_1(\text{row}_1\cdot x) + c_2(\text{row}_2\cdot x) = 0
$$

So $x$ is orthogonal to *any* combination of the rows — the entire row space. The same argument on $A^T$ gives column space ⊥ left null space.

### Worked example

$A = \begin{pmatrix} 1 & -1 & 2 \\ 2 & -2 & 4 \end{pmatrix}$ — both rows are multiples of $(1,-1,2)$, rank 1.

Null space: solve $x_1-x_2+2x_3=0$. Take $x=(1,1,0)$: checks out, and $(1)(1)+(-1)(1)+(2)(0)=0$ — orthogonal to the row, as required. Geometrically, this null space is the entire plane perpendicular to $(1,-1,2)$ — the same "normal vector" idea from calculus.

### 3a. What happens to the null-space piece when it passes through $A$?

Since row space and null space split all of $\mathbb{R}^n$ between them (Section 4), any $x$ decomposes uniquely as $x = x_{\text{row}} + x_{\text{null}}$. Applying $A$:

$$
Ax = Ax_{\text{row}} + Ax_{\text{null}} = Ax_{\text{row}} + 0
$$

The null-space piece doesn't shrink or distort — it's **completely erased** the instant $A$ acts, by definition. $A$ never "sees" that component at all; only $x_{\text{row}}$ survives. The row space carries all the real information; the null space is the part $A$ is structurally blind to.

---

## 4. Orthogonal complements — "all," not just "some"

**Definition.** The orthogonal complement of $S$ contains *every* vector orthogonal to $S$ — not merely some.

Two illustrations of why "some" isn't enough:

- In $\mathbb{R}^3$, let $S$ be the vertical $z$-axis. The $x$-axis alone is orthogonal to $S$ — but it's not the complement, since it leaves out the $y$-axis and every diagonal line in the floor that's also at $90^\circ$ to $S$. The actual orthogonal complement is the *entire* floor (the $xy$-plane) — the full, exhaustive set.
- The null space isn't just *a* subspace that happens to be orthogonal to the row space — by the proof in Section 3, it gathers up *every* vector orthogonal to the row space. It's the complete complement, not a sample of one.

The dimension count confirms it:

$$
\dim(\text{row space}) + \dim(\text{null space}) = r + (n-r) = n
$$

No room left over — which is why you can never have a 1-D line as both the row space and the null space in $\mathbb{R}^3$ ($1+1\ne3$). A rank-1 matrix in $\mathbb{R}^3$ must pair a 1-D row space with a 2-D null space.

> **Fundamental Theorem of Linear Algebra — Part 2:** the four subspaces aren't just correctly sized (Part 1, rank-nullity); they're oriented at $90^\circ$ as orthogonal complements.

---

## 5. $A^TA$ and least squares — the geometric derivation

**The real problem:** solve $Ax=b$ when $b$ isn't in the column space — the everyday case with more equations (rows) than unknowns (columns) and any measurement noise.

**Why $A^TA$ is square and symmetric:** $A$ is $m\times n$, so $A^TA$ is $n\times n$; and $(A^TA)^T = A^T(A^T)^T = A^TA$.

### The derivation

Since $b$ is unreachable, find the closest reachable point instead. "Closest" inside a subspace always means dropping a perpendicular — Section 1's idea, applied to a whole subspace. Call that point $p$, the **projection** of $b$ onto the column space, with $A\hat{x}=p$ for some $\hat{x}$.

The gap is the **error vector** $e = b - A\hat{x}$. Because $p$ is the *closest* point, $e$ must be perpendicular to the entire column space — any other direction would mean $p$ wasn't actually closest. "Perpendicular to the entire column space" is exactly the left null space (Section 0), whose defining property is $A^Ty=0$. Apply $A^T$ to the error vector:

$$
A^T(b - A\hat{x}) = 0 \;\;\Longrightarrow\;\; A^TA\,\hat{x} = A^Tb
$$

That's the normal equation, derived from nothing but "closest point ⟹ perpendicular error ⟹ error lives in the left null space."

**Key fact:** $\text{null space}(A^TA) = \text{null space}(A)$ and $\text{rank}(A^TA)=\text{rank}(A)$, so $A^TA$ is invertible exactly when $A$ has independent columns. This gives the **left inverse**:

$$
\hat{x} = (A^TA)^{-1}A^Tb
$$

### Worked examples

Full column rank: $A=\begin{pmatrix}1&0\\0&1\\1&1\end{pmatrix}$, $A^TA=\begin{pmatrix}2&1\\1&2\end{pmatrix}$, $\det=3\ne0$ — invertible.

Dependent columns: $A=\begin{pmatrix}1&2\\2&4\\3&6\end{pmatrix}$ (col 2 = 2×col 1), $A^TA=\begin{pmatrix}14&28\\28&56\end{pmatrix}$, $\det=0$ — singular, exactly as predicted.

**Why row dependence never threatens this:** $(A^TA)$ only depends on column rank. A tall matrix with independent columns is *guaranteed* to have dependent rows (Section 0) — harmless here, since $(A^TA)$ never references row rank. Physically: consistent dependent rows (row 2 exactly double row 1, target doubled too) add no new information; conflicting dependent rows (the realistic case with noise) are exactly what pushes $b$ outside the column space in the first place — and the left inverse is the mediator that minimizes the total squared disagreement.

---

## 6. The full picture: left inverse, right inverse, pseudoinverse

| Matrix shape | Rank condition | What's trivial | Tool | Formula | What it optimizes |
|---|---|---|---|---|---|
| Tall ($m>n$) | Full column rank | Null space | **Left inverse** | $(A^TA)^{-1}A^T$ | $\min\lVert b-Ax\rVert$ (Section 5) |
| Wide ($n>m$) | Full row rank | Left null space | **Right inverse** | $A^T(AA^T)^{-1}$ | $\min\lVert x\rVert$ among exact solutions |
| Square | Full rank | Both | **True inverse** | $A^{-1}$ | Exact, unique — nothing to optimize |
| Any | Rank-deficient | Neither | **Pseudoinverse** | $A^+$ (via SVD) | Both simultaneously |

### 6.1 Right inverse — the minimum-norm case

Flip the shape: $n>m$ (underdetermined), rows independent ($r=m$). The left null space vanishes, so every $b$ is reachable — but the input-space null space is now non-trivial ($n-m>0$), so there are **infinitely many exact solutions**. The question flips from "what's closest?" to "which exact solution is best?"

Forcing the normal-equation approach fails: $A^TA$ is $n\times n$ but only rank $m<n$, so it's singular. Use $AA^T$ instead — $m\times m$, full rank (rows independent), giving the **right inverse**:

$$
x^* = A^T(AA^T)^{-1}b
$$

Geometrically, $x^*$ is the exact solution with smallest length — it lives entirely in the row space, contributing nothing from the null space (recall Section 3a: $A$ can't even see that component anyway).

### 6.2 Rank-deficient — neither inverse works

If both rows and columns are dependent ($r<m$ and $r<n$), $(A^TA)$ and $(AA^T)$ are both singular. Neither inverse exists. The fix is the **Singular Value Decomposition**, isolating exactly the $r$ informative directions and building the **Moore–Penrose pseudoinverse** $A^+$ — which reduces to the left inverse, right inverse, or true inverse in their respective special cases. See Week 2, Topic 4.

---

## 7. Applied walkthroughs

Short, worked-through scenarios to ground the theory in something concrete.

**A neural net layer, $100\times80$, full column rank.** Row space: dim 80 (= all of $\mathbb{R}^{80}$). Null space: dim 0. Column space: dim 80, sitting inside the 100-dimensional output. Left null space: dim 20 — twenty output directions this layer's weights simply cannot reach.

**A square $50\times50$ matrix with a null space of dimension 5.** By rank-nullity, $r + 5 = 50$, so $r=45$ — this matrix is rank-deficient, not full rank, even though it's square. Can it reach every point in $\mathbb{R}^{50}$? No: since $m=n=50$ here, row rank = column rank = $r=45$ too, so the left null space has dimension $m-r = 50-45=5$ as well — five full dimensions of the output are unreachable. A non-trivial null space and a non-trivial left null space *both* show up together here precisely because the matrix is square: for a square matrix, $r<n$ always forces $r<m$ in lockstep, so injectivity and surjectivity fail or hold together, never just one of them (this is Section 0's "impossible matrix" fact, Q4 below, working in reverse).

**A robot at a kinematic singularity.** The Jacobian $J$ normally maps joint velocities to 3-D foot velocity. At full leg extension, the column space of $J$ momentarily *loses a dimension* — the robot can no longer push its foot directly along the leg's axis. By Section 0's "real estate" logic, that lost dimension has to go *somewhere*: it shows up as the left null space gaining exactly that dimension. Physically, the expanded left null space is the literal direction of motion the robot has lost control over in that instant.

**A trading pipeline: 1,000 indicator columns, 50,000 timestamp rows, $A^TA$ still won't invert.** With $m \gg n$, you'd expect a clean left-inverse setup — row dependence here is expected and harmless (Section 5). A singular $A^TA$ despite the huge row count means the *columns themselves* aren't actually independent: some indicators are exact or near-exact combinations of others (duplicated or derived features). That shows up as a non-trivial null space tied directly to those columns — no number of additional rows can fix column dependence, since $(A^TA)$ never looks at row count at all.

**A Markov/RL transition matrix where every state is reachable, but several actions land on the same state.** "Every state reachable" means the column space spans the whole output — full row rank, left null space $=\{0\}$. "Multiple actions, same state" means the map isn't injective — the null space is non-trivial. To trace an optimal action sequence backward through this many-to-one-but-fully-reachable system, you want the **right inverse**: it picks the minimum-effort action sequence among the many that land exactly on target, rather than approximating something unreachable.

**A wide recommender system: 1,000 user features mapped to 5 behavior categories, rows independent.** Left null space vanishes — every category combination is reachable. Use $(AA^T)^{-1}$, the right inverse, which finds the smallest-magnitude feature-weight vector that exactly reproduces the target category mix — minimizing redundant, unnecessary weight rather than minimizing error (there is none to minimize here).

---

## 8. Quick self-test

Answer from memory before checking the section reference.

1. **The proof, in words only:** how does Pythagoras force the dot product of perpendicular vectors to be exactly zero? *(→ §1)*
2. **The "all vs. some" trap:** in $\mathbb{R}^4$, you find a 2-D plane $S$ and a 1-D line $T$ where every vector in $S$ is orthogonal to every vector in $T$. Are they necessarily orthogonal complements? *(→ §4)*
3. **The error vector:** why is $e=b-A\hat{x}$ forced specifically into the left null space, not just "some" perpendicular subspace? *(→ §5)*
4. **The impossible matrix:** why can a matrix never have both its null space and left null space equal to $\{0\}$ unless it's square? *(→ §0)*
5. **The orthogonal paradox:** $A$ is square, $n\times n$. You find a non-zero $v$ in the row space with $Av=0$. Why is this impossible? *(→ §3 + §4 together)*
6. **No free variables:** explain in your own words why full column rank rules out "infinitely many solutions" as an outcome for $Ax=b$ — what specifically would have to exist for that outcome to be possible, and why does full column rank kill it? *(→ §0, full column rank bullet)*
7. **Diagnosing a crash, generalized:** an optimization script throws a singular-matrix error inverting $A^TA$, on a matrix where $m \gg n$. Walk through, from first principles, why row count alone can never rescue this — what's the one and only thing that determines whether $A^TA$ is invertible? *(→ §5, "why row dependence never threatens this," then invert the logic to find what *would* threaten it)*
8. **The recommender system:** $n=1000$ user features map to $m=5$ behavior categories, rows independent. Which subspace vanishes completely, and do you reach for $(A^TA)^{-1}$ or $(AA^T)^{-1}$ to find the optimal weights — and what are you actually minimizing when you do? *(→ §6.1, then the worked walkthrough in §7)*
9. **Mixed case:** suppose $A$ is tall ($m>n$) but rank-deficient — the columns are *also* dependent, not just the rows. Which of the four tools in §6's table applies, and why do both the left and right inverse fail here even though the matrix is tall like the "normal" least-squares case? *(→ §6.2)*

---

## Where this shows up later

- **Topic 5 (Projections, least squares):** Section 5 *is* the theory behind $A^TA\hat{x}=A^Tb$ — the rest of that topic builds the computational machinery on top of it.
- **Week 2, Gram-Schmidt/QR:** building orthogonal *bases*, not just orthogonal subspaces, is the natural next step.
- **Week 2, Symmetric matrices:** $A^TA$ being symmetric foreshadows why symmetric matrices get real eigenvalues and orthogonal eigenvectors.
- **Week 2, SVD:** Section 6.2's rank-deficient case is exactly what the SVD and pseudoinverse are built to handle.

## Questions / things to revisit

- Re-derive row space ⊥ null space from scratch — the linearity step is the part most worth being able to reproduce instantly.
- Make the "dimensions add to $n$" fact feel obvious, not memorized.
- Re-derive why $A^TA$ inherits $A$'s null space once Topic 5 formalizes it.
- Make sure §5 (left inverse) and §6.1 (right inverse) feel like mirror-image derivations, not two separate things to memorize.
