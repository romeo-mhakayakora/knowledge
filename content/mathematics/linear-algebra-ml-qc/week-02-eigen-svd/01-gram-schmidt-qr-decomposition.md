# Lesson 1: Gram-Schmidt process, QR decomposition

## Overview
How to construct an orthonormal basis from any set of linearly independent vectors, and how this process compiles into the matrix factorization $A = QR$.

---

## 1. The Gram-Schmidt Process

To turn a basis $\{v_1, v_2, \dots, v_n\}$ into an orthonormal basis $\{u_1, u_2, \dots, u_n\}$:

### Step 1: Orthogonalization
Project each successive vector onto the subspace spanned by the previous vectors, and subtract the projection to get the orthogonal component.
- $u_1 = v_1$
- $u_2 = v_2 - \text{proj}_{u_1}(v_2) = v_2 - \frac{u_1 \cdot v_2}{\|u_1\|^2} u_1$
- $u_k = v_k - \sum_{i=1}^{k-1} \text{proj}_{u_i}(v_k)$

### Step 2: Normalization
Divide each orthogonal vector by its length to make it unit-length:
$$e_i = \frac{u_i}{\|u_i\|}$$

---

## 2. QR Decomposition

Every real $m \times n$ matrix $A$ with linearly independent columns can be factored as:
$$A = QR$$

- **$Q$**: An $m \times n$ matrix with orthonormal columns ($Q^T Q = I$).
- **$R$**: An $n \times n$ upper triangular matrix with positive diagonal entries.

### Connections to Gram-Schmidt
The columns of $Q$ are the normalized vectors $e_i$ resulting from the Gram-Schmidt process on the columns of $A$. The matrix $R$ contains the projection coefficients:
$$R = Q^T A$$
