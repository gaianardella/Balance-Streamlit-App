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
        # print(f"Expense added: {category} (${amount}). New balance: ${self.balance}")

    def get_expenses(self):
        return self.expenses

    def print_balance(self):
        print(f"Current balance: ${self.balance}")

    def print_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Expenses:")
            for amount, category in self.expenses:
                print(f"- {category}: ${amount}")


def main():
           
    # budget_amount = float(input("Enter your daily budget: "))
    dailyBudget = 13.30
    budget_manager = BudgetManager(dailyBudget)
    
    st.text("1. Aggiungi spesa")
    expense = st.number_input('Inserisci spesa')
    
    option = st.selectbox(
        "Seleziona categoria",
        ("Spesa", "Trasporti", "Ristoranti", "Shopping"),
        index=None,
        placeholder="Seleziona una categoria"
    )
    st.write('Hai selezionato: ', option)

    if st.button('Aggiungi spesa'):
        budget_manager.add_expense(expense, option)

    # Get the expenses from the BudgetManager instance
    expenses = budget_manager.get_expenses()

    if 'expenses' not in st.session_state:
        # Store the expenses in st.session_state
        st.session_state['expenses'] = expenses
    else:
        st.session_state['expenses'] += expenses

    expenses_sum=0
    st.write(st.session_state['expenses'])
    for el in st.session_state['expenses']:
        expenses_sum += el[0]
    bilancio = dailyBudget - expenses_sum
    st.write('Il valore corrente è ', bilancio)
    
    # st.text("2. Visualizza stato")
    # current_balance = budget_manager.balance
    # st.write(current_balance)
    # # st.write('Stato attuale: ', current_balance)
    
    # st.text("3. Visualizza spese")
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
