import kivy
kivy.require('1.8.0')  # replace with your current kivy version !

from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.dropdown import DropDown
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.uix.image import Image

from functools import partial
from account import Account
from budget import Budget
from debt import Debt
import account
import extras_functions
from goals import Goal
from paymentHistory import PaymentHistory
from savingTips import SavingTips
from spendingTips import SpendingTips

#manipulatable touples and lists for debt
debt1 = Debt("No Debt", 0)
debt2 = Debt("No Debt", 0)
debt3 = Debt("No Debt", 0)
debt4 = Debt("No Debt", 0)
debt5 = Debt("No Debt", 0)
debtList =[debt1, debt2, debt3, debt4, debt5]
#manipulatable touples and lists for goals
goal1 = Goal("No Goal", 0)
goal2 = Goal("No Goal", 0)
goal3 = Goal("No Goal", 0)
goal4 = Goal("No Goal", 0)
goal5 = Goal("No Goal", 0)
goalList =[goal1, goal2, goal3, goal4, goal5]
#manipulatable touples and lists for accounts
account1 = Account("This account", 0, "Exist")
account2 = Account("This account", 0, "Exist")
account3 = Account("This account", 0, "Exist")
account4 = Account("This account", 0, "Exist")
account5 = Account("This account", 0, "Exist")
AccountList = [account1, account2, account3, account4, account5]
#The budget [total, remaining]
BudgetList = [0, 0]
Payment_History= PaymentHistory()
#Options for spending
TypeList = ["Housing", "Transportation", "Food", "Entertainment", "Insurance", "Apparel", "Taxes", "Services"]

# UI for the main home screen
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        root = Accordion(orientation='vertical')  # The home screen will have an accordion menu

        #The title screen, hosts the image
        PictureScreen = AccordionItem(title='Peanut Storm Finance Manager')
        PictureScreen_layout = GridLayout(cols=1, padding=0, spacing=0)
        wimg = Image(source='sun.jpg')
	
        PictureScreen_layout.add_widget(wimg)
        PictureScreen.add_widget(PictureScreen_layout)

        # The manage Menu
        manage = AccordionItem(title='Manage')

        manage_layout = GridLayout(cols=3, padding=50, spacing=15)
        # creates buttons for the "Manage" menu
        accounts = Button(text='Manage Accounts')
        accounts.bind(on_press=self.accounts_pressed)

        payments = Button(text='Payments')
        payments.bind(on_press=self.payments_pressed)

        debt = Button(text='Debt Manager')
        debt.bind(on_press=self.debt_pressed)

        history = Button(text='History')
        history.bind(on_press=self.history_pressed)

        budget = Button(text='Budget')
        budget.bind(on_press=self.budget_pressed)

        goals = Button(text='Goals')
        goals.bind(on_press=self.goals_pressed)

        manage_layout.add_widget(accounts)
        manage_layout.add_widget(payments)
        manage_layout.add_widget(debt)
        manage_layout.add_widget(history)
        manage_layout.add_widget(budget)
        manage_layout.add_widget(goals)
        manage.add_widget(manage_layout)

        extras = AccordionItem(title='Extras')
        extras_layout = GridLayout(cols=2, padding=50, spacing=15)

        # Adds buttons for the 'Extras' menu
        tip_calc = Button(text='Tip Calculator')
        tip_calc.bind(on_press=self.tip_pressed)

        bill_split = Button(text='Bill Splitter')
        bill_split.bind(on_press=self.bill_pressed)

        save_money = Button(text='Save Money')
        save_money.bind(on_press=self.save_pressed)

        spend_money = Button(text='Spend Money')
        spend_money.bind(on_press=self.spend_pressed)

        extras_layout.add_widget(tip_calc)
        extras_layout.add_widget(bill_split)
        extras_layout.add_widget(save_money)
        extras_layout.add_widget(spend_money)
        extras.add_widget(extras_layout)

        root.add_widget(PictureScreen)
        root.add_widget(manage)
        root.add_widget(extras)
        PictureScreen.collapse = False  # the 'manage' tab will automatically be open first
        self.add_widget(root)

    # called when user selects the "Manage Accounts" button
    def accounts_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'accounts'

    # called when user selects the "Payments" button
    def payments_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'payments'

    # called when user selects the "Debt Manager" button
    def debt_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'debt'

    # called when user selects the "History" button
    def history_pressed(self, *args):
    	# create popup for the history.
        popupLayout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        title_label = Label(text='[b]Payment History:[/b]', markup=True, size_hint_y=0.25)
        sub_layout = GridLayout(cols=3, padding=50, spacing=10)

        sub_layout.add_widget(Label(text='Payment:'))
        sub_layout.add_widget(Label(text='Amount:'))
        sub_layout.add_widget(Label(text='Account:'))
        #dynamically generate labels based on history in the app
        for entry in Payment_History.getHistory():  # adds information for each entry in the payment history
            for sub_entry in entry:  # adds payment data to sub layout
                label = Label(text=str(sub_entry))
                sub_layout.add_widget(label)

        popupLayout.add_widget(title_label)
        popupLayout.add_widget(sub_layout)
        popup = Popup(title='Accounts', content=popupLayout, size_hint=(None, None), size=(500, 500))
        popup.open()

    # called when user selects the "Budget" button
    def budget_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'budget'

    # called when user selects the "Goals" button
    def goals_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'goal'

    # called when user selects the "Tip Calculator" button
    def tip_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'tipCalc'

    # called when user selects the "Bill Splitter" button
    def bill_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'billSplitter'

    # called when user selects the "Save Money" button
    def save_pressed(self, *args):
        popupLayout = GridLayout(cols=3, padding=50, spacing=10)
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        title_label = Label(text='[b]Tips for Saving Money:[/b]', markup=True)
        
        mySavingTips = SavingTips(Payment_History.getHistory())
        content_label = Label(text= mySavingTips.getTip())

        layout.add_widget(title_label)
        layout.add_widget(content_label)
        popupLayout.add_widget(layout)
            
        popup = Popup(title='Saving Tips',
            content=popupLayout,
            size_hint=(None, None), size=(400, 400))
            
        popup.open()

    # called when user selects the "Spend Money" button
    def spend_pressed(self, *args):
        popupLayout = GridLayout(cols=3, padding=50, spacing=10)
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        title_label = Label(text='[b]Tips for Spending Money:[/b]', markup=True)
        
        mySpendingTips = SpendingTips(AccountList)
        content_label = Label(text=mySpendingTips.getTip()) #Retrive tip for user spending custom to the user's spend-ability.

        layout.add_widget(title_label)
        layout.add_widget(content_label)
        popupLayout.add_widget(layout)
            
        popup = Popup(title='Spending Tips',
            content=popupLayout,
            size_hint=(None, None), size=(400, 400))
            
        popup.open()


# UI for the accounts screen
class AccountsScreen(Screen):
    def __init__(self, **kwargs):
        super(AccountsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        new_button = Button(text='+ New Account')
        new_button.bind(on_press=self.new_pressed)

        modify_button = Button(text='Modify')
        modify_button.bind(on_press=self.modify_pressed)

        view_button = Button(text='View Accounts')
        view_button.bind(on_press=self.view_pressed)

        income_button = Button(text='Add Income')
        income_button.bind(on_press=self.income_pressed)

        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)

        layout.add_widget(new_button)
        layout.add_widget(modify_button)
        layout.add_widget(view_button)
        layout.add_widget(income_button)
        layout.add_widget(menu_button)
        self.add_widget(layout)

    def income_pressed(self, *args):
        popupLayout = BoxLayout(orientation='vertical', padding=50, spacing=10)
        popup = Popup(title='Add an income', content=popupLayout, size_hint=(None, None), size=(400, 400))

        def add_pressed(*args):
            selected_account = account.findAccount(main_button.text)
            income = float(add_input.text)
            selected_account.addFunds(income)
            Payment_History.addNewPayment(description_input.text, "+" + add_input.text, selected_account.getName())
            popup.dismiss()

        account_dropdown = DropDown()
        for account_item in AccountList:
            if account_item.getName() != "This account":
                new_button = Button(text=account_item.getName(), size_hint_y=None, height=44)
                new_button.bind(on_release=lambda btn: account_dropdown.select(btn.text))
                account_dropdown.add_widget(new_button)
        main_button = Button(text='Select an Account')
        main_button.bind(on_release=account_dropdown.open)
        account_dropdown.bind(on_select=lambda instance, x: setattr(main_button, 'text', x))

        add_label = Label(text='Amount to add to account:')
        add_input = TextInput(multiline=False, text='0.00')
        description_label = Label(text='Payer:')
        description_input = TextInput(multiline=False)
        add_button = Button(text='Add Income')
        add_button.bind(on_press=add_pressed)

        popupLayout.add_widget(main_button)
        popupLayout.add_widget(add_label)
        popupLayout.add_widget(add_input)
        popupLayout.add_widget(description_label)
        popupLayout.add_widget(description_input)
        popupLayout.add_widget(add_button)
        popup.open()

    def new_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'newAccount'

    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
        
    def view_pressed(self, *args):
        popupLayout = GridLayout(cols=3, padding=50, spacing=10)
        
        for account_item in AccountList:
            name_label = Label(text=account_item.getName())
            amount_label = Label(text=str(account_item.getAmount()))
            type_label = Label(text=account_item.getAccountType())
            popupLayout.add_widget(name_label)
            popupLayout.add_widget(amount_label)
            popupLayout.add_widget(type_label)
            
        popup = Popup(title='Accounts', content=popupLayout, size_hint=(None, None), size=(400, 400))
        popup.open()

    def modify_pressed(self, *args):
        popupLayout = BoxLayout(padding=50, spacing=10)
        reset_button = Button(text='Reset Accounts')
        reset_button.bind(on_press=self.reset_pressed)
        popupLayout.add_widget(reset_button)
        popup = Popup(title='Modify', content=popupLayout, size_hint=(None, None), size=(400, 400))
        popup.open()

    def reset_pressed(self, *args):
        new_account = Account("This account", "Does not", "Exist")
        for account_item in AccountList:
            index = AccountList.index(account_item)
            AccountList[index] = new_account



# UI for screen that lets user add a new account
class AccountsScreenNewAcct(Screen):
    def __init__(self, **kwargs):
        super(AccountsScreenNewAcct, self).__init__(**kwargs)
        layout = GridLayout(cols=2, padding=50, spacing=10)

        name_label = Label(text='Account Name')
        self.name_input = TextInput(multiline=False)

        type_label = Label(text='Account type: (Credit, debit, etc.)')
        self.type_input = TextInput(multiline=False)

        starting_label = Label(text='Starting Balance:')
        self.starting_input = TextInput(multiline=False, text='0.00')

        limit_label = Label(text='Limit: (optional)')
        self.limit_input = TextInput(multiline=False)

        back_button = Button(text='Back')
        back_button.bind(on_press=self.back_pressed)

        done_button = Button(text='Done')
        done_button.bind(on_press=self.done_pressed)
        
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(type_label)
        layout.add_widget(self.type_input)
        layout.add_widget(starting_label)
        layout.add_widget(self.starting_input)
        layout.add_widget(back_button)
        layout.add_widget(done_button)
        self.add_widget(layout)


    def back_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'accounts'

    def done_pressed(self, *args):
        name = self.name_input.text
        typex = self.type_input.text
        start = self.starting_input.text
        start = float(start)
        newAccount = Account(name, start, typex)
        for account in AccountList:
            if account.getName() == "This account":
                index = AccountList.index(account)
                AccountList[index] = newAccount
                break
        self.manager.transition.direction = 'right'
        self.manager.current = 'accounts'

# UI for screen that lets user add a payment
class PaymentsScreen(Screen):
    main_button = Button(text='Select an Account')
    account_select_button = Button(text='Choose Account')
    amount_input = TextInput(multiline=False, text='0.00')
    type_select_button = Button(text='Choose Type')
    def __init__(self, **kwargs):
        super(PaymentsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)
        sub_layout = GridLayout(cols=2, size_hint_y=None, height=300)  # nested grid layout

        self.account_select_button.bind(on_press=self.select_account_pressed)

        amount_label = Label(text='Amount:')

        type_label = Label(text= 'Payment Type:')

        
        self.type_select_button.bind(on_press=self.type_pressed)

        submit_button = Button(text='Submit Payment')
        submit_button.bind(on_press=self.submit)
       

        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)

        sub_layout.add_widget(self.account_select_button)
        sub_layout.add_widget(self.type_select_button)
        sub_layout.add_widget(amount_label)
        sub_layout.add_widget(self.amount_input)
        

        layout.add_widget(sub_layout)
        layout.add_widget(submit_button)
        layout.add_widget(menu_button)
        self.add_widget(layout)

    def select_account_pressed(self, *args):
        popupLayout = BoxLayout(padding=50, spacing=10)
        account_dropdown = DropDown()
        for account in AccountList:
            if account.getName() != "This account":
                new_button = Button(text=account.getName(), size_hint_y=None, height=44)
                new_button.bind(on_release=lambda btn: account_dropdown.select(btn.text))
                account_dropdown.add_widget(new_button)
        self.main_button = Button(text='Select an Account')
        self.main_button.bind(on_release=account_dropdown.open)
        account_dropdown.bind(on_select=lambda instance, x: setattr(self.account_select_button, 'text', x))
        
        popupLayout.add_widget(self.main_button)
        popup = Popup(title='Select an account', content=popupLayout, size_hint=(None, 0.4), size=(400, 100))
        popup.open()

    def type_pressed(self, *args):
        popupLayout = BoxLayout(padding=50, spacing=10)
        type_dropdown = DropDown()
        for typex in TypeList:
                new_button = Button(text=typex, size_hint_y=None, height=44)
                new_button.bind(on_release=lambda btn: type_dropdown.select(btn.text))
                type_dropdown.add_widget(new_button)
        self.main_button = Button(text='Select a category')
        self.main_button.bind(on_release=type_dropdown.open)
        type_dropdown.bind(on_select=lambda instance, x: setattr(self.type_select_button, 'text', x))
        
        popupLayout.add_widget(self.main_button)
        popup = Popup(title='Select a category', content=popupLayout, size_hint=(None, 0.4), size=(400, 100))
        popup.open()


    def submit(self, *args):
        Accountname = self.account_select_button.text
        Payment = self.amount_input.text
        Payment = float(Payment)
        for account in AccountList:
                if account.getName() == Accountname:
                        account.removeFunds(Payment)
                        Payment_History.addNewPayment(self.type_select_button.text, Payment, account.getName())
                        BudgetList[1] = BudgetList[1] - Payment
                        if (BudgetList[1] < 0 and BudgetList[0]):
                                OverBudget()
                                break	
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
      
    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'


# UI for screen where user can view their debt
class DebtScreen(Screen):
    mainAccount_button = Button(text='Select an Account')
    mainDebt_button = Button(text='Select a Debt')
    amount_input = TextInput(multiline=False, text='0.00')
    name_input = TextInput(multiline=False, text='')
    def __init__(self, **kwargs):
        super(DebtScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        new_button = Button(text='New Debt')
        new_button.bind(on_press=self.new_pressed)

        payment_button = Button(text='Make Payment')
        payment_button.bind(on_press=self.payment_pressed)

        increase_button = Button(text='Increase Debt')
        increase_button.bind(on_press=self.increase_pressed)

        view_button = Button(text='View Debts')
        view_button.bind(on_press=self.view_pressed)

        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)

        layout.add_widget(new_button)
        amount_input = TextInput(multiline=False, text='0.00')
        name_input = TextInput(multiline=False, text='')
        layout.add_widget(increase_button)
        layout.add_widget(payment_button)
        layout.add_widget(view_button)
        layout.add_widget(menu_button)
        self.add_widget(layout)
        
    def increase_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'DebtIncrease'

    def payment_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'DebtPayment'

    


    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
    
    def new_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'newDebt'    
        
    def view_pressed(self, *args):
        popupLayout = GridLayout(cols=2, padding=50, spacing=10)
        
        for debt_item in debtList:
            name_label = Label(text=debt_item.getName())
            amount_label = Label(text=str(debt_item.getAmount()))
            popupLayout.add_widget(name_label)
            popupLayout.add_widget(amount_label)
            
        popup = Popup(title='Debts', content=popupLayout, size_hint=(None, None), size=(400, 400))
        popup.open()
 


class DebtPayment(Screen):
    mainAccount_button = Button(text='Select an Account')
    mainDebt_button = Button(text='Select a Debt')
    amount_input = TextInput(multiline=False, text='0.00')
    def __init__(self, **kwargs):
        super(DebtPayment, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)
        sub_layout = GridLayout(cols=2, size_hint_y=None, height=300)  # nested grid layout

        account_select_button = Button(text='Choose Account')
        account_select_button.bind(on_press=self.select_account_pressed)

        debt_select_button = Button(text='Choose Debt')
        debt_select_button.bind(on_press=self.select_debt_pressed)
                
        amount_label = Label(text='Amount:')

        submit_button = Button(text='Submit Payment')
        submit_button.bind(on_press=self.submit)

        sub_layout.add_widget(amount_label)
        sub_layout.add_widget(self.amount_input)


        layout.add_widget(account_select_button)
        layout.add_widget(debt_select_button)
        layout.add_widget(sub_layout)
        layout.add_widget(submit_button)
        self.add_widget(layout)
        
    def select_account_pressed(self, *args):
        popupLayout = BoxLayout(padding=50, spacing=10)
        account_dropdown = DropDown()
        for account in AccountList:
            if account.getName() != "This account":
                new_button = Button(text=account.getName(), size_hint_y=None, height=44)
                new_button.bind(on_release=lambda btn: account_dropdown.select(btn.text))
                account_dropdown.add_widget(new_button)
        self.mainAccount_button = Button(text='Select an Account')
        self.mainAccount_button.bind(on_release=account_dropdown.open)
        account_dropdown.bind(on_select=lambda instance, x: setattr(self.mainAccount_button, 'text', x))
        
        popupLayout.add_widget(self.mainAccount_button)
        popup = Popup(title='Select an account', content=popupLayout, size_hint=(None, None), size=(400, 400))
        popup.open()   
 
    def select_debt_pressed(self, *args):
        popupLayout = BoxLayout(padding=50, spacing=10)
        account_dropdown = DropDown()
        for debt in debtList:
            if debt.getName() != "No Debt":
                new_button = Button(text=debt.getName(), size_hint_y=None, height=44)
                new_button.bind(on_release=lambda btn: account_dropdown.select(btn.text))
                account_dropdown.add_widget(new_button)
        self.mainDebt_button = Button(text='Select a debt')
        self.mainDebt_button.bind(on_release=account_dropdown.open)
        account_dropdown.bind(on_select=lambda instance, x: setattr(self.mainDebt_button, 'text', x))
        
        popupLayout.add_widget(self.mainDebt_button)
        popup = Popup(title='Select a debt', content=popupLayout, size_hint=(None, None), size=(400, 400))
        popup.open() 
 
    def submit(self, *args):
        Accountname = self.mainAccount_button.text
        Debtname = self.mainDebt_button.text
        Payment = float(self.amount_input.text)
        for account in AccountList:
                if account.getName() == Accountname:
                        account.removeFunds(Payment)
                        Payment_History.addNewPayment("Debt Payment", Payment, account.getName())
                        BudgetList[1] = BudgetList[1] - Payment	
                        break
        for debt in debtList:
                if debt.getName() == Debtname:
                        debt.makePayment(Payment)
                        if (debt.getAmount() <= 0):
                                self.say_gj()
                        if (BudgetList[1] < 0 and BudgetList[0]):
                                OverBudget()
                        break
     
        self.manager.transition.direction = 'right'
        self.manager.current = 'debt'
        
    def say_gj(self, *args):
        popupLayout = GridLayout(cols=3, padding=50, spacing=10)
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        title_label = Label(text='[b]Congratualations![/b]', markup=True)
        
        content_label = Label(text='You paid off your debt!')

        layout.add_widget(title_label)
        layout.add_widget(content_label)
        popupLayout.add_widget(layout)
            
        popup = Popup(title='Congratulations',
            content=popupLayout,
            size_hint=(None, None), size=(400, 400))
            
        popup.open()
 
# UI for screen where user can make a new debt       
class DebtScreenNewDebt(Screen):
    name_label = Label(text='Debt Name')
    name_input = TextInput(multiline=False)

    starting_label = Label(text='Total Amount:')
    starting_input = TextInput(multiline=False, text='0.00')
    def __init__(self, **kwargs):
        super(DebtScreenNewDebt, self).__init__(**kwargs)
        layout = GridLayout(cols=2, padding=50, spacing=10)

        back_button = Button(text='Back')
        back_button.bind(on_press=self.back_pressed)

        done_button = Button(text='Done')
        done_button.bind(on_press=self.done)

        layout.add_widget(self.name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(self.starting_label)
        layout.add_widget(self.starting_input)
        layout.add_widget(back_button)
        layout.add_widget(done_button)
        self.add_widget(layout)


    def back_pressed(self, *args):
        popupLayout = BoxLayout(padding=50, spacing=10)
        account_dropdown = DropDown()
        for debt in debtList:
            if debt.getName() != "No Debt":
                new_button = Button(text=debt.getName(), size_hint_y=None, height=44)
                new_button.bind(on_release=lambda btn: account_dropdown.select(btn.text))
                account_dropdown.add_widget(new_button)
        self.mainDebt_button = Button(text='Select a debt')
        self.mainDebt_button.bind(on_release=account_dropdown.open)
        account_dropdown.bind(on_select=lambda instance, x: setattr(self.mainDebt_button, 'text', x))
        
        popupLayout.add_widget(self.mainDebt_button)
        popup = Popup(title='Select a debt', content=popupLayout, size_hint=(None, None), size=(400, 400))
        popup.open() 
        self.manager.transition.direction = 'right'
        self.manager.current = 'debt'

    def done(self, *args):
        name = self.name_input.text
        start = self.starting_input.text
        start = float(start)
        newDebt = Debt(name, start)
        for debt in debtList:
            if debt.getName() == "No Debt":
                index = debtList.index(debt)
                debtList[index] = newDebt
                break
        self.manager.transition.direction = 'right'
        self.manager.current = 'debt'


class DebtIncrease(Screen):
    mainDebt_button = Button(text='Select a Debt')
    amount_input = TextInput(multiline=False, text='0.00')
    def __init__(self, **kwargs):
        super(DebtIncrease, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)
        sub_layout = GridLayout(cols=2, size_hint_y=None, height=300)  # nested grid layout

        debt_select_button = Button(text='Choose Debt')
        debt_select_button.bind(on_press=self.select_debt_pressed)
                
        amount_label = Label(text='Amount:')

        submit_button = Button(text='Increase Debt')
        submit_button.bind(on_press=self.submit)

        sub_layout.add_widget(amount_label)
        sub_layout.add_widget(self.amount_input)

        layout.add_widget(debt_select_button)
        layout.add_widget(sub_layout)
        layout.add_widget(submit_button)
        self.add_widget(layout)
        
    def select_debt_pressed(self, *args):
        popupLayout = BoxLayout(padding=50, spacing=10)
        account_dropdown = DropDown()
        for debt in debtList:
            if debt.getName() != "No Debt":
                new_button = Button(text=debt.getName(), size_hint_y=None, height=44)
                new_button.bind(on_release=lambda btn: account_dropdown.select(btn.text))
                account_dropdown.add_widget(new_button)
        self.mainDebt_button = Button(text='Select a debt')
        self.mainDebt_button.bind(on_release=account_dropdown.open)
        account_dropdown.bind(on_select=lambda instance, x: setattr(self.mainDebt_button, 'text', x))
        
        popupLayout.add_widget(self.mainDebt_button)
        popup = Popup(title='Select a debt', content=popupLayout, size_hint=(None, None), size=(400, 400))
        popup.open() 
 
    def submit(self, *args):
        Debtname = self.mainDebt_button.text
        Payment = float(self.amount_input.text)
        for debt in debtList:
                if debt.getName() == Debtname:
                        debt.increaseDebt(Payment)
                        break
        self.manager.transition.direction = 'right'
        self.manager.current = 'debt'        



# UI for screen where user can view their budget
class BudgetScreen(Screen):
    set_input = TextInput(multiline=False, text='0.00')
    total_label = Label(text='Total Budget: $%.2f' % BudgetList[0], size_hint_y=None, height=30)
    used_label = Label(text='$%.2f of your budget left!' % BudgetList[1], size_hint_y=None, height=30)
        
    def __init__(self, **kwargs):
        super(BudgetScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)

        
        reset_layout = GridLayout(cols=2)  # this nested layout will hold the options for how often to reset budget
        
        refresh_btn = Button(text='Refresh')
        refresh_btn.bind(on_press=self.refresh)


        submit_button = Button(text='Reset to:')
        submit_button.bind(on_press=self.newBudget)

        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)

        layout.add_widget(self.total_label)
        layout.add_widget(self.used_label)

        reset_layout.add_widget(submit_button) 
        reset_layout.add_widget(self.set_input)       
        layout.add_widget(reset_layout)
        layout.add_widget(refresh_btn)
        layout.add_widget(menu_button)
        self.add_widget(layout)
        
    def refresh(self, *args):
        text='Total Budget: $%.2f' % BudgetList[0]
        self.used_label.text = '$%.2f of your budget left!' % BudgetList[1]
        
        
    def newBudget(self, *args): 
        text='Total Budget: $%.2f' % float(self.set_input.text)
        BudgetList[0] = float(self.set_input.text)
        BudgetList[1] = float(self.set_input.text)
        self.total_label.text = text
        self.used_label.text = '$%.2f of your budget left!' % BudgetList[1]
    
    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'

#The function that is called when you have gone over budget based off budget input and your account
def OverBudget(*args):
	#the grid layout for the popup box
        popupLayout = GridLayout(cols=3, padding=50, spacing=10)
        #the layout for the popup box
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
	#the label of the box
        title_label = Label(text='[b]Over Budget[/b]', markup=True)
        #The over budget label of the notification
        content_label = Label(text='You have exceeded your budget!')
	#Adding all the neccessary widgets to the popup box
        layout.add_widget(title_label)
        layout.add_widget(content_label)
        popupLayout.add_widget(layout)
        #The popup box itself and dimensions
        popup = Popup(title='Over Budget',
            content=popupLayout,
            size_hint=(None, None), size=(400, 400))
            
        popup.open()

# UI for screen where user can view their goal
class GoalsScreen(Screen):
    #The button to select accounts
    mainAccount_button = Button(text='Select an Account')
    #Button to select goal you are working towards
    mainGoals_button = Button(text='Select a Goal')
    #Input taken from users to do the input from account to goal
    amount_input = TextInput(multiline=False, text='0.00')
    #Creating the goal screen when pressed from home interface
    name_input = TextInput(multiline=False, text='')
    def __init__(self, **kwargs):
        super(GoalsScreen, self).__init__(**kwargs)
        #Grid screen layout
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)
        #Creating the new goal button and function call when pressed
        new_button = Button(text='New Goal')
        new_button.bind(on_press=self.new_pressed)
        #Creating payment button and function call
        payment_button = Button(text='Contribute')
        payment_button.bind(on_press=self.payment_pressed)
        #Creating increase goal button and the function call when pressed
        increase_button = Button(text='Increase Goal')
        increase_button.bind(on_press=self.increase_pressed)
        #Creating view goal button and its function call
        view_button = Button(text='View Goals')
        view_button.bind(on_press=self.view_pressed)
        #The button to go back to the homescreen
        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)
        
        #Adding all the widgets to the goal screen
        layout.add_widget(new_button)
        amount_input = TextInput(multiline=False, text='0.00')
        name_input = TextInput(multiline=False, text='')
        layout.add_widget(increase_button)
        layout.add_widget(payment_button)
        layout.add_widget(view_button)
        layout.add_widget(menu_button)
        self.add_widget(layout)
        
        #The transtion left when pressing Increase Goal and moving to the matching screen
    def increase_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'GoalsIncrease'
        #The transtion left when pressing contribute and moving to the matching screen
    def payment_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'GoalsPayment'
        #The transtion right when pressing Back to home sending you back to home screen
    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
        #The transtion left when pressing NewGOal and moving to the matching screen
    def new_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'newGoals'    
        #The function that opens a popup window when pressing View Goals
    def view_pressed(self, *args):
        popupLayout = GridLayout(cols=2, padding=50, spacing=10)
        
        #Inserting the List of goals into the popup menu with name and amount
        for goal_item in goalList:
            name_label = Label(text=goal_item.getName())
            amount_label = Label(text=str(goal_item.getAmount()))
            popupLayout.add_widget(name_label)
            popupLayout.add_widget(amount_label)
        #Just setting up the title of box, its dimensions and its layout
        popup = Popup(title='Goals', content=popupLayout, size_hint=(None, None), size=(400, 400))
        popup.open()
 

#The screen that shows up when pressing contribute
class GoalsPayment(Screen):
    #The button to select accounts
    mainAccount_button = Button(text='Select an Account')
    #The button to select the goal you are contributing towards
    mainGoals_button = Button(text='Select a Goal')
    #Input from account into goal as payment
    amount_input = TextInput(multiline=False, text='0.00')
    
    #Initializing all the buttons and labels for the popup screen
    def __init__(self, **kwargs):
        super(GoalsPayment, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)
        sub_layout = GridLayout(cols=2, size_hint_y=None, height=300)  # nested grid layout
        
        #Making the button and function for pressing Choose Account button
        account_select_button = Button(text='Choose Account')
        account_select_button.bind(on_press=self.select_account_pressed)
        
        #Making the button and function for pressing Choose Goal button
        goal_select_button = Button(text='Choose Goals')
        goal_select_button.bind(on_press=self.select_goal_pressed)
        
        #An amount for the input box        
        amount_label = Label(text='Amount:')
        
        #The button for submitting payment and its function call 
        submit_button = Button(text='Submit Payment')
        submit_button.bind(on_press=self.submit)

        #Adding the amount label and action to the box
        sub_layout.add_widget(amount_label)
        sub_layout.add_widget(self.amount_input)

        #Adding all the widgets to the Contribute Screen
        layout.add_widget(account_select_button)
        layout.add_widget(goal_select_button)
        layout.add_widget(sub_layout)
        layout.add_widget(submit_button)
        self.add_widget(layout)
        
        #The loop that runs to bring down the pulldown menu to select an account
    def select_account_pressed(self, *args):
    	#Creates a pulldown menu 
        popupLayout = BoxLayout(padding=50, spacing=10)
        account_dropdown = DropDown()
        #Goes through the AccountList to find the right account with matching name and creates a new button with it
        for account in AccountList:
            if account.getName() != "This account":
                new_button = Button(text=account.getName(), size_hint_y=None, height=44)
                new_button.bind(on_release=lambda btn: account_dropdown.select(btn.text))
                account_dropdown.add_widget(new_button)
        #This is the button used to select an account to transfer money from 
        self.mainAccount_button = Button(text='Select an Account')
        self.mainAccount_button.bind(on_release=account_dropdown.open)
        account_dropdown.bind(on_select=lambda instance, x: setattr(self.mainAccount_button, 'text', x))
        
        #Adding the dropdown menu to the popupbox
        popupLayout.add_widget(self.mainAccount_button)
        popup = Popup(title='Select an account', content=popupLayout, size_hint=(None, None), size=(400, 400))
        popup.open()   
 
        #The loop that runs to bring down pulldown menu for selecting goals
    def select_goal_pressed(self, *args):
        #Creates pulldown menu
        popupLayout = BoxLayout(padding=50, spacing=10)
        account_dropdown = DropDown()
        #Goes through goalList to find the names of the goalList and creats a button with all the goals on it
        for goal in goalList:
            if goal.getName() != "No Goal":
                new_button = Button(text=goal.getName(), size_hint_y=None, height=44)
                new_button.bind(on_release=lambda btn: account_dropdown.select(btn.text))
                account_dropdown.add_widget(new_button)
        #The selected button is the one used for the Goal working with 
        self.mainGoals_button = Button(text='Select a goal')
        self.mainGoals_button.bind(on_release=account_dropdown.open)
        account_dropdown.bind(on_select=lambda instance, x: setattr(self.mainGoals_button, 'text', x))
        
        #Adding the dropdown menu to the popupbox
        popupLayout.add_widget(self.mainGoals_button)
        popup = Popup(title='Select a goal', content=popupLayout, size_hint=(None, None), size=(400, 400))
        popup.open() 
 
        #The function that runs when submit is selected 
    def submit(self, *args):
    	#Account selected
        Accountname = self.mainAccount_button.text
        #Goal selected
        Goalsname = self.mainGoals_button.text
        #Amount of money to transfer
        Payment = float(self.amount_input.text)
        #The function that gets the account name and performs functions on it
        for account in AccountList:
        	#When account is found
                if account.getName() == Accountname:
                	#remove input amount from total in account
                        account.removeFunds(Payment)
                        #add the transaction to the payment history 
                        Payment_History.addNewPayment("Goals Payment", Payment, account.getName())
                        #updates budget
                        BudgetList[1] = BudgetList[1] - Payment	
                        break
        #The function that gets the goal name and performs functions on it                
        for goal in goalList:
        	#finds the goal
                if goal.getName() == Goalsname:
                	#adds money to the goal progression (subtracts from goal working towards 0)
                        goal.makePayment(Payment)
                        #if goal amount is met popup menu saying with notification
                        if goal.getAmount() <= 0:
                                self.say_gj()
                        #if goal amount is less then zero then display over budget message
                        if (BudgetList[1] < 0 and BudgetList[0]):
                                OverBudget()
                        break
        #transitions right and returns to goal screen 
        self.manager.transition.direction = 'right'
        self.manager.current = 'goal'
        
        #The popup screen displaying the message of congrats for reaching goal
    def say_gj(self, *args):
        #popup box with grid layout
        popupLayout = GridLayout(cols=3, padding=50, spacing=10)
        
        #popup box layout
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        #title label stating congrats
        title_label = Label(text='[b]Congratualations![/b]', markup=True)
        
        #content label stating purpose of notification 
        content_label = Label(text='You have enough money saved up!')
        
        #adding widgets to the main popout screen 
        layout.add_widget(title_label)
        layout.add_widget(content_label)
        popupLayout.add_widget(layout)
        
        #Initializing the popup congrats notification
        popup = Popup(title='Congratulations',
            content=popupLayout,
            size_hint=(None, None), size=(400, 400))
            
        popup.open()
# UI for screen where user can make a new goal       
class GoalsScreenNewGoals(Screen):
    #The goal name and it's input    
    name_label = Label(text='Goal Name')
    name_input = TextInput(multiline=False)
    #Amount of the goal and the input box
    starting_label = Label(text='Starting Amount:')
    starting_input = TextInput(multiline=False, text='0.00')
    def __init__(self, **kwargs):
        super(GoalsScreenNewGoals, self).__init__(**kwargs)
        #layout for the GoalsScreenNewGoals with a grid
        layout = GridLayout(cols=2, padding=50, spacing=10)
        #A back button to return to home screen 
        back_button = Button(text='Back')
        back_button.bind(on_press=self.back_pressed)
        #A done button to finish the creation
        done_button = Button(text='Done')
        done_button.bind(on_press=self.done)
        #adding all the widgets into this window
        layout.add_widget(self.name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(self.starting_label)
        layout.add_widget(self.starting_input)
        layout.add_widget(back_button)
        layout.add_widget(done_button)
        self.add_widget(layout)

        #back pressed button goes to goal screen
    def back_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'goal'
        #done function when pressing done button
    def done(self, *args):
        #goal name and amount    
        name = self.name_input.text
        start = self.starting_input.text
        start = float(start)
        #Creates a new goal object
        newGoals = Goal(name, start)
        #Inserts the new goal into goalList
        for goal in goalList:
            if goal.getName() == "No Goal":
                index = goalList.index(goal)
                goalList[index] = newGoals
                break
        #Returns to goal screen 
        self.manager.transition.direction = 'right'
        self.manager.current = 'goal'
        
#method to increase the goal amount        
class GoalsIncrease(Screen):
    #account button 
    mainAccount_button = Button(text='Select an Account')
    #goal button
    mainGoals_button = Button(text='Select a Goals')
    #amount to input
    amount_input = TextInput(multiline=False, text='0.00')
    def __init__(self, **kwargs):
        super(GoalsIncrease, self).__init__(**kwargs)
        #create the screen for increase
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)
        sub_layout = GridLayout(cols=2, size_hint_y=None, height=300)  # nested grid layout
        #Choose goals button and its function when pressed
        goal_select_button = Button(text='Choose Goals')
        goal_select_button.bind(on_press=self.select_goal_pressed)
        #An amount label        
        amount_label = Label(text='Amount:')
        #The button to submit your changes
        submit_button = Button(text='Increase Goal')
        submit_button.bind(on_press=self.submit)
        #Add widgets to the screen
        sub_layout.add_widget(amount_label)
        sub_layout.add_widget(self.amount_input)


        layout.add_widget(goal_select_button)
        layout.add_widget(sub_layout)
        layout.add_widget(submit_button)
        self.add_widget(layout)
        #function when Choose Goals is pressed
    def select_goal_pressed(self, *args):
        #A popup window
        popupLayout = BoxLayout(padding=50, spacing=10)
        #The dropdown bar
        account_dropdown = DropDown()
        #For getting the list of Goals in the dropdown menu
        for goal in goalList:
            if goal.getName() != "No Goal":
                new_button = Button(text=goal.getName(), size_hint_y=None, height=44)
                new_button.bind(on_release=lambda btn: account_dropdown.select(btn.text))
                account_dropdown.add_widget(new_button)
        #The selected button is now the goal selected        
        self.mainGoals_button = Button(text='Select a goal')
        self.mainGoals_button.bind(on_release=account_dropdown.open)
        account_dropdown.bind(on_select=lambda instance, x: setattr(self.mainGoals_button, 'text', x))
        
        popupLayout.add_widget(self.mainGoals_button)
        popup = Popup(title='Select a goal', content=popupLayout, size_hint=(None, None), size=(400, 400))
        popup.open() 
        #Function for when submit is pressed
    def submit(self, *args):
        #The goal name
        Goalsname = self.mainGoals_button.text
        #The amount gotten from input
        Payment = float(self.amount_input.text)
        #finds the goal in goal list
        for goal in goalList:
                if goal.getName() == Goalsname:
                        #Increases the goal amount
                        goal.increaseGoal(Payment)
                        break
        #Return to goal screen
        self.manager.transition.direction = 'right'
        self.manager.current = 'goal'  
  

        
        
        
# UI for screen that calculates tips
class TipCalcScreen(Screen):
    # initialize all variables
    #The bill label and the box to put input
    bill_label = Label(text='Bill amount:')
    bill_input = TextInput(multiline=False, text='0.00', input_filter='float')
    #The label to select how much of a tip you want 
    ten_label = Label(text='10% Tip:')
    fifteen_label = Label(text='15% Tip:')
    twenty_label = Label(text='20% Tip:')
    other_label = Label(text='Other %')

    ten_button = CheckBox(group='tip')
    fifteen_button = CheckBox(group='tip')
    twenty_button = CheckBox(group='tip')
    other_button = CheckBox(group='tip')

    #The label for tip and the amount of tip to do
    tip_label = Label(text='Tip %:')  # The user can enter a custom tip amount
    tip_input = TextInput(multiline=False, text='0', input_filter='int')

    #A button for Calculating tip and it's labels
    calculate_button = Button(text='Calculate')
    tip_total_label = Label(text='Tip amount: $-.--')
    total_label = Label(text='[b]Total bill amount: $-.--[/b]', markup=True)

    def __init__(self, **kwargs):
        super(TipCalcScreen, self).__init__(**kwargs)
        #The layout for the box for the tipcalculator screen
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        bill_layout = GridLayout(cols=2, spacing=10)  # adds a nested grid layout where user inputs bill amount
        bill_layout.add_widget(self.bill_label)
        bill_layout.add_widget(self.bill_input)

        # Add these options to the tip layout widget
        tip_layout = GridLayout(cols=4)  # adds a nested grid layout with choices for tip %
        tip_layout.add_widget(self.ten_label)
        tip_layout.add_widget(self.ten_button)
        tip_layout.add_widget(self.fifteen_label)
        tip_layout.add_widget(self.fifteen_button)
        tip_layout.add_widget(self.twenty_label)
        tip_layout.add_widget(self.twenty_button)
        tip_layout.add_widget(self.other_label)
        tip_layout.add_widget(self.other_button)
        tip_layout.add_widget(self.tip_label)
        tip_layout.add_widget(self.tip_input)

        self.calculate_button.bind(on_press=partial(self.calculate_pressed, self.total_label, self.tip_total_label))

        calculate_layout = GridLayout(cols=2)  # adds a nested grid layout where the calculated totals are displayed
        calculate_layout.add_widget(self.tip_total_label)
        calculate_layout.add_widget(self.total_label)

        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)
        # add all the widgets to the main layout for this screen
        layout.add_widget(bill_layout)
        layout.add_widget(tip_layout)
        layout.add_widget(self.calculate_button)
        layout.add_widget(calculate_layout)
        layout.add_widget(menu_button)

        self.add_widget(layout)

        #Function that runs when calculate button is pressed 
    def calculate_pressed(self, totalLabel, tipLabel, *args):
        tip_percent = 0
        #the if statements to work with if one of the predetermined tip percentbuttons were pressed
        if self.ten_button.active: tip_percent = 10
        elif self.fifteen_button.active: tip_percent = 15
        elif self.twenty_button.active: tip_percent = 20
        #The if statement taking the userinput of tip amount
        elif self.other_button.active: tip_percent = float(self.tip_input.text)

        #bill amount is the input label
        bill_amount = self.bill_input.text

        #calculates the amount of tip based off the extras_function.calculate_tip
        total_amount, tip_amount = extras_functions.calculate_tip(bill_amount, tip_percent)
        #Label on tip is equal to the calculated amount to 2 decimal places
        tipLabel.text = 'Tip amount: $%.2f' % tip_amount
        totalLabel.text = '[b]Total bill amount: $%.2f[/b]' % total_amount

    def menu_pressed(self, *args):  # called when the "back to menu" button is pressed
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'


# UI for screen that lets users split a bill
class BillSplitterScreen(Screen):
    #bill amount from input box        
    bill_input = TextInput(multiline=False, text='0.00')
    #tip amount from input box
    tip_input = TextInput(multiline=False, text='0')
    #people amount from input box
    people_input = TextInput(multiline=False, text='0')
    tip_box = CheckBox()

    def __init__(self, **kwargs):
        super(BillSplitterScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        input_layout = GridLayout(cols=2)  # adds a nested grid layout for widgets where user inputs bill information
        bill_label = Label(text='Bill Amount:')
        people_label = Label(text='Number of People:')

        # add these widgets to the input layout
        input_layout.add_widget(bill_label)
        input_layout.add_widget(self.bill_input)
        input_layout.add_widget(people_label)
        input_layout.add_widget(self.people_input)

        tip_layout = GridLayout(cols=3) # adds nested grid layout for widgets where user inputs tip information
        tip_label = Label(text='Include tip %:')

        # Add all widgets relating to tip information to the tip layout
        tip_layout.add_widget(tip_label)
        tip_layout.add_widget(self.tip_box)
        tip_layout.add_widget(self.tip_input)

        #the calculate button function and its labels
        calculate_button = Button(text="Calculate")
        total_label = Label(text='Each person pays $-.--.')
        calculate_button.bind(on_press=partial(self.calculate_pressed, total_label))

        #A menu button that returns you to the home screen when pressed
        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)
        # add all widgets on the page to the main layout
        layout.add_widget(input_layout)
        layout.add_widget(tip_layout)
        layout.add_widget(calculate_button)
        layout.add_widget(total_label)
        layout.add_widget(menu_button)
        self.add_widget(layout)

        #function that runs when calculate is pressed
    def calculate_pressed(self, totalLabel, *args):
        tip_percent = 0
        bill_amount = self.bill_input.text
        num_of_people = self.people_input.text
        if self.tip_box.active: tip_percent = self.tip_input.text
        total_amount = extras_functions.calculate_bill_split(bill_amount, num_of_people, tip_percent)
        totalLabel.text = "Each person pays $%.2f" % total_amount

        #return home screen
    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'


# UI for screen where user can view tips for saving money
class SaveMoneyScreen(Screen):
    def __init__(self, **kwargs):
        super(SaveMoneyScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        myPaymentHistory = PaymentHistory()
        title_label = Label(text='[b]Tips for Saving Money:[/b]', markup=True)
        
        #Draws savingtips based off payment history
        mySavingTips = SavingTips(myPaymentHistory.getHistory())
        content_label = Label(text= mySavingTips.getTip())
        #button to return you back to home screen
        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)

        layout.add_widget(title_label)
        layout.add_widget(content_label)
        layout.add_widget(menu_button)
        self.add_widget(layout)
        
        #return home screen
    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'


# UI for screen where user can view tips for spending money
class SpendMoneyScreen(Screen):
    def __init__(self, **kwargs):
        super(SpendMoneyScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        title_label = Label(text='[b]Tips for Spending Money:[/b]', markup=True)
        
        #Draws spendingtips based off payment history
        mySpendingTips = SpendingTips(AccountList)
        content_label = Label(text=mySpendingTips.getTip()) #Retrive tip for user spending custom to the user's spend-ability.

        #button to return you back to home screen
        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)

        layout.add_widget(title_label)
        layout.add_widget(content_label)
        layout.add_widget(menu_button)
        self.add_widget(layout)

        #return home screen
    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
