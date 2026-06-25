---
title: Stackelberg Leadership Model
---

# Module 09: Stackelberg Leadership Model (Lectures 31–32)

This module analyzes the **Stackelberg Duopoly Model**, a sequential quantity-setting game where a market Leader moves first, followed by a Follower.

---

## 1. Model Setup

We use the same parameters as the Cournot Duopoly Model:
*   **Inverse Demand:** $P(Q) = a - Q = a - (q_1 + q_2)$ (where $a > c > 0$).
*   **Marginal Cost:** Constant marginal cost $c$ for both firms.
*   **Sequential Order:**
    1.  **Firm 1 (Leader)** chooses quantity $q_1 \ge 0$ first.
    2.  **Firm 2 (Follower)** observes $q_1$ and then chooses $q_2 \ge 0$.

---

## 2. Solving using Backward Induction

### Step 1: Solve the Follower's Problem
The Follower (Firm 2) observes $q_1$ and maximizes its profit:
$$\max_{q_2 \ge 0} \ \pi_2(q_1, q_2) = (a - q_1 - q_2)q_2 - c q_2 = (a - c - q_1)q_2 - q_2^2$$

Taking the first-order condition with respect to $q_2$:
$$\frac{\partial \pi_2}{\partial q_2} = a - c - q_1 - 2q_2 = 0 \implies R_2(q_1) = \frac{a - c - q_1}{2}$$

This is the Follower's reaction function, exactly as in the Cournot model.

---

### Step 2: Solve the Leader's Problem
Unlike in Cournot, the Leader (Firm 1) knows the Follower's reaction function $R_2(q_1)$ and substitutes it directly into its own profit function before optimizing:
$$\max_{q_1 \ge 0} \ \pi_1(q_1, R_2(q_1)) = (a - q_1 - q_2)q_1 - c q_1$$
Substitute $q_2 = \frac{a - c - q_1}{2}$:
$$\pi_1 = \left(a - q_1 - \frac{a - c - q_1}{2}\right)q_1 - c q_1$$
$$\pi_1 = \left(\frac{2a - 2q_1 - a + c + q_1}{2}\right)q_1 - c q_1 = \left(\frac{a - c - q_1}{2}\right)q_1$$
$$\pi_1 = \frac{(a - c)q_1 - q_1^2}{2}$$

Now, take the derivative of $\pi_1$ with respect to $q_1$ and set it to 0:
$$\frac{d \pi_1}{d q_1} = \frac{a - c - 2q_1}{2} = 0 \implies q_1^* = \frac{a - c}{2}$$

---

### Step 3: Solve for the Follower's Equilibrium Quantity
Substitute the Leader's quantity $q_1^*$ back into the Follower's reaction function:
$$q_2^* = R_2(q_1^*) = \frac{a - c - \left(\frac{a - c}{2}\right)}{2} = \frac{a - c}{4}$$

---

## 3. Equilibrium Payoffs and Outcomes

*   **Total Output:**
    $$Q^* = q_1^* + q_2^* = \frac{a - c}{2} + \frac{a - c}{4} = \frac{3(a - c)}{4}$$
*   **Market Price:**
    $$P^* = a - Q^* = a - \frac{3(a - c)}{4} = \frac{a + 3c}{4}$$
*   **Leader Profit ($\pi_1^*$):**
    $$\pi_1^* = (P^* - c)q_1^* = \left(\frac{a - c}{4}\right)\left(\frac{a - c}{2}\right) = \frac{(a - c)^2}{8}$$
*   **Follower Profit ($\pi_2^*$):**
    $$\pi_2^* = (P^* - c)q_2^* = \left(\frac{a - c}{4}\right)\left(\frac{a - c}{4}\right) = \frac{(a - c)^2}{16}$$

---

## 4. Comparison: Cournot vs. Stackelberg

| Variable | Cournot (Simultaneous) | Stackelberg (Sequential) |
| :--- | :---: | :---: |
| **Leader Quantity ($q_1$)** | $\frac{a-c}{3} \approx 0.33(a-c)$ | $\frac{a-c}{2} = 0.50(a-c)$ |
| **Follower Quantity ($q_2$)** | $\frac{a-c}{3} \approx 0.33(a-c)$ | $\frac{a-c}{4} = 0.25(a-c)$ |
| **Total Quantity ($Q$)** | $\frac{2(a-c)}{3} \approx 0.67(a-c)$ | $\frac{3(a-c)}{4} = 0.75(a-c)$ |
| **Price ($P$)** | $\frac{a+2c}{3}$ | $\frac{a+3c}{4}$ (Lower price) |
| **Leader Profit ($\pi_1$)** | $\frac{(a-c)^2}{9} \approx 0.11(a-c)^2$ | $\frac{(a-c)^2}{8} \approx 0.125(a-c)^2$ |
| **Follower Profit ($\pi_2$)** | $\frac{(a-c)^2}{9} \approx 0.11(a-c)^2$ | $\frac{(a-c)^2}{16} \approx 0.06(a-c)^2$ |

> **First-Mover Advantage:** By choosing first, the Leader commits to a high quantity, forcing the Follower to scale back production. The Leader's profit increases while the Follower's profit decreases relative to the Cournot benchmark.
