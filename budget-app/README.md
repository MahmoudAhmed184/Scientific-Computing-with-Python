# Budget App

The Budget App is a simple financial management tool built with Python. It enables users to manage their budget by creating categories, tracking deposits and withdrawals, and visualizing spending habits through a bar chart.

## Project Structure

The project consists of the following files:

- **`main.py`**: The entry point of the application that demonstrates the functionality of the Budget App.
- **`budget.py`**: This file contains the implementation of the `Category` class and the `create_spend_chart` function.
- **`test_module.py`**: This file includes unit tests to validate the functionality of the Budget App.

## Assignment

### Features

- **Category Management**: Create and manage various budget categories (e.g., Food, Clothing).
- **Deposit and Withdrawal Tracking**: Easily log your income and expenses.
- **Funds Transfer**: Move money between different budget categories seamlessly.
- **Balance Checking**: Ensure sufficient funds before making withdrawals or transfers.
- **Spending Visualization**: Generate a bar chart that shows the percentage spent in each category.

### Class: `Category`

The `Category` class is defined in `budget.py` and includes the following methods:

- `__init__(self, name)`: Initializes a budget category with the given name and an empty ledger.
  
- `deposit(self, amount, description='')`: Records a deposit in the ledger, with an optional description.

- `withdraw(self, amount, description='')`: Withdraws an amount from the budget category, returning `True` if successful and `False` if funds are insufficient.

- `get_balance(self)`: Returns the current balance of the budget category.

- `transfer(self, amount, category)`: Transfers funds to another budget category, updating both ledgers accordingly.

- `check_funds(self, amount)`: Checks if there are sufficient funds for a transaction (withdrawal or transfer).

- `__str__(self)`: Returns a formatted string representation of the category, displaying the title, ledger entries, and total balance.

### Function: `create_spend_chart`

The `create_spend_chart` function is also defined in `budget.py` and creates a bar chart representing the spending distribution across different categories. The chart features:

- Vertical percentage labels (0-100) on the left.
- Bars represented by 'o' characters corresponding to spending levels.
- A horizontal line at the bottom with category names.

### Example Usage

Here's an example of how to use the Budget App:

```python
# Import necessary classes and functions
from budget import Category, create_spend_chart

# Create instances of Category
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
food.transfer(50, clothing)

# Print the budget category
print(food)

# Create and print the spend chart
print(create_spend_chart([food, clothing]))
```

**Output**

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

And here’s how the spending chart might appear:

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```


For more information about the project, visit: [Build a Budget App Project](https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-budget-app-project/build-a-budget-app-project)