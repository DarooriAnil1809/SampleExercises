import os
#File Handling
#Create- Read - Update - Delete

# #To Open File for reading
# f = open("demofile.txt")

# #read-r, text - t
# f = open("demofile.txt", "rt")


#FILE HANDLING - Read Files
f = open("D:\Filehandling\demo.txt", "r")
print(f.read())

#Reads only parts of file
f = open("D:\Filehandling\demo.txt", "r")
print(f.read(10))


#Readlines - return one line 
f = open("D:\Filehandling\demo.txt", "r")
print(f.readline())


#Readlines - return two lines
f = open("D:\Filehandling\demo.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())



#Looping through lines
f = open("D:\Filehandling\demofile.txt", "r")
for x in f:
    print(x)

#Close the Files - using close method
f = open("D:\Filehandling\demofile.txt", "r")
print(f.readline())
f.close()


#PYTHON FILE WRITE
# "a"- append the file
# "w" - write the file

# f = open("D:\Filehandling\demofile3.txt", "a")
# f.write("now the file has more content")
# f.close()

#Open and Read the file after append 
f = open("D:\Filehandling\demofile3.txt", "r")
print(f.read())
f.close()


#Overwrite the content
f = open("D:\Filehandling\demofile3.txt", "w")
f.write("now the file has more content - Modified")
f.close()


#Create new file
f = open("D:\Filehandling\createfile.txt", "w")
f.write("HELLO")
f.close()



#Delete File 
#Must use import os

os.remove("D:\Filehandling\Delete.txt")


#Check File Exists
#Before Delete the file has to check file exists or not
if os.path.exists("D:\Filehandling\Delete.txt"):
    os.remove("D:\Filehandling\Delete.txt")
else:
    print("file not exists")

#Delete Folder
os.rmdir("D:\Filehandling\Delete")