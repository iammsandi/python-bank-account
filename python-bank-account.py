class bankaccount: 
def __init__(self, name, balance):
    self.name = name
    self.balance = balance 
    def desposit (self, amount ):
    self.balance += amount
    def withdraw (self, amount):
    self.balnce -= amount 
    
    def display(self):
    print("Account Holder:", self.name)
    print("Balance:", self.balance)
Account1 = bankaccount("Rewaldo  Mkhumbane", 1000)
account1.desposit(500)
account1.withdraw(200)
Account1.display()