MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# logo = """
#     _____       __  __             _____ _
#   / ____|     / _|/ _|           / ____| |
#  | |     ___ | |_| |_ ___  ___  | (___ | |__   ___  _ __
#  | |    / _ \|  _|  _/ _ \/ _ \  \___ \| '_ \ / _ \| '_ \
#  | |___| (_) | | | ||  __/  __/  ____) | | | | (_) | |_) |
#   \_____\___/|_| |_| \___|\___| |_____/|_| |_|\___/| .__/
#                                                    | |
#                                                    |_|    """

# print(logo)
on = True
money = 0


def check_resources(coffee_type):
    for key in resources:
        if resources[key] < MENU[coffee_type]["ingredients"][key]:
            print(f"Sorry, there is not enough {key}.\n")
            return False
    return True

def check_money(inserted_money, coffee_type):
    if inserted_money < MENU[coffee_type]["cost"]:
        print("You didn't insert enough money. Here's the refund.\n")
        return False
    return True

def give_change(inserted_money, coffee_type):
    if inserted_money > MENU[coffee_type]["cost"]:
        print(f"Here's your change. ${inserted_money - MENU[coffee_type]["cost"]}\n")

def consume_resources(coffee_type):
    for key in resources:
        resources[key] -= MENU[coffee_type]["ingredients"][key]

while on:
    order = input("\nWhat would you like?\n"
                  "1. Espresso\n"
                  "2. Latte\n"
                  "3. Cappuccino\n").lower()

    if order == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}ml")
        print(f"Money: ${money}\n")
        continue

    elif order == "off":
        on = False
        break

    elif order == "espresso":
        checked_resources = check_resources("espresso")
        if not checked_resources:
            continue
        else:
            print("Please insert coins\n")
            money_inserted = int(input("How many dollars?\n$"))
            checked_money = check_money(money_inserted, "espresso")

            if not checked_money:
                continue
            else:
                money += MENU["espresso"]["cost"]
                consume_resources("espresso")
                give_change(money_inserted, "espresso")
                print("Enjoy your Espresso!\n")

    elif order == "latte":
        checked_resources = check_resources("latte")
        if not checked_resources:
            continue
        else:
            print("Please insert coins\n")
            money_inserted = float(input("How many dollars?\n$"))
            checked_money = check_money(money_inserted, "latte")

            if not checked_money:
                continue
            else:
                money += MENU["latte"]["cost"]
                consume_resources("latte")
                give_change(money_inserted, "latte")
                print("Enjoy your Latte!\n")

    elif order == "cappuccino":
        checked_resources = check_resources("cappuccino")
        if not checked_resources:
            continue
        else:
            print("Please insert coins\n")
            money_inserted = int(input("How many dollars?\n$"))
            checked_money = check_money(money_inserted, "cappuccino")

            if not checked_money:
                continue
            else:
                money += MENU["cappuccino"]["cost"]
                consume_resources("cappuccino")
                give_change(money_inserted, "cappuccino")
                print("Enjoy your Cappuccino!\n")

    else:
        print(f"Invalid choice. {order} isn't available.\n")
