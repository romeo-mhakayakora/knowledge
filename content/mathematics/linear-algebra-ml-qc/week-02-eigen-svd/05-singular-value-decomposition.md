# Lesson 5: Singular value decomposition

## Overview
Reconstructing any rectangular or square matrix into orthogonal and diagonal components, representing the ultimate generalization of the Spectral Theorem.

---

## 1. The Singular Value Decomposition (SVD)

Every real $m \times n$ matrix $A$ can be factored into:
$$A = U \Sigma V^T$$

Where:
- **$U$**: An $m \times m$ orthogonal matrix ($U^T U = I$) whose columns are the **left singular vectors** of $A$ (eigenvectors of $A A^T$).
- **$\Sigma$**: An $m \times n$ diagonal-like matrix containing the non-negative **singular values** $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$ on the diagonal, sorted in descending order.
- **$V$**: An $n \times n$ orthogonal matrix ($V^T V = I$) whose columns are the **right singular vectors** of $A$ (eigenvectors of $A^T A$).

---

## 2. Geometric Interpretation

The SVD shows that any linear transformation can be decomposed into three simple geometric steps:
1. **Rotation/Reflection** in the domain space via $V^T$.
2. **Scaling** along the coordinate axes via $\Sigma$.
3. **Rotation/Reflection** in the codomain space via $U$.

---

## 3. Connection to Symmetric Matrices

The SVD of $A$ is deeply connected to the spectral decomposition of symmetric matrices:
- $A^T A = (V \Sigma^T U^T)(U \Sigma V^T) = V (\Sigma^T \Sigma) V^T$
- $A A^T = (U \Sigma V^T)(V \Sigma^T U^T) = U (\Sigma \Sigma^T) U^T$

Thus, the singular values $\sigma_i$ are the square roots of the eigenvalues of the positive semidefinite symmetric matrix $A^T A$ (or $A A^T$).
