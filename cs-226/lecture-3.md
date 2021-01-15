---
layout: page
title: Lecture 3 - Implementation of Gates
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

Logic Design takes input, performs some operation(s), and gives output. The common binary operators encountered are the OR ($$\vee$$), AND ($$\wedge$$), and XOR ($$\oplus$$).

A truth table/operator can be written as a "sum of products" (a disjunction of conjunctions). For example,

$$X\oplus Y = \overline{X}\cdot Y + X\cdot\overline{Y}.$$

Similarly, we can represent any function with just $$\neg$$, $$\wedge$$, and $$\vee$$. Therefore, these are known as the _basic operators_.    
For a given function, truth tables are unique whereas expressions are not.    
Since there are $$2^n$$ rows in the truth table, there are $$2^{2^n}$$ possible truth tables for a given function.

So to implement say the full adder, we need to obviously figure out how to implement these basic operations first. We can do so using switches. Say for the input, logic $$0$$ corresponds to the switch being closed and logic $$1$$ corresponds to it being open. Similarly, for the output, logic $$0$$ corresponds to a light being off and logic $$1$$ corresponds to it being on.    
The NOT gate uses a switch such that logic $$1$$ corresponds to the switch being open and logic $$0$$ corresponds to it being closed.    
Switches in parallel correspond to an OR gate and switches in series correspond to an AND gate.

An electromechanical relay contains an electromagnet, a current source, and a switch that is spring-loaded that can be either normally open or closed.    
We can have one switch controlling another (either to get $$Y=X$$ or $$Y=\overline{X}$$) by arranging the electromagnets appropriately.    
As mentioned earlier, we can keep the switches in series/parallel to get AND/OR.

<!-- Later on, this was changed to electronic switching devices (electron tubes/point contact transistors). -->

Eventually, the switch was changed to a field effect transistor (FET).    
If gate potential higher than source potential, closed switch. If same potential, then open switch. So the gate switch is the "controlling" terminal.

In the trivial NOT gate, there is power dissipation, so we change to a complementary PMOS-NMOS pair. Both are never simultaneously shorted, so there is no flow from $$V_{DD}$$ to the ground and thus, no power dissipation.