class Budget:
#contruct budget
	def __init__(self, amount): 
		self.amount = amount
		self.initialAmount = amount
#lowers the budget by specifed amount	
	def lowerFunds(self, amount):
		self.amount -= amount
#Resets budget based on user input		
	def reset(self):
		self.amount = self.initialAmount
#Gets the amount of budget left
	def getRemaining(self):
		return self.amount
		
	
