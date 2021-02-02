---
layout: page
title: Lecture 8 - 
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script> 

There are a couple of good variable orderings: fan-in heuristic, weight heuristic, variable swap, window permutation, sifting. The first two are "static orderings" whereas the last three are "dynamic orderings".

Finding the optimal variable ordering is NP-hard. Some functions (such as the multiplier) have exponential BDD size for all orders. Most functions do have reasonable-size ROBDDs however. Heuristic ordering methods are satisfactory for our purposes. We typically use dynamic ordering based on variable sifting. We also sometimes use application-specific heuristics such as DFS-based ordering for combinational circuits.

A restriction of a function $$f$$ to $$x=d$$, denoted $$f_{x=d}$$, where $$x\in\mathsf{Vars}(F)$$ and $$d\in\{0,1\}$$ is equal to $$f$$ after assigning $$x=d$$.

If $$v_1,v_2$$ are leaves, $$f_1\circ f_2$$ is a leaf node with value $$\operatorname{val}(v_1)\circ\operatorname{val}(v_2)$$.