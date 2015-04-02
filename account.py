import userInterface

#Initialize account
class Account:
    def __init__(self, name, amount, accountType):
        self.name = name
        self.amount = amount
        self.accountType = accountType
#use add funds to increase account amount total
    def addFunds(self, amount):
        self.amount += amount
#decrements the total funds in the account
    def removeFunds(self, amount):
        self.amount -= amount
#returns the name of the account
    def getName(self):
        return self.name
#returns the amount in the account
    def getAmount(self):
        return self.amount
#returns the type of the account
    def getAccountType(self):
        return self.accountType
#allows to change name of the account
    def setName(self, new_name):
        self.name = new_name
#Allows to change the funds in the account
    def setAmount(self, new_amount):
        self.amount = new_amount
#Allows to change the type of the account
    def setAccountType(self, new_account_type):
        self.accountType = new_account_type

#Runs through the list of accounts and looks for account of specified name
def findAccount(account_name):
    found = False
    for account_item in userInterface.AccountList:
        if account_item.getName() == account_name:
            return account_item
            found = True
    if found == False: return userInterface.AccountList[0]
