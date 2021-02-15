---
layout: page
title: Lecture 12
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script> 

The parameters we care about when minimizing circuits are:
* Cost - How many switches?
* Performance/Delay - How many switches between an input-output pair?
* Power - How many switches? This is slightly different from the first point but we shall not treat the two very differently.
* Testability - How can we ensure that the hardware is correct?

MOSFET stands for Metal Oxide Semiconductor Field Effect Transistor.    
In NMOSFET, open if VGS is $$0$$ and short if VGS is high. In PMOSFET, short if VGS is $$0$$ and open if VGS is high.    
We can implement a NOT gate using one PMOSFET and one NMOSFET. The signal has to pass through one transistor.    
A NAND gate can be implemented using two PMOSFETs and two NMOSFETs. The signal has to pass through at most two transistors.

| Gate | No. of transistors (2/N-input) | Maximum no. of transistors to pass through (2/N-input) |
|------|-----------------------------------|-----------------------------------------------------------|
| NOT  | 2/-                               | 1/-                                                       |
| AND  | 6/2N+2                            | 3/N+1                                                     |
| OR   | 6/2N+2                            | 3/N+1                                                     |
| NAND | 4/2N                              | 2/N                                                       |
| NOR  | 4/2N                              | 2/N                                                       |

For a sum of minterms expression, the cost is proportional to the sum of the number of terms and the number of literals. On the other hand, the delay is proportional to sum of the number of terms and the maximum number of literals in any term.    
It is seen that if we want to minimize both the cost and the delay, we must try to minimize the number of product terms.