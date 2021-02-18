---
layout: page
title: Lecture 14
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

A _redundant prime implicant_ is one where every minterm is covered by an _essential_ prime implicant. A prime implicant that is neither redundant nor essential is called a _selective prime implicant_. Selective prime implicants always occur in pairs.

If we want to construct the minimum sum of pairs with prime implicants only,
* Use all the essential prime implicants.
* Use no redundant prime implicant.
* Choose the cheaper selective prime implicants.

We want to minimize the number of EPIs and (selected) SPIs. Simultaneously, we want to minimize the number of literals in the selected SPIs. To identify essential prime implicants,
* Find all prime implicants
* From prime implicant SOP, remove a particular PI.
* Apply the consensus theorem on the remaining SOP.
* If the remove PI is generated, it is either an RPI or SPI. Otherwise, it is an EPI.

So the overall algorithm is
* Find all prime implicants
* Include all the EPIs in the MSOP
* Find the set of uncovered minterms. The current SOP is minimum if this set is empty.
* Otherwise, for a minterm in it, include the largest PI from the remaining PIs. Repeat the previous step.

If we have a five variable function, we can draw it in another dimension, one corresponding to a variable being $$0$$ and the other corresponding to variable $$1$$. If we have six variables, we can extend the same idea as before. Beyond six variables becomes very difficult to visualize.

If for some inputs we don't care, then we can optionally set them as $$0$$ or $$1$$ depending on what would be more beneficial for us.

To get a POS expression, you can try grouping the 0s instead of 1s.