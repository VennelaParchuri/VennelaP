# Account Challange

class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        print (f'total balance is {self.balance}')
        amount = int(input('Enter the amount you want to deposit: '))
        self.balance = self.balance + amount
        print (f'total balance is {self.balance}')
    def withdraw(self):
        print (f'total balance is {self.balance}')
        amount1 = int(input('Enter the amount you want to deposit: '))
        if (self.balance-amount1)> 0:
            print('Please collect the amount {} and the remaining balance is {}'.format(amount1, (self.balance-amount1)))
            self.balance = self.balance - amount1
        else:
            print('Insufficient funds. Your balance is {}'.format(self.balance))
            