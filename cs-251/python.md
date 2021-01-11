---
layout: page
title: Python
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

## Basic Python

Python has a huge range of uses: web development (django, flask, twisted), data science (numpy, pandas, matplotlib), and ML, AI (Tensorflow, Pytorch, Keras).

Python is popular primarily because it has a massive number of libraries; you don't need to write basic code since it's probably already been implemented by someone. ([Relevant](https://xkcd.com/353/))

Python is an *interpreted* language, unlike C++, which is a *compiled* language.

In relation to syntax, the following program in C++:

	int collatz(int n){
		while(n>1){
			cout << n << ' ';
			if(n%2){
				n = 3*n+1; //n is odd
			}
			else{
				n = n/2;
			}
		}
		cout << "1" << endl;
	}

is equivalent to the following in Python:

	def collatz(n):
		while n>1:
			print(n, end=' ')
			if n%2:
				n = 3*n+1 #n is odd
			else:
				n = n/2
		print(1)

Note that we use indentation (instead of ```{}```), ```#``` for comments (instead of ```//```), and ```:``` when beginning a loop or function definition. We use ```//``` for division to return an integer (otherwise, it will return a double).    
We also explicitly mention ```end=' '``` to keep a space after the statement is printed (instead of the default newline ```\n```).

Unlike C++ where we have a ```main``` function, in Python we just write the main code normally and call functions whenever necessary.

If we want to take input from the user in Python, say an integer which we store in ```n```, we can do
	
	n = int(input('Enter n: '))

It first prints ```Enter n: ``` and waits for the user to give input. The ```int()``` converts the input from a string to an integer.

If we want to execute a program ```example.py```, we just do ```python example.py```.    
If we want enter the "Python shell", we can just do ```python``` in the terminal. If we then want to run ```example.py```, we can do ```exec(open('example.py').read())```. This loads the program into the shell and then executes it. In this case, we remain in the Python shell even after running the program. Note that similar to Bash or MATLAB, we can write some commands directly in the Python shell, such as ```2+3```.

A complete working example can be seen in [example.py](./example.py).

### Interpretation v. Compilation

A highly simplified version of what happens with a compiled language is:

* Syntax analysis: It verifies if the program is well-formed.
* Semantic analysis: It verifies slightly more stuff; checks for type errors for example.
* Optimizations: Attempts to make the program be made more efficient (both in terms of time and space).
* Code generation: Converts the program to an equivalent x86-64 program, which we see as ```a.out```.
* The processor runs the program and we see the answer.

On the other hand, what a Python interpreter does is:

* Syntax analysis: It verifies if the program is well-formed.
* Bytecode Generation: It generates something called a "bytecode", which runs on a simulated system -- a Virtual Machine (VM).
* Bytecode Optimizer: Optimizes the bytecode (both in terms of time and space).
* The bytecode runs on the VM simulator running on our system and we see the answer.

How come we don't check for type errors in Python? The reason for this is that Python does *dynamic type checking*. The reader might have noticed that we did not mention the type of any variable in the program given above. (This is the reason we did ```n//2``` above, otherwise the type of ```n``` would change to double!). Consider the following program:

	def returntype(n):
		if n<0:
			return "The argument is negative."
		else:
			return n
	arg = int(input("Type a number: "))
	print(4+returntype(n))

The type of variable returned by a function can be anything and is not fixed beforehand. However, the above code will generate an error at runtime because we are adding an integer to a string.

We typically use "static" to mean at compile time and "dynamic" to mean at run time. Thus, we say that Python has dynamic type checking.

### Bytecode and Garbage Collection

We can view the bytecode of a code by adding ```import dis``` at the beginning of the program and using the function ```dis.dis()``` at an appropriate point (See [this program](./collatzBytecode.py)).

The bytecode is essentially an explicit set of instructions telling the system what to do.

	7        28 LOAD_CONST               5 (3)
             30 LOAD_FAST                0 (n)
             32 BINARY_MULTIPLY
             34 LOAD_CONST               1 (1)
             36 BINARY_ADD
             38 STORE_FAST               0 (n)
             40 JUMP_ABSOLUTE            0

For example, in the above part of the bytecode, we load, multiply, and add to get ```3*n+1``` and store the result in ```n```. The dynamic type checking we mentioned earlier is actually inbuilt in the ```BINARY_MULTIPLY``` and ```BINARY_ADD``` functions! 

In C++, memory is allocated in the stack and the heap and if we wish to free up data on the heap, we must manually call ```delete``` or something similar. As a consequence, memory leaks tend to be a frequent occurrence (assuming, of course, that you are an incompetent programmer like the author).    
Python on the other hand has automated garbage collection; you don't have to manually delete allocated memory. If the program runs out of memory, it calls garbage collection and removes all the data on the heap that is not being pointed to.

## Ways to store data

Lists and tuples are some of the most useful data structures in Python and tend to be present in nearly any nontrivial program.

### Lists

* Lists are ordered.
* Lists are heterogenous (A single list can have multiple types of objects). So ```l = [int, collatz, 1, "dQw4w9WgXcQ"]``` is a valid list (Note that ```int``` is a type and ```collatz``` is a function).
* Similar to arrays in C++, list elements can be accessed by index. However, an important distinction is that we can have negative indices as well. So for example, in the above list, ```l[0]==l[-4]``` and ```l[2]==l[-2]``` (More generally, ```l[i]==l[len(l)-i]```).
* We can also get *slices* of lists. If we want a sublist containing the elements of list ```l``` from index 1 up to (and not including) 3, we can do ```l[1:3]```.
	There are also several handy shortforms in slices. For example, ```l[:n]``` is ```l[0:n]```, ```l[n:]``` is ```l[n:len(l)]```. We can also access the entire array using ```l[:]```.
	Further, we can include a *step* or *stride* in the slices. So ```l[0:8:2]``` gives the sublist which contains elements at indices 0,2,4, and 6. An important point is that the step size can also be negative; which corresponds to going backwards through the list (```l[8:0:-2]``` has the elements at indices 8,6,4, and 2 in that order).
	As an exercise, show that for a list ```l```,  ```l=l[::-1]``` reverses the list.
* Lists can be nested to an arbitrary depth. For example,

		l=[int, ["spaniard", "dragon"], [[True, 'a'], 43]]

	is a valid list.

* Lists are dynamic in size. We can add new elements to a list ```l``` using ```l.append(element)```.
	An important point is that if we have a list of size 4 and we add a new element to the list, then increase in size of the list corresponds to *4* (the size of the existing list) more elements, not 1. This is because allocation of cells is costly. It is easier to allocate a "chunk" of cells than allocate an individual cell. The size of this chunk is equal to the size of the pre-existing list.
* Lists are mutable. We can add an element ```elem``` at an index ```i``` by doing ```l.insert(2,elem)```.
		
		>>> l = [1,2,3, [True,int]]
		>>> l.insert(2,'hola')
		>>> l
		[1, 2, 'hola', 3, [True,int]]

	How is this achieved? When we do ```l.insert(2,'hola')```, 4 more cells are allocated as we mentioned earlier. The cells at indices 3 and 4 are pushed down, and the new element ```hola``` is inserted in the resulting empty cell (where the index 2 is).
	This is different from functional languages which don't entertain such side effects.

* List comprehension is an extremely powerful tool which enables us to generate new lists using old lists with close to no effort.

		>>> [x*x*x for x in [1,2,3,4,5] if x%2==1]
		[1, 27, 125]

	We iterate over each element ```x``` in the list ```[1,2,3,4,5]``` and add the expression ```x**3``` to a new list if ```x``` is odd.    
	Here, ```for x in [1,2,3,4,5]``` is known as a *generator* and ```if x%2==1``` is known as a *guard*.

	In general, list comprehension is in the form

		[expr qual1 qual2 qual3 ...]

	where each ```qual```, known as a qualifier, is either a generator or a guard.

	The order of qualifiers is the same as the order you'd write it in a for loop. For example,

		for x in l1:
			for y in l2:
				l.append(x*x+y)

	is equivalent to

		l = [x*x+y for x in l1 for y in l2]

	Quick sort can be implemented rather efficiently as follows (adding two lists is the same as appending the second to the first):

		def quicksort(l):
			if l == []:
				return []
			piv = l[0]
			l = quicksort([x for x in list[1:] if x < piv])
			u = quicksort([x for x in list[1:] if x >= piv])
			return (l + [piv] + u)

### Dictionaries

A dictionary stores objects that are identified by *keys*, such as the key of each definition in a dictionary being the word it defines. The key of the dictionary must be hashable. As strings are hashable and lists are not, we cannot have a dictionary whose keys are lists.

We can create a dictionary as
	
	dic = {"Alice": 15, "Bob": 43, "Charlie": 29}

We can define the above dictionary using list comprehension as
	
	dic = {name:num for name in ["Alice", "Bob", "Charlie"] for num in [15,43,29]}

We access the elements of a dictionary similar to how we access elements of a list (like ```dic["Alice"]```).

### Some other data structures

* Tuples are immutable containers. Immutability means that we cannot change the elements of the tuple. For example, the following is invalid:

		>>> tup = (1,0,0,2)
		>>> tup[1] = 2.7
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		TypeError: 'tuple' object does not support item assignment

	Note that the tuple ```tup``` itself can be assigned to a new tuple as ```tup = (2,3,5)```.

* Arrays (similar to those in C++) can be created as ```arr = array.array('f', (1.0,2.0))``` (we must import ```array``` for this to work). The ```'f'``` denotes that the elements in the array are all of type ```float```. Arrays are similar to lists except that they are homogenous. The advantage over lists is that they are more (space and time) efficient. (Some answers in [this StackOverflow question](https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use) might be an interesting read.)

[This article](https://dbader.org/blog/python-arrays) gives a comparison between a few data structures in Python.

* Sets are unordered collections of elements that can only have one copy of each element (as you'd expect). They can be created as

		>>> names = {'Alice', 'Bob', 'Charlie', 'Alice'}
		>>> names
		{'Alice', 'Charlie', 'Bob'}

	There is also a variant of the set known as the multiset that stores the elements along with the number of times they occur.

[This page](https://wiki.python.org/moin/TimeComplexity) gives a measure of the time complexity of various operations relating to different data structures in Python.

## Functional Programming in Python

If we write a function in some program, then we can use it in the same file as a script (standalone).

We can also use the function in another program by importing the first file. 

We can use the ```dir()``` function while in the Python shell to see all the available variables. To see the value each has, we can use ```globals()```. This is known as a *namespace*.    
The fact that most variables are flanked on either side by ```__``` represents that they are system-defined.

Most of the default functions (such as say ```print```) are there in the ```__builtins__``` variable.

This naturally gives rise to the notion of an *environment* where we do all our work.

When we call something a module, we mean that we are defining it in one program and importing and using it somewhere else. When you write a program, its name (with the extension stripped) is immediately recognized as a module so that you can import it into other programs.

When we import ```example```, it is recognized as a module object. If we now want to calculate ```collatz(43)```, where ```collatz``` is defined within ```examples.py```. So we must use ```example.collatz(43)```, not just ```collatz(43)```.

As the name implies, modules assist modularization of code.

If we change something in ```example```, then importing it again will not change anything as Python recognizes that it has already imported the module and ignores the command (which we do not desire).   
To reload the module, we must then ```import importlib``` and ```importlib.reload(example)```.

If we feel that calling ```example.collatz``` is far too tiring, then we can do ```import example as ex``` and just do ```ex.collatz```.    
Alternatively, we can do ```from example import collatz``` and just use ```collatz```. We can also import all the functions from a given by file by ```from example import *```.

Finally, the variable ```__name__``` distinguishes whether we are using a particular file as a script or a module. If we import ```example``` into another program, we see that the ```__name__``` of ```example``` is ```example``` and the name of the main program we are running is ```__main__```.

This enables us to define a ```main()``` function similar to C++. We can then decide to run the ```main()``` function depending on whether or not the ```__name__``` is equal to ```__main__```.    
This allows us to test modules separately without having a different version for whether it is being used as a module or the main program.

## Functional Programming in Python

### Higher Order Functions

Consider the functions

$$\tan(x) = \dfrac{x}{1-\dfrac{x^2}{3-\dfrac{x^2}{5-\cdots}}}$$

$$s(x) = \sqrt{x+\sqrt{x+\sqrt{x+\cdots}}}$$

$$\sin(x) = \frac{x}{1!}-x^2\cdot\left(\frac{x}{3!}-x^2\cdot\left(\frac{x}{5!}-\cdots\right)\right)$$

Is it possible to view these computations as part of some pattern? They do something like 

	f -- g -- f -- g -- ...
	|    |    |    |
	n1   m1   n2   m2

where we calculate from the right to the left. For example, in the first case, we can think of $$f$$ as division, $$g$$ as subtraction, $$n_i$$ as $$x^i$$, and $$m_i$$ as $$2i-1$$.

We can terminate the program at $$n_{k+1}$$. Can we write a function that performs the general abstract method, so we can later substitute appropriate $$f,g,n_i,$$ and $$m_i$$ for the desired result?

	def higherorder(f, g, n, m, x, k):

We now do something that the reader might not have seen before: a nested function, which helps keep track of the "level" of the tree we are currently at.

		def higherorder_helper(i):
			...
	higherorder_helper(1)

In ```higherorder_helper```, we define it recursively to compute the current level and go the next and break if $$i>k$$ The body of the function is given as:

		def higherorder_helper(i):
			if(i>k):
				return n(i)
			else:
				return f(n(i), g(m(i), higherorder_helper(i+1))

We can then define the $$\tan$$ function by

	def td(x,y):
		#td for true division
		return (x/y)
		#we do this because we cannot pass just / as an argument
	def sub(x,y):
		return x-y
	def tan(x,k):
		def n_tan(i):
			if(i==1):
				return x
			else:
				return x*x
		def m_tan(i):
			return 2*i-1
		higherorder(td, sub, n_tan, m_tan, x_k)