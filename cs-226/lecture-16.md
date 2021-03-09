---
layout: page
title: Lecture 16
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

So how do we create fast adders? Separate the carry chain and sum logic. A _partial full adders_ has only the sum part of a full adder.  In the carry lookahead adder, the $$C_i$$ is changed to a more global function. It is then defined by $$P_i = A_i \oplus B_i$$, $$G_i = A_i B_i$$, $$S_i = P_i \oplus C_i$$, and $$C_{i+1} = G_i + P_i C_i$$.

For a $$4$$-bit adder, the total delay comprises $$2$$-input XOR, a $$4$$-input AND, a $$4$$-input OR, and a $$2$$-input XOR. In general, there are $$2$$ $$2$$-input XORs, a $$n$$-input AND, and a $$n$$0input OR. The delay is still proportional to $$n$$! Compared to the ripple carry adder, we have reduced it by a factor of $$1/2$$, but it is still $$\mathcal{O}(n)$$.

In TTL technology, the delay is constant. It can then be implemented with just $$4$$ logic levels, so the delay is constant. Moving to CMOS technology is problematic. We trade area/power for speed. We calculate assuming the carry is $$0$$ and assuming the carry is $$1$$ and then we use a multiplexer to decide which one to use.    
So the number of levels of logic can be reduced to $$\log_2 N$$ for a $$N$$-bit adder, compared to the ripple carry adder which has $$N$$ levels. However, more gates are needed as well (around $$\log_2 N$$ as many).

We use _prefix computation_. We want to convert it into a tree structure (a divide-and-conquer algorithm?).

We precalculate the $$P_i$$ and $$G_i$$ terms (as in the CLA adder). We then calculate the carries. This part is parallelizable using prefix graphs. Finally, use a simple adder to generate the sum.