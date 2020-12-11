class Balance:
    def __init__(self, account_number):
        self.money = 100
        self.account_number = account_number

    def getBalance(self, account_number):
        if account_number != self.account_number:
            return False
        return self.money

    def withdraw(self, account_number, withdraw_money):
        if account_number != self.account_number:
            return False
        self.money = self.getBalance(account_number)
        if self.money - withdraw_money < 0:
            print("false withdraw money")
            return False
        else:
            self.money -= withdraw_money
        return self.money
        
    def deposit(self,  account_number, withdraw_money):
        if account_number != self.account_number:
            return False
        self.money = self.getBalance(account_number)
        self.money += withdraw_money
        return self.money