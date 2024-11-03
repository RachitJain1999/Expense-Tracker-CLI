class Expense:
    def __init__(self, amount, date, category, description=""):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description
    def view(self):
        print(f"{self.date} - {self.category}: ${self.amount} - {self.description}")
