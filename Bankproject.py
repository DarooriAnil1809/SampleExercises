import random
import json
from datetime import datetime, timedelta


class BankAccount:
    def open_account(self, kwargs):
        self.name = kwargs["name"]
        self.adhar_no = kwargs["adhar_no"] if "adhar_no" in kwargs else None
        self.pan_no = kwargs["pancard_no"] if "pancard_no" in kwargs else None
        self.address = kwargs["address"]
        self.photo = kwargs["photo"]
        account_no = random.randint(10000000000, 99999999999)
        self.account_no = account_no
        data_list = []
        with open("data.json", "r", encoding="utf-8") as file:
            data = file.read()
            if len(data) > 0:
                data = json.loads(data)
            else:
                data = []
        with open("data.json", "w", encoding="utf-8") as file:
            data_dict = {
                "name": self.name,
                "pancard_no": self.pan_no,
                "adhar_no": self.adhar_no,
                "address": self.address,
                "account_no": self.account_no,
                "profile_img": self.photo,
                "balance": 0
            }
            data_list.append(data_dict)
            data.extend(data_list)
            data = json.dumps(data)
            file.write(data)
            return print("your account no is", self.account_no)

    def search_customer(self, account_no=None, atm_card_no=None, loan_account_no=None):
        with open("data.json", "r", encoding="utf-8") as file:
            data = file.read()
            data = json.loads(data)
            if account_no is not None or atm_card_no is not None or loan_account_no is not None:
                for customer in data:
                    if account_no == customer["account_no"] or atm_card_no == customer["atm"]["card_no"] or loan_account_no == customer["loan_account"]["loan_account_no"]:
                        return [customer, data]
                else:
                    return print("customer not found!")
            return print("please enter the account no or atm card")

    def deposite(self, account_no, balance_deposite):
        customer = self.search_customer(account_no)[0]
        balance = customer["balance"]
        data = self.search_customer(account_no)[1]
        if balance == None:
            balance = 0
        balance += float(balance_deposite)
        data[data.index(customer)]["balance"] = balance
        with open("data.json", "w", encoding="utf-8") as file:
            data = json.dumps(data)
            file.write(data)
        return balance

    def withdrow(self, account_no, balance_withdrow):
        customer = self.search_customer(account_no)[0]
        balance = customer["balance"]
        data = self.search_customer(account_no)[1]
        if balance == None:
            balance = 0
        balance -= float(balance_withdrow)
        data[data.index(customer)]["balance"] = balance
        with open("data.json", "w", encoding="utf-8") as file:
            data = json.dumps(data)
            file.write(data)
        return balance

    def check_balance(self, account_no):
        cust_balance = self.search_customer(account_no)[0]
        return cust_balance["balance"]


# base class ---->Drvie class
# single inheritance 1 base class ----> drive class
# BankAccount--->AtmCard
# multiple inheritance
# 1 base class --> multiple drive class
# BankAccount-->AtmCard
# BankAccount-->LoanAccount
# multilable inheritance
# Base class ----> drive class--->drive class

class AtmCard(BankAccount):
    def asign_atm_card(self, account_no):
        self.card_no = random.randint(1000000000000000, 9999999999999999)
        self.expire_date_obj = datetime.today()+timedelta(days=1095)
        self.expire_date = str(self.expire_date_obj.strftime("%b/%y"))
        self.cvv = random.randint(100, 999)
        customer = self.search_customer(account_no)[0]
        data = self.search_customer(account_no)[1]
        data[data.index(customer)]["atm"] = {
            "card_no": self.card_no,
            "expire_date": self.expire_date,
            "cvv": self.cvv
        }
        with open("data.json", "w", encoding="utf-8") as file:
            data = json.dumps(data)
            file.write(data)
        return print("Atm is asigned sucessfully!")

    def genrate_pin(self, account_no, atm_card_no, pin=None):
        customer = self.search_customer(account_no)[0]
        if customer["atm"]["card_no"] == atm_card_no:
            print("you are verified customer")
            if pin is not None:
                pin = pin
            else:
                pin = int(input("Enter 4 Number Pin:"))
            data = self.search_customer(account_no)[1]
            data[data.index(customer)]["atm"]["pin"] = pin
            with open("data.json", "w", encoding="utf-8") as file:
                data = json.dumps(data)
                file.write(data)
            return print("pin genrated sucessfully!")

    def atm_withdrow(self, atm_card_no, balance_withdrow):
        customer = self.search_customer(atm_card_no=atm_card_no)[0]
        if customer["atm"]["card_no"] == atm_card_no:
            pin = int(input("enter four digit pin:"))
            try:
                if customer["atm"]["pin"] == pin:
                    account_no = customer["account_no"]
                    return super().withdrow(account_no, balance_withdrow)
            except KeyError:
                print("please genrate pin")
                atm_card_no = customer["atm"]["card_no"]
                account_no = customer["account_no"]
                self.genrate_pin(account_no, atm_card_no, pin)

    def change_pin(self, atm_card_no, old_pin):
        customer = self.search_customer(atm_card_no=atm_card_no)[0]
        if customer["atm"]["pin"] == old_pin:
            account_no = customer["account_no"]
            self.genrate_pin(account_no=account_no, atm_card_no=atm_card_no)
        else:
            print("you have entered wrong pin")

    def check_balance(self, atm_card_no):
        cust_balance = self.search_customer(atm_card_no=atm_card_no)[0]
        return cust_balance["balance"]


class LoanAccount(BankAccount):
    def apply_for_loan(self, account_no):
        customer = self.search_customer(account_no=account_no)[0]
        if customer:
            user_input_amount = float(input("Enter the Loan Amount:"))
            print(
                "Note:", "The total Principal amount calculatation is based on your cash flow")
            if customer["balance"]*5 < user_input_amount:
                user_input_amount = user_input_amount*0.75
        type_of_loan = int(input("""
            enter the type of loan 
            1 Personal Loan
            2 Education Loan
            3 Home Loan
            4 Car Loan
            5 Gold Loan
            enter option:"""))
        roi = ""
        total_year = 0
        if type_of_loan == 1:
            roi = "16%"
            total_year = int(
                input("How many year of time do you want for your personal loan:"))
        elif type_of_loan == 2:
            roi = "12%"
            total_year = 7
        elif type_of_loan == 3:
            roi = "7.72"
            total_year = 20
        elif type_of_loan == 4:
            roi = "8%"
            total_year = 8
        elif type_of_loan == 5:
            roi = "8%"
            total_year = 3
        data = self.search_customer(account_no)[1]
        amount = round(user_input_amount*(1+eval(roi[0])/100)**total_year, 2)
        emi = round(amount/(12*total_year), 2)
        loan_account_no = random.randint(10000000000, 99999999999)
        data[data.index(customer)]["loan_account"] = {
            "loan_account_no": loan_account_no,
            "total_amount": user_input_amount,
            "emi": emi,
            "no_of_emi": f"{total_year*12}",
            "roi": roi,
            "total_months": f"{total_year*12} months",
            "outstanding_balance": amount
        }
        with open("data.json", "w") as file:
            data = json.dumps(data)
            file.write(data)
        return print("your loan account is successfully opened ")

    def emi_deposite(self, loan_account_no, emi_deposite):
        search_customer_data = self.search_customer(
            loan_account_no=loan_account_no)
        customer = search_customer_data[0]
        if customer:
            balance = customer["balance"]
        data = search_customer_data[1]
        if balance == None:
            balance = 0
        balance -= float(emi_deposite)
        out_standing_balance = customer["loan_account"]["outstanding_balance"]
        out_standing_balance -= emi_deposite
        data[data.index(customer)]["balance"] = balance
        data[data.index(customer)]["loan_account"]["outstanding_balance"] = round(
            out_standing_balance, 2)
        with open("data.json", "w", encoding="utf-8") as file:
            data = json.dumps(data)
            file.write(data)
        return print(balance, out_standing_balance)

    def check_outstanding_balance(self, loan_account_no):
        search_customer_data = self.search_customer(
            loan_account_no=loan_account_no)
        customer = search_customer_data[0]
        return print(customer["loan_account"]["outstanding_balance"], "/- rs only")


# Driver Code
while True:
    q = str(input("press q for quit:")).upper()

    if q == "Q":
        print("thank you using this program:")
        break
    else:

        choose = int(input(""""
        1 for open account
        2 for deposite in account
        3 for withdrow from account
        4 for check balance
        5 for getting atm card
        6 for withdrow from atm
        7 for change atm pin
        8 for Applying for loan amount
        9 for depositing EMI
        10 for check out standing balance
        enter:"""))
        obj = AtmCard()
        obj_loan = LoanAccount()
        if choose == 1:
            name = str(input("name of account holder:"))
            adhar_card = str(input("enter the adhar no:"))
            pancard_no = str(input("Pancard Card No:"))
            address = str(input("Address:"))
            photo = str(input("add link of your photo:"))
            user_input = {
                "name": name,
                "address": address,
                "photo": photo
            }

            if len(adhar_card) == 12 and adhar_card.isdigit() == True:
                user_input["adhar_no"] = adhar_card
            else:
                print("please inter the coreect no")

            if pancard_no[:2].isalpha() == True and pancard_no[3] in ["A", "B", "C", "F", "G", "H", "L", "J", "P", "T"] and pancard_no[5:-1].isdigit() == True and pancard_no[-1].isalpha() == True:
                user_input["pancard_no"] = pancard_no
            else:
                print("please write correct pan card no.")
            obj.open_account(user_input)

        elif choose == 2:
            account_no = int(input("please enter your account no:"))
            amount = float(input("how mach do you want to deposite:"))
            print(obj.deposite(account_no, amount))
        elif choose == 3:
            account_no = int(input("please enter your account no:"))
            amount = float(input("how mach do you want to withdrow:"))
            print(obj.withdrow(account_no, amount))
        elif choose == 4:
            account_no = int(input("please enter your account no:"))
            print(obj.check_balance(account_no))
        elif choose == 5:
            account_no = int(input("please enter your account no:"))
            print(obj.asign_atm_card(account_no))
        elif choose == 6:
            atm_card_no = int(input("please enter your atm card no:"))
            amount = float(input("how mach do you want to withdrow:"))
            print(obj.atm_withdrow(atm_card_no, amount))
        elif choose == 7:
            atm_card_no = int(input("please enter your atm card no:"))
            old_pin = int(input("enter the old pin:"))
            obj.change_pin(atm_card_no, old_pin)
        elif choose == 8:
            account_no = int(input("please enter your account no:"))
            obj_loan.apply_for_loan(account_no=account_no)
        elif choose == 9:
            loan_account_no = int(input("please enter your loan account no:"))
            amount = float(input("how mach do you want to emi deposite:"))
            obj_loan.emi_deposite(
                loan_account_no=loan_account_no, emi_deposite=amount)
        elif choose == 10:
            loan_account_no = int(input("please enter your loan account no:"))
            obj_loan.check_outstanding_balance(loan_account_no)
        else:
            print("please enter correct option")
