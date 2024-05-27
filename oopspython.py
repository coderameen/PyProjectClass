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

    
    
    
