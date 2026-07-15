# Lesson 4: Rayleigh quotient

## Overview
Analyzing the Rayleigh quotient as an optimization tool for symmetric matrices, and understanding its connection to eigenvalues.

---

## 1. The Rayleigh Quotient

For a real symmetric matrix $A$, the **Rayleigh Quotient** $R(A, x)$ for a non-zero vector $x$ is defined as:
$$R(A, x) = \frac{x^T A x}{x^T x}$$

---

## 2. Courant-Fischer Minimax Theorem

The Rayleigh quotient is bounded by the minimum and maximum eigenvalues of $A$:
$$\lambda_{\min} \le \frac{x^T A x}{x^T x} \le \lambda_{\max}$$

### Achievability
- The minimum value $\lambda_{\min}$ is achieved when $x$ is the eigenvector corresponding to $\lambda_{\min}$.
- The maximum value $\lambda_{\max}$ is achieved when $x$ is the eigenvector corresponding to $\lambda_{\max}$.

### Generalization to Other Eigenvalues
For any eigenvalue $\lambda_k$ (sorted $\lambda_1 \le \lambda_2 \le \dots \le \lambda_n$):
$$\lambda_k = \min_{\dim(S) = k} \max_{x \in S, x \neq 0} R(A, x)$$

---

## 3. Geometric Interpretation

Geometrically, if you project the unit sphere under the quadratic form $x^T A x$, the extrema of the Rayleigh quotient trace out the principal axes of the resulting multidimensional ellipsoid. This property forms the mathematical foundation of principal component analysis (PCA).
