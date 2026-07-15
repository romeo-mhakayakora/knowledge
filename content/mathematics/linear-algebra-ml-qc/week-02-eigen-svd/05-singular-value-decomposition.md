<article class="post-layout">
  <header class="post-header">
    <div class="post-meta-details">
      <span class="post-category-tag">Linear Algebra</span>
      <span class="post-separator">&bull;</span>
      <span class="post-date-tag">July 15, 2026</span>
    </div>
    <h1 class="post-full-title">Singular value decomposition</h1>
    <p class="post-lead-intro">Generalizing diagonalizations to any matrix and decomposing linear mappings geometrically.</p>
  </header>

  <div class="post-body-content">
    <p>
      Reconstructing any rectangular or square matrix into orthogonal and diagonal components, representing the ultimate generalization of the Spectral Theorem.
    </p>

    <hr style="margin: 2rem 0; border: 0; border-top: 1px solid rgba(170,170,170,0.15);">

    <h2>1. The Singular Value Decomposition (SVD)</h2>
    <p>
      Every real $m \times n$ matrix $A$ can be factored into:
      $$A = U \Sigma V^T$$
    </p>
    <p>
      Where:
    </p>
    <ul>
      <li><strong>$U$:</strong> An $m \times m$ orthogonal matrix ($U^T U = I$) whose columns are the <strong>left singular vectors</strong> of $A$ (eigenvectors of $A A^T$).</li>
      <li><strong>$\Sigma$:</strong> An $m \times n$ diagonal-like matrix containing the non-negative <strong>singular values</strong> $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$ on the diagonal, sorted in descending order.</li>
      <li><strong>$V$:</strong> An $n \times n$ orthogonal matrix ($V^T V = I$) whose columns are the <strong>right singular vectors</strong> of $A$ (eigenvectors of $A^T A$).</li>
    </ul>

    <hr style="margin: 2rem 0; border: 0; border-top: 1px solid rgba(170,170,170,0.15);">

    <h2>2. Geometric Interpretation</h2>
    <p>
      The SVD shows that any linear transformation can be decomposed into three simple geometric steps:
    </p>
    <ol>
      <li><strong>Rotation/Reflection</strong> in the domain space via $V^T$.</li>
      <li><strong>Scaling</strong> along the coordinate axes via $\Sigma$.</li>
      <li><strong>Rotation/Reflection</strong> in the codomain space via $U$.</li>
    </ol>

    <hr style="margin: 2rem 0; border: 0; border-top: 1px solid rgba(170,170,170,0.15);">

    <h2>3. Connection to Symmetric Matrices</h2>
    <p>
      The SVD of $A$ is deeply connected to the spectral decomposition of symmetric matrices:
      $$A^T A = (V \Sigma^T U^T)(U \Sigma V^T) = V (\Sigma^T \Sigma) V^T$$
      $$A A^T = (U \Sigma V^T)(V \Sigma^T U^T) = U (\Sigma \Sigma^T) U^T$$
    </p>
    <p>
      Thus, the singular values $\sigma_i$ are the square roots of the eigenvalues of the positive semidefinite symmetric matrix $A^T A$ (or $A A^T$).
    </p>
  </div>
</article>
