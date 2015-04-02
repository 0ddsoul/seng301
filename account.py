import userInterface

class Account:
    def __init__(self, name, amount, accountType):
        self.name = name
        self.amount = amount
        self.accountType = accountType

    def addFunds(self, amount):
        self.amount += amount

    def removeFunds(self, amount):
        self.amount -= amount

    def getName(self):
        return self.name

    def getAmount(self):
        return self.amount

    def getAccountType(self):
        return self.accountType

    def setName(self, new_name):
        self.name = new_name

    def setAmount(self, new_amount):
        self.amount = new_amount

    def setAccountType(self, new_account_type):
        self.accountType = new_account_type


def findAccount(account_name):
    found = False
    for account_item in userInterface.AccountList:
        if account_item.getName() == account_name:
            return account_item
            found = True
    if found == False: return userInterface.AccountList[0]
