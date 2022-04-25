import numpy as np

# 1-D Array 
myarray1 = np.array([10,52,24,85,86,32,47,67],int)
print(myarray1)

myarray2 = np.arange(8)
print((myarray2))

myarray3 = np.arange(14,19)
print((myarray3))

print("mean : ",np.mean(myarray1))
print("median : ",np.median(myarray1))
print("sorted : ",np.sort(myarray1))
myarray4=np.append(myarray1, 50)
print(myarray4)
print(np.append(myarray1, 109))
print(np.append(myarray1, myarray3))

myarray4 = np.append(myarray4, [16,79])
print(myarray4)

# Multi-Dimentional Array

mymultiarray1=np.reshape([[myarray1],[myarray2]], (4,4))
print(mymultiarray1)
print(mymultiarray1[0][0])
print(mymultiarray1[3][3])

#only 3rd row
print(mymultiarray1[2,])
#only 3rd column
print(mymultiarray1[0:4,2])
# 
print("test",mymultiarray1[0:1])

#Transpose
#makes rows to columns and columns to rows
print(mymultiarray1.transpose())

#ndim - dimension of array
print(mymultiarray1.ndim) #2 dimensional array
print(myarray1.ndim) #1 dimensional array

#shape - Shape of array
print(mymultiarray1.shape) # (4,4) array
print(myarray1.shape) # (8,0) or (8, ) array

#flatten - flats multidimensional array to 1-dimensional array
print(mymultiarray1.flatten())

#Mathematical
myarray2[0]=2
mymultiarray2=np.reshape([[myarray2],[myarray1]], (4,4))
print(mymultiarray1,'\n')
print(mymultiarray2,'\n')
print(mymultiarray1+mymultiarray2,'\n') #addition
print(mymultiarray1-mymultiarray2,'\n') #subraction
print(mymultiarray1*mymultiarray2,'\n') #multiplication
print(mymultiarray1/mymultiarray2,'\n') #division

print(mymultiarray2.max())
