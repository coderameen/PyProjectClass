#Python Statements
#1.Conditional Statement
'''
Sytax: if condition:
            executing the statement
'''
# num = int(input("enther the number"))
# if num > 5:
#     num = num * 100
# print(num)#4



conn = None
if conn != None:
    print("Success connection")
else:
    print("Failure")
    
#if else
n = 6
if n%2 != 0:
    print("odd")
else:
    print("even")
    
#elif stateme
a = 200000
b = 55
c = 1000
if a>b and a>c:
    print(a, " is greater")
elif b>a and b>c:
    print(b, " is the greater!!")
else:
    print(c ," is greater")
    
#
a = 20
b = 55
c = 10

#bad practice
if a==20:
    if b==55:
        if c==10:
            print("Hello this is python!!")

if a==20 and b==55 and c==10:
    print("all condition passed")
else:
    print("fail in condition")

         
if all([a==20,b==65,c==10]):
    print("This is python!!!")
else:
    print("some condition is not met")

x = 10
y = 30
if x==200 or y==30:
    print("Hii!!")
if any([x==200, y==30]):
    print("helloooo") 
    
a = 100#mandetory
b = 20
c = 44
if a == 100 and (b==2000 or c == 44):
    print("success")
else:
    print("fail")

if all([a==100, any([b==2000,c==474]) ]):
    print("Succesc condition")
else:
    print("Failure condition")
    
#
# def myfunc():
#     print("this is my function")
# myfunc()
#overcome use of switch statement in python we make use of match statemnt
def access(user):
    match user:
        case "manager": return "Manager have full access"
        case "guest": return "guest have limited acces"
        
print(access("guest"))


#iterative statement(looping )
#for loop, while loop
#1 to 10 using for loop:
for i in range(1,11):
    # print(i)#line by line
    print(i, end=" ")#in single line

# for i in range(6):
#     print(i)
#only even number from 1 to 10:
print()#break /n
for i in range(1,11):
    if i%2==0:
        print(i, end=" ")

#only odd number from 1 to 10:
# print()#break /n
# for i in range(1,11):
#     if i%2!=0:
#         print(i, end=" ")       

print()
#even
for i in range(0,11,2):
    print(i, end=" ")

print()
#odd
for i in range(1,11,2):
    print(i, end=" ")

#1 to 10 using while loop
print()

i = 1#init
while i<11:
    print(i, end=" ")
    i+=1#i=i+1
    
# while True:
#     n = input("enter ur name")
#     print("hi ",n)
#     if n == "quit":
#         break



#Uncondtional Statementss in python
#ex: break and continue

print()
#Q: I need to print 1 to 10. if 5 encounters terminate/stop the loop
for i in range(1,11):
    if i == 5:
        break#terminating/stopping
    print(i)
        
print("done")   
print()
#Q: I need to print 1 to 10. except 5
for i in range(1,11):
    if i == 5:
        continue#skipping the loop
    print(i, end=" ")
    