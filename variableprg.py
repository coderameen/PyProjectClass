#variable: is a container used to store data in repective memory loaction
#Syntax: variable_name = data  (or) variable_name = value
name = "Alen"#string
age = 35
height = 5.96
print(name)
print(age)
print(height)

#To check the type of variable
print(type(name))#string
print(type(age))#integer
print(type(height))#float
'''
Alen
35
5.96
<class 'str'>
<class 'int'>
<class 'float'>
'''
#single line comment
'''
skdfjlksd
sdfsdf
sfdfsd
'''
"""This is an doc string similar to normal comment in python."""

a = 10
print(id(a))#2256612819472
print(a)
a = 40
print(id(a))#2256612820432
print(a)#40

#Valid and invalid type of variable
#valid
myvar = 30#(valid)
print(myvar)#30
_myvar = 80
print(_myvar)#80

my_var = 70
print(my_var)

# 3myvar = 50#(invalid)
# print(3myvar)

# $myvar = 60#(invalid: can't use special symbols)
# print(&myvar)

# for else None while and or elif 
# for = 100
# print(for)#can't use built keyword as a variable


a = 30
print(id(a))#1476823811216
print(a)
a = 40
print(id(a))#1476823811536
print(a)#40


#Type casting/Type conversion
#changing one datatype to another datatype
a =  10
print(type(a))#int
a = "10"
print(type(a))#str


a = "10"
b = "20"
print(a+b)#1020
print(int(a) + int(b))#30

c = 5
print(c)
print(float(c))#int -> float

a = 'a'#97
b = 'b'#98
# print(int(a)+int(b))#ValueError: invalid literal for int() with base 10: 'a'
#To convert any charect to acsii value
print(ord(a))
print(ord(b))
print(ord(a)+ord(b))#195
#to conver acsii to char
print(chr(97))#a
print(chr(65))#A



#Type of print statement in python
#1.General print statement
print("Hello geek!, this is python ")
#variable print statement
name = "Alen"
age = 35
print("The name is: ",name)
print("The name is: ",name, " and age is: ",age)

print("The name is: "+name)

#3.Formatted print statement
print(f"This formatted st4ring: The name is {name} and age is {age}")
print("The name is {1} and age is {0}".format(age,name))


#To take input from user in python
# name = input("Enter your name here: ")
# print("The input name is: ",name)
#NOTE: input() always take input in string
# n1 = int(input("Enter a number: "))
# n2 = int(input("Enter second number: "))
# print(n1 + n2)#2030

# n1 = input("Enter a number: ")
# n2 = input("Enter second number: ")
# print(int(n1) + int(n2))#2030


a,b= input("Enter two number").split()
print(int(a) + int(b))