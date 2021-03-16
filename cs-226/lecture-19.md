---
layout: page
title: Lecture 19
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

A sequential adder can be modelled using a state machine $$M = (I,O,S,S_0,\delta,\lambda)$$. In the two-bit case,

* $$I = \{00,01,10,11\}$$ is the set of input symbols,
* $$O = \{0,1\}$$ is the set of output symbols,
* $$S = \{0,1\}$$ is the set of states,
* $$S_0 = \{0\}$$ is the initial state,
* $$\delta:S\times I\to S$$ is the state transition function, and
* $$\lambda: S\times I\to O$$ is the output function.

$$\delta$$ can explicitly be given by

$$\{(0,00)\mapsto 0, (0,01)\mapsto 0, (0,11)\mapsto 1, (0,10)\mapsto 0, (1,00)\mapsto 0, (1,01)\mapsto 1, (1,11)\mapsto 1, (1,10)\mapsto 1\}.$$

We can use K-map to get the reduced expression

$$\delta(s,a,b) = a\cdot b + s\cdot a + s\cdot b.$$

On the other hand, $$\lambda$$ can be given as

$$\{(0,00)\mapsto 0, (0,01)\mapsto 1, (0,11)\mapsto 0, (0,10)\mapsto 1, (1,00)\mapsto 1, (1,01)\mapsto 0, (1,11)\mapsto 1, (1,10)\mapsto 0\}.$$

That is,

$$\lambda(s,a,b) = \overline{s}\overline{a}b + \overline{s}a\overline{b} + s\overline{a}\overline{b} + sab = s \oplus a \oplus b.$$