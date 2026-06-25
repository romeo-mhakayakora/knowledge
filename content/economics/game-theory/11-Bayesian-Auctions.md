---
title: Auctions as Bayesian Games
---

# Module 11: Auctions as Bayesian Games (Lectures 39–44)

This module models **Auctions** as Bayesian games of incomplete information, deriving optimal bidding strategies and introducing the Revenue Equivalence Theorem.

---

## 1. Auction Setup as a Bayesian Game (Lecture 39)

Let there be $n$ bidders.
*   **Types:** Each bidder $i$ has a private valuation $v_i \in [0, \bar{v}]$. We assume valuations are Independent and Identically Distributed (i.i.d.) according to a Cumulative Distribution Function $F(v)$.
*   **Actions:** Bidders submit bids $b_i \ge 0$.
*   **Utility:** For a bidder who wins the item:
    *   First-Price Auction: $u_i = v_i - b_i$
    *   Second-Price Auction: $u_i = v_i - \max_{j \ne i} b_j$
    *   Losers get $0$ utility.

---

## 2. Sealed-Bid First-Price Auction BNE (Lectures 40–41)

In a First-Price auction, bidding your true value ($b_i = v_i$) yields a payoff of 0. Bidders must shade their bids ($b_i < v_i$) to obtain positive utility.

### Derivation for Uniform Valuations $v_i \sim U[0, 1]$
Suppose there are $n$ bidders. We look for a symmetric, increasing linear bidding strategy:
$$b(v) = a \cdot v \quad (\text{where } a \in (0,1))$$

Suppose bidder 1 has valuation $v_1$ and bids $b_1$. They win if their bid is higher than all other bids $b_j = b(v_j) = a \cdot v_j$:
$$\text{Win Probability} = P(b_1 > a \cdot v_j \ \forall j \ne 1) = P\left(v_j < \frac{b_1}{a} \ \forall j \ne 1\right)$$
Since valuations are i.i.d. $U[0, 1]$:
$$P\left(v_j < \frac{b_1}{a}\right) = \frac{b_1}{a}$$
$$\text{Win Probability} = \left(\frac{b_1}{a}\right)^{n-1}$$

Bidder 1 maximizes expected payoff:
$$\max_{b_1} \ E[u_1] = (v_1 - b_1) \cdot \left(\frac{b_1}{a}\right)^{n-1} = \frac{1}{a^{n-1}} (v_1 b_1^{n-1} - b_1^n)$$

Take the derivative with respect to $b_1$ and set it to 0:
$$\frac{d E[u_1]}{d b_1} = (n-1)v_1 b_1^{n-2} - n b_1^{n-1} = 0$$
$$(n-1)v_1 = n b_1 \implies b_1 = \frac{n-1}{n} v_1$$

By symmetry, the equilibrium bidding strategy for all bidders is:
$$b_i^*(v_i) = \frac{n-1}{n} v_i$$

> **Takeaway:** Under uniform valuations, bidders shade their bids by a factor of $\frac{n-1}{n}$. As the number of competitors $n \to \infty$, the bid approaches the true valuation $v_i$ due to intense competition.

---

## 3. Sealed-Bid Second-Price Auction BNE (Lectures 42–43)

In a Second-Price (Vickrey) auction, bidding your true valuation is a **weakly dominant strategy**, regardless of the valuation distribution $F(v)$ or number of bidders $n$.

Let $B^* = \max_{j \ne i} b_j$ be the highest bid submitted by other players. Player $i$ bids $b_i$:
*   If $b_i > B^*$, player $i$ wins and gets utility $v_i - B^*$.
*   If $b_i < B^*$, player $i$ loses and gets utility $0$.

### Case 1: Bid $b_i = v_i$
*   If $v_i > B^*$, you win and get $v_i - B^* > 0$.
*   If $v_i < B^*$, you lose and get $0$.

### Case 2: Shade your bid ($b_i < v_i$)
*   If $B^* < b_i < v_i$, you still win and get $v_i - B^*$.
*   If $b_i < B^* < v_i$, you now **lose** (getting 0), whereas bidding $v_i$ would have won you a positive utility $v_i - B^*$. Shading can only hurt you.

### Case 3: Overbid ($b_i > v_i$)
*   If $v_i < b_i < B^*$, you still lose and get $0$.
*   If $v_i < B^* < b_i$, you now **win** but pay $B^*$, getting negative utility $v_i - B^* < 0$. Overbidding can only hurt you.

---

## 4. The Revenue Equivalence Theorem (RET)

> **Theorem:** For $n$ risk-neutral bidders with private valuations drawn i.i.d. from a strictly increasing cumulative distribution $F(v)$, the expected revenue of the seller is **identical** across the four standard auction formats (English, Dutch, First-Price, Second-Price).

---

## 5. All-Pay Auctions (Lecture 44)

In an **All-Pay Auction**, the highest bidder wins the item, but **every bidder** must pay their submitted bid, regardless of whether they win.
*   **Applications:** Political lobbying, R&D races, job promotions (effort spent is not returned).
*   In equilibrium, bidding is highly conservative to avoid loss, and strategies involve mixed randomization or heavy bid-shading.
