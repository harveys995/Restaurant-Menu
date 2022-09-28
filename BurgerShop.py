import datetime


class FoodItem:
    pass


class Burger(FoodItem):
    def __init__(self, condiments):
        self.condiments = condiments

    def display(self):
        totalOrder = ""
        if self.condiments == "Dip" or self.condiments == "Salt":
            totalOrder = "Burger, with " + self.condiments
            return totalOrder
        else:
            totalOrder = "Burger"
            return totalOrder
        return totalOrder

    def price(self):
        basePrice = 3
        if self.condiments == "Dip":
            basePrice = basePrice + 0.2
        if self.condiments == "Salt":
            basePrice = basePrice
        return basePrice


class Drink(FoodItem):
    def __init__(self, size):
        self.size = size

    def display(self):
        totalOrder = "Drink(" + self.size + ")"
        return totalOrder

    def price(self):
        basePrice = 1
        if self.size == "small":
            basePrice = basePrice + 0.2
        if self.size == "medium":
            basePrice = basePrice + 0.5
        if self.size == "large":
            basePrice = basePrice + 0.75
        return basePrice


class Side(FoodItem):
    def __init__(self, side):
        self.side = side

    def display(self):
        totalOrder = self.side
        return totalOrder

    def price(self):
        basePrice = 2
        if self.side == "Fries":
            basePrice = basePrice + 0.5
        if self.side == "Coleslaw":
            basePrice = basePrice + 0.5
        if self.side == "Corn":
            basePrice = basePrice + 0.75
        return basePrice


class Combo(FoodItem):
    def __init__(self, condiments, side, drink):
        self.condiments = condiments
        self.side = side
        self.drink = drink

    def display(self):
        totalOrder = "Combo Burger meal with " + self.side.display() + " and " + self.drink.display()
        return totalOrder

    def price(self):
        basePrice = 5
        return basePrice


class Order:
    def __init__(self):
        self.itemList = []
        self.priceList = []

    def createOrder(self, orderItem):
        self.itemList.append(orderItem.display())
        self.priceList.append(orderItem.price())

    def displayOrder(self):
        if len(self.itemList) == 0:
            print("No items chosen, please re-enter...")
            return 0

        totalPrice = 0
        for i in range(len(self.itemList)):
            itemPrice = "£ " + str(format(self.priceList[i], ".2f"))
            print("{:>50} {:>30}".format(self.itemList[i], itemPrice))
            totalPrice = totalPrice + self.priceList[i]
        print("---------------------------------------------------------------------------------")
        print("\033[1;32mTotal amount £", format(totalPrice, ".2f"))
        print("Thank you!")


def user_input_burger():
    while True:
        while True:
            try:
                ch = int(input(
                    "What condiments would you like?\n(1) Dip\n(2) Salt\n(3) No condiments\n(0) Cancel Order\n(5) Return to Main\n"))
            except ValueError:
                print("Please enter a numbered value from the options shown: ")
                continue
            break

        if ch == 1:
            b = Burger("Dip")
            return b
        elif ch == 2:
            b = Burger("Salt")
            return b
        elif ch == 3:
            b = Burger("")
            return b
        elif ch == 0:
            return 0
        elif ch == 5:
            return 5
        else:
            print("Invalid entry, please pick again...")


def user_input_drink():
    while True:
        while True:
            try:
                ch = int(input(
                    "What size drink would you like?\n(1) Small = 20p\n(2) Medium = 50p\n(3) Large = 75p\n(0) Cancel Order\n(5) Return to Main\n"))
            except ValueError:
                print("Please enter a numbered value from the options shown: ")
                continue
            break

        if ch == 1:
            d = Drink("small")
            return d
        elif ch == 2:
            d = Drink("medium")
            return d
        elif ch == 3:
            d = Drink("large")
            return d
        elif ch == 0:
            return 0
        elif ch == 5:
            return 5
        else:
            print("Invalid entry, please pick again...")


def user_input_side():
    while True:
        while True:
            try:
                ch = int(input(
                    "What side would you like?\n(1) Fries = 50p\n(2) Coleslaw = 50\n(3) Corn = 75p\n(0) Cancel Order\n(5) Return to Main\n"))
            except ValueError:
                print("Please enter a numbered value from the options shown: ")
                continue
            break

        if ch == 1:
            s = Side("Fries")
            return s
        elif ch == 2:
            s = Side("Coleslaw")
            return s
        elif ch == 3:
            s = Side("Corn")
            return s
        elif ch == 0:
            return 0
        elif ch == 5:
            return 5
        else:
            print("Invalid entry, please pick again...")


def user_input_combo():
    burger = user_input_burger()
    if burger == 0:
        return 0
    elif burger == 5:
        return 5
    side = user_input_side()
    if side == 0:
        return 0
    elif side == 5:
        return 5
    drink = user_input_drink()
    if drink == 0:
        return 0
    elif drink == 5:
        return 5
    c = Combo(burger, side, drink)
    return c


def take_order():
    ob = Order()
    print("Welcome to Burger Shop")
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    name = input("Whats your name?  :   ")
    while True:
        while True:
            try:
                ch = int(
                    input(
                        "Please pick an item:\n(1) Burger\n(2) Side\n(3) Drink\n(4) Combo\n(5) Complete Order(show receipt)\n(0) Cancel Order\n"))
            except ValueError:
                print("Please enter a numbered value from the options shown: ")
                continue
            break

        orderOb = ""
        if ch == 1:
            b = user_input_burger()
            if b == 0:
                print("Order cancelled")
                break
            elif b == 5:
                continue
            ob.createOrder(b)
        elif ch == 2:
            s = user_input_side()
            if s == 0:
                print("Order cancelled")
                break
            elif s == 5:
                continue
            ob.createOrder(s)
        elif ch == 3:
            d = user_input_drink()
            if d == 0:
                print("Order cancelled")
                break
            elif d == 5:
                continue
            ob.createOrder(d)
        elif ch == 4:
            c = user_input_combo()
            if c == 0:
                print("Order cancelled")
                break
            elif c == 5:
                continue
            ob.createOrder(c)
        elif ch == 5:
            print()
            print("Order for: ", name)
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print("---------------------------------------------------------------------------------")
            if ob.displayOrder() == 0:
                continue
            else:
                break

        elif ch == 0:
            print("---------------------------------------------------------------------------------")
            print("Order cancelled")
            print("Thank you!")
            break


take_order()

