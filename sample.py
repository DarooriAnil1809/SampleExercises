class bankaccount:
    def __init__(self):
        self.balance = 0
        print("Enter deposit and withdrawal amount")
    
    def deposit(self):
        amount = float(input('enter deposit amt'))
        self.balance += amount
        print("deposit amount is", amount)


    def withdrawal(self):
        amount = float(input("withdrawal amount"))
        if self.balance >= amount:
            self.balance -= amount
            print(w)