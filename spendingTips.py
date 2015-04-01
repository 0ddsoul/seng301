class SpendingTips:
	def __init__(self, accounts):
		self.accounts = accounts
		self.renovation = 20000
		self.vacation = 10000
		self.computer = 1500
		self.console = 500
		self.aGame = 70
		self.movie = 15
		
	def getTip(self):
		amount = 0
		for account in self.accounts:
			amount += account.getAmount()
			
		if amount >= self.renovation:
			return "You could afford to do a small home renovation."
		elif amount >= self.vacation:
			return "You could afford to go on a vacation."
		elif amount >= self.computer:
			return "You could afford to buy a decent laptop."
		elif amount >= self.console:
			return "You could afford to buy a new game console."	
		elif amount >= self.aGame:
			return "You could buy a video game if you like."
		elif amount >= self.movie:
			return "You could go out to the movies."
		else:
			return "You're poor AF, stop spending money on shit and make some bank."
