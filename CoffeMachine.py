class CoffeeMachine:

    espresso = [250, 0, 16, 1, 4]
    latte = [350, 75, 20, 1, 7]
    cappuccino = [200, 100, 12, 1, 6]

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "menu"
        self.user_action = ""
        self.fillstep = 0
        self.hello()

    def hello(self):
        print("Write action (buy, fill, take, remaining, exit):")

    def action(self, user_action):
        if user_action == "buy":
            self.state = "buy"
            print()
            self.buy(user_action)
        elif self.state == "buy":
            self.buy(user_action)
        elif user_action == "fill":
            self.state = "fill"
            print()
            self.fill("")
        elif self.state == "fill":
            self.fill(user_action)
        elif user_action == "take":
            self.take()
            self.hello()
        elif user_action == "remaining":
            self.remaining()
            self.hello()
        elif user_action == "exit":
            pass

    def check_resourses(self, recipe):
        check_result = "ok"
        compared_recipe = None

        if recipe == "1":
            compared_recipe = self.espresso
        elif recipe == "2":
            compared_recipe = self.latte
        elif recipe == "3":
            compared_recipe = self.cappuccino

        if self.water < compared_recipe[0]:
            check_result = "water"
        elif self.milk < compared_recipe[1]:
            check_result = "milk"
        elif self.beans < compared_recipe[2]:
            check_result = "beans"
        elif self.cups < compared_recipe[3]:
            check_result = "cups"

        return check_result

    def buy(self, user_action):
        current_recipe = None

        if user_action == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")

        if user_action == "back":
            self.state = "menu"
            print()
            self.hello()
            self.action("")
        elif user_action == "1":
            current_recipe = self.espresso
        elif user_action == "2":
            current_recipe = self.latte
        elif user_action == "3":
            current_recipe = self.cappuccino

        if current_recipe != None:
            enough_resources = self.check_resourses(user_action)
            if enough_resources == "ok":
                print("I have enough resources, making you a coffee!")
                print()
                self.state = "menu"
                self.hello()
                self.action("")
                self.water -= current_recipe[0]
                self.milk -= current_recipe[1]
                self.beans -= current_recipe[2]
                self.cups -= current_recipe[3]
                self.money += current_recipe[4]
            else:
                print("Sorry, not enough " + enough_resources + "!")
                print()
                self.state = "menu"
                self.hello()
                self.action("")

    def fill(self, fill_amount):
        if self.fillstep == 0:
            print("Write how many ml of water do you want to add:")
        elif self.fillstep == 1:
            self.water += int(fill_amount)
            print("Write how many ml of milk do you want to add:")
        elif self.fillstep == 2:
            self.milk += int(fill_amount)
            print("Write how many grams of coffee beans do you want to add:")
        elif self.fillstep == 3:
            self.beans += int(fill_amount)
            print("Write how many disposable cups of coffee do you want to add:")
        elif self.fillstep == 4:
            self.cups += int(fill_amount)
            self.fillstep = 0
            self.state = "menu"
            print()
            self.hello()
            self.action("")
        self.fillstep += 1

    def remaining(self):
        print()
        print("The coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.beans))
        print("{} of disposable cups".format(self.cups))
        print("{} of money".format(self.money))
        print()

    def take(self):
        print()
        print("I gave you ${}".format(self.money))
        print()
        self.money = 0

robo_coffee = CoffeeMachine()

while True:
    user_input = input()
    if user_input != "exit":
        robo_coffee.action(user_input)
    else:
        break
