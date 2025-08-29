class Account:
    def __init__(self,balance,acc_no):
        self.balance = balance
        self.acc_no = acc_no
        
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount, "was debited")
        print("Total balance = ", self.get_balance())
    
    
    def credit(self,amount):
        self.balance += amount
        print("rs.",amount , "was credited")
        print("Total balance = ", self.get_balance())
        
    def get_balance(self):
        return self.balance

acc1 = Account(100000, 98786756)
acc1.debit(30000)
acc1.credit(40000)