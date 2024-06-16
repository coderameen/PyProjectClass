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

#Random 
print(np.arange(1,10,6))