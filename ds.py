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



#Tuple: it is the collection of mix data which are enclosed with the ()
#explem: t = (10,20,30,40,"alen",'a',5.5,(22,33,44),[10,20,30])
'''
NOTE: Tuple are immutable(can't be modified)

Mutable: list,set,dictionary
IMMUTABLE: Tuple
'''
#immutable
t =(10,20,30)
# print(t[1])#20
# t[1] = 200
# print(t)#TypeError: 'tuple' object does not support item assignment

l =[10,20,30,40]
l[1] = 2000
print(l)#[10, 2000, 30, 40]

print("---")
#emplty tuple
t = ()
print(type(t))
t = tuple()


#cancatination
t1 = (10,20,30)
t2 =(40,50,60)
print(t1 + t2)

#repitation
t1 =(1,2,3)
print(t1*3)#(1, 2, 3, 1, 2, 3, 1, 2, 3)

# membershipt(in, not in)
t = (10,20,30,40)
print(20 in t)#true
print(50 in t)#false
print(50 not in t)#true


#access: use of indexing
t = (10,20,30,40)
print(t[3])

#slicing: fetch 20 and 30
print(t[1:3])
print(t[1:-1])

#length
print(len(t))

#count in tuple
t = (11,22,22,33,44,22,22,22)
print(t.count(22))#5

#write program to count element without using count() method
cnt = 0
for i in t:
    # print(i)
    if i == 22:
        cnt += 1

print("Total 22 are: ",cnt)


#index() used to find the index for repective element

t = (1,2,3,4,5)
print(t.index(3))

t = (4,3,1,2,5)
print(sorted(t))#(1,2,3,4,5)
print(sorted(t, reverse=True))#sort in decending ording



#tuple methods
t = (4,3,1,2,5)
print(sum(t))
#sum the elements without using sum() method
summ = 0
for i in t:
    summ = summ + i
print("The sum of t: ", summ)


#min
print(min(t))#1
print(max(t))#5

#NOTE: Tuple is immutable, we can't change/modified/update the data/item/elemen/value



#SET in python
#SET: it is unordered collection of mixed unique data which is enclosed within {}
s = {10,20,20,"alen",'a'}
print(s)#{10, 20, 'alen', 'a'}
print(type(s))
    
#emplty set(***)
s = {}
print(type(s))#<class 'dict'>
s = set()#EMPTY SET
print(type(s))

#note: ***
t = (10)
print(type(t))#<class 'int'>

t = (10,)
print(type(t))#<class 'tuple'>

s = {10,20,20,20,30,40,40,50}
print(s)#{50, 20, 40, 10, 30}

#sort
print(sorted(s))#[10, 20, 30, 40, 50]
print(sorted(s,reverse=True))#[50, 40, 30, 20, 10]

#main method() in SET
#union or '|'
s1 = {10,20,30}
s2 = {40,50,60}
res = s1.union(s2)
print(res)#{50, 20, 40, 10, 60, 30}
myres = s1 | s2
print(myres)#{50, 20, 40, 10, 60, 30}


#intersection
s1 ={1,2,3,4}
s2 = {3,4,5}

res = s1.intersection(s2)
print(res)#{3, 4}

#difference
s1 = {10,20,30,40,50}
s2 ={30,40,50}
print(s1.difference(s2))#s1-s2

#adding the element in set 
'''
.add
.update
'''
s1 ={10,20,30,40}
s1.add(50)
print(s1)#{40, 10, 50, 20, 30}

s2 = {11,22}
s1.update(s2)
print(s1)#40, 10, 11, 50, 20, 22, 30}

#remove
s1 ={10,20,30,40}
s1.remove(30)
print(s1)#{40, 10, 20}


s1 ={10,20,30,40}
# s1.remove(70)#KeyError: 70
# print(s1)

# s1.discard(70)
print(s1)#ignore the error, if element not belogns to the original set
s1.discard(20)
print(s1)#{40, 10, 30}


#pop(): to remove only last element
s1 ={10,20,30,40}
s1.pop()
print(s1)#{10, 20, 30}
# s1.pop(1)
# print(s1)#TypeError: set.pop() takes no arguments (1 given)


#clear(): it delete all element in the set
s1.clear()
print(s1)#set() 



#Dictionary in Python
#it is collection of key and value pair which is enclosed within the {}
d = {"name":"alen","age":30}
print(len(d))#2 => two elements
print(type(d))#<class 'dict'>


#empty dictionary
d = {}
print(type(d))

d = dict()
print(type(d))


#accessing
d = {"name":"alen","age":30}
print(d['name'])

# print(d['usn'])#KeyError: 'usn'
print(d['age'])

#get() access the element
print(d.get('name'))
print(d.get('age'))
print(d.get('usn'))#None
print(d.get('usn',0))#0


#adding the element in dictionary
d = {"name":"alen","age":30}
d['usn'] = 'CS01'
print(d)#{'name': 'alen', 'age': 30, 'usn': 'CS01'}

d2 = {'address':'Bangalore'}
d.update(d2)
print(d)#{'name': 'alen', 'age': 30, 'usn': 'CS01', 'address': 'Bangalore'}

#deleting
d = {'name': 'alen', 'age': 30, 'usn': 'CS01', 'address': 'Bangalore'}
#to delete address
del d['address']
print(d)#{'name': 'alen', 'age': 30, 'usn': 'CS01'}


#membership(in, not in)
d = {'name': 'alen', 'age': 30, 'usn': 'CS01', 'address': 'Bangalore'}

print('name' in d)#True
print('marks' in d)#False


#len
print(len(d))#4

#keys
print(d.keys())#dict_keys(['name', 'age', 'usn', 'address'])

#values()
print(d.values())#dict_values(['alen', 30, 'CS01', 'Bangalore'])


#items()
print(d.items())#dict_items([('name', 'alen'), ('age', 30), ('usn', 'CS01'), ('address', 'Bangalore')])


#pop(key)
d.pop('address')
print(d)#{'name': 'alen', 'age': 30, 'usn': 'CS01'}

d = {2:10,1:30,3:50}
print(sorted(d))#[1, 2, 3] sored key
print(sorted(d.values()))#[10, 30, 50]
print(sorted(d.items()))#[(1, 30), (2, 10), (3, 50)]

#min
d = {2:10,1:30,3:50}
print(min(d.keys()))#1
print(min(d.values()))#10

#max
print(max(d.keys()))#3
print(max(d.values()))#50

d = {2:10,1:30,3:50}
d.clear()
print(d)#{}


# del d
# print(d)#delte from compllete memory


