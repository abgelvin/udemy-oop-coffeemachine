from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def run_machine():
    is_on = True

    while is_on:
        options = menu.get_items()
        order_name = (input(f"What would you like? ({options}): ")).lower()
        if order_name == 'off':
            print('Good-bye.')
            is_on = False
        elif order_name == 'report':
            coffee_maker.report()
            money_machine.report()
        else :
            drink = menu.find_drink(order_name)
            if drink:
                if coffee_maker.is_resource_sufficient(drink):
                    print(f'That will be ${drink.cost:.2f}')
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)


run_machine()