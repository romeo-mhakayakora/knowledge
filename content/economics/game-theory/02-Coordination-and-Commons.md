---
title: Coordination Games and Tragedy of the Commons
---

# Module 02: Coordination Games and Tragedy of the Commons (Lectures 7–10)

This module explores scenarios with multiple pure equilibria (Coordination Games) and situations where public goods are overexploited (Tragedy of the Commons).

---

## 1. Coordination Games (Lecture 7)

In a **Coordination Game**, players benefit from selecting the same actions. They must align their strategies to achieve positive outcomes.

### Battle of the Sexes (Lecture 8)
A couple wants to go out. Player 1 (Row) prefers Opera ($O$); Player 2 (Col) prefers Football ($F$). Both prefer going together over going alone.

| Player 1 \ Player 2 | Opera ($O$) | Football ($F$) |
| :--- | :---: | :---: |
| **Opera ($O$)** | $(2, 1)$ | $(0, 0)$ |
| **Football ($F$)** | $(0, 0)$ | $(1, 2)$ |

*   **Pure Strategy Nash Equilibria:** $(O, O)$ and $(F, F)$.
*   This represents a coordination dilemma: there are multiple equilibria, and they differ on which player receives the higher payoff.

---

## 2. Tragedy of the Commons (Lectures 9–10)

The **Tragedy of the Commons** models the overexploitation of shared resources (such as pastures, fisheries, or shared network bandwidth) when individuals act in their own self-interest.

### The $N$-Player Mathematical Model
Let there be $N$ players sharing a common resource.
Each player $i$ chooses an effort level (e.g. number of cattle to graze) $x_i \ge 0$.
The total effort is:
$$X = \sum_{j=1}^N x_j$$

The marginal value of the common resource decreases as total effort increases. Let the value per unit of effort be:
$$v(X) = A - X \quad (\text{where } A > 0)$$
Each unit of effort costs $c$ to maintain, where $A > c > 0$.

Player $i$'s payoff function is:
$$u_i(x_i, x_{-i}) = x_i \cdot v(X) - c \cdot x_i = x_i (A - x_i - \sum_{j \ne i} x_j) - c \cdot x_i$$

---

### Solving for the Nash Equilibrium
To find player $i$'s best response, we take the partial derivative of $u_i$ with respect to $x_i$ and set it to 0:
$$\frac{\partial u_i}{\partial x_i} = A - 2x_i - \sum_{j \ne i} x_j - c = 0$$

Assuming symmetric players in equilibrium ($x_1^* = x_2^* = \cdots = x_N^* = x^*$), total effort is $X^* = N x^*$. The best-response equation simplifies to:
$$A - 2x^* - (N-1)x^* - c = 0 \implies A - (N+1)x^* - c = 0$$
Solving for $x^*$:
$$x^* = \frac{A - c}{N + 1}$$

The total equilibrium effort is:
$$X_{\text{eq}}^* = N x^* = \frac{N(A - c)}{N + 1}$$

---

### Comparison with Social Optimum
To maximize total welfare (social utility), we maximize the sum of all payoffs:
$$\max_X U(X) = \sum_{i=1}^N u_i = X(A - X) - cX$$

Taking the derivative with respect to $X$ and setting it to 0:
$$\frac{d U}{d X} = A - 2X - c = 0 \implies X_{\text{opt}}^* = \frac{A - c}{2}$$

Comparing the two:
$$\text{For } N > 1, \quad X_{\text{eq}}^* = \frac{N}{N+1}(A-c) > \frac{1}{2}(A-c) = X_{\text{opt}}^*$$

> **Conclusion:** The Nash equilibrium effort level $X_{\text{eq}}^*$ is strictly greater than the socially optimal level $X_{\text{opt}}^*$. As $N \to \infty$, $X_{\text{eq}}^* \to A-c$, reducing the value of the common resource to zero. This is the **Tragedy of the Commons**.
