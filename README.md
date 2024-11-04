# Expense Tracker Application

This is a Command-Line Interface (CLI) application built with Python. The Expense Tracker Application supports adding, viewing, updating, deleting, and categorizing expenses and generates a report as a CSV file.

## Features

- **Add, Update, Delete Expenses**: Record your expenses with details like amount, date, category, and description.
- **Categorize Expenses**: Organize your expenses by default categories i.e. Groceries, Entertainment, and Utility. However, you can also add your custom category as well
- **View and Filter**: View all expenses or filter by category for analysis.

## Setup

1. **Clone the Repository**:
   Run this in Git-Bash: git clone https://github.com/RachitJain1999/Expense-Tracker-CLI.git
2. **cd src**
3. **To Start the Application**:
     python main.py
   
## Requirements
  Python3

## Instructions
Once you’ve set up the application and started it. Use the menu to manage your expenses by following the instructions below.

Main Menu Options:
1. **Add Expense** : Select this option to record a new expense.Enter the amount, date (in YYYY-MM-DD format), category (e.g., groceries, entertainment), and a description.

2. **Show All Expenses** : Choose this option to see a list of all expenses.

3. **Update Expense** : Select this to modify an existing expense.You’ll be prompted to enter index of the expense you want to update.

4 **Delete Expense** : Choose this option to delete an expense from the list.Enter the index of the expense you wish to delete.

5 **Add Category** : Choose this option to create new category for expense.

6 **Show All Categories** : Choose this option to see a list of all Categories.

7 **Expenses by Category** : Choose this option to see a list of all Expenses under selected category.

8. **Save to csv** : Choose this option to save the curre expense data into csv file(expenses.csv).

9. **Exit** : Choose this option to close the Application 
