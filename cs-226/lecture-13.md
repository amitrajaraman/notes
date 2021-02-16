---
layout: page
title: Lecture 13
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

A minterms is also called a _$$0$$-implicant_ or _$$0$$-cube_. A $$1$$-implicant is a product with one variable eliminated It can be obtained by combining two adjacent $$0$$-cubes. For example, $$ABCD+ABC\overline{D} = ABC$$. How do we perform minimization?

* Algebraic methods using boolean algebra. This isn't really a set procedure though, alternate routes could lead to non-minimal solutions. It is not scalable at all.
* Algorithmic methods - either graphical method (K-Map) or tabular method (Q-M).

The truth table is a graphical way of manipulation. In the K-Map (Karnaugh-Map) method, for some subset of the truth table that is $$1$$, if we notice that the value is the same irrespective of the value of some variable, we can eliminate that variable.    
We represent the function as a sequence of values, where the input to adjacent cells differs by exactly one input. We then want to pair off adjacent $$1$$s, each pairing eliminates a variable from that minterm.    
How do we generate such an input sequence? For two variables, it is ordered as $$00$$, $$01$$, $$11$$, $$10$$. If we have three variables, we can repeat a similar sequence but starting at a different point in the cycle! So we would get $$000$$, $$001$$, $$011$$, $$010$$, $$110$$, $$111$$, $$101$$, $$100$$.    
Instead of eliminating just once, we can recurse to eliminate blocks of $$4$$ or in general, any power of $$2$$ at a time.

A larger cube _covers_ a smaller cube if all the minterms of the smaller cube are included in the larger cube. We then say that the smaller cube _implies_ or _subsumes_ the larger cube.    
A _prime implicant_ is an implicant that cannot grow larger by expanding into other cubes. If among the minterms subsuming a prime implicant, there is at least one minterm that is covered by only this prime implicant, then the prime implicant is called an _essential prime implicant_.