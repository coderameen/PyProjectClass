#Operators in python:
#operator: are special symbols  used to perform/compute mathematical operation for given operands (value/data)
'''
1.Arithematic operator(+,-,*,/,%,**,//)
2.Comparition operator/Relation operator(==,!=,>,<,>=,<=)
3.Logical operator(AND,OR,NOT,XOR)
4.Assignment operator(=,+=,-=,*=,/=)
5.Bitwise operator(<<, >>)
6.Membership operator(in, not in)
7.Identity operator(is, is not)
'''
# # a = 20
# # b = a
# a = 20
# b = 50
# print(a != b)#Ture


# a = 100
# b = 300
# if a == 102 or b == 300:
#     print("True")
# else:
#     print("False")


#assignment operator
summ = 20
summ += 10#sum = sum + 10
print(summ)


#bitwis operator
#1.right swift(>>)
#2.left swift(<<)

print(4<<2)#16
print(4<<1)#8
print(4<<3)#32


l = [10,20,30,40]
print(200 not in l)#membership

#identity operator
#it compare the memory location of two objects
a = [10,20,30,40]
b = [10,20,30,40]
c = a
print(id(a))#1364526265472
print(id(b))#1364530568448
print(id(c))#1364526265472
print(a is c)

#logical: and or 

#datatype: int float str bool and or