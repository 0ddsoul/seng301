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
		
		paymentTypes = ["Your housing seems to consume the\nlargest portion of your income.\nPerhaps you could downsize?",
		"Your transportation costs are the highest\nof all your expences.\nPerhaps you could pick up biking?", 
		"Try stopping at wholesale grocery stores\nto lower your food costs.", 
		"Your entertainment costs are quite high,\nWork more play less!", 
		"Your insurance costs are very high\ncompared to your other expenses.\nPerhaps expore other insurance providers?", 
		"You spend most of your money on apparel.\nInvesting in high quality products can increase\nthe life of the product significantly.", 
		"Most of your income is going towards taxes.\nConsider depositing some income into a RRSP\nto lower your tax bracket.", 
		"You spend most of your money on services.\nInvesting in high quality products can lower\nthe cost of its maintenance significantly."]
		
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
		
		return typeOfMost
		
		
