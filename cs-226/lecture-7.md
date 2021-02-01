---
layout: page
title: Lecture 7 - Logic Representation
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script> 


It is often helpful to specify Boolean functions in some standard form. The usual forms are:
* Truth table
* Sum of minterms (SOM)
* Product of maxterms (POM)
* Binary Decision Diagram (BDD)
* Reed-Muller Representation

We want to be able to compare boolean functions. Truth tables easily allow us to check for equality, but they take a lot of space and consequently, comparison may take a long time as well.     
If an expression is of the form $$a_1\cdot a_2\cdot \cdots \cdot a_n$$, it is called a _product term_. If it is of the form $$a_1 + a_2 + \cdots + a_n$$, it is called a _sum term_.    
A _minterm_ is a product term with every variable present in either true or complemented form. For $$n$$ variables, there are $$2^n$$ possible minterms. The canonical sum of minterms representation shows those minterms that are true.     
Similarly, a _maxterm_ is a sum term with every variable present in either true or complemented form. For $$n$ variables, there are $$2^n$$ possible maxterms. The canonical representation involves taking the dual of the sum of minterms to give the complement of the function as a product of maxterms.    
We usually use $$m$$ to denote a minterm and $$M$$ to denote a maxterm.

Neither of the canonical representations are scalable. We use _Shannon's expansion_. Given a function $$f$$, we can write

$$f(x_1,\ldots,x_n) = x_i\cdot f(x_1,\ldots,x_i=1,\ldots,x_n) + \overline{x_i}\cdot f(x_1,\ldots,x_i=0,\ldots,x_n) $$

The two terms on the right are denoted $$f_{x_i}$$ and $$f_{\overline{x_i}}$$ and called _cofactors_. Note that they are orthogonal to each other. This means that we can write them as $$x_i f_{x_i} \oplus \overline{x_i} f_{x_i}$$.    
We can represent it graphically. Given a node $$x_i$$, we have one edge to a node representing how it evaluates if $$x_i=1$$ and another edge representing how it evaluates if $$x_i=0$$. We can recurse on the children to get a binary tree. This is called the _Binary Decision Tree_ representation. We follow a particular path down the tree and at the leaf, we have the value of the function for that choice of variables. This is just a replica of the truth table, however it requires even more $$2^n$$ entries (it has $$2^n - 1$$ internal nodes in addition to the $$2^n$$ leaves).    
First, to reduce the number of leaves, we can delete all the leaves and replace them with just $$0$$ or $$1$$, thus forming a directed acyclic graph. This gives close to $$2^n$$ nodes overall, so we are getting close to at least the truth table representation.    
To make it even more compact, we can collapse isomorphic subgraphs to a single one, adding new edges wherever required.    
Now, if both the $$0$$ and $$1$$ edges from a node go to the same node, we can remove this redundant node and take it directly to the lower node.    
This has a very low number of nodes compared to any of the canonical representations we have seen thus far. This is known as the _Reduced Ordered Binary Decision Diagram_ representation.