CHARS_PER_LINE = 30
MAX_DESCRIPTION_LENGTH = 23
MAX_AMOUNT_LENGTH = 7
MAX_PERCENTAGE = 100
MIN_PERCENTAGE = 0
PERCENTAGE_STEP = 10
MAX_PERCENTAGE_LENGTH = 3
DASHES_PER_CATEGORY = 3


class Category:
    def __init__(self, name: str):
        self.ledger = []
        self.name = name
        self.balance = 0.0
        self.total_spent = 0.0

    def __str__(self):
        header = f"{self.name}".center(CHARS_PER_LINE, "*") + "\n"
        transactions = "".join(
            f"{transaction['description'][:MAX_DESCRIPTION_LENGTH].ljust(MAX_DESCRIPTION_LENGTH)}"
            + f"{transaction['amount']:.2f}".rjust(MAX_AMOUNT_LENGTH)
            + "\n"
            for transaction in self.ledger
        )
        total = f"Total: {self.balance:.2f}"
        return header + transactions + total

    def deposit(self, amount: float, description: str = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount: float, description: str = "") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.total_spent += amount
            self.balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        return self.balance

    def transfer(self, amount: float, target_category: "Category") -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {target_category.name}")
            target_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount: float) -> bool:
        return self.balance >= amount


def round_down_to_nearest_ten(percentage: float) -> float:
    return (percentage // 10) * 10


def calculate_spending_percentages(categories: list[Category]) -> list[float]:
    total_spent = sum(category.total_spent for category in categories)
    if total_spent == 0:
        return [0] * len(categories)
    return [
        round_down_to_nearest_ten(category.total_spent * 100 / total_spent)
        for category in categories
    ]


def build_percentage_lines(spending_percentages: list[float]) -> str:
    percentage_lines = ""
    for percentage in range(MAX_PERCENTAGE, MIN_PERCENTAGE - PERCENTAGE_STEP, -PERCENTAGE_STEP):
        percentage_lines += f"{percentage:>{MAX_PERCENTAGE_LENGTH}}| "
        percentage_lines += "".join(
            "o  " if spending_percentage >= percentage else "   "
            for spending_percentage in spending_percentages
        )
        percentage_lines += "\n"
    return percentage_lines


def build_category_name_lines(categories: list[Category]) -> str:
    category_name_lines = ""
    max_name_length = max(len(category.name) for category in categories)

    for i in range(max_name_length):
        category_name_lines += "     "
        for category in categories:
            category_name_lines += (category.name[i] + "  ") if i < len(category.name) else "   "
        category_name_lines += "\n"

    return category_name_lines


def create_spend_chart(categories: list[Category]) -> str:
    spending_percentages = calculate_spending_percentages(categories)
    chart = "Percentage spent by category\n"
    chart += build_percentage_lines(spending_percentages)
    chart += "    " + "-" * (len(categories) * DASHES_PER_CATEGORY + 1) + "\n"
    chart += build_category_name_lines(categories)
    return chart.rstrip() + "  "
