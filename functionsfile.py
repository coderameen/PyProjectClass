#Functions: "Block of code used to avoid redencency of the code!"

'''
def function_name:
    block of code
'''
#1. non paramenterized and non return function
def myfunc1():
    a = 10
    b = 30
    c = a + b
    print("The sum is: ",c)

myfunc1()

#2.parameterized and non return function
def myfunc2(name,age):
    print("The Student name is: ",name," the age is ",age)
    
myfunc2("Alen",24)

#3. non para and return function
# def myfunc1():
#     a = 10
#     b = 30
#     c = a + b
#     return f"The sum is {c}"

# result  = myfunc1()
# print(result)

def myfunc3():
    x = 100
    res = 100 * 1000
    return f"The result is :{res}"

# result = myfunc3()
# print(result)

#or

# print(myfunc3())

#4.para and return function
def add(x,y):
    return x+y#66
print("The result is ",add(33,33))

# def add2(x,y):
#     num1 = x
#     num2 = y
#     mysum = num1 + num2
#     return mysum
# # print(add2(3,4))
# output = add2(40,20)
# print(output)


#example: student detail function
# def studentDetail(name,usn,marks):
#     return f"Student name is {name} | usn is {usn} | marks is {marks}"
# name = input("Enter the Studen name")
# usn = input("Enter the student usn")
# marks = input("Enter the student marks")
# print(studentDetail(name,usn,marks))#Hard coded


#Default Argument in python function
'''
def myfunc(x,y,z):
    return x+y+z
print(myfunc(10,20)) #TypeError: myfunc() missing 1 required positional argument: 'z' 
'''
def myfunc(x,y,z=300):
    return x+y+z
print(myfunc(10,20))#330

def myfunc(x,y,z=300):
    return x+y+z
print(myfunc(10,20,500))#530
