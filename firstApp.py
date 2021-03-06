import kivy
kivy.require('1.8.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

import userInterface


class MyApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        # adds all the pages in the app to the screen manager
        sm.add_widget(userInterface.HomeScreen(name='home'))

        sm.add_widget(userInterface.AccountsScreen(name='accounts'))
        sm.add_widget(userInterface.AccountsScreenNewAcct(name='newAccount'))
        sm.add_widget(userInterface.PaymentsScreen(name='payments'))
        sm.add_widget(userInterface.DebtScreen(name='debt'))
        sm.add_widget(userInterface.DebtScreenNewDebt(name='newDebt'))
        sm.add_widget(userInterface.DebtPayment(name='DebtPayment'))
        sm.add_widget(userInterface.DebtIncrease(name='DebtIncrease'))
        sm.add_widget(userInterface.BudgetScreen(name='budget'))
        sm.add_widget(userInterface.GoalsScreen(name='goal'))
        sm.add_widget(userInterface.GoalsPayment(name='GoalsPayment'))
        sm.add_widget(userInterface.GoalsScreenNewGoals(name='newGoals'))
        sm.add_widget(userInterface.GoalsIncrease(name='GoalsIncrease'))
        sm.add_widget(userInterface.TipCalcScreen(name='tipCalc'))
        sm.add_widget(userInterface.BillSplitterScreen(name='billSplitter'))
        sm.add_widget(userInterface.SaveMoneyScreen(name='saveMoney'))
        sm.add_widget(userInterface.SpendMoneyScreen(name='spendMoney'))

        return sm
#executes the program
if __name__ == '__main__':
    MyApp().run()

