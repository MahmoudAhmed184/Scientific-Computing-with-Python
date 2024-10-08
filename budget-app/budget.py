class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category

    def __str__(self):
        string = f"{self.category}".center(30, "*") + "\n"
        for transaction in self.ledger:
            amount = transaction["amount"]
            description = transaction["description"]
            string += description[:23].ljust(23) + f"{amount:.2f}".rjust(7) + "\n"
        string += f"Total: {self.get_balance():.2f}"
        return string

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0.0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()


def create_spend_chart(categories):
    total_spends = 0
    spend_percentages = []

    for category in categories:
        category_spends = 0
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                category_spends -= transaction["amount"]

        spend_percentages.append(category_spends)
        total_spends += category_spends

    number_of_categories = len(categories)
    for i in range(number_of_categories):
        spend_percentages[i] = spend_percentages[i] * 100 / total_spends // 10 * 10
        print(spend_percentages[i])

    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "

        for percent in spend_percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (number_of_categories * 3 + 1) + "\n"

    longest_name_length = max([len(category.category) for category in categories])
    for i in range(longest_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip() + "  "
