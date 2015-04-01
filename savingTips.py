class SavingTips:
	def __init__(self, history):
		self.history = history
		
	def updateHistory(self, history):
		self.history = history

	def getTip(self):
		housing = 0
		transportation = 0
		food = 0
		entertainment = 0
		insurance = 0
		apparel = 0
		taxes = 0
		services = 0
		
		paymentTypes = ["housing", "transportation", "food", "entertainment", "insurance", "apparel", "taxes", "services"]
		
		for payment in self.history:
			if payment[0] == "Food":
				food += payment[1]
			elif payment[0] == "Housing":
				housing += payment[1]
			elif payment[0] == "Transportation":
				transportation += payment[1]
			elif payment[0] == "Entertainment":
				entertainment += payment[1]
			elif payment[0] == "Insurance":
				insurance += payment[1]
			elif payment[0] == "Apparel":
				apparel += payment[1]
			elif payment[0] == "Taxes":
				taxes += payment[1]
			elif payment[0] == "Services":
				services += payment[1]
				
		payments = [housing, transportation, food, entertainment, insurance, apparel, taxes, services]
		mostMoney = max(payments)
		if mostMoney == 0:
			return "You have spent no money."
		typeOfMost = payments.index(mostMoney)
		typeOfMost = paymentTypes[typeOfMost]
		
		return "You spend the most on " + typeOfMost + ", you should cut down on that if possible."
		
		
