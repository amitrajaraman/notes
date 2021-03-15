---
layout: page
title: Lecture 18
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

In a _serial adder_, we use a single full adder to compute the sum, controlling the timing of the input exactly. We feed the output carry back into the adder after 8 unit time along with the next bits, computing the next bit.    
We require some temporary storage for the carry together with a clock. Suppose the clock timer is $$\tau$$. The storage element loads the value whenever the clock tick arrives, which is when the time is a multiple of $$\tau$$.