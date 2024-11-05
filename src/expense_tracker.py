import datetime
from expense import Expense
from category import Category
import csv
import os

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = [Category('Entertainment') , Category('Utility') , Category('Groceries')]

    def add_expense(self, amount, date, category, description):
        try:
            # Validating amount
            if amount <= 0:
                raise ValueError("Amount must be positive.\U0001F641")
            
            # Validate category
            if not category:
                raise ValueError("Category cannot be empty.\U0001F641")
            categories = [i.name for i in self.categories]
            if(category not in categories):
                raise ValueError('Please add this Category First \U0001F44B')
            
            new_expense = Expense(amount, date, category, description)
            self.expenses.append(new_expense)
            print(f" Expense Added \U0001F44B")
        except ValueError as e:
            print(f"Error adding expense: {e}")

    def delete_expense(self, index):
        try:
            self.expenses.pop(index - 1)
            print(f"Expense Deleted Successfully! \U0001F44D")
        except IndexError:
            print(f"Error: No expense found at index {index}. \U0001F641")
        except ValueError:
            print("Error: Please enter a valid index number. \U0001F641")


    def update_expense(self, index):
        try:
            expense = self.expenses[index - 1]
            amount = int(input("Enter New Amount (\u20B9): "))
            if(amount == 0):
                amount = expense.amount
            if(amount <= 0):
                raise ValueError('Amount Must be Positive')
            date = input("Enter New Date (YYYY-MM-DD): ")
            if(not date):
                date = expense.date
            category = input("Enter New Category: ")
            if(not category):
                category = expense.category
            if not category:
                raise ValueError("Category cannot be empty.\U0001F641")
            categories = [i.name for i in self.categories]
            if(category not in categories):
                raise ValueError('Please add this Category First \U0001F44B')
            description = input("Enter New Description (optional): ")
            if(not description):
                description = expense.description
    
            self.expenses[index - 1] = Expense(amount, date, category, description)
            print(f"Expense Updated Successfully! \U0001F973")
        except IndexError:
            print(f"Error: No expense found at index {index}. \U0001F641")
        except ValueError as e:
            print(f"Error: {e}")

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

