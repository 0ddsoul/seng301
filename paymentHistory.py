class PaymentHistory:
#Construct payment history as an empty list
    def __init__(self):
        self.history = []
#adds a new payment to the history list
    def addNewPayment(self, paymentType, amount, account):
        newPaymentTup = (paymentType, amount, account)
        self.history.append(newPaymentTup)
#clears the history list
    def clearHistory(self):
        self.history = []
#retrieves the history list
    def getHistory(self):
        return self.history
