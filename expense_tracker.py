import csv
import os
File_NAME = "expenses.csv"
#---------------- ADD EXPENSE ----------------
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: ₹"))
    

    expense = {
        "name": name,
        "amount": amount
    } 
    if not os.path.exists(File_NAME):
        with open(File_NAME, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'amount'])
            writer.writeheader()
            writer.writerow(expense)
    else:
        with open(File_NAME, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'amount'])
            writer.writerow(expense)
    
    print("Expense added successfully!\n")

#---------------- SHOW EXPENSES ----------------
def show_expenses():
    with open(File_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        expenses = list(reader)
    total = 0
    if not expenses:
        print("\nNo expenses found.\n")
        return
    print("\n----- EXPENSE LIST -----")

    for expense in expenses:
        print(f"{expense['name']} - ₹{expense['amount']}")
        total += float(expense['amount'])

    print("------------------------")
    print(f"Total Expense: ₹{total}\n")
    # ........Delete expense.........
def delete_expense():
    expenses = []
    with open(File_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            data= list(reader)
    if not data:
        print("\nNo expenses found.\n")
        return
    for i, expense in enumerate(data, start=1):
            print(f"{i}. {expense['name']} - ₹{expense['amount']}")
    choice = int(input("Enter the number of the expense to delete: "))

    if choice < 1 or choice > len(data):
        print("Invalid choice!\n")
        return
    deleted_expense = data.pop(choice - 1)
    print(f"Deleting expense: {deleted_expense['name']} - ₹{deleted_expense['amount']}")

    with open(File_NAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'amount'])
        writer.writeheader()
        writer.writerows(data)

    print("Expense deleted successfully!\n")

#---------------- MAIN FUNCTION ----------------
def main():
    while True:

        print("===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            show_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice!\n")

#---------------- RUN THE PROGRAM ----------------
main()