# Looping through lines
f = open("D:\Filehandling\examplefile.txt", "r")
for x in f:
    print(x)


file = open("D:\Filehandling\examplefile.txt", "r")
print(file.read())


file = open("D:\Filehandling\meenafile.txt", "r")
print(file.read(2))


file = open('D:\Filehandling\writefile.txt', 'w')
file.write("THIS IS THE FIRST COMMAND")
file.write("THIS IS THE SECOND COMMAND")
file.close()
