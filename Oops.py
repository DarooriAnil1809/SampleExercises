

#Creatin class and object with class and instance attributes

from unicodedata import name


class DoG:
    #Class Attribute
    attr = "Mammal"

    #Instance Attribute
    def __init__(self, name):
        self.name = name

    #object Inititialization
RODGER= DoG("RodGer")
Tommy = DoG("Tommy")

    #Accessin class attributes
print("RoGer is a {}".format(RODGER.__class__.attr))
print("Tommy is a {}".format(Tommy.__class__.attr))


    #Accessin instance attributes
print("My Name is {}".format(RODGER.name))
print("My name is {}".format(Tommy.name))



#Create Class and Object with methods

class obj:
    attr1 = "Animal"

    def __init__(self,name):
        self.name = name

    def speak(self):
        print("My Name is {}".format(self.name))

Bella = obj("bella")
Lucy = obj("Lucy")

Bella.speak()
Lucy.speak()


#Inheritance example 01
class person:
    def __init__(self, name, IDno):
        self.name = name
        self.idnum = IDno

    def display(self):
        print(self.name)
        print(self.idnum)

    def details(self):
        print("My Name is {}".format(self.name))
        print("ID Number is {}".format(self.idnum))

class Employee(person):
    def __init__(self, name, idnum, salary, post):
        self.salary = salary
        self.post = post

        #invokin the __init_ parent class
        person.__init__(self,name,idnum)

    def details(self):
        print("My Name is {}".format(self.name) )
        print("ID Number: {}".format(self.idnum))
        print("Post:{}".format(self.post))

#invokin parent class
a = Employee('ANIL',401, 50000, 'Software Analyst')

#callin Function

a.display()
a.details()


#Inheritance Example-02









    


