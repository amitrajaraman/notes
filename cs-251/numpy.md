---
layout: page
title: Numpy
---

There are several libraries available for scientific computation in Python; some of the most important of these are Numpy, Scipy, Matplotlib, and Pandas. Numpy is built on Python, Scipy is built on Numpy, Matplotlib is helpful for plotting graphs, and Pandas gives some additional functionality.

### Arrays in Numpy

The basic data structure in Numpy is the ```ndarray``` (n-dimensional array). It is homogenous (all elements must be of the same type). There are individual element operations, and there are several whole array operations which can do things like change the shape of an array. Operations on integers are similarly lifted to arrays. These array operations are extremely efficient. Throughout this section, suppose that we have imported ```numpy as np```.

While Python lists have some general list information followed by all the pointers to the data, Python arrays have the general array information (such as dimension and shape) followed by the data itself in contiguous blocks (much like in C++). Each block is of a fixed size.    

Numpy arrays have similar representation to ```array.array```: some general information followed by the data in contiguous blocks.    
The *shape* of an ```ndarray``` can be accessed by ```arr.shape``` and represents the "dimensions" of the array. So the shape of ```[12]``` is ```(1,)```. Similarly, the shape of ```[[],[]]``` is ```(2,0)```.

Now consider the following sequence of commands:

	>>> narr = np.arange(1,5)
	>>> narr
	array([1, 2, 3, 4])
	>>> narr1 = narr.reshape(2,2)
	>>> narr1
	array([[1, 2],
	       [3, 4]])

If we instead try to reshape into ```(3,1)```, then as expected,

	>>> narr2 = narr.reshape(3,1)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: cannot reshape array of size 4 into shape (3,1)

An important point is that when we reshape an array, it shares its data with the original array and merely carries the general array information.

Alternatively, if we do ```narr2 = narr1.copy()```, the data in the original array is copied into the new array. This is known as a "deep copy". 

### Time Comparison between Arrays and Lists

To start off, do 

	>>> import numpy as np
	>>> from timeit import Timer
	>>> X_list = range(size_of_vec)
	>>> Y_list = range(size_of_vec) #Initializes two vectors
	>>> X = np.arange(size_of_vec)
	>>> Y = np.arange(size_of_vec) #Initializes two np arrays
	>>> 

Let us also define two functions that we shall use to compare the speed of addition between the vector and the array.

	>>> def python_add():
	...     Z = [X_list[i] + Y_list[i] for i in range(len(X_list))]
	...
	>>> def numpy_add():
	...     Z = X + Y
	...

To actually time the operation, let us create two ```Timer``` objects. The first argument is the operation we want to time and the second is the setup statement.

	>>> timer_obj1 = Timer("python_add()","from __main__ import python_add")
	>>> timer_obj2 = Timer("numpy_add()","from __main__ import numpy_add")

The ```Timer``` object has a ```timeit``` method.

	>>> for i in range(3):
	...     t1 = timer_obj1.timeit(10) #does it 10 times
	...     t2 = timer_obj2.timeit(10)
	...     print("time for pure python is: ", t1)
	...     print("time for numpy is: ", t2)
	...		print(f"Numpy was {t1 / t2:7.2f}") times faster")
	...

	>>> for i in range(3):
	...     t1 = timer_obj1.timeit(10) #does it 10 times
	...     t2 = timer_obj2.timeit(10)
	...     print("time for pure python is: ", t1)
	...     print("time for numpy is: ", t2)
	...
	time for pure python is: 0.00121212005615
	time for numpy is: 8.6784362793e-05
	time for pure python is: 0.00131702423096
	time for numpy is: 4.19616699219e-05
	time for pure python is: 0.00155520439148
	time for numpy is: 3.2901763916e-05

Note that numpy is *significantly* faster than the pure Python version. This is primarily because
* it does not have to check the type at every stage (which lists need to do).
* there is very efficient implementation of whole array operations using vector support. A bunch of array elements (usually 4 or 8) are added together in a single "SIMD" instruction. Most modern processors support this, and Numpy exploits it.

### Structured Arrays

The elements of an array are described by a class called ```dtype```.

	>>> narr1 = np.array([[1],[2],[3]])
	>>> narr1.dtype
	dtype('int64')

We can make a custom dtype to store our own custom data as follows.    
Suppose we wanted an array that stores the table


| Country | Population Density |
|:--------|:-------------------|
| Belgium | 337                |
| Germany | 233                |
| Italy   | 192                |

We can then do something like

	>>> dt = np.dtype([('country', np.unicode_, 20), ('density', 'i4')])
	>>> pop_table = np.array([
	...     ('Belgium', 337),
	...     ('Germany', 233),
	...     ('Italy', 192)],
	...     dtype=dt)
	>>> pop_table
	array([(u'Belgium', 337), (u'Germany', 233), (u'Italy', 192)],
	      dtype=[('country', '<U20'), ('density', '<i4')])

If we had directly tried to fit this data into an array, it would have tried to guess the type, giving unintended output.    
If we now want only the ```density``` fields, we can do
	
	>>> pop_table['density']
	array([337, 233, 192], dtype=int32)

### Numerical Operations on Arrays

If we have an array ```narr``` (of floats, say) and we want to add 2 to every element of the array, it is as simple as
	
	narr = narr + 2

We can create an $$n\times n$$ matrix of ones using ```np.ones((n,n))```.

If we have two arrays ```A``` and ```B```, ```A * B``` returns their element-wise product. If we want their matrix product, we use ```np.dot(A, B)```

Let us now talk about *broadcasting*, which explains how numpy did the addition we showed above.

	>>> A = np.array([[11,12,13], [21,22,23], [31,32,33]])
	>>> B = np.array([1,2,3])
	>>> print(A * B)
	[[11 24 39]
	 [21 44 69]
	 [31 64 99]]

The first array ```A``` has shape ```(3,3)``` and ```B``` has shape ```(3)```. The product is carried out as 
* First convert ```B``` to shape ```(1,3)``` by adding a wrapper. We get ```[[1,2,3]]```.
* Convert the ```(1,3)``` array to a ```(3,3)``` array by replicating it thrice to get ```[[1,2,3], [1,2,3], [1,2,3]]```.
* Now do ordinary element-wise multiplication.

Note that by a similar logic, the following code which (adds a column vector to a row vector) works

	>>> np.arange(3).reshape(3,1) + np.arange(3)
	array([[0, 1, 2],
	       [1, 2, 3],
	       [2, 3, 4]])

### Array Indexing

Simple indexing and slicing/striding are very similar to the corresponding in lists in regular Python.

Numpy arrays are powerful because we can combine multiple such indexing operations along different indices. For example,
	
	>>> y = np.arange(35).reshape(5,7)
	>>> y
	array([[ 0,  1,  2,  3,  4,  5,  6],
	       [ 7,  8,  9, 10, 11, 12, 13],
	       [14, 15, 16, 17, 18, 19, 20],
	       [21, 22, 23, 24, 25, 26, 27],
	       [28, 29, 30, 31, 32, 33, 34]])
	>>> y[1:5:2,::3]
	array([[ 7, 10, 13],
	       [21, 24, 27]])

Slices do not copy the internal array, they also produce new views of the original data.

Further, we can also have index arrays - arrays that acts as indices for another array.

	>>> x = np.arange(10,1,-1)
	>>> x
	array([10,  9,  8,  7,  6,  5,  4,  3,  2])
	>>> x[np.array([3,1,4,1])]
	array([7, 9, 6, 9])
	>>> x[np.array([[1,1],[2,3]])]
	array([[9, 9],
	       [8, 7]])

Unlike slices, this returns a copy of the array. Note that the array returned has the same dimensions as the index array.    
We can also index multi-dimensional arrays by inserting a comma between the index arrays along each dimension.

We can also use boolean masks, such as
	
	>>> y = np.arange(35).reshape(5,7)
	>>> b = (y%3 == 0)
	>>> b
	array([[ True, False, False,  True, False, False,  True],
	       [False, False,  True, False, False,  True, False],
       [False,  True, False, False,  True, False, False],
       [ True, False, False,  True, False, False,  True],
       [False, False,  True, False, False,  True, False]])

Note that we can then easily access the elements divisible by 3 by just doing ```y[b]```. A function along similar lines is ```np.where()```. We can do ```np.where(b)``` to get the indices of the elements of ```b``` that are ```True```.    

We can use ```newaxis()``` to add a new dimension.

	>>> x = np.arange(5)
	>>> x[:,np.newaxis]
	array([[0],
	       [1],
	       [2],
	       [3],
	       [4]])
	>>> x[:,np.newaxis] + x[np.newaxis,:]
	array([[0, 1, 2, 3, 4],
	       [1, 2, 3, 4, 5],
	       [2, 3, 4, 5, 6],
	       [3, 4, 5, 6, 7],
	       [4, 5, 6, 7, 8]])

It just works by putting an array wrapper ```[]``` at appropriate places.

Finally, we can use ```...``` when indexing to reduce the amount of typing.

	>>> x = np.arange(16).reshape(2,2,2,2)
	>>> x
	array([[[[ 0,  1],
	         [ 2,  3]],

	        [[ 4,  5],
	         [ 6,  7]]],


	       [[[ 8,  9],
	         [10, 11]],

	        [[12, 13],
	         [14, 15]]]])
	>>> x[1,...,1] #equivalent to x[1,:,:,1]
	array([[ 9, 11],
	       [13, 15]])
