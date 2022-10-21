#empty dictionary
dict= {}

#dict with inteGer Values
dict ={1:"ANIL", 2:"Bear Grylls"}
print(dict)

#dict with mixed keys
dict = {'name': "Anil", 'aGe':  30, 1:[2,3,4]}
print(dict)


#AccessinG the Dict elements
my_dict = {'name':"ANIL", 'address':"UPPAL", 'CONTACTNO':9000124144}
print(my_dict)
print(my_dict['name'])
print(my_dict['address'])
#usin GET Method
print(my_dict.get('CONTACTNO'))

#Displays the error as None element
print(my_dict.get('Family'))

#Key error Displays
#print(my_dict['Relation'])

#ChanGinG and AddinG Dictionary Elements
#Update Elements
my_dict = {'name':"ANIL", 'address':"UPPAL", 'CONTACTNO':9000124144}
my_dict['CONTACTNO'] = 8126985754
print(my_dict)
#Addin Elements
my_dict['Favorite place'] = "AGRA"
print(my_dict)


#Remove Elements from Dict
my_dict = {'name':"ANIL", 'address':"UPPAL", 'CONTACTNO':9000124144}
#usin POP METHOD TO REMOVE ELEMENTS
print(my_dict.pop('name'))
print(my_dict.pop('CONTACTNO'))

#Arbritary Item to REMOVE 
my_dict = {'name':"ANIL", 'address':"UPPAL", 'CONTACTNO':9000124144}
print(my_dict.popitem())
print(my_dict)

#Remove all elements
my_dict = {'name':"ANIL", 'address':"UPPAL", 'CONTACTNO':8794562142}
my_dict.clear()
print(my_dict)


#Delete Dictionary
my_dict = {'name':"ANIL", 'address':"UPPAL", 'CONTACTNO':8794562142}
del my_dict
#print(my_dict)

#Dictionary Methods
#fromKeys Method
marks = {}.fromkeys(['MATHS','SCIENCE','GK'],0)
print(marks)
marks = {}.fromkeys(['CS','M1','M2'],25)
print(marks)

marks = {}.fromkeys(['MATHS','SCIENCE','GK'])
for item in marks.items():
    print(item)

#dict Comprehension
squares = {x: x*x for x in range(6)}
print(squares)

cubes = {x: x*x*x for x in range(10)}
print(cubes)

#dict comprehension with if conditional statement
odd_squares = {x : x*x for x in range(6) if x %2 == 0}
print(odd_squares)


#Iteration throuGh Dict
squares = {x: x for x in range(6)}
for i in squares:
    print(squares[i])


#Dict Built in Functions
squares = {0:0,1:1,3:9,5:25,7:49,9:81}
