# Code that does calculations for the tip calculator
def calculate_tip(bill_amount, tip_percent):
    bill_amount = float(bill_amount)
    tip_percent = float(tip_percent)
    tip_percent /= 100
    tip = bill_amount * tip_percent
    total_amount = bill_amount + tip
    return total_amount, tip

# Code that does calculations for the bill splitter
def calculate_bill_split(bill_amount, num_of_people, tip_percent):
    bill_amount = float(bill_amount)
    num_of_people = float(num_of_people)
    tip_percent = float(tip_percent)
    total_amount = bill_amount / num_of_people
    tip_percent /= 100
    tip_amount = total_amount * tip_percent
    total_amount += tip_amount
    return total_amount
