---
layout: page
title: Lecture 10
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script> 

Generalizing the Davio decompositions, we get the Reed Muller decomposition. For two variables for example, we get

$$f = f_{\overline{x_i},\overline{x_j}} \oplus x_j (f_{\overline{x_i},x_j} \oplus f_{\overline{x_i},\overline{x_j}}) \oplus x_i (f_{\overline{x_i},\overline{x_j}} \oplus x_j (f_{x_i,\overline{x_j}} \oplus f_{x_i,\overline{x_j}})) \oplus (f_{\overline{x_i},\overline{x_j}} \oplus x_j (f_{\overline{x_i},x_j} \oplus f_{\overline{x_i},\overline{x_j}}). $$

So it is something like

$$f(x_1,\ldots,x_i,\ldots,x_n) = (a_0) \oplus (a_1x_1) \oplus (a_2x_2)\oplus\cdots \oplus (a_r x_1 x_2)\oplus (a_p x_1x_2x_3)\oplus\cdots\oplus (a_m x_1x_2\cdots x_n)$$

for some constants $$(a_i)$$. Every variable is present uncomplemented and we only use ANDs and XORs. If we wanted to build a circuit of this, we could have it in two levels - one level containing all the ANDs and another level containing a XOR of all the terms.

If we have a function $$f$$, how do we generate the above canonical representation? Just find the Davio decompositions and recurse on the restricted functions.

It is also called a _disjoint sum of products_. While the circuit with the NANDs is almost always smaller than this circuit, the current representation is very convenient, especially for testability. There is a constant number of test vectors to test a particular circuit.

There is one more way to represent a function - an and inverter graph. This is a non-canonical representation. An AIG is a boolean network with two types of nodes: two input ANDs and NOTs (inverters). This is constructed from the netlist available from technology independent logic synthesis.

The size of an AIG is measured as the number of ANDs. The depth of an AIG is the number of ANDs on the longest path from a primary input to a primary output. The inverters are usually ignored when counting nodes and levels.