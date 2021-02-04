---
layout: page
title: Lecture 9
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script> 

Complementation of a variable corresponds to switching the two arrows in the ROBDD.

We can use the idea of equivalent ROBDDs to show equivalence of different circuits.    
Observe that given an ROBDD, we can create an equivalent circuit by replacing each node with a multiplexer. So, a $$2\times 1$$ multiplexer is a universal operation as well, it can be used to synthesize any logic. So if the cost of each multiplexer is $$c$$, the total cost to implement the system is just $$c$$ times the number of nodes. What is the total time for it to run? We just need to consider the longest path from the leaves to the top multiplexer. This can bounded above by the number of variables involved.

The final representation we discuss is the _Reed Muller Representation_. We have already seen Shannon's decomposition

$$f(x_1,\ldots,x_n) = x_i\cdot f(x_1,\ldots,x_i=1,\ldots,x_n)\oplus \overline{x_i}\cdotf(x_1,\ldots,x_i=1,\ldots,x_n).$$

Consider the _positive Davio decomposition_

$$f(x_1,\ldots,x_n) = \cdotf(x_1,\ldots,x_i=0,\ldots,x_n)\oplus x_i\cdot\left(f(x_1,\ldots,x_i=1,\ldots,x_n)\oplus\cdotf(x_1,\ldots,x_i=0,\ldots,x_n)\right)$$

and the _negative Davio decomposition_

$$f(x_1,\ldots,x_n) = \cdotf(x_1,\ldots,x_i=1,\ldots,x_n)\oplus \overline{x_i}\cdot\left( f(x_1,\ldots,x_i=1,\ldots,x_n)\oplus\cdotf(x_1,\ldots,x_i=0,\ldots,x_n)\right).$$

Note that there's no $$\overline{x_i}$$ literal in the former and no $$x_i$$ literal in latter. We can extend this to the general Reed Muller representation.