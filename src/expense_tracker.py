from expense import Expense
from category import Category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = []

    def add_expense(self, amount, date, category, description="Not Available"):
        categoryName = [i.name for i in self.categories]
        if category not in categoryName:
            print(f"{category} does not exist. Please add it first.")
        else:
            expense = Expense(amount, date, category, description)
            self.expenses.append(expense)
            print(f"Added expense. \U0001F600")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            ind = 1
            for expense in self.expenses:
                print(f"{ind}. {expense.view()}")
                ind += 1

    def view_expenses_Category_wise(self, category_name):
        categoryName = [i.name for i in self.categories]
        if category_name not in categoryName:
            print(f"{category_name}' does not exist.")
        else:
            selectedExpenses = [expense for expense in self.expenses if expense.category == category_name]
            if not selectedExpenses:
                print(f"No expenses under '{category_name}' ")
            else:
                if not selectedExpenses:
                    print("No expenses recorded.")
                else:
                    ind = 1
                    for expense in selectedExpenses:
                        print(f"{ind}. {expense.view()}")
                        ind += 1

    def add_category(self, category_name):
        if category_name in self.categories:
            print(f"{category_name} already exists.")
        else:
            category = Category(category_name)
            self.categories.append(category)
            print("Category added \U0001F973")

    def view_categories(self):
        if not self.categories:
            print("No Categories Available. \U0001F641")
        else:
            ind = 1
            for category in self.categories:
                print(f" {ind}. {category.view()}")
                ind += 1
