from expense import Expense
from file_handle import read_data, write_data
from datetime import datetime


class ExpenseManager:

    def add_expense(self):
        rows = read_data()

        expense_id = len(rows)

        category = input("Category: ")
        description = input("Description: ")
        amount = float(input("Amount: "))

        date = datetime.now().strftime("%d-%m-%Y")

        expense = Expense(
            expense_id,
            date,
            category,
            description,
            amount
        )

        rows.append(expense.to_list())

        write_data(rows)

        print("Expense added successfully!")

    def view_expenses(self):
        rows = read_data()

        print("\nExpenses:\n")

        for row in rows:
            print(row)