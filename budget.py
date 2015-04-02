class Budget:
	def __init__(self, resetint, amount): ##reset interval
		self.resetint = resetint
		self.amount = amount
		self.initialAmount = amount
	
	def lowerFunds(self, amount):
		self.amount -= amount
		
	def reset(self):
		self.amount = self.initialAmount

	def getRemaining(self):
		return self.amount

	def getResetint(self):
		return self.resetint
		
	
