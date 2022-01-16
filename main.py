MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": {"amount": 300, "label": "ml"},
    "milk": {"amount": 200, "label": "ml"},
    "coffee": {"amount": 100, "label": "g"},
}
is_on = True


def print_resources():
    for resource in resources:
        print(f"{resource.capitalize()}: {resources[resource]['amount']}{resources[resource]['label']}")
    print(f"Money: ${profit}")


def is_resource_efficient(order):
    """return true when order can be made, False if ingredients are insufficient"""
    for item in order:
        if order[item] >= resources[item]['amount']:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Return the total sum of coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        print(f"Here is {round(money_received - drink_cost, 2)} change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return True


def make_coffee(drink_name, order_ingredients):
    """Deduct the required resources"""
    for item in order_ingredients:
        resources[item]['amount'] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_resources()
    else:
        drink = MENU[choice]
        if is_resource_efficient(drink['ingredients']) and is_transaction_successful(process_coins(), drink['cost']):
            make_coffee(choice, drink['ingredients'])
