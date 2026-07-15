# Lesson 3: Diagonalization, Positive semidefinite matrices

## Overview
Reconstructing matrices into diagonal forms, and identifying the properties and geometries of positive semidefinite matrices.

---

## 1. Diagonalization and Powers

A square matrix $A$ is **diagonalizable** if it is similar to a diagonal matrix:
$$A = S \Lambda S^{-1}$$

- **$S$**: A matrix whose columns are $n$ linearly independent eigenvectors of $A$.
- **$\Lambda$**: The diagonal matrix of eigenvalues.

### Application: Matrix Powers
Diagonalization makes computing high powers of a matrix trivial:
$$A^k = S \Lambda^k S^{-1}$$

---

## 2. Positive Semidefinite (PSD) Matrices

A symmetric matrix $A \in \mathbb{R}^{n \times n}$ is **positive semidefinite (PSD)**, denoted as $A \succeq 0$, if:
$$x^T A x \ge 0 \quad \text{for all } x \in \mathbb{R}^n$$

It is **positive definite (PD)**, denoted as $A \succ 0$, if:
$$x^T A x > 0 \quad \text{for all } x \neq 0$$

### Equivalent Characterizations
1. **Eigenvalues**: All eigenvalues are non-negative ($\lambda_i \ge 0$ for PSD; $\lambda_i > 0$ for PD).
2. **Gram Matrix**: $A$ can be written as $A = B^T B$ for some matrix $B$.
3. **Pivots**: All pivots in elimination are non-negative (positive for PD).
