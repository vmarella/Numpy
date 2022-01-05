import numpy
a = list(range(10)) # range adds a range of numbers to the array
print(a)

---------------------------------------------------------------------------------------------------

import numpy
b = [0] *10  # create a array of value specified in the square brackets with size of the number specified with *
print(b)

-----------------------------------------------------------------------------------------------------------------

for i in range(len(a)):
    b[i] = a[i]**2
print(b)

------------------------------------------------------------------------------------------------------------------

import numpy as np
a = np.array([1,2,3])
b = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
print(a.dtype)
print("********")
print(b)
print(b.shape)
print(b.dtype)

--------------------------------------------------------------------------------------------------------------------

import numpy as np
a = np.zeros((2, 3))           # 2x3 array with all elements 0
b = np.ones((1,2))             # 1x2 array with all elements 1
c = np.full((2,2),7)           # 2x2 array with all elements 7
d = np.eye(2)                  # 2x2 identity matrix

--------------------------------------------------------------------------------------------------------------------

np.arange(10)              # Evenly spaced values in an interval
np.linspace(0,9,10)        # same as above, see exercise

e = np.ones((3,3))
f = np.ones((3, 2), bool)  # 3x2 boolean array
g = np.arange(10)
h = np.linspace(0,9,10)

---------------------------------------------------------------------------------------------------------------------

a = np.random.random((3,2))
a.astype('int')
print(a)

---------------------------------------------------------------------------------------------------------------------

a = np.arange(10)
b = np.linspace(0,9,10).astype(int)
print(a)
print(b)
c = np.array(np.random.random())
print(c)

---------------------------------------------------------------------------------------------------------------------

import numpy as np
x = np.eye(4)
y = x[:-1]

z = np.round(1.5)
print(z)

---------------------------------------------------------------------------------------------------------------------