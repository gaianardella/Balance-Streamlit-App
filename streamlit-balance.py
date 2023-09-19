class BudgetManager:
    def __init__(self, budget):
        self.budget = budget
        self.expenses = []
        self.balance = budget

    def add_expense(self, amount, description):
        if amount > self.balance:
            print("Expense exceeds available balance. Cannot add expense.")
        else:
            self.expenses.append((amount, description))
            self.balance -= amount
            print(f"Expense added: {description} (${amount}). New balance: ${self.balance}")

    def print_balance(self):
        print(f"Current balance: ${self.balance}")

    def print_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Expenses:")
            for amount, description in self.expenses:
                print(f"- {description}: ${amount}")

def main():
    budget_amount = float(input("Enter your budget for the month: "))
    budget_manager = BudgetManager(budget_amount)

    while True:
        print("\nOptions:")
        print("1. Add an expense")
        print("2. View current balance")
        print("3. View expenses")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            amount = float(input("Enter the expense amount: "))
            description = input("Enter a description for the expense: ")
            budget_manager.add_expense(amount, description)
        elif choice == "2":
            budget_manager.print_balance()
        elif choice == "3":
            budget_manager.print_expenses()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
