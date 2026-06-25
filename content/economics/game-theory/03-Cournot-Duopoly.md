---
title: Cournot Duopoly Model
---

# Module 03: Cournot Duopoly Model (Lectures 10–11)

This module analyzes **Cournot Competition**, where two competing firms simultaneously choose output quantities of a homogeneous good. It is a foundational model of oligopoly with continuous strategy spaces.

---

## 1. Model Setup

Let there be two firms, Firm 1 and Firm 2.
*   **Strategies:** Each firm $i \in \{1, 2\}$ chooses quantity $q_i \ge 0$.
*   **Total Quantity:** $Q = q_1 + q_2$.
*   **Market Price:** Determined by the linear inverse demand function:
    $$P(Q) = \begin{cases} a - Q & \text{if } Q < a \\ 0 & \text{if } Q \ge a \end{cases}$$
    where $a > 0$.
*   **Cost Function:** Both firms face constant marginal cost $c$, where $0 < c < a$. There are no fixed costs.
    $$C(q_i) = c \cdot q_i$$

---

## 2. Firm Optimization

Each firm $i$ maximizes its profit $\pi_i$ given the quantity chosen by the competitor $q_{-i}$:
$$\pi_i(q_i, q_{-i}) = P(q_i + q_{-i}) \cdot q_i - C(q_i) = (a - q_i - q_{-i})q_i - c q_i$$

For Firm 1:
$$\max_{q_1 \ge 0} \ \pi_1(q_1, q_2) = (a - q_1 - q_2)q_1 - c q_1 = (a - c - q_2)q_1 - q_1^2$$

To find the optimal quantity, take the derivative of $\pi_1$ with respect to $q_1$ and set it to 0 (First Order Condition):
$$\frac{\partial \pi_1}{\partial q_1} = a - c - q_2 - 2q_1 = 0$$

Solving for $q_1$ gives Firm 1's **Best-Response (or Reaction) Function**:
$$R_1(q_2) = \max\left(0, \frac{a - c - q_2}{2}\right)$$

By symmetry, Firm 2's Best-Response Function is:
$$R_2(q_1) = \max\left(0, \frac{a - c - q_1}{2}\right)$$

---

## 3. Solving for the Nash Equilibrium

A Cournot Nash Equilibrium is a quantity profile $(q_1^*, q_2^*)$ where each firm plays its best response to the other:
$$q_1^* = R_1(q_2^*) \quad \text{and} \quad q_2^* = R_2(q_1^*)$$

Assuming an interior equilibrium ($q_1^*, q_2^* > 0$), we solve the system of equations:
$$q_1^* = \frac{a - c - q_2^*}{2}$$
$$q_2^* = \frac{a - c - q_1^*}{2}$$

Substitute the second equation into the first:
$$q_1^* = \frac{a - c - \left(\frac{a - c - q_1^*}{2}\right)}{2} = \frac{2(a-c) - (a-c) + q_1^*}{4} = \frac{a-c}{4} + \frac{q_1^*}{4}$$
$$q_1^* - \frac{q_1^*}{4} = \frac{a-c}{4} \implies \frac{3q_1^*}{4} = \frac{a-c}{4}$$
$$q_1^* = \frac{a - c}{3}$$

By symmetry:
$$q_2^* = \frac{a - c}{3}$$

---

## 4. Equilibrium Payoffs and Outcomes

*   **Total Output:**
    $$Q^* = q_1^* + q_2^* = \frac{2(a - c)}{3}$$
*   **Market Price:**
    $$P^* = a - Q^* = a - \frac{2(a - c)}{3} = \frac{a + 2c}{3}$$
*   **Firm Profits:**
    $$\pi_1^* = \pi_2^* = (P^* - c)q_1^* = \left(\frac{a + 2c}{3} - c\right) \left(\frac{a - c}{3}\right) = \frac{(a - c)^2}{9}$$
