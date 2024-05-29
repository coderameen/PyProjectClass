class BankManagementSystem:
    #constructor
    def __init__(self):
        self.acc_no = None
        self.acc_holder = None
        self.__balance = 0
        
    def add_user(self,acc_no,acc_holder,amount):
        self.acc_no = acc_no
        self.acc_holder = acc_holder
        self.__balance = amount
        print(f"{acc_holder} has created successfully!!")
        
    def check_balance(self,acc_no):
        if acc_no == self.acc_no:
            print(f"The Account Holder {self.acc_holder} | Balance amount {self.__balance}")
        else:
            print("Invalid Account No")
            
    def credit_amount(self,acc_no,amount):
        if acc_no == self.acc_no:
            self.__balance += amount
            print(f"{amount} has been credited successfully!!")
        else:
            print("Invalid Account Number")
            
            
    def withdraw_amount(self,acc_no,amount):
        if acc_no == self.acc_no:
            self.__balance -= amount
            print(f"{amount} has been debited successfully!!")
        else:
            print("Invalid Accoun no.")
            
    def update_holder(self,acc_no,new_holder):
        if acc_no == self.acc_no:
            self.acc_holder = new_holder
            print(f"{new_holder} name has updated successfully!!")
        else:
            print("Invalid accout number")
        

c1 = BankManagementSystem()
c1.add_user("SBI01","Alen",1000)
c1.credit_amount("SBI01",500)
c1.check_balance("SBI01")
c1.withdraw_amount("SBI01",800)
c1.check_balance("SBI01")
c1.update_holder("SBI01","Alen Walker")
c1.check_balance("SBI01")
c2 = BankManagementSystem()
c2.add_user("SBI02","BOB",10000)
c2.check_balance("SBI02")


