class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.balance = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, destination):
        if self.check_funds(amount): 
            self.withdraw(amount, f"Transfer to {destination.category}")
            destination.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True
        
    def __str__(self):
        lines = [self.category.center(30, '*')]
        for item in self.ledger:
            lines.append(f"{item['description'][:23].ljust(23)}{item['amount']:>7.2f}")
        lines.append(f"Total: {self.balance:.2f}")
        return '\n'.join(lines)




rent = Category("Rent")
groceries = Category("Groceries")
school = Category("School")
car = Category("Car")


rent.deposit(500)
rent.deposit(100)
rent.withdraw(300)

groceries.deposit(1000)
groceries.withdraw(250)
groceries.withdraw(300)

school.deposit(10000)
school.withdraw(1000)
school.deposit (1500)
school.withdraw (250)

car.deposit(600)
car.withdraw(300)
car.withdraw(100)
car.withdraw(100)


def create_spend_chart(categories):
    if not isinstance(categories, list):
        raise TypeError("Input must be a list")
    
    withdrawals = []
    for category in categories:
        withdrawals.append(sum([transaction["amount"] for transaction in category.ledger if transaction["amount"] < 0]))

    total_withdrawals = sum(withdrawals)
    percentages = [int((withdrawal / total_withdrawals) * 100) for withdrawal in withdrawals]
    
    lines = ["Percentage spent by category"]
    for i in range(100, -10, -10):
        lines.append(f"{str(i).rjust(3)}| {'  '.join(['o' if percentage >= i else ' ' for percentage in percentages])}  ")
    separator = "    "
    separator += "-" * (len(categories) * 3 + 1)
    lines.append(separator)

    max_length = max(len(category.category) for category in categories)
    for i in range(max_length):
        category_line = "    "
        for category in categories:
            if i < len(category.category):
                if category.category == "Entertainment":
                    category_line += " " + category.category[i] + "  "
                else:
                    category_line += " " + category.category[i] + " "
            else:
                category_line += "   "
        lines.append(category_line)

    return '\n'.join(lines)

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([business, food, entertainment]))