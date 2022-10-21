import datetime
import math
#OOPS
#Defining Classes and Objects

#Create Class

class MyClass:
    x = 10
    print(x)


#Object 

class MyClass:
    x =100
objMyClass = MyClass()
print(objMyClass.x)


#__INIT__ Function
# Built in function - created when class and object are initiated


#Class and Object Examples

class person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

objperson = person("ANIL", 30)
print(objperson.name)
print(objperson.age)
    






class student:
    def __init__(self, studentid,studentname,studentage,studentcollege):
        self.studentid = studentid
        self.studentname = studentname
        self.studentage = studentage
        self.studentcollege = studentcollege

objstudent = student("401","AKR","30","AVCR")
print(objstudent.studentid)
print(objstudent.studentname)
print(objstudent.studentage)
print(objstudent.studentcollege)


#__STR__FUNCTION - controls what should returned when the class object is created
class person:
    def __init__(self,address, salary):
        self.address = address
        self.salary = salary
    def __str__(self):
        return f"{self.address}({self.salary})"

objperson = person("CHICAGO", 360000)
print(objperson)


#Object Method

class Employee:
    def __init__(self,EmployeeID, EmployeeName, EmployeeSalary):
        self.employeeid = EmployeeID
        self.employeename = EmployeeName
        self.employeesalary = EmployeeSalary
    def myfunct(self):
        print("MY Name is " + self.employeename)

objemployee = Employee("0044KN", "Daroori", "35000")
objemployee.myfunct()


#Self parameter
#reference to current instance of the class,to access variables that belong to class







#PYTHON INHERITANCE

#Create Parent Class

class Person:
    def __init__(root, firstname,lastname):
        root.firstname = firstname
        root.lastname = lastname

    def printname(root):
        print(root.firstname, root.lastname)

objperson = Person("ANIL","Kumar")
objperson.printname()

#Create Child Class and inherit 
class student(Person):
    pass

objperson = student("MIKE","TISON")
objperson.printname()






#PYTHON ITERATORS = object
#Countable number of Values

#Iterator Example
myTuple = ("HYDERABAD","BANGALORE","CHENNAI","GOA")
myit = iter(myTuple)

print(next(myit))
print(next(myit))
print(next(myit))


#STRING ITERATOR

mystr = "DAROORI"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#OUTPUT - D A R O O R I

#LOOPING THROUGH ITERATOR
myTuple = ("HYDERABAD","BANGALORE","CHENNAI","GOA")
for x in myTuple:
    print(x)


mystr = "ANIL KUMAR"
for x in mystr:
    print(x)




#VARIABLES IN PYTHON
#LOCAL SCOPE - GLOBAL SCOPE

def myfunct():
    x = 500
    print(x)
myfunct()


def myfunction():
    x = 25.63
    def my_innerfunction():
            print(x)
    my_innerfunction()
myfunction()


#Global Scope
x = 300

def my_functionglobal():
    print(x)
my_functionglobal()
print(x)

x = 300
def my_functionglobal():
    global x 
    x = 200
my_functionglobal()
print(x)




#PYTHON MODULES - CODE LIBRARY
#A File CONTAINS SET OF FUNCTIONS
#mymodule.py

def greeting(name):
    print("HELLO," + name)
greeting("ANIL")

#import module as import file.py name
# modulename.functionname
#import w3schools02

#w3schools02.greeting("DAROORI")


#PYTHON DATES

x = datetime.datetime.now()
print(x)



#To Get Year and Name of weekday

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

#output - 2022 and MONDAY


#PYTHON MATH FUNCTION - BUILT IN FUNCTION 
#MATHEMATICAL TASKS
#import math

#MIN and MAX Functions
x = min(10,25,52,65,1,23,56,98)
y = max(52,256,258,987,456)
print(x,y)

#Absolute Positive Value
x = abs(-7.25)
print(x)

#POWER FUNCTION(4 to power of 8*8*8)
x = pow(4,8)
print(x)

x = math.sqrt(64)
print(x)


x = math.ceil(1.8) #returns 2
y = math.floor(1.8) # returns 1
print(x)
print(y)

#PI VALUE 3.14
x = math.pi
print(x)

