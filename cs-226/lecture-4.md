---
layout: page
title: Lecture 4 - 
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

Now, we generate the logical expression as a disjunction of conjunctions (of the terms which evaluate to true). Replace these operators by logic gates and then replace these logic gates with an equivalent switching circuit.

_Enabling_ permits an input signal to pass through to an output. _Disabling_ blocks an input signal from passing to the output and replacing it with a fixed value.

_Decoding_ converts an $$n$$-bit input to $$m$$-bit output (where $$n\leq m\leq 2^n$$). Circuits that perform decoding are called _decoders_ or $$n$$ to $$m$$ line decoders.

Similarly, _encoding_ converts an $$m$$-bit input to $$n$$-bit output (where $$m\leq 2^n$$). Circuits that perform encoding are called _encoders_.

A _decimal to BCD converter_ (BCD is Binary Coded Decimal) takes $$10$$ bits of input (corresponding to the decimal digits $$0$$ through $$9$$) and outputs $$4$$ bits. The corresponding eqations are

$$A_3 = D_8 + D_9$$
$$A_2 = D_4 + D_5 + D_6 + D_7$$
$$A_1 = D_2 + D_3 + D_6 + D_7$$
$$A_0 = D_1 + D_3 + D_5 + D_7 + D_9$$

Selecting data is an important function to be performed. The input is some set of information and there is a single output. Further, there is a set of control lines for making this selection. Selection circuits are called _multiplexers_.    
More concretely, there are $$n$$ control inputs for selection and at most $$2^n$$ pieces of information. For example, for $$n=1$$, we might have

$$Y = I_0\cdot\overline{S} + I_1\cdot S$$

This requires one inverter (not-gate), two 2-input and-gates, and one 2-input or-gate.

Now, we need to _optimize_ logic functions in general. For example, one might have

$$F = \overline{X}\cdot\overline{Y}\cdot Z + X\cdot\overline{Y}\cdot\overline{Z} + X\cdot\overline{Y}\cdot Z + X\cdot Y\cdot\overline{Z} X\cdot Y\cdot Z$$

but this is equivalent to

$$F = X + \overline{Y}\cdot Z.$$

There are various optimization parameters:
* Area - Number of switches/gates
* Performance (delay) - Number of switches in series
* Power - Number of switches
* Testability - Level of interconnectedness of network
* Security
* Intelligence

