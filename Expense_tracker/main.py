from manager import ExpenseManager
from reports import total_expense
from utils import menu

manager = ExpenseManager()

while True:

    menu()
    choice = input("Enter Choice: ")

    if choice == "1":
        manager.add_expense()

    elif choice == "2":
        manager.view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")