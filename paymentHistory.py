class PaymentHistory:
	def __init__(self):
		self.history = []
		
	def addNewPayment(self, paymentType, amount, date):
		newPaymentTup = (paymentType, amount, date)
		self.history.append(newPaymentTup)
		
	def clearHistory(self):
		self.history = []
		
	def getHistory(self):
		return self.history
