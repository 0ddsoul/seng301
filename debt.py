class Debt:
#constructor for  debt
	def __init__(self, name, amount):
		self.name = name
		self.amount = amount
#reduces the amount left to pay
	def makePayment(self, amount):
		self.amount -= amount
#increases the amount left to pay in debt
	def increaseDebt(self, amount):
		self.amount += amount
#gets the name of the debt
	def getName(self):
		return self.name
#gets the amount left to pay
	def getAmount(self):
		return self.amount
