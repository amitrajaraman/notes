---
layout: page
title: Lecture 5 - Boolean Algebra
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

As mentioned earlier, the name of any digital designer is to minimize the number of gates used in some expression.

A _binary operator_ $$\circ$$ defined on a set $$S$$ of elements is a function from $$S\times S\to S$$, where we denote $$\circ(a,b)$$ as $$a\circ b$$.

* Commutative law: An operator $$\circ$$ on $$S$$ is _commutative_ if for any $$a,b\in S$$, $$a\circ b=b\circ a$$.

* Associative law: An operator $$\circ$$ is said to be associative if for any $$a,b,c\in S$$, $$a\circ(b\circ c)=(a\circ b)\circ c$$.

* Identity element: Given an operator $$\circ$$ on $$S$$, $$e\in S$$ is said to be an identity element if for any $$a\in S$$, $$a\circ e = e\circ a = a$$.

* Inverse: An operator $$\circ$$ is said to be closed under inverses if for every $$a\in S$$, there exists $$a^{-1}\in S$$ such that $$a\circ a^{-1} = a^{-1}\circ a = e$$.

* Distributive law: Given two operators $$\circ$$ and $$+$$, $$\circ$$ is said to be distributive over $$+$$ if for any $$a,b,c\in S$$, $$a\circ(b+c) = (a\circ b)+(a\circ c)$$.

The Boolean algebra is the $$5$$-tuple with the set of postulates $$B$$, operators $$\{+,\cdot,\sim\}$$, and the symbols $$\{0,1\}$$ in $$B$$.    
The operators $$+$$ and $$\cdot$$ are commutative and associative. The identity of $$+$$ is $$0$$ and that of $$\cdot$$ is $$1$$. $$+$$ is distributive over $$\cdot$$. The unary operator $$\sim$$ is known as the _complement_. Finally, for any $$a\in B$$, $$a+\sim a=1$$ and $$a\cdot\sim a=0$$.

Each postulate in $$B$$ contains a pair of expressions such that one can be transformed to the other by interchanging the operators $$+$$ and $$\cdot$$ and the identities $$0$$ and $$1$$. <!-- These two expressions are complements. --> This is sometimes referred to as the _duality principle_. If two expressions are equal, their duals are equal as well.     

We often drop the $$\cdot$$ and denote $$A\cdot B$$ as just $$AB$$.

So for example, $$A+(BC) = (A+B)(A+C)$$ and $$A(B+C)=(AB + AC)$$ are duals.

