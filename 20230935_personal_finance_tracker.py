#importing json and date and time
import json
from datetime import date #importing time to auto generate date

# Function to load transactions from JSON file
def load_transactions():
    try:
        with open("transactions.json", "r") as file:
            return json.load(file)
    except:
        return []

# Function to save transactions to JSON file
def save_transactions(transactions):
    with open("transactions.json","w") as file:
        json.dump(transactions, file)

# Function to display all transactions
def view_transaction(transactions):
    if not transactions:
        print("No transactions found.")
    else:
        print("Transactions:")
        for idx, transaction in enumerate(transactions, start=1):
            print(f"{idx}. {transaction}")

# Function to add a new transaction
def add_transaction(transactions):
    while True:
        try:
            amount = float(input("Enter transaction amount: "))
            break
        except ValueError:
            print ("Enter a valid amount!!!")
    description = input("Enter transaction description: ")
    usertypeselection = input("What is the type of the transaction?(Income/Expense) : ")
    transactions.append([amount, description, usertypeselection, str(date.today())])
    save_transactions(transactions)
    print("Transaction added successfully.")

# Function to update a transaction
def update_transaction(transactions):
    view_transaction(transactions)
    if not transactions: return

    idx = int(input("Enter the index of the transaction to update: ")) - 1
    if 0 <= idx < len(transactions):
        amount = float(input("Enter new amount: "))
        description = input("Enter new description: ")
        usertypeselection = input("Update the type of the transaction\n1. Income\n2. Expense\n")
        if (usertypeselection == "1"):
            inextype = "Income"
        else:
            inextype = "Expense"

        transactions[idx][0] = amount
        transactions[idx][1] = description
        transactions[idx][2] = inextype
        transactions[idx][3] = str(date.today())

        save_transactions(transactions)
        print("Transaction updated successfully.")
    else:
        print("Invalid index.")

# Function to delete a transaction
def delete_transaction(transactions):
    view_transaction(transactions)
    if not transactions: return
    
    idx = int(input("Enter the index of the transaction to delete: ")) - 1
    if 0 <= idx < len(transactions):
        del transactions[idx]
        save_transactions(transactions)
        print("Transaction deleted successfully.")
    else:
        print("Invalid index.")

#function to display summary
def display_summary(transactions):
    view_transaction(transactions)
    incomes = 0
    expenses = 0
    for transaction in transactions:
        if transaction[2] == 'Income':
            incomes += transaction[0]
        else:
            expenses += transaction[0]
    print(f"Total Income: {incomes}")
    print(f"Total Expenses: {expenses}")
    print(f"Balance: {incomes - expenses}")

# Main function
def main():
    transactions = load_transactions()
    while True:
        print("\n1. Add Transaction")
        print("2. Update Transaction")
        print("3. Delete Transaction")
        print("4. View Transactions")
        print("5. Display summary ")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            update_transaction(transactions)
        elif choice == "3":
            delete_transaction(transactions)
        elif choice == "4":
            view_transaction(transactions)
        elif choice == "5":
            display_summary(transactions)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

            print("Thishakya Kumarathunga")

#calling the main function
if __name__ == "__main__":
    main()