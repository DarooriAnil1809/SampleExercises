class bankaccount:
    def __init__(self):
        self.balance=0
        print("Welcome to Deposit and Withdrawal Machine")

    def deposit(self):
        amount = float(input("Enter the Deposit Amount"))
        self.balance += amount
        print("Amount Deposited", amount)

    def withdrawal(self):
        amount = float(input("Enter the Withdrawal Amount"))
        if self.balance >= amount:
            self.balance -= amount
            print("withdrawal amount", amount)
        else:
            print("insufficient balance")
    
    def display(self):
        print("Net Available Balance=", self.balance)


s = bankaccount()
s.deposit()
s.withdrawal()
s.display()
