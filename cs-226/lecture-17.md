---
layout: page
title: Lecture 17
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

The calculation of the carries is done using prefix graphs. The effort goes into making the tree.

$$G_[i:k] = G_[i:j] + P_[i:j]G_[j-1:k] \text{ and } P_[i:k] = P_[i:j] P_[j-1:k]$$

Finally,

$$c_{i+1} = G_[i:0] + P_[i:0] c_ \text{ and } s_i = p_i \oplus c_i.$$

Kogge-Stone uses $$\log_2 n$$ logical levels and at most $$2$$ fanouts.