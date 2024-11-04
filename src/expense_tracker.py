from expense import Expense
from category import Category
import csv
import os

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = []

    def add_expense(self, amount, date, category, description="Not Available"):
        categoryName = [i.name for i in self.categories]
        if category not in categoryName:
            print(f"{category} does not exist. Please add it first.")
            print("*"*25)
        else:
            expense = Expense(amount, date, category, description)
            self.expenses.append(expense)
            print(f"Added expense. \U0001F600")
            print("*"*25)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            print("*"*25)
        else:
            ind = 1
            for expense in self.expenses:
                print(f"{ind}. {expense.view()}")
                ind += 1
            print("*"*25)

    def view_expenses_Category_wise(self, category_name):
        categoryName = [i.name for i in self.categories]
        if category_name not in categoryName:
            print(f"{category_name}' does not exist.")
            print("*"*25)
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
        categoryName = [i.name for i in self.categories]
        if category_name in categoryName:
            print(f"{category_name} already exists.")
        else:
            category = Category(category_name)
            self.categories.append(category)
            print("Category added \U0001F973")
            print("*"*25)

    def view_categories(self):
        if not self.categories:
            print("No Categories Available. \U0001F641")
            print("*"*25)
        else:
            ind = 1
            for category in self.categories:
                print(f" {ind}. {category.view()}")
                ind += 1
            print("*"*25)

    # src/expense_tracker.py

# src/expense_tracker.py

    def save_to_csv(self, filename="C:/Users/jaink/Desktop/html and css/Fynd/MidProject/Expense-Tracker-CLI/data/expenses.csv"):
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        try:
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                # Write header
                writer.writerow(["Amount", "Date", "Category", "Description"])
                for expense in self.expenses:
                    writer.writerow([expense.amount, expense.date, expense.category, expense.description])
            print(f"Expenses saved to {filename}")
        except Exception as e:
            print(f"Error saving to CSV: {e}")
