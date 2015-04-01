class Goals:
	def __init__(self):
		Goal1 = ("Title", 0, 0)
		Goal2 = ("Title", 0, 0)
		Goal3 = ("Title", 0, 0)
		self.GoalList = [Goal1, Goal2, Goal3]
		
	def addNewGoal(self, goalNumber, name, amount):
		newGoal = (name, 0, amount)
		self.GoalList[goalNumber] = newGoal
	
	def contribute(self, goalNumber, amount):
		contribution = self.GoalList[goalNumber][1]
		contribution += amount
		newGoal = (self.GoalList[goalNumber][0], contribution, self.GoalList[goalNumber][2])
		self.GoalList[goalNumber] = newGoal
		
	def deleteGoal(self, goalNumber):
		self.GoalList[goalNumber] = ("Title", 0, 0)
		
	def getGoal(self, goalNumber):
		return self.GoalList[goalNumber][0], self.GoalList[goalNumber][1], self.GoalList[goalNumber][2]
