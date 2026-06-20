# 05 — Orthogonal Vectors and Subspaces

**MIT Lecture:** 14 — Orthogonal Vectors and Subspaces
**Maps to:** IIT Indore Week 1, Topic 4 — Inner products, norms, and orthogonality
**Sets up:** Topic 5 — Projections and the least-squares problem

---

## Big picture first

Up to now we know the *sizes* of the four fundamental subspaces:

- Row space and null space both live in $\mathbb{R}^n$, with dimensions $r$ and $n-r$.
- Column space and left null space both live in $\mathbb{R}^m$, with dimensions $r$ and $m-r$.

This lecture adds a second, geometric fact on top of the dimension count: each pair doesn't just split the space by dimension — it splits it **at a right angle**.

$$
\text{row space} \perp \text{null space}, \qquad \text{column space} \perp \text{left null space}
$$

That single fact is the engine behind least squares later in the chapter, so it's worth understanding *why* it's true, not just memorizing it.

---

## 1. When are two vectors orthogonal?

**Definition.** Two vectors are orthogonal if the angle between them is $90^\circ$.

**Test.** $x$ and $y$ are orthogonal exactly when

$$
x^Ty = 0
$$

### Why the dot product is the right test (the *how*)

This isn't a coincidence — it falls straight out of the Pythagorean theorem. Picture a triangle with sides $x$, $y$, and $x+y$ as the hypotenuse. The triangle has a right angle (i.e. $x \perp y$) exactly when:

$$
\|x\|^2 + \|y\|^2 = \|x+y\|^2
$$

Now expand the right-hand side using $\|v\|^2 = v^Tv$:

$$
\|x+y\|^2 = (x+y)^T(x+y) = x^Tx + x^Ty + y^Tx + y^Ty
$$

Since we're working with real vectors, $x^Ty = y^Tx$ (same sum $x_1y_1 + x_2y_2 + \dots$ either way), so this becomes:

$$
\|x+y\|^2 = \|x\|^2 + \|y\|^2 + 2x^Ty
$$

Plugging back into the Pythagorean equation:

$$
\|x\|^2 + \|y\|^2 = \|x\|^2 + \|y\|^2 + 2x^Ty \;\;\Longrightarrow\;\; x^Ty = 0
$$

Everything cancels except the cross term. That's the whole proof — Pythagoras *is* the dot-product test, just multiplied out.

**Edge case:** the zero vector is orthogonal to every vector, since $0^Ty = 0$ always. Geometrically "angle" is meaningless for the zero vector, but algebraically the test still passes — and treating it as orthogonal to everything is what keeps the definitions downstream (orthogonal subspaces, orthogonal complements) consistent.

### Worked example

Let $x = (3, 1, -2)$ and $y = (1, -1, 1)$.

$$
x^Ty = (3)(1) + (1)(-1) + (-2)(1) = 3 - 1 - 2 = 0 \quad \checkmark \text{ orthogonal}
$$

Check Pythagoras directly:

$$
\|x\|^2 = 9+1+4 = 14, \qquad \|y\|^2 = 1+1+1 = 3
$$
$$
x+y = (4, 0, -1), \qquad \|x+y\|^2 = 16+0+1 = 17 = 14+3 \quad \checkmark
$$

---

## 2. When are two *subspaces* orthogonal?

This is where intuition needs correcting. The natural guess is "two subspaces are orthogonal if they only meet at the origin." That's **necessary but not sufficient**.

**Definition.** Subspace $S$ is orthogonal to subspace $T$ if *every* vector in $S$ is orthogonal to *every* vector in $T$.

### Why "doesn't intersect" isn't enough

Think of a wall and the floor of a room, meeting at the origin (the corner). They only share the line where they meet — yet they are clearly **not** orthogonal subspaces, because a $45^\circ$ vector in the wall and a vector in the floor are not at $90^\circ$ to each other. Worse: any vector lying exactly on the wall–floor seam belongs to *both* planes, so it would have to be orthogonal to itself — impossible unless it's zero. Two genuine orthogonal subspaces can only share the zero vector, but sharing only the zero vector doesn't guarantee orthogonality.

### Quick check in $\mathbb{R}^2$

The only subspaces of the plane are $\{0\}$, lines through the origin, and the whole plane.

| $S$ | $T$ | Orthogonal? |
|---|---|---|
| Line | $\{0\}$ | Always (vacuously) |
| Line | Whole plane | Never (the line is *inside* the plane) |
| Line | A different line | Only if they're literally perpendicular |

So "orthogonal subspaces" is a much stricter condition than "different subspaces."

---

## 3. The main result: row space ⊥ null space

**Claim:** every vector in the null space of $A$ is orthogonal to every vector in the row space of $A$.

### Why (the proof, built from nothing but the definition)

A vector $x$ in the null space satisfies $Ax = 0$. Write that out row by row:

$$
\begin{pmatrix} \text{row}_1 \\ \text{row}_2 \\ \vdots \\ \text{row}_m \end{pmatrix} x = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix}
$$

Each line of this is literally a dot product: $\text{row}_i \cdot x = 0$. So $x$ is automatically orthogonal to **every row** of $A$ — that fact was hiding inside $Ax=0$ the whole time.

But the row *space* is more than just the rows — it's every combination of them. So we need $x$ orthogonal to combinations too. That follows immediately from linearity of the dot product: if $\text{row}_1 \cdot x = 0$ and $\text{row}_2 \cdot x = 0$, then for any scalars $c_1, c_2$:

$$
(c_1\,\text{row}_1 + c_2\,\text{row}_2) \cdot x = c_1(\text{row}_1 \cdot x) + c_2(\text{row}_2 \cdot x) = 0
$$

So $x$ is orthogonal to *any* linear combination of the rows — i.e. to the entire row space. The same argument applied to $A^T$ gives column space ⊥ left null space.

### Worked example

Let $A = \begin{pmatrix} 1 & -1 & 2 \\ 2 & -2 & 4 \end{pmatrix}$. Both rows are multiples of $(1,-1,2)$, so the row space is the line through $(1,-1,2)$ — rank $1$.

Null space: solve $x_1 - x_2 + 2x_3 = 0$. Pick $x = (1, 1, 0)$:

$$
1 - 1 + 2(0) = 0 \quad \checkmark \text{ in the null space}
$$

Check orthogonality to the row:

$$
(1)(1) + (-1)(1) + (2)(0) = 0 \quad \checkmark
$$

Geometrically: the null space here is a whole *plane* in $\mathbb{R}^3$ (dimension $n - r = 3 - 1 = 2$), and that plane is exactly the set of vectors perpendicular to $(1,-1,2)$ — the same "normal vector" idea from calculus, now explained by linear algebra.

---

## 4. Orthogonal complements — "all," not just "some"

This is the upgrade that makes the fact genuinely useful, not just true.

**Definition.** The orthogonal complement of a subspace $S$ in $\mathbb{R}^n$ contains *every* vector orthogonal to $S$ — not merely some perpendicular vectors sitting nearby.

The null space isn't just *a* subspace that happens to be orthogonal to the row space — it is the *entire* orthogonal complement of the row space in $\mathbb{R}^n$. That's a stronger statement, and the dimension count backs it up:

$$
\dim(\text{row space}) + \dim(\text{null space}) = r + (n - r) = n
$$

There's no room left over. This is also why you can't have a line and a line be row-space/null-space partners in $\mathbb{R}^3$ — $1 + 1 \ne 3$. A rank-1 matrix in $\mathbb{R}^3$ must pair a 1-D row space with a 2-D null space (a line and a plane), never two lines.

> **Fundamental Theorem of Linear Algebra — Part 2:** the four subspaces aren't just sized correctly (Part 1, rank-nullity); they're also oriented at $90^\circ$ as orthogonal complements of each other.

---

## 5. Where this is heading: $A^TA$ and least squares

**The real problem of this chapter:** solve $Ax = b$ when $b$ is *not* in the column space — i.e., no exact solution exists. This is the normal situation when you have more equations than unknowns: many noisy measurements (sensor readings, repeated pulse measurements, satellite tracking) and few true parameters. You don't want to throw away "extra" equations — you want the solution that uses *all* of them best.

The matrix that makes this solvable is $A^TA$.

**Why $A^TA$ is square and symmetric:**

- $A$ is $m \times n$, so $A^T$ is $n \times m$, and $A^TA$ is $n \times n$ — square.
- $(A^TA)^T = A^T(A^T)^T = A^TA$ — symmetric, since transposing twice cancels.

**Why we care whether $A^TA$ is invertible:** the strategy for the noisy system is to multiply both sides of $Ax=b$ by $A^T$, giving the *normal equation*:

$$
A^TA\,\hat{x} = A^Tb
$$

This will have a clean, unique solution $\hat{x}$ exactly when $A^TA$ is invertible.

**The key fact (tying straight back to Section 3):**

$$
\text{null space of } A^TA = \text{null space of } A, \qquad \text{rank}(A^TA) = \text{rank}(A)
$$

So $A^TA$ is invertible **exactly when $A$ has independent columns** — i.e., when the only solution to $Ax=0$ is $x=0$.

### Worked example — full column rank (invertible case)

$$
A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{pmatrix}, \qquad A^TA = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}
$$

$\det(A^TA) = 4 - 1 = 3 \ne 0$ — invertible, because the two columns of $A$ are independent.

### Worked example — dependent columns (singular case)

$$
A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \\ 3 & 6 \end{pmatrix} \quad (\text{column 2} = 2 \times \text{column 1})
$$

$$
A^TA = \begin{pmatrix} 14 & 28 \\ 28 & 56 \end{pmatrix}, \qquad \det(A^TA) = 14(56) - 28(28) = 784 - 784 = 0
$$

Singular — exactly as predicted, because $A$'s columns are dependent ($\text{rank}(A) = 1$).

---

## Where this shows up later

- **Topic 5 (Projections, least squares):** the orthogonality of row space and null space is *the* reason $A^TA\hat{x} = A^Tb$ works — the error vector $b - A\hat{x}$ ends up living in the left null space, perpendicular to the column space, which is precisely how you make an "unsolvable" system as solvable as possible.
- **Week 2, Gram-Schmidt/QR:** building orthogonal *bases* (not just orthogonal subspaces) is the natural next step — this lecture is the geometric foundation that makes Gram-Schmidt meaningful rather than just a computational recipe.
- **Week 2, Symmetric matrices:** $A^TA$ being symmetric here foreshadows why symmetric matrices get real eigenvalues and orthogonal eigenvectors later.

## Questions / things to revisit

- Re-derive the row space ⊥ null space proof from scratch without looking — the linearity step (orthogonal to each row ⟹ orthogonal to all combinations) is the part most worth being able to reproduce instantly.
- Make sure the "dimensions add to $n$" fact feels obvious, not just memorized — it's what rules out impossible pairings (like two lines in $\mathbb{R}^3$).
- Sit with *why* $A^TA$ inherits the same null space as $A$ — it isn't proven in full here, just used; worth re-deriving once Topic 5 introduces it formally.
