---
title: Indicator Random Variables and the Fundamental Bridge
subject: probability
chapter: 05-expectation
tags:
- probability
- mathematics
date: '2026-06-18'
updated: '2026-06-19'
status: complete
difficulty: intermediate
---

# Indicator Random Variables and the Fundamental Bridge

This section covers indicator random variables and their connection to probability.

## Indicator Random Variables

An indicator random variable $I_A$ for an event $A$ is defined as:

$$I_A = \begin{cases} 1 & \text{if } A \text{ occurs} \\ 0 & \text{if } A \text{ does not occur} \end{cases}$$

## The Fundamental Bridge

The fundamental bridge connects the expected value of an indicator random variable to the probability of the corresponding event:

$$E(I_A) = P(A)$$

This relation is extremely powerful because it allows us to compute probabilities by calculating expectations and vice versa, often simplifying complex problems using linearity of expectation.
