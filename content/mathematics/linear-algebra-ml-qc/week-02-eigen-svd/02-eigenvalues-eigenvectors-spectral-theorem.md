# Lesson 2: Eigenvalues and eigenvectors, spectral theorem

## Overview
Understanding eigenvectors as invariant directions under linear transformations, and the Spectral Theorem as the geometric decomposition of real symmetric matrices.

---

## 1. Eigenvalues and Eigenvectors

For a square matrix $A \in \mathbb{R}^{n \times n}$, a non-zero vector $v$ is an **eigenvector** with **eigenvalue** $\lambda$ if:
$$Av = \lambda v$$

### The Characteristic Equation
To find the eigenvalues, solve the characteristic polynomial:
$$\det(A - \lambda I) = 0$$

For each eigenvalue $\lambda_i$, find the corresponding eigenvectors by finding the null space (eigenspace) of $A - \lambda_i I$:
$$(A - \lambda_i I)v = 0$$

---

## 2. The Spectral Theorem for Symmetric Matrices

A matrix $A$ is real **symmetric** if $A = A^T$. Symmetric matrices have remarkably clean spectral properties.

### Theorem Statement
Every real symmetric matrix $A$ can be decomposed into:
$$A = Q \Lambda Q^T = \sum_{i=1}^{n} \lambda_i q_i q_i^T$$

Where:
- **$Q$**: An orthogonal matrix ($Q^T Q = I$) whose columns $\{q_1, \dots, q_n\}$ are orthonormal eigenvectors of $A$.
- **$\Lambda$**: A diagonal matrix containing the real eigenvalues $\lambda_1, \dots, \lambda_n$.

### Key Properties of Symmetric Matrices
1. **Real Eigenvalues**: All eigenvalues of a real symmetric matrix are guaranteed to be real.
2. **Orthogonal Eigenspaces**: Eigenvectors corresponding to distinct eigenvalues are orthogonal.
3. **Orthonormal Basis**: There exists an orthonormal basis of $\mathbb{R}^n$ consisting entirely of eigenvectors of $A$.
