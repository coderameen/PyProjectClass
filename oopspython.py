#1.class and objectd
#1.class: "collection of attributes or methods" or "It is an collection of instance variables and function"
#objes: instance of class

class StudentDetail:
    n = 10#instance variable
    #method / function

    def print_details(self):
        print("This is my local function")

#to create the object
obj = StudentDetail()
print(obj.n)
obj.print_details()


print("----------------")

class Student:
    name = "Alen"#instance varaible
    usn = "CS01"#instance variable #SEFT: it is an argument that point to itself
    def student_details(self):
        print(f"The student name is  {self.name} and usn is {self.usn}")
        
obj = Student()
obj.student_details()


#Constructors: it is used to initialize the instence variable 
class AIML:
    #Constructors
    def __init__(self,usn,name,marks):
        self.usn = usn
        self.name = name
        self.marks = marks
    
    def print_details(self):
        print(f"The Student usn: {self.usn} | name: {self.name} | marks: {self.marks}" )
        
s1 = AIML("AI01","Alen",89)
s1.print_details()
s2 = AIML("AI02","Bob",97)
s2.print_details()


#3. Scope of variable
myv = 10000#Global variable
class MyClass:
    n = 10#Instance variable
    
    def display(self):
        n = 20#local variable 
        print(f"The instance varialbe: {self.n}")
        print("The local variable is ",n)
        print("The Global varaible is: ",myv)
obj = MyClass()
obj.display()

#4. Encapsulation:"Wrapping up of data/bidning the data into a Signle Entity/class!!"
#we can achieve encapsulation using Access specifiers (Public,protected,private)

class Encap:
    n = 10#PUBLIC
    _n = 20#Protected
    __n = 300#Private
    def display(self):
        print("this is my loacl fucntion")
        print("Protected varaible is : ",self.__n)
    
obj = Encap()
print(obj.n)#10
print(obj._n)#20 I can access protected variable outside the class
# print(obj.__n)#
obj.display()

    
    
    
#Inheritence
#1.Single Level inheritence
class Parent:
    def pdisplay(self):
        print("This is parent property!!")
        
class Child(Parent):
    def cdisplay(self):
        print("This is child property!!")
        
c = Child()
c.cdisplay()
c.pdisplay()

print("------------------------")
#2.Multi-level Inheritence
class GrandParent:
    def gpdisplay(self):
        print("This is gp property!!")
        
class Parent(GrandParent):
    def pdisplay(self):
        print("This is parent property")
        
class Child(Parent):
    def cdisplay(self):
        print("This is c property")
    
c = Child()
c.cdisplay()
c.pdisplay()
c.gpdisplay()

print("-------------------")

#Multiple inheritence
class Father:
    def fdisplay(self):
        print("This is father display")
class Mother:
    def mdisplay(self):
        print("This is mother display")
class Child(Father,Mother):
    def cdisplay(self):
        print("This is child display")
        
c = Child()
c.mdisplay()
c.fdisplay()
print("-----------")
#4.Hybrid inheritence
class Parent(GrandParent):
    def pdisplay(self):
        print("This is parent property")
        
class Child1(Parent):
    def cdisplay(self):
        print("This is c property")

class Child2(Parent):
    def cdisplay(self):
        print("This is c property")

class Child3(Parent):
    def cdisplay(self):
        print("This is c property")
        
c1 = Child1()
c1.pdisplay()
c2 = Child2()
c2.pdisplay()

#Abstract: "Hidding the implementation details by showing essential details"
#explame: Installation of softwares(vs code)
from abc import ABC,abstractmethod
class AbstClass(ABC):
    @abstractmethod
    def absfunc(self):
        pass
class ConcreteClass(AbstClass):
    def absfunc(self):
        print("This is abstract method-defined")
#NOTE: We cant create object for abstract class
obj = ConcreteClass()
obj.absfunc()

#Polymorphism:"Implementing same thing in a differnt way"
#we can acheive using Overloading and Overrinding
#1.Overloading
'''
a.Operator Overloading
b.Method Overloading
'''
#a.operator overloading
a = 10
b = 30
print(a+b)#30(addition - + operator act as addition wrt Integers)
a = "hi"
b = "hello"
print(a+b)#hihello (+ operator act as concationation wrt strings)

print(10*20)#multiplication
l = [1,2,3]
print(l*3)#[1, 2, 3, 1, 2, 3, 1, 2, 3] replication wrt python datastructures

#b.method overloading
def add():
    a = 10
    b = 20
    print(a+b)
add()

def add(a,b):
    print(a+b)
add(10,40)

def add(a,b,c):
    print(a+b+c)
add(10,20,30)

#Overriding
class Parent:
    def display(self):
        print("This is parent property")

class Child(Parent):
    def display(self):
        super().display()
        print("This is child property")
c = Child()
c.display()