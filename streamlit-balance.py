import streamlit as st
import pandas as pd
import numpy as np

class BudgetManager:
    # set daily goal, expenses list and balance
    def __init__(self, dailyBudget):
        self.budget = dailyBudget
        self.expenses = []
        self.balance = dailyBudget

    def add_expense(self, amount, category):
        self.expenses.append((amount, category))
        self.balance -= amount
        print(f"Expense added: {category} (${amount}). New balance: ${self.balance}")


    def print_balance(self):
        print(f"Current balance: ${self.balance}")

    def print_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Expenses:")
            # for amount, description in self.expenses:
                # print(f"- {description}: ${amount}")
            for amount, category in self.expenses:
                print(f"- {category}: ${amount}")


def main():
    # budget_amount = float(input("Enter your daily budget: "))
    dailyBudget = 13.30
    budget_manager = BudgetManager(dailyBudget)
    
    st.text("1. Aggiungi spesa")
    # expense = st.number_input('Inserisci spesa')
    expense = st.number_input("Inserisci spesa", value=None, placeholder="Inserisci spesa")
    st.write('Il valore corrente è ', expense)

    option = st.selectbox(
        "Seleziona categoria",
        ("Spesa", "Trasporti", "Ristoranti", "Shopping"),
        index=None,
        placeholder="Seleziona una categoria"
    )
    st.write('Hai selezionato: ', option)
    
    budget_manager.add_expense(expense, option)
    
    st.text("2. Visualizza stato")
    current_balance = budget_manager.balance
    st.write('Stato attuale: ', current_balance)
    
    st.text("3. Visualizza spese")
#         # view table with expenses, filter, view graphs
         # df = pd.DataFrame(1, columns=("spesa", "categoria", "descrizione"))
         # st.table(df)
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
    main()
#     dailyBudget = 13.30
# monthlyBudget = 400
# expense = st.number_input('Inserisci spesa')
# dailyBudget -= expense  
