---
layout: page
title: Lecture 1 - Introduction
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>


Engineering is essentially _design under constraint_. We have a set of constraints such as size, weight, reliability, etc, and we want to optimize our solution under these constraints.

_Logic_ is the study of valid reasoning. We try to establish criteria to decide whether some reasoning is valid or invalid. The reasoning is valid if the statements claimed to be true do indeed follow from the previous ones.

_Propositions_ are statements that are either true or false (but not both). Opinions, interrogatives, and imperatives are not statements.    
We use operators/connectives to create a compound proposition from multiple proposition. These connectives are the negation ($$\neg$$), conjunction ($$\wedge$$), disjunction ($$\vee$$), exclusive or ($$\oplus$$), implication ($$\implies$$), and biconditional ($$\iff$$).

A number with _radix_ $$r$$ is represented b a string of digits

$$A_{n-1}A_{n-2}\ldots A_1 A_0 . A__{-1} \ldots A_{-n}$$

where $$A_i$$ represents $$r^{i}$$.

Binary is radix $$2$$, octal is radix $$8$$, decimal is radix $$10$$, and hexadecimal is radix $$16$$.

We typically use radix $$2$$. There are some special names for certain powers. In particular, $$2^{10}$$ is "kilo" (k), $$2^{20}$$ is "mega" (M), and $$2^{30}$$ is "giga" (G).     
In a fixed length binary representation, the left-most bit (called _most significant bit_ or _MSB_) is used for sign - $$0$$ for positive and $$1$$ for negative. However, this isn't very convenient because then we need to treat the two bits differently. Addition and subtraction would require different logic circuits. Overflow is difficult to detect. Therefore, in modern computers, we typically don't use signed integers.    
Most computers today use $$64$$-bit (we use $$64$$ bits to represent any number).