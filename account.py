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
