class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(self.owner + ", Your balance is " + str(self.balance)+ " tenge")
    def deposit(self, moneyplus):
        self.balance = self.balance + moneyplus
        print("Operation has been carried out succesfully")
        print(self.owner + ", Your balance now is " + str(self.balance)+ " tenge")
    def withdraw(self, moneyminus):
        self.balance = self.balance - moneyminus
        if self.balance < 0:
            print("Error!!!")
            print("Not enough money on your bank account!")
        else:
            print("Operation has been carried out succesfully")
            print(self.owner + ", Your balance now is " + str(self.balance)+ " tenge")
a = Account("Ali Zhanzakov", 10000)
a.deposit(20000)
a.withdraw(30000)
a.deposit(3000)
a.withdraw(5000)