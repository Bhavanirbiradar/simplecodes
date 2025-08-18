class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc
    def credit(self,amount):
        self.amount=amount
        self.balance+=amount
        print("Balance after credit is", self.balance)
        print(self.check())
    def debit(self,amount):
        self.amount=amount
        self.balance-=amount
        print("Balance after debit is", self.balance) 
        print(self.check()) 
    def check(self):
        #print("Current balance is", self.balance)
        return self.balance
         
s1=account(100,1234)
s1.credit(50)
s1.debit(200)
s2=account(200,5678)
s2.credit(100)      

s2.debit(50)