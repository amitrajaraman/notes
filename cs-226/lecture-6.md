---
layout: page
title: Lecture 6 - Simplification
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script> 

De Morgan's Laws imply that $$+$$ can be expressed in terms of $$\sim$$ and $$\cdot$$ and $$\cdot$$ can be expressed in terms of $$+$$ and $$\sim$$. So, it suffices to have $$\sim$$ and $$+$$ or $$\cdot$$.

In fact, any operator can be expressed in terms of NAND.

* $$\bar{a} = \overline{a\cdot a}$$.
* $$a\cdot b = \overline{\overline{a\cdot b}}$$.
* $$a+b = \overline{\overline{a}\cdot\overline{b}}.$$

Similarly, any operator can be expressed in terms of NOR. For example,

$$a\cdot b+c\cdot d = (a \operatorname{NAND} b)\operatorname{NAND}(c\operatorname{NAND} d).$$

Even in general, if the expression is given as a sum of products, just change every operator to a NAND.