import unittest
from account import Account
from budget import Budget
from debt import Debt
from goals import Goals
from paymentHistory import PaymentHistory
from savingTips import SavingTips
from spendingTips import SpendingTips

#Tests for the account closs
class TestAccount(unittest.TestCase):
	#Checking initial amount
	def testInitAmount(self):
		myAccount = Account("Lukas' Savings", 1000, "Savings")
		expected = 1000
		actual = myAccount.getAmount()
		self.assertEqual(expected, actual)
	
	#Checking initial name
	def testAccountName(self):
		myAccount = Account("Lukas' Savings", 1000, "Savings")
		expected = "Lukas' Savings"
		actual = myAccount.getName()
		self.assertEqual(expected, actual)
	
	#Checking account type
	def testAccountType(self):
		myAccount = Account("Lukas' Savings", 1000, "Savings")
		expected = "Savings"
		actual = myAccount.getAccountType()
		self.assertEqual(expected, actual)
	
	#Testing the add funds function
	def testAddFunds(self):
		myAccount = Account("Lukas' Savings", 1000, "Savings")
		expected = 1100
		myAccount.addFunds(100)
		actual = myAccount.getAmount()
		self.assertEqual(expected, actual)
	
	#Testing the remove funds function
	def testRemoveFunds(self):
		myAccount = Account("Lukas' Savings", 1000, "Savings")
		expected = 900
		myAccount.removeFunds(100)
		actual = myAccount.getAmount()
		self.assertEqual(expected, actual)
	
	#Testting both add and remove
	def testAddAndRemoveFunds(self):
		myAccount = Account("Lukas' Savings", 1000, "Savings")
		expected = 1000
		myAccount.removeFunds(100)
		myAccount.addFunds(100)
		actual = myAccount.getAmount()
		self.assertEqual(expected, actual)

#Tests for budget class
class TestBudget(unittest.TestCase):
	#Test intital amount
	def testInitAmount(self):
		myBudget = Budget("Monthly Moolah", 1000)
		expected = 1000
		actual = myBudget.getRemaining()
		self.assertEqual(expected, actual)
	
	#Test name
	def testBudgetName(self):
		myBudget = Budget("Monthly Moolah", 1000)
		expected = "Monthly Moolah"
		actual = myBudget.getName()
		self.assertEqual(expected, actual)
	
	#Test the lower funds function	
	def testLowerFunds(self):
		myBudget = Budget("Monthly Moolah", 1000)
		expected = 900
		myBudget.lowerFunds(100)
		actual = myBudget.getRemaining()
		self.assertEqual(expected, actual)
	
	#Test the reset function
	def testReset(self):
		myBudget = Budget("Monthly Moolah", 1000)
		expected = 1000
		myBudget.lowerFunds(100)
		myBudget.reset()
		actual = myBudget.getRemaining()
		self.assertEqual(expected, actual)

#Test the debt class		
class TestDebt(unittest.TestCase):
	#Test initial amount
	def testInitAmount(self):
		myDebt = Debt("Lukas' Debt", 1000)
		expected = 1000
		actual = myDebt.getAmount()
		self.assertEqual(expected, actual)
	
	#Test the name	
	def testName(self):
		myDebt = Debt("Lukas' Debt", 1000)
		expected = "Lukas' Debt"
		actual = myDebt.getName()
		self.assertEqual(expected, actual)
	
	#Test the make payment function
	def testMakePayment(self):
		myDebt = Debt("Lukas' Debt", 1000)
		expected = 900
		myDebt.makePayment(100)
		actual = myDebt.getAmount()
		self.assertEqual(expected, actual)
	
	#Test the increase debt function	
	def testIncreaseDebt(self):
		myDebt = Debt("Lukas' Debt", 1000)
		expected =1100
		myDebt.increaseDebt(100)
		actual = myDebt.getAmount()
		self.assertEqual(expected, actual)

#Test the goals class	
class TestGoals(unittest.testcase):
	#Test initial amount
	def testInitAmount(self):
		myGoal = Goal("Lukas' Goal", 1000)
		expected = 1000
		actual = Goal.getAmount()
		self.assertEqual(expected, actual)
	
	#Test the name	
	def testName(self):
		myGoal = Goal("Lukas' Goal", 1000)
		expected = "Lukas' Goal"
		actual = Goal.getName()
		self.assertEqual(expected, actual)
	
	#Test the make payment function
	def testMakePayment(self):
		myGoal = Goal("Lukas' Goal", 1000)
		expected = 900
		myGoal.makePayment(100)
		actual = myGoal.getAmount()
		self.assertEqual(expected, actual)
	
	#Test the increase goal function	
	def testIncreaseGoal(self):
		myGoal = Debt("Lukas' Goal", 1000)
		expected =1100
		myGoal.increaseGoal(100)
		actual = myGoal.getAmount()
		self.assertEqual(expected, actual)
#Test the payment history class		
class TestPaymentHistory(unittest.TestCase):
	#Test empty history
	def testNoHistory(self):
		myPaymentHistory = PaymentHistory()
		expected = []
		actual = myPaymentHistory.getHistory()
		self.assertEqual(expected, actual)
	
	#Test single history	
	def testOneHistory(self):
		myPaymentHistory = PaymentHistory()
		expected = [("Food", 10, "March 28, 2015")]
		myPaymentHistory.addNewPayment("Food", 10, "March 28, 2015")
		actual = myPaymentHistory.getHistory()
		self.assertEqual(expected, actual)
	
	#Test multi history	
	def testTwoHistory(self):
		myPaymentHistory = PaymentHistory()
		expected = [("Food", 10, "March 28, 2015"), ("Transportation", 20, "March 29, 2015")]
		myPaymentHistory.addNewPayment("Food", 10, "March 28, 2015")
		myPaymentHistory.addNewPayment("Transportation", 20, "March 29, 2015")
		actual = myPaymentHistory.getHistory()
		self.assertEqual(expected, actual)
	
	#Test clear function	
	def testClearHistory(self):
		myPaymentHistory = PaymentHistory()
		expected = []
		myPaymentHistory.addNewPayment("Food", 10, "March 28, 2015")
		myPaymentHistory.addNewPayment("Transportation", 20, "March 29, 2015")
		myPaymentHistory.clearHistory()
		actual = myPaymentHistory.getHistory()
		self.assertEqual(expected, actual)

#Test the saving tips class		
class TestSavingTips(unittest.TestCase):
	#Test on empty history
	def testEmptyHistory(self):
		myPaymentHistory = PaymentHistory()
		mySavingTips = SavingTips(myPaymentHistory.getHistory())
		expected = "You have spent no money."
		actual = mySavingTips.getTip()
		self.assertEqual(expected, actual)
	
	#Test on one history	
	def testOneHistory(self):
		myPaymentHistory = PaymentHistory()
		mySavingTips = SavingTips(myPaymentHistory.getHistory())
		myPaymentHistory.addNewPayment("Food", 10, "March 28, 2015")
		expected = "Try stopping at wholesale grocery stores\nto lower your food costs." 
		actual = mySavingTips.getTip()
		self.assertEqual(expected, actual)
	
	#Test on multi history	
	def testMultipleHistory(self):
		myPaymentHistory = PaymentHistory()
		mySavingTips = SavingTips(myPaymentHistory.getHistory())
		myPaymentHistory.addNewPayment("Food", 10, "March 28, 2015")
		myPaymentHistory.addNewPayment("Food", 10, "March 28, 2015")
		myPaymentHistory.addNewPayment("Transportation", 50, "March 28, 2015")
		expected = "Your transportation costs are the highest\nof all your expences.\nPerhaps you could pick up biking?"
		actual = mySavingTips.getTip()
		self.assertEqual(expected, actual)
	
	#Test a cleared history
	def testClearedHistory(self):
		myPaymentHistory = PaymentHistory()
		mySavingTips = SavingTips(myPaymentHistory.getHistory())
		myPaymentHistory.addNewPayment("Food", 10, "March 28, 2015")
		myPaymentHistory.addNewPayment("Food", 10, "March 28, 2015")
		myPaymentHistory.addNewPayment("Transportation", 50, "March 28, 2015")
		myPaymentHistory.clearHistory()
		mySavingTips.updateHistory(myPaymentHistory.getHistory())
		expected = "You have spent no money."
		actual = mySavingTips.getTip()
		self.assertEqual(expected, actual)

#Test the spending tips class		
class TestSpendingTips(unittest.TestCase):
	#Test when theres no account
	def testNoAccount(self):
		mySpendingTips = SpendingTips([])
		expected = "You're poor AF, stop spending money on shit and make some bank."
		actual = mySpendingTips.getTip()
		self.assertEqual(expected, actual)
	
	#Test when the account is empty	
	def testEmptyAccount(self):
		myAccount = Account("Lukas' Savings", 0, "Savings")
		mySpendingTips = SpendingTips([myAccount])
		expected = "You have less than 15 dollars.\nPerhaps you should save more?"
		actual = mySpendingTips.getTip()
		self.assertEqual(expected, actual)
	
	#Test when the account is not empty	
	def testNonEmptyAccount(self):
		myAccount = Account("Lukas' Savings", 20, "Savings")
		mySpendingTips = SpendingTips([myAccount])
		expected = "You could go out to the movies."
		actual = mySpendingTips.getTip()
		self.assertEqual(expected, actual)
	
	#Test multiple empty accounts	
	def testEmptyAccounts(self):
		myAccount = Account("Lukas' Savings", 0, "Savings")
		myAccount2 = Account("Lukas' Chequings", 0, "Chequings")
		mySpendingTips = SpendingTips([myAccount, myAccount2])
		expected = "You have less than 15 dollars.\nPerhaps you should save more?"
		actual = mySpendingTips.getTip()
		self.assertEqual(expected, actual)
	
	#Test multiple non empty accounts	
	def testNonEmptyAccounts(self):
		myAccount = Account("Lukas' Savings", 10, "Savings")
		myAccount2 = Account("Lukas' Chequings", 10, "Chequings")
		mySpendingTips = SpendingTips([myAccount, myAccount2])
		expected = "You could go out to the movies."
		actual = mySpendingTips.getTip()
		self.assertEqual(expected, actual)

unittest.main()
