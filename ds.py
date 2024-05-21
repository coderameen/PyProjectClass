#List
#List: "Sequential collection of mix data which is enclosed in square braces"
# ex: l = [10,20,30,'a','b',1.34,7.8]
#dynamic  sized array(***)


#Empty list
l = []
print(type(l))#list
l = list()
print(type(l))

#concatination('+')
l1 = [10,20,30]
l2 = [40,50,60]
print(l1+l2)#[10, 20, 30, 40, 50, 60]

#Replication
l = [10,20,30]
print(l*3)#[10, 20, 30, 10, 20, 30, 10, 20, 30]

#membership(in and not in)
l = ['apple','mango','banana']
print('apple' in l)#True
print('orange' in l)
print('orange' not in l)


#index ([])
l = ['alen','bol',10,20,30]
print(l[3])#20

#slicing
l = [10,20,30,40,50,60]
#syntax [start:end-1]
print(l[2:5])
print(l[-1])
print(l[-2])
print(l[-3:])
print(l[:3])
print(l[:])


#length of the list
l = [10,20,30,40,50,60]
# print(len(l))
mylen = len(l)
print(mylen)


#iterate the list
for i in l:
    print(i,end=" ")

print()
#find the length of list without using len() method
l = [10,20,30,40,50,60,70]
cnt = 0
for i in l:
    cnt += 1
print(cnt)



l =[11,22,33,44]
for i in range(0,len(l)):
    print(l[i])



#Ways to insert/adding element into the list
'''
1.append
2.insert
3.extend
'''
#append: it add the element at the last index position
l = [10,20,30]
l.append(40)
print(l)


l = ['apple','banana','orange']
l.append('grapes')
print(l)

l = [10,20,30]
#insert(pos,ele)
l.insert(1,15)
print(l)

l.insert(0,5)
print(l)


#extend
l =[1,2,3]
l2 = [6,8,9]
l.extend(l2)
print(l)



def myfunc(lst,l2):
    myl1_1 = lst[0]
    myl1_1 =[myl1_1]
    myl1_2 = lst[1:]
    myl1_1.append(l2)
    myl1_1.append(myl1_2)
    return myl1_1
    
lst =[1,2,3]
l2 = [6,8,9]
print(myfunc(lst,l2))

l = [11,22,33,44,55]
l.pop()#delete last element
print(l)

l.pop(0)
print(l)
l.pop(1)
print(l)

# del l #it delete list from complete memory
# print(l)#error
l = [10,20,30,40]
l.clear()
print(l)#[]


l = [10,20,30,40]
#list.remove(ele)
l.remove(30)
print(l)


#sort

l = [4,7,2,1,3]
l.sort()
print(l)#[1, 2, 3, 4, 7]

#revere
l = [11,22,33,44,55]
# l.reverse()
# print(l)

#or
print(l[::-1])

#copy
l = [10,20,30,40]
l2 = l.copy()
print(l2)



#list comprehension(***)
#1-10
myval = [x for x in range(1,11)]
print(myval)

#to sqluare all element for 1-10
mysqure = [x*x for x in range(1,11)]
print(mysqure)

#add 100 from 1-10

myvar = [x+100 for x in range(1,11)]
print(myvar)


#print even number from 1-10
myeven = [x%2==0 for x in range(1,11)]
myeven = [x for x in range(1,11) if x%2==0]
print(myeven)

#functions in list
# l = [1,2,3,4]
# print(sum(l))
# print(min(l))
# print(max(l))
# res =  sorted(l)
# print(res)

