#TensorFlow :- Tensorflow is nothing but array/ it is a vector or matrix of N-dimension.

#pip install tensorflow==2.0.0
#pip install numpy
#pip install matplotlib

import tensorflow as tf
#to check the version of tensorFlow
print(tf.__version__)


#To create the constant variable
a = tf.constant("Hello")
b = tf.constant("world")

print(a)#tf.Tensor(b'Hello', shape=(), dtype=string)
tf.print(a)#Hello
tf.print(b)


num1 = tf.constant(10)
num2 = tf.constant(30)
tf.print(num1+num2)

#(3,3) matrix of 5
mat = tf.fill((3,3),5)
tf.print(mat)
'''
[[5 5 5]
 [5 5 5]
 [5 5 5]]
 '''
 
#(3,3) matrix of 0
zero = tf.zeros((3,3))
tf.print(zero)
'''
[[0 0 0]
 [0 0 0]
 [0 0 0]]
'''
#(3,3) matrix of 1
one = tf.ones((3,3))
tf.print(one)

'''
[[1 1 1]
 [1 1 1]
 [1 1 1]]
'''

#2d array of (2,2)
mat = tf.constant([[2,3],
                   [4,5]])

tf.print(mat)
#to check the shape of matrix
print(mat.get_shape())#(2,2)

mat2 = tf.constant([[2],
                    [4]])

print(mat2.get_shape())#(2,1)


#TensorFlow Variabvle
string = tf.Variable("Hello we are working on Deep learning!!", tf.string)
tf.print(string)

number = tf.Variable(78, tf.int16)
tf.print(number)

floating = tf.Variable(3.162, tf.float64)
tf.print(floating)


#Unifromlly generated random numbers
random_mat = tf.random.uniform((5,5),0,1)#Uniform(shpe,start,end)
tf.print(random_mat)
