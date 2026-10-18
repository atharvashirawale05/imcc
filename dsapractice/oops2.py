class Accounts:
    def __init__(self,bal,acc):
         self.balance=bal
         self.accountno=acc
    def debit(self,amount):
         self.balance-=amount
         print("rs.",amount,"was debited")
         print("remaining balance is :",self.get_balance())
    def credit(self,amount):
         self.balance+=amount
         print("rs.",amount,"was credited")
         print("remaining balance is :",self.get_balance())
    def get_balance(self):
        return self.balance
acc1=Accounts(10000,12345)
acc1.debit(1000)
acc1.credit(2000)
 
          
