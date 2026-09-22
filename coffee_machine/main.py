MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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
    "money":0
}

representation = {
    "penny": 0.01,
    "dime": 0.1,
    "nickel": 0.05,
    "quarter":0.25
}

is_on = True


while is_on:
    choice=input("which type of coffee would you like (espresso/latte/cappuccino)or off to switch the machine off):")




    if choice == "report":
        print(resources)
    elif  choice == "latte" or choice=="espresso" or choice == "cappuccino":
        money = input("What do you wanna use(penny/dime/nickel/quarter):")
        how_many = int(input("how many do you want to put:"))

        # calculating the money
        ###getting the money a drink cost
        how_much_each_drink_cost = MENU[choice]["cost"]
        ###getting the amount entered
        total_money_entered = representation[money] * how_many

        # checking needed resources to make the required drink
        needed_water = MENU[choice]["ingredients"]["water"]
        needed_coffee = MENU[choice]["ingredients"]["coffee"]
        needed_milk = MENU[choice]["ingredients"]["milk"]
        # checking the available resources in the machine
        available_water = resources["water"]
        available_coffee = resources["coffee"]
        available_milk = resources["milk"]
        if available_coffee>=needed_coffee and available_water>=needed_water and available_milk >= needed_milk:
            if total_money_entered==how_much_each_drink_cost:
                #updating the resources
                resources["water"]= resources["water"] -MENU[choice]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
                resources["milk"] = resources["milk"]  - MENU[choice]["ingredients"]["milk"]
                resources["money"] = resources["money"] + how_much_each_drink_cost
                print(f"Here is your {choice} ☕")
            elif total_money_entered > how_much_each_drink_cost:
                #updating the resources
                resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
                resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["milk"]
                resources["money"] = resources["money"] + how_much_each_drink_cost
                print(f"Here is your {choice} ☕")
                remain_money = round(total_money_entered - how_much_each_drink_cost,1)
                print(f" here is your balance :{remain_money} ")
            else:
                print(f"The money you entered is not enough here is you money back {total_money_entered}:")

        else:
            print("no enough resources available in the machine 😭")

    elif choice=="off":
        is_on = False
    else:
        print("the coffee entered does not exist so fuck you and them too you look like a baboon 🦍🦍🦍:")