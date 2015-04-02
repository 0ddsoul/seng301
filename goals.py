class Goal:
#constructor for goals
	def __init__(self, name, amount):
		self.name = name
		self.amount = amount
#deduct paid amount from goal total
	def makePayment(self, amount):
		self.amount -= amount
#increase the amount left to pay for the goal
	def increaseGoal(self, amount):
		self.amount += amount
#get the name of the goal
	def getName(self):
		return self.name
#get amount left to pay for goal
	def getAmount(self):
		return self.amount
