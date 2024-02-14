# -*- coding: utf-8 -*-
"""Numpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19AVZBydTK8b0fh4gxFV0-AX4mw7uBrcX
"""

import numpy as np

#creating arrays
arr=np.array([1,2,3,4,5])
print(arr)

zeros_arr=np.zeros(((3,3)),dtype=int)
print(zeros_arr)

arrange_arr=np.arange(10)
print(arrange_arr)

#Array manipulation
reshape_arr=arr.reshape(5,1)
print(reshape_arr)

sliced_arr=arr[2:4]
print(sliced_arr)

import numpy as np

#split
arr=np.array([1,2,3,4])
arr1=np.split(arr,2)
print(arr1)

import numpy as np

#Stack
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr3=np.stack(arr1+arr2)
print(arr3)

import numpy as np

#vstack
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr3=np.vstack(arr1+arr2)
print(arr3)

import numpy as np

#Addition of Arrays
m1=np.array([[1,2,3],[2,3,4]])
m2=np.array([[3,7,4],[2,5,1]])
result=m1+m2
r2=m1+3
print(result)
print(r2)

import numpy as np

#transposing

a=np.array([[1,2,3,4],[5,6,7,8]])
b=a.T
print(b)

import numpy as np

#linear Algebra

arr=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])

#dot product
r=np.dot(arr,arr2)

d=np.linalg.eig(r)
print(r)
print(d)

import numpy as np

#Sum of Array
e1=np.array([[1,2,3],[4,5,6]])
e3=np.sum(e1,axis=0)
e2=np.sum(e1,axis=1)
print(e2)
print(e3)

import numpy as np

#Statistical operaions

a=np.array([1,2,3,4,5])

Mean=np.mean(a)
med=np.median(a)
vari=np.var(a)
SD=np.std(a)

print(Mean)
print(med)
print(vari)
print(SD)

import numpy as np

#Load and Saving files

data=np.loadtxt("/content/Mahi.txt",dtype=int)
daa=np.savetxt("/content/Mahu.txt",data)
print(data)

#mathplot lib
import numpy as np
import matplotlib.pyplot as plt
#Graph plot
a=np.array([1,2])
plt.plot(a)