class Expense:
    def __init__(self, expense_id, date, category, description, amount):
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.description = description
        self.amount = float(amount)

    def to_list(self):
        return [
            self.expense_id,
            self.date,
            self.category,
            self.description,
            self.amount
        ]