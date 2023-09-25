import streamlit as st
import pandas as pd
import numpy as np

class BudgetManager:
    # set daily goal, expenses list and balance
    def __init__(self, budget):
        self.budget = budget
        self.expenses = []
        self.balance = budget

    # def add_expense(self, amount, description):
        # self.expenses.append((amount, description))
#         self.expenses.append((amount, category))
#         self.balance -= amount
#         # print(f"Expense added: {description} (${amount}). New balance: ${self.balance}")
#         print(f"Expense added: {category} (${amount}). New balance: ${self.balance}")


#     def print_balance(self):
#         print(f"Current balance: ${self.balance}")

#     def print_expenses(self):
#         if not self.expenses:
#             print("No expenses recorded.")
#         else:
#             print("Expenses:")
#             # for amount, description in self.expenses:
#                 # print(f"- {description}: ${amount}")
#             for amount, category in self.expenses:
#                 print(f"- {category}: ${amount}")


# def main():
#     budget_amount = float(input("Enter your daily budget: "))
#     budget_manager = BudgetManager(budget_amount)

#     while True:
#         # print("\nOptions:")
#         #st.text
#         print("1. Add an expense")
#         # add input field
#         # add st.button (Add)
#         #st.text
#         print("2. View current balance")
#         # add st.button (status)
#         #st.text
#         print("3. View expenses")
#         # view table with expenses, filter, view graphs
#         # print("4. Exit")
#         choice = input("Enter your choice (1/2/3/4): ")

#         if choice == "1":
#             amount = float(input("Enter the expense amount: "))
#             description = input("Enter a description for the expense: ")
#             budget_manager.add_expense(amount, description)
#         elif choice == "2":
#             budget_manager.print_balance()
#         elif choice == "3":
#             budget_manager.print_expenses()
#         elif choice == "4":
#             break
#         else:
#             print("Invalid choice. Please choose a valid option.")

if __name__ == '__main__':
  st.title("Budget :sun_with_face: :money_with_wings:")

  df = pd.DataFrame(1, columns=("spesa", "categoria", "descrizione"))
  st.table(df)

  
  dailyBudget = 13.30
  monthlyBudget = 400
  expense = st.number_input('Inserisci spesa')
  dailyBudget -= expense  
  st.write('Stato attuale: ', dailyBudget)
