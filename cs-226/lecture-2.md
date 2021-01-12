---
layout: page
title: Lecture 2 - Binary Arithmetic
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

We as human beings prefer to use the decimal computer system, but computers find it more convenient to use the binary system.

### Binary operations on unsigned numbers

Given binary digits $$X$$ and $$Y$$, their sum is $$S = X \oplus Y$$ and the carry $$C = X \wedge Y$$ (the binary sum overall is $$CS$$).    
It would be more convenient to have a system that adds $$3$$ bits at a time, since then we can use recurrence to add some long binary numbers. So given two binary digits $$(X,Y)$$ along with a carry in $$Z$$, we get the following:

* If the carry $$Z$$ is $$0$$, then it's the same as the two-bit case.
* Otherwise, we get $$S = \neg (X \oplus Y)$$ and $$C = \neg X \vee \neg Y$$.

The above is known as a _full adder_. The two bit version is known as a _half adder_.

How do we do binary subtraction? Given $$(X,Y)$$, for computing $$X-Y$$, the difference is $$D = X \oplus Y$$ and the borrow is $$B = \neg x \wedge Y$$.

For the $$3$$-bit version,

* If the borrow $$Z$$ is $$0$$, then it's the same as the two-bit case.
* Otherwise, we get $$D = Z$$ and $$B = \neg X \vee \neg Y$$.

For multiplication, we can just do the partial products with each of the digits of the multiplier (the second term) to get $$3$$ different binary numbers, and add them up (just like how we multiply in decimal). Each individual step is given by $$X \wedge Y$$, there is no carry or anything.

### Towards signed numbers

Now this is all fine given _unsigned_ numbers, but what if we have signed numbers?

As mentioned earlier, the left-most bit (MSB) is used for sign ($$0$$ for positive and $$1$$ for negative). So

$$(+18)_{10} = (00010010)_2 \quad (-18)_{10} = (10010010)_2$$

This is equivalent to representing it on a "dial", so for example when I reach $$255$$, I roll back and hit $$0$$ again (or rather, $$-0$$). I have a balanced number of positive and negative numbers. The issues with this are those mentioned in the previous lecture, which all arise due to the sign bit being completely separate from the magnitude bits, so existing operations for unsigned numbers can't be adapted easily. Further one minor issue is that we have two representations for $$0$$, one with all $$0$$s and one with all $$0$$s except the leftmost bit.

So instead of the dial "winding around" like above, we instead use one such that the negative numbers start from the same place as the positive numbers. For example,

| $$000$$ | $$001$$ | $$010$$ | $$011$$ | $$100$$ | $$101$$ | $$110$$ | $$111$$ |
| $$0$$   | $$1$$   | $$2$$   | $$3$$   | $$-0$$  | $$-1$$  | $$-2$$  | $$-3$$  |
| $$000$$ | $$001$$ | $$010$$ | $$011$$ | $$100$$ | $$101$$ | $$110$$ | $$111$$ |
| $$0$$   | $$1$$   | $$2$$   | $$3$$   | $$-3$$  | $$-2$$  | $$-1$$  | $$-0$$  |

This is known as the $$1$$s complement system. Observe that complementing each bit of $$x$$ is just $$-x$$ in this case. The only issue that remains is that $$0$$ still has two representations.

To solve this, we introduce the $$2$$s complement system, wherein for positive $$x$$, $$-x$$ is obtained by complementing (each bit of) $$x$$ and adding $$1$$. This is also equivalent to subtracting the number from $$2^n$$. This is the preferred representation usually used.

| $$000$$ | $$001$$ | $$010$$ | $$011$$ | $$100$$ | $$101$$ | $$110$$ | $$111$$ |
| $$0$$   | $$1$$   | $$2$$   | $$3$$   | $$-4$$  | $$-3$$  | $$-2$$  | $$-1$$  |

This is basically a fixed length representation with no explicit sign bit. It is important to note that here, there is one negative number here with no positive counterpart. In this case, addition and subtraction are very easy as well. We just move along the dial. The same addition operation can be used to do the subtraction operation as well.

Converting binary to decimal is easy as well. It is given by

$$-2^{n-1}b_{n-1} + \sum_{i=0}^{n-1} 2^i b_i.$$