from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
menu = Menu()

coffee_machine = True
while coffee_machine:
    user = menu.get_items()
    choice = input(f"What would you like? ({user})? ")
    if choice == "off":
        coffee_machine = False
    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)

