#program to make simple Calculator

#This function adds two numbers
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print("Select the Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:

    #Take input from the user
    choice = input("Enter the Choice(1/2/3/4")

    #if choice is one of the above options
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter the first number:"))
        num2 = float(input("Enter the second number:"))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1,num2))
        
        elif choice == '3':
            print(num1, "*", num2, "=", mul(num1,num2))
        
        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))

        #Check if user wants to do another calculation
        #break the while loop if answer is no


        next_calculation = input("Do you want to next calculation? yes/no")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")