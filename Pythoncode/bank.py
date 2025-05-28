# Create Account class with 2 attributes - balance & account no. 
#Create methods for debit, credit & printing the balance.

class Account:

    def __init__(self,bal,acc_no):
        self.balance = bal
        self.account_no = acc_no
    
    def credit(self,amt):
        self.balance = self.balance + amt
    def debit(self,amt):
        self.balance = self.balance - amt
    def disp_bal(self):
        return print('Amount is - ',self.balance,' Account number - ',self.account_no)

a1 = Account(1000,'xyzz')
a1.credit(100)
a1.disp_bal()