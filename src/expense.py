class Expense:
    def __init__(self, amount, date, category, description=""):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description
    def view(self):
        return f"{self.date} ,Catergory - {self.category}, Amount - Rs {self.amount} , Description :  {self.description}"
