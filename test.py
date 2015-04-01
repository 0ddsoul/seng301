import unittest
from account import Account
from budget import Budget
from debt import Debt
from goals import Goals
from paymentHistory import PaymentHistory
from savingTips import SavingTips
from spendingTips import SpendingTips

class TestAccount(unittest.TestCase):
	def testInitAmount(self):
		myAccount = Account("Lukas' Savings", 1000, "Savings")
		expected = 1000
		actual = myAccount.getAmount()
		self.assertEqual(expected, actual)

	def testAccountName(self):
		myAccount = Account("Lukas' Savings", 1000, "Savings")
		expected = "Lukas' Savings"
		actual = myAccount.getName()
		self.assertEqual(expected, actual)
	
	def testAccountType(self):
		myAccount = Account("Lukas' Savings", 1000, "Savings")
		expected = "Savings"
		actual = myAccount.getAccountType()
		self.assertEqual(expected, actual)

	def testAddFunds(self):
		myAccount = Account("Lukas' Savings", 1000, "Savings")
		expected = 1100
		myAccount.addFunds(100)
		actual = myAccount.getAmount()
		self.assertEqual(expected, actual)

	def testRemoveFunds(self):
		myAccount = Account("Lukas' Savings", 1000, "Savings")
		expected = 900
		myAccount.removeFunds(100)
		actual = myAccount.getAmount()
		self.assertEqual(expected, actual)
		
	def testAddAndRemoveFunds(self):
		myAccount = Account("Lukas' Savings", 1000, "Savings")
		expected = 1000
		myAccount.removeFunds(100)
		myAccount.addFunds(100)
		actual = myAccount.getAmount()
		self.assertEqual(expected, actual)

class TestBudget(unittest.TestCase):
	def testInitAmount(self):
		myBudget = Budget("Monthly Moolah", 1000)
		expected = 1000
		actual = myBudget.getRemaining()
		self.assertEqual(expected, actual)

	def testBudgetName(self):
		myBudget = Budget("Monthly Moolah", 1000)
		expected = "Monthly Moolah"
		actual = myBudget.getName()
		self.assertEqual(expected, actual)
		
	def testLowerFunds(self):
		myBudget = Budget("Monthly Moolah", 1000)
		expected = 900
		myBudget.lowerFunds(100)
		actual = myBudget.getRemaining()
		self.assertEqual(expected, actual)
		
	def testReset(self):
		myBudget = Budget("Monthly Moolah", 1000)
		expected = 1000
		myBudget.lowerFunds(100)
		myBudget.reset()
		actual = myBudget.getRemaining()
		self.assertEqual(expected, actual)
		
class TestDebt(unittest.TestCase):
	def testInitAmount(self):
		myDebt = Debt("Lukas' Debt", 1000)
		expected = 1000
		actual = myDebt.getAmount()
		self.assertEqual(expected, actual)
		
	def testName(self):
		myDebt = Debt("Lukas' Debt", 1000)
		expected = "Lukas' Debt"
		actual = myDebt.getName()
		self.assertEqual(expected, actual)
		
	def testMakePayment(self):
		myDebt = Debt("Lukas' Debt", 1000)
		expected = 900
		myDebt.makePayment(100)
		actual = myDebt.getAmount()
		self.assertEqual(expected, actual)
		
	def testIncreaseDebt(self):
		myDebt = Debt("Lukas' Debt", 1000)
		expected =1100
		myDebt.increaseDebt(100)
		actual = myDebt.getAmount()
		self.assertEqual(expected, actual)
		
class TestGoals(unittest.TestCase):
	def testInitName(self):
		myGoals = Goals()
		expected = "Title"
		actual1, actual2, actual3 = myGoals.getGoal(0)
		self.assertEqual(expected, actual1)
		
	def testInitContribution(self):
		myGoals = Goals()
		expected = 0
		actual1, actual2, actual3 = myGoals.getGoal(0)
		self.assertEqual(expected, actual2)
		
	def testInitGoal(self):
		myGoals = Goals()
		expected = 0
		actual1, actual2, actual3 = myGoals.getGoal(0)
		self.assertEqual(expected, actual3)
		
	def testAddGoalName(self):
		myGoals = Goals()
		expected = "TV"
		myGoals.addNewGoal(0, "TV", 3000)
		actual1, actual2, actual3 = myGoals.getGoal(0)
		self.assertEqual(expected, actual1)
		
	def testAddGoalInitContribution(self):
		myGoals = Goals()
		expected = 0
		myGoals.addNewGoal(0, "TV", 3000)
		actual1, actual2, actual3 = myGoals.getGoal(0)
		self.assertEqual(expected, actual2)
		
	def testAddGoalAmount(self):
		myGoals = Goals()
		expected = 3000
		myGoals.addNewGoal(0, "TV", 3000)
		actual1, actual2, actual3 = myGoals.getGoal(0)
		self.assertEqual(expected, actual3)
		
	def testAddGoalWithContribution(self):
		myGoals = Goals()
		expected = 100
		myGoals.addNewGoal(0, "TV", 3000)
		myGoals.contribute(0, 100)
		actual1, actual2, actual3 = myGoals.getGoal(0)
		self.assertEqual(expected, actual2)
		
	def testDeleteGoal(self):
		myGoals = Goals()
		expected = "Title"
		myGoals.addNewGoal(0, "TV", 3000)
		myGoals.contribute(0, 100)
		myGoals.deleteGoal(0)
		actual1, actual2, actual3 = myGoals.getGoal(0)
		self.assertEqual(expected, actual1)
		
	def testAddMultipleGoalName(self):
		myGoals = Goals()
		expected = "TV"
		myGoals.addNewGoal(0, "TV", 3000)
		myGoals.addNewGoal(1, "Trampline", 3000)
		actual1, actual2, actual3 = myGoals.getGoal(0)
		self.assertEqual(expected, actual1)
		
	def testAddMultipleGoalNameTwo(self):
		myGoals = Goals()
		expected = "Trampoline"
		myGoals.addNewGoal(0, "TV", 3000)
		myGoals.addNewGoal(1, "Trampoline", 3000)
		actual1, actual2, actual3 = myGoals.getGoal(1)
		self.assertEqual(expected, actual1)
		
	def testAddMultipleGoalContribution(self):
		myGoals = Goals()
		expected = 100
		myGoals.addNewGoal(0, "TV", 3000)
		myGoals.addNewGoal(1, "Trampline", 3000)
		myGoals.contribute(0, 100)
		actual1, actual2, actual3 = myGoals.getGoal(0)
		self.assertEqual(expected, actual2)
		
	def testAddMultipleGoalContributionTwo(self):
		myGoals = Goals()
		expected = 0
		myGoals.addNewGoal(0, "TV", 3000)
		myGoals.addNewGoal(1, "Trampline", 3000)
		myGoals.contribute(0, 100)
		actual1, actual2, actual3 = myGoals.getGoal(1)
		self.assertEqual(expected, actual2)
		
	def testDeleteWithMultiple(self):
		myGoals = Goals()
		expected = "Title"
		myGoals.addNewGoal(0, "TV", 3000)
		myGoals.addNewGoal(1, "Trampline", 3000)
		myGoals.contribute(0, 100)
		myGoals.deleteGoal(0)
		actual1, actual2, actual3 = myGoals.getGoal(0)
		self.assertEqual(expected, actual1)
		
	def testDeleteWithMultipleTwo(self):
		myGoals = Goals()
		expected = "Title"
		myGoals.addNewGoal(0, "TV", 3000)
		myGoals.addNewGoal(1, "Trampline", 3000)
		myGoals.contribute(0, 100)
		myGoals.deleteGoal(1)
		actual1, actual2, actual3 = myGoals.getGoal(1)
		self.assertEqual(expected, actual1)
		
class TestPaymentHistory(unittest.TestCase):
	def testNoHistory(self):
		myPaymentHistory = PaymentHistory()
		expected = []
		actual = myPaymentHistory.getHistory()
		self.assertEqual(expected, actual)
		
	def testOneHistory(self):
		myPaymentHistory = PaymentHistory()
		expected = [("Food", 10, "March 28, 2015")]
		myPaymentHistory.addNewPayment("Food", 10, "March 28, 2015")
		actual = myPaymentHistory.getHistory()
		self.assertEqual(expected, actual)
		
	def testTwoHistory(self):
		myPaymentHistory = PaymentHistory()
		expected = [("Food", 10, "March 28, 2015"), ("Transportation", 20, "March 29, 2015")]
		myPaymentHistory.addNewPayment("Food", 10, "March 28, 2015")
		myPaymentHistory.addNewPayment("Transportation", 20, "March 29, 2015")
		actual = myPaymentHistory.getHistory()
		self.assertEqual(expected, actual)
		
	def testClearHistory(self):
		myPaymentHistory = PaymentHistory()
		expected = []
		myPaymentHistory.addNewPayment("Food", 10, "March 28, 2015")
		myPaymentHistory.addNewPayment("Transportation", 20, "March 29, 2015")
		myPaymentHistory.clearHistory()
		actual = myPaymentHistory.getHistory()
		self.assertEqual(expected, actual)
		
class TestSavingTips(unittest.TestCase):
	def testEmptyHistory(self):
		myPaymentHistory = PaymentHistory()
		mySavingTips = SavingTips(myPaymentHistory.getHistory())
		expected = "You have spent no money."
		actual = mySavingTips.getTip()
		self.assertEqual(expected, actual)
		
	def testOneHistory(self):
		myPaymentHistory = PaymentHistory()
		mySavingTips = SavingTips(myPaymentHistory.getHistory())
		myPaymentHistory.addNewPayment("Food", 10, "March 28, 2015")
		expected = "You spend the most on food, you should cut down on that if possible."
		actual = mySavingTips.getTip()
		self.assertEqual(expected, actual)
		
	def testMultipleHistory(self):
		myPaymentHistory = PaymentHistory()
		mySavingTips = SavingTips(myPaymentHistory.getHistory())
		myPaymentHistory.addNewPayment("Food", 10, "March 28, 2015")
		myPaymentHistory.addNewPayment("Food", 10, "March 28, 2015")
		myPaymentHistory.addNewPayment("Transportation", 50, "March 28, 2015")
		expected = "You spend the most on transportation, you should cut down on that if possible."
		actual = mySavingTips.getTip()
		self.assertEqual(expected, actual)
		
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
		
class TestSpendingTips(unittest.TestCase):
	def testNoAccount(self):
		mySpendingTips = SpendingTips([])
		expected = "You're poor AF, stop spending money on shit and make some bank."
		actual = mySpendingTips.getTip()
		self.assertEqual(expected, actual)
		
	def testEmptyAccount(self):
		myAccount = Account("Lukas' Savings", 0, "Savings")
		mySpendingTips = SpendingTips([myAccount])
		expected = "You're poor AF, stop spending money on shit and make some bank."
		actual = mySpendingTips.getTip()
		self.assertEqual(expected, actual)
		
	def testNonEmptyAccount(self):
		myAccount = Account("Lukas' Savings", 20, "Savings")
		mySpendingTips = SpendingTips([myAccount])
		expected = "You could go out to the movies."
		actual = mySpendingTips.getTip()
		self.assertEqual(expected, actual)
		
	def testEmptyAccounts(self):
		myAccount = Account("Lukas' Savings", 0, "Savings")
		myAccount2 = Account("Lukas' Chequings", 0, "Chequings")
		mySpendingTips = SpendingTips([myAccount, myAccount2])
		expected = "You're poor AF, stop spending money on shit and make some bank."
		actual = mySpendingTips.getTip()
		self.assertEqual(expected, actual)
		
	def testNonEmptyAccounts(self):
		myAccount = Account("Lukas' Savings", 10, "Savings")
		myAccount2 = Account("Lukas' Chequings", 10, "Chequings")
		mySpendingTips = SpendingTips([myAccount, myAccount2])
		expected = "You could go out to the movies."
		actual = mySpendingTips.getTip()
		self.assertEqual(expected, actual)

unittest.main()
