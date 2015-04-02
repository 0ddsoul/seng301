class Goal:
	def __init__(self, name, amount):
		self.name = name
		self.amount = amount
		
	def makePayment(self, amount):
		self.amount -= amount
		
	def increaseGoal(self, amount):
		self.amount += amount
		
	def getName(self):
		return self.name
		
	def getAmount(self):
		return self.amount
