from expense_tracker import ExpenseTracker

def addExpense(tracker):
    try:
        amount = int(input("Enter amount: "))
        date = input("Enter Date (YYYY-MM-DD): ")
        category = input("Enter Category: ")
        description = input("Enter Description (optional) : ")
        tracker.add_expense(amount, date, category, description)
    except:
        print('Something went wrong')
        

def addCategory(tracker):
    category_name = input("Enter category name: ")
    tracker.add_category(category_name)

def main():
    tracker = ExpenseTracker()

    print("Welcome to the Expense Tracker Application! \U0001F600")  
    print("Hello! \U0001F44B")  
    print("Let's get started! \U0001F680")  

    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Add Category")
        print("4. Show All Categories")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            addExpense(tracker)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            addCategory(tracker)
        elif choice == "4":
            tracker.view_categories()
        elif choice == "5":
            print("Exiting Expense Tracker. See You Again!")
            break
        else:
            print("Invalid choice :( ") 
            print("Please enter a valid choice ")

def addExpense(tracker):
    try:
        amount = int(input("Enter amount: "))
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        description = input("Enter description (optional): ")
        tracker.add_expense(amount, date, category, description)
    except ValueError:
        print("Invalid input. Please enter a valid number for amount.")

def addCategory(tracker):
    category_name = input("Enter category name: ")
    tracker.add_category(category_name)

if __name__ == "__main__":
    main()
