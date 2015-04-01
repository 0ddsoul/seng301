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
import extras_functions
from goals import Goals
from paymentHistory import PaymentHistory
from savingTips import SavingTips
from spendingTips import SpendingTips

account1 = Account("This account", "Does not", "Exist")
account2 = Account("This account", "Does not", "Exist")
account3 = Account("This account", "Does not", "Exist")
account4 = Account("This account", "Does not", "Exist")
account5 = Account("This account", "Does not", "Exist")
AccountList = [account1, account2, account3, account4, account5]

# UI for the main home screen
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        root = Accordion(orientation='vertical')  # The home screen will have an accordion menu

        #The title screen
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
        self.manager.transition.direction = 'left'
        self.manager.current = 'history'

    # called when user selects the "Budget" button
    def budget_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'budget'

    # called when user selects the "Goals" button
    def goals_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'goals'

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
        self.manager.transition.direction = 'left'
        self.manager.current = 'saveMoney'

    # called when user selects the "Spend Money" button
    def spend_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'spendMoney'


# UI for the accounts screen
class AccountsScreen(Screen):
    def __init__(self, **kwargs):
        super(AccountsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        new_button = Button(text='+ New Account')
        new_button.bind(on_press=self.new_pressed)

        modify_button = Button(text='Modify')

        view_button = Button(text='View Accounts')
        view_button.bind(on_press=self.view_pressed)

        income_button = Button(text='Add Income')

        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)

        layout.add_widget(new_button)
        layout.add_widget(modify_button)
        layout.add_widget(view_button)
        layout.add_widget(income_button)
        layout.add_widget(menu_button)
        self.add_widget(layout)

    def new_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'newAccount'

    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
        
    def view_pressed(self, *args):
        popupLayout = GridLayout(cols=3, padding=50, spacing=10)
        
        for account in AccountList:
            name_label = Label(text=account.getName())
            amount_label = Label(text=str(account.getAmount()))
            type_label = Label(text=account.getAccountType())
            popupLayout.add_widget(name_label)
            popupLayout.add_widget(amount_label)
            popupLayout.add_widget(type_label)
            
        popup = Popup(title='Accounts',
            content=popupLayout,
            size_hint=(None, None), size=(400, 400))
            
        popup.open()

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
       # layout.add_widget(limit_label)
       # layout.add_widget(limit_input)
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
            if account.getName() == "This Account":
                index = AccountList.index(account)
                AccountList[index] = newAccount
                break
        self.manager.transition.direction = 'right'
        self.manager.current = 'accounts'

# UI for screen that lets user add a payment
class PaymentsScreen(Screen):
    def __init__(self, **kwargs):
        super(PaymentsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)
        sub_layout = GridLayout(cols=2, size_hint_y=None, height=300)  # nested grid layout

        account_label = Label(text='Choose Account:')
        account_input = TextInput(multiline=False)

        amount_label = Label(text='Amount:')
        amount_input = TextInput(multiline=False, text='0.00')

        one_time_label = Label(text='One time')
        one_time_button = CheckBox(group='radio')

        recurring_label = Label(text='Recurring')
        recurring_button = CheckBox(group='radio')

        weekly_grid = GridLayout(cols=2)
        weekly_label = Label(text="Weekly:")
        weekly_button = CheckBox()
        weekly_grid.add_widget(weekly_label)
        weekly_grid.add_widget(weekly_button)

        monthly_grid = GridLayout(cols=2)
        monthly_label = Label(text='Monthly:')
        monthly_button = CheckBox()
        monthly_grid.add_widget(monthly_label)
        monthly_grid.add_widget(monthly_button)

        yearly_grid = GridLayout(cols=2)
        yearly_label = Label(text='Yearly:')
        yearly_button = CheckBox()
        yearly_grid.add_widget(yearly_label)
        yearly_grid.add_widget(yearly_button)

        submit_button = Button(text='Submit Payment')

        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)

        sub_layout.add_widget(account_label)
        sub_layout.add_widget(account_input)
        sub_layout.add_widget(amount_label)
        sub_layout.add_widget(amount_input)
        sub_layout.add_widget(one_time_label)
        sub_layout.add_widget(one_time_button)
        sub_layout.add_widget(recurring_label)
        sub_layout.add_widget(recurring_button)

        sub_layout.add_widget(weekly_grid)
        sub_layout.add_widget(monthly_grid)
        sub_layout.add_widget(yearly_grid)

        layout.add_widget(sub_layout)
        layout.add_widget(submit_button)
        layout.add_widget(menu_button)
        self.add_widget(layout)

    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'


# UI for screen where user can view their debt
class DebtScreen(Screen):
    def __init__(self, **kwargs):
        super(DebtScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        add_button = Button(text='Add New Debt')
        title_label = Label(text='[b]Current Debts:[/b]', markup=True)
        info_label = Label(text='No current debts to display')

        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)

        layout.add_widget(add_button)
        layout.add_widget(title_label)
        layout.add_widget(info_label)
        layout.add_widget(menu_button)
        self.add_widget(layout)

    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'


# UI for screen where user can view their payment history
class HistoryScreen(Screen):
    def __init__(self, **kwargs):
        super(HistoryScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        title_label = Label(text='[b]Payment History:[/b]', markup=True)
        info_label = Label(text='No payment history to show')

        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)

        layout.add_widget(title_label)
        layout.add_widget(info_label)
        layout.add_widget(menu_button)
        self.add_widget(layout)

    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'


# UI for screen where user can view their budget
class BudgetScreen(Screen):
    def __init__(self, **kwargs):
        super(BudgetScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)

        total_label = Label(text='Total Budget: $-.--', size_hint_y=None, height=30)
        used_label = Label(text='$-.-- of your budget has been used!', size_hint_y=None, height=30)
        over_label = Label(text='you are $-.-- over budget.', size_hint_y=None, height=30)

        set_label = Label(text='[b]Set Budget:[/b]', markup=True)
        set_input = TextInput(multiline=False, text='0.00')

        reset_layout = GridLayout(cols=2)  # this nested layout will hold the options for how often to reset budget
        reset_label = Label(text='Reset:')
        reset_sub_layout = GridLayout(cols=2, spacing=10)  # this layout will hold the options' labels + checkboxes
        daily_label = Label(text='Daily')
        daily_box = CheckBox(group='reset')
        weekly_label = Label(text='Weekly')
        weekly_box = CheckBox(group='reset')
        monthly_label = Label(text='Monthly')
        monthly_box = CheckBox(group='reset')
        yearly_label = Label(text='Yearly')
        yearly_box = CheckBox(group='reset')

        reset_sub_layout.add_widget(daily_label)
        reset_sub_layout.add_widget(daily_box)
        reset_sub_layout.add_widget(weekly_label)
        reset_sub_layout.add_widget(weekly_box)
        reset_sub_layout.add_widget(monthly_label)
        reset_sub_layout.add_widget(monthly_box)
        reset_sub_layout.add_widget(yearly_label)
        reset_sub_layout.add_widget(yearly_box)

        reset_layout.add_widget(reset_label)
        reset_layout.add_widget(reset_sub_layout)

        submit_button = Button(text='Submit New Budget')

        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)

        layout.add_widget(total_label)
        layout.add_widget(used_label)
        layout.add_widget(over_label)
        layout.add_widget(set_label)
        layout.add_widget(set_input)
        layout.add_widget(reset_layout)
        layout.add_widget(submit_button)
        layout.add_widget(menu_button)
        self.add_widget(layout)

    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'


# UI for screen where users can view and input goals
class GoalsScreen(Screen):
    def __init__(self, **kwargs):
        super(GoalsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        add_button1 = Button(text='Add New Goal')
        add_button1.bind(on_press=self.add1_pressed)
        add_button2 = Button(text='Add New Goal')
        add_button2.bind(on_press=self.add2_pressed)
        add_button3 = Button(text='Add New Goal')
        add_button3.bind(on_press=self.add3_pressed)

        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)

        layout.add_widget(add_button1)
        layout.add_widget(add_button2)
        layout.add_widget(add_button3)
        layout.add_widget(menu_button)
        self.add_widget(layout)

    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'

    def add1_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'newGoal'

    def add2_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'newGoal'

    def add3_pressed(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'newGoal'

                
# UI for screen that creates new goal
class NewGoalsScreen(Screen):
    def __init__(self, **kwargs):
        super(NewGoalsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)

        name_label = Label(text='Name:')  # The user can enter a custom name for the goal
        name_input = TextInput(multiline=False, text='0')

        price_label = Label(text='Price:')  # The user can enter a custom final amount
        price_input = TextInput(multiline=False, text='0', input_filter='float')

        current_label = Label(text='Current Contribution:')  # The user can enter a custom starting amount
        current_input = TextInput(multiline=False, text='0', input_filter='float')

        done_button = Button(text='Done')
      #  done_button.bind(on_press=self.done_pressed)

        NGS_layout = GridLayout(cols=2, spacing=10)  # adds a two column grid to take in new goal input
        NGS_layout.add_widget(name_label)
        NGS_layout.add_widget(name_input)
        NGS_layout.add_widget(price_label)
        NGS_layout.add_widget(price_input)
        NGS_layout.add_widget(current_label)
        NGS_layout.add_widget(current_input)
        NGS_layout.add_widget(done_button)
        self.add_widget(NGS_layout)

       # def done_pressed()
# UI for screen that calculates tips
class TipCalcScreen(Screen):
    # initialize all variables
    bill_label = Label(text='Bill amount:')
    bill_input = TextInput(multiline=False, text='0.00', input_filter='float')

    ten_label = Label(text='10% Tip:')
    fifteen_label = Label(text='15% Tip:')
    twenty_label = Label(text='20% Tip:')
    other_label = Label(text='Other %')

    ten_button = CheckBox(group='tip')
    fifteen_button = CheckBox(group='tip')
    twenty_button = CheckBox(group='tip')
    other_button = CheckBox(group='tip')

    tip_label = Label(text='Tip %:')  # The user can enter a custom tip amount
    tip_input = TextInput(multiline=False, text='0', input_filter='int')

    calculate_button = Button(text='Calculate')
    tip_total_label = Label(text='Tip amount: $-.--')
    total_label = Label(text='[b]Total bill amount: $-.--[/b]', markup=True)

    def __init__(self, **kwargs):
        super(TipCalcScreen, self).__init__(**kwargs)

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

    def calculate_pressed(self, totalLabel, tipLabel, *args):
        tip_percent = 0
        if self.ten_button.active: tip_percent = 10
        elif self.fifteen_button.active: tip_percent = 15
        elif self.twenty_button.active: tip_percent = 20
        elif self.other_button.active: tip_percent = float(self.tip_input.text)

        bill_amount = self.bill_input.text

        total_amount, tip_amount = extras_functions.calculate_tip(bill_amount, tip_percent)
        tipLabel.text = 'Tip amount: $%.2f' % tip_amount
        totalLabel.text = '[b]Total bill amount: $%.2f[/b]' % total_amount

    def menu_pressed(self, *args):  # called when the "back to menu" button is pressed
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'


# UI for screen that lets users split a bill
class BillSplitterScreen(Screen):
    bill_input = TextInput(multiline=False, text='0.00')
    tip_input = TextInput(multiline=False, text='0')
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

        calculate_button = Button(text="Calculate")
        total_label = Label(text='Each person pays $-.--.')
        calculate_button.bind(on_press=partial(self.calculate_pressed, total_label))


        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)
        # add all widgets on the page to the main layout
        layout.add_widget(input_layout)
        layout.add_widget(tip_layout)
        layout.add_widget(calculate_button)
        layout.add_widget(total_label)
        layout.add_widget(menu_button)
        self.add_widget(layout)

    def calculate_pressed(self, totalLabel, *args):
        tip_percent = 0
        bill_amount = self.bill_input.text
        num_of_people = self.people_input.text
        if self.tip_box.active: tip_percent = self.tip_input.text
        total_amount = extras_functions.calculate_bill_split(bill_amount, num_of_people, tip_percent)
        totalLabel.text = "Each person pays $%.2f" % total_amount

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
        
        mySavingTips = SavingTips(myPaymentHistory.getHistory())
        content_label = Label(text= mySavingTips.getTip())

        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)

        layout.add_widget(title_label)
        layout.add_widget(content_label)
        layout.add_widget(menu_button)
        self.add_widget(layout)

    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'


# UI for screen where user can view tips for spending money
class SpendMoneyScreen(Screen):
    def __init__(self, **kwargs):
        super(SpendMoneyScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        title_label = Label(text='[b]Tips for Spending Money:[/b]', markup=True)
        myAccount = []
        
        mySpendingTips = SpendingTips(myAccount)
        content_label = Label(text=mySpendingTips.getTip()) #Retrive tip for user spending custom to the user's spend-ability.

        menu_button = Button(text='Back to home menu', size_hint_x=.5, size_hint_y=.75)
        menu_button.bind(on_press=self.menu_pressed)

        layout.add_widget(title_label)
        layout.add_widget(content_label)
        layout.add_widget(menu_button)
        self.add_widget(layout)

    def menu_pressed(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'
