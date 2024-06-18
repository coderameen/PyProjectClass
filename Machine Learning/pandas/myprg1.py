import pandas as pd
import numpy as np#pip install numpy
l = [10,20,30,40]

print(np.array(l))

#read dataset
df = pd.read_csv('diabetes.csv')
print(df)
#df.head()=> prints the top 5 records/tail() = bottom 5 records
df.head(12)
print(df['Pregnancies'])
print(df['BMI'])

print(df.columns)#to see all columns names

for i in df.columns:
    # print(i)
    # print(df[i][0])
    print(df[i][2])
    

l = [1,2,3]
print(type(l))#list

myl = np.array(l)
print(myl)

#To check the dimension of the array
l = [1,2,3]
print(np.ndim(l))#1 dim

l = [l,l,l]
'''
[[1,2,3],
 [4,5,6],
 [7,8,9]]
'''
print(np.ndim(l))#2 dim (rows,columns)
l =[[1,2,3],
 [4,5,6],
 [7,8,9]]
print(l)
print(l[1][1])
#to check the shape of the matrix or 2d array
l = np.array(l)
print(l.shape)#(3,3)

l = [[1,2],[3,4],[7,8],[11,22]]
l = np.array(l)
print(l.shape)#(4,3)

#to check the datatype
print(l.dtype)

#zeros matrix
#if u wanted u print zero matrix of (3,3)

myzero = np.zeros((3,4))
print(myzero)

#ones matrix
myones = np.ones((2,2))
print(myones)

#Random
myarr = np.random.random((3,3))
print(myarr)


myvar = np.random.random()
print("this is my random number:   ",myvar)

if np.random.random() > 0.5:
    print("you won")
else:
    print("game end")
    
    
#reshape

#shape: size of matrix (row,column)

l = [[1,2,3],
     [4,5,6],
     [9,10,11]]
arr = np.array(l)
print(arr.shape)


randomarr = np.random.random((4,3))
print(randomarr)

newarr = np.reshape(randomarr,(3,4))
print(newarr)
l = [[1,2,3,22],
     [4,5,6,33],
     [9,10,11,44]]
arr = np.array(l)
newarr2 = np.reshape(arr,(4,3))
print(newarr2)


#Arithematic operation
arr = np.array([1,2,3,4,5,6])
print(arr + 1)
print(arr * 10)
print(arr - 1)
print(arr ** 2)



arr = np.array([13,2,3,48,52,6])
print(arr.min())
print(arr.max())

#imp
arr = np.array([[9,2,3],
                [4,6,8],
                [7,5,1]])

#output: [9,6,8]
print(arr.max(axis=0)) #axis = 0 is to find maximum in column wise, if axis=1(row wise)
print(arr.max(axis=1)) #max in row wise



#sorting
arr = np.array([[7,3,8,6,4],[7,2,9,8,6],[5,4,2,3,1]])

print(arr.ndim)

#sorting the above array
arr = np.sort(arr,axis=0,kind="mergesort")
print(arr)
arr = np.sort(arr,axis=1,kind="mergesort")
print(arr)

