from expense_tracker import ExpenseTracker

def addExpense(tracker):
    try:
        amount = int(input("Enter amount (\u20B9): "))
        date = input("Enter Date (YYYY-MM-DD): ")
        category = input("Enter Category: ")
        description = input("Enter Description (optional): ")
        tracker.add_expense(amount, date, category, description)
    except ValueError as e:
        print(f"Error: {e} \U0001F641")
        
def addCategory(tracker):
    category_name = input("Enter category name: ")
    tracker.add_category(category_name)

def expensesByCategory(tracker):
    category_name = input("Enter the category to filter by: ")
    tracker.view_expenses_Category_wise(category_name)

def saveCSV(tracker):
    tracker.save_to_csv()

def deleteExpense(tracker):
    try:
        index = int(input("Enter the expense number to delete: "))
        tracker.delete_expense(index)
    except ValueError:
        print("Error: Please enter a valid number. \U0001F641")

def updateExpense(tracker):
    try:

        index = int(input("Enter the expense number to update: "))
        print("Enter Values only for fields where you want to update. \U0001F680")
        tracker.update_expense(index)
    except ValueError:
        print("Error: Please enter a valid number. \U0001F641")

def main():
    tracker = ExpenseTracker()

    print("Welcome to the Expense Tracker Application! \U0001F600")  
    print("Hello! \U0001F44B")  
    print("Let's get started! \U0001F680")  
    print()

    while True:
        print("Expense Tracker Menu:")
        print()
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Delete Expense ")
        print("4. Update Expense")
        print("5. Add Category")
        print("6. Show All Categories")
        print("7. Expenses by Category")
        print("8. Save to csv")
        print("9. Exit")
        print()
        print('*'*25)
        choice = input("Enter your choice: ")

        if choice == "1":
            addExpense(tracker)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            deleteExpense(tracker)
        elif choice == "4":
            updateExpense(tracker)
        elif choice == "5":
            addCategory(tracker)
        elif choice == "6":
            tracker.view_categories()
        elif choice == "7":
            expensesByCategory(tracker)
        elif choice == "8":
            saveCSV(tracker)
        elif choice == "9":
            print("Exiting Expense Tracker. See You Again!")
            break
        else:
            print("Invalid choice :( ") 
            print("Please enter a valid choice ")

if __name__ == "__main__":
    main()
