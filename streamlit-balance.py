import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# class BudgetManager:
#     # set daily goal, expenses list and balance
#     def __init__(self, dailyBudget):
#         self.budget = dailyBudget
#         self.expenses = []
#         self.balance = dailyBudget

#     def add_expense(self, amount, category):
#         self.expenses.append((amount, category))
#         # self.balance -= amount
#         # print(f"Expense added: {category} (${amount}). New balance: ${self.balance}")

#     def get_expenses(self):
#         return self.expenses

#     def print_balance(self, dailyBudget):
#     #     print(f"Current balance: ${self.balance}")
#         expenses_sum=0
#         for el in self.expenses:
#             expenses_sum += el[0]
#         self.balance = dailyBudget - expenses_sum
#         return self.balance
    

#     def print_expenses(self):
#         if not self.expenses:
#             print("No expenses recorded.")
#         else:
#             print("Expenses:")
#             for amount, category in self.expenses:
#                 print(f"- {category}: ${amount}")


def main():
           
    # budget_amount = float(input("Enter your daily budget: "))
    dailyBudget = 13.30
    # budget_manager = BudgetManager(dailyBudget)
    # Get the expenses from the BudgetManager instance
    # expenses = budget_manager.get_expenses()

    # expenses = []
    # if 'expenses' not in st.session_state:
    #     # Store the expenses in st.session_state
    #     st.session_state['expenses'] = expenses
    # else:
    #     st.session_state['expenses'] += expenses
    
    st.text("1. Aggiungi spesa")
    expense = st.number_input('Inserisci spesa')
    st.write('Il valore corrente è ', expense)
    
    category = st.selectbox(
        "Seleziona categoria",
        ("Spesa", "Trasporti", "Ristoranti", "Shopping"),
        index=None,
        placeholder="Seleziona una categoria"
    )
    st.write('Hai selezionato: ', category)

    day = st.selectbox(
        "Seleziona giorno",
        (range(1, 32)),
        index=None,
        placeholder="Seleziona una categoria"
    )
    
    month = st.selectbox(
        "Seleziona categoria",
        (range(1, 12)),
        index=None,
        placeholder="Seleziona una categoria"
    )

    year = st.selectbox(
        "Seleziona categoria",
        (2023, 2024),
        index=None,
        placeholder="Seleziona una categoria"
    )
    if day is not None and month is not None and year is not None:
        date_string = f"{day:02d}/{month:02d}/{year}"
        st.write('Hai selezionato: {}'.format(date_string))
    # date_string = f"{day:02d}{month:02d}{year}"
    # # Convert the date string into a datetime object
    # date_format = "%d%m%Y"
    # date_datetime = datetime.strptime(date_string, date_format)

    
    if st.button('Aggiungi spesa'):
        # if date_string not in st.session_state:
            # Store the expenses in st.session_state
            # st.session_state[date_string] = []
        # else:
        #     st.session_state[date_string].append((expense, category))

        if st.session_state:
        # Example: The starting and ending dates
            last_key = list(st.session_state.keys())[-1].split('/')
            start_date = datetime(last_key[2], last_key[0], last_key[1])
            end_date = datetime(year, day, month)
            st.write(start_date)
            st.write(end_date)
    # Calculate the range of dates
    # date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
    
    # # Assuming you have st.session_state with the existing data
    # # If not, you can initialize it as an empty dictionary: st.session_state = {}
    
    # # Check and add missing dates to st.session_state
    # for date in date_range:
    #     date_string = date.strftime('%d/%m/%Y')
    #     if date_string not in st.session_state:
    #         st.session_state[date_string] = [(0)]
    
    # # Print the updated st.session_state
    # st.write(st.session_state)

    st.text("2. Visualizza stato")
    # current_balance = budget_manager.balance
    # current_balance = dailyBudget - expenses_sum
    # st.write('Stato attuale: ', current_balance)

    # # Initialize a dictionary to store the cumulative balances for each day
    # cumulative_balances = {}
    
    # # Initialize a variable to track the cumulative balance
    # cumulative_balance = 0
    
    # # Iterate through the keys (dates) in the session_state dictionary
    # for date, expenses in st.session_state.items():
    #     # Calculate the sum of expenses for the current date
    #     sum_of_expenses = sum(expense[0] for expense in expenses)
        
    #     # Calculate the cumulative balance by subtracting expenses from 10 euros
    #     cumulative_balance += (dailyBudget - sum_of_expenses)
        
    #     # Store the cumulative balance for the current date in the dictionary
    #     cumulative_balances[date] = cumulative_balance
    
    # # Print the dictionary of cumulative balances
    # for date, balance in cumulative_balances.items():
        # st.write(f"Date: {date}, Cumulative Balance: {balance} euros")
        
    ##############################################################
    
    # st.text("3. Visualizza spese")
    # storico = budget_manager.print_expenses()
    # st.write(storico)
        # view table with expenses, filter, view graphs
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
