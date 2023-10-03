import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def main():
    
    dailyBudget = 13.30
    
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
        placeholder="Seleziona giorno"
    )
    
    month = st.selectbox(
        "Seleziona mese",
        (range(1, 12)),
        index=None,
        placeholder="Seleziona mese"
    )

    year = st.selectbox(
        "Seleziona anno",
        (2023, 2024),
        index=None,
        placeholder="Seleziona anno"
    )
    if day is not None and month is not None and year is not None:
        date = f"{day:02d}/{month:02d}/{year}"
        st.write('Hai selezionato: {}'.format(date))
    
    if st.button('Aggiungi spesa'):
        
        if len(st.session_state)==0:
            st.session_state[date] = [(expense, category)]
            
        else:
            if date in st.session_state:
                st.session_state[date].append((expense, category))
            else:
                
                sorted_keys = sorted(st.session_state.keys())
                last_key = sorted_keys[-1].split('/')
                
                start_date = datetime(int(last_key[2]), int(last_key[1]), int(last_key[0]))
                start_date_string = f"{int(last_key[0]):02d}/{int(last_key[1]):02d}/{int(last_key[2])}"
                end_date = datetime(year, month, day)
                
                date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
                # Convert the dates to strings in 'dd/mm/yyyy' format
                date_strings = [date.strftime('%d/%m/%Y') for date in date_range]

                st.session_state[date] =[(expense, category)]

                # Print the resulting date strings
                for date_string in date_strings:
                    if date_string not in st.session_state:
                        st.session_state[date_string] = [[0]]

    st.text("2. Visualizza stato")
    
    # Initialize a dictionary to store the cumulative balances for each day
    cumulative_balances = {}
    
    # Initialize a variable to track the cumulative balance
    cumulative_balance = 0
    
    # Iterate through the keys (dates) in the session_state dictionary
    for date, expenses in st.session_state.items():
        
        # Calculate the sum of expenses for the current date
        sum_of_expenses = sum(expense[0] for expense in expenses)
        
        # Calculate the cumulative balance by subtracting expenses from 10 euros
        cumulative_balance += (dailyBudget - sum_of_expenses)
        
        # Store the cumulative balance for the current date in the dictionary
        cumulative_balances[date] = cumulative_balance

    #CALCOLARE DATA ODIERNA E RESTITUIRE CUMULATIVE BALANCE DI DATA ODIERNA + CAMBIARE COLORE
    # E EMOJI IN BASE A SOPRA O SOTTO BUDGET O NEUTRO
    today_date = datetime.now().date()
    # Format the date as "dd/mm/yyyy"
    formatted_date = today_date.strftime('%d/%m/%Y')
    
    if formatted_date in st.session_state:
        st.write(f"Date: {formatted_date}, Cumulative Balance: {cumulative_balances[formatted_date]} euros")
    else:
        # trovare ultima chiave in cumulative_balances, calcolare range con giorno attuale
        # e fare cumulato + dailybudget x giorni in range (compreso giorno attuale) - 1 (giorno di partenza)
        sorted_keys = sorted(cumulative_balances.keys())
        if len(sorted_keys)!=0:
            last_key = sorted_keys[-1].split('/')
        start_date = datetime(int(last_key[2]), int(last_key[1]), int(last_key[0]))
        start_date_string = f"{int(last_key[0]):02d}/{int(last_key[1]):02d}/{int(last_key[2])}"
        end_date = datetime.combine(today_date, datetime.min.time())
        
        # Calculate the range of dates
        date_range = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
        # Convert the dates to strings in 'dd/mm/yyyy' format
        # date_strings = [date.strftime('%d/%m/%Y') for date in date_range]
        
        contatore=0
        # for date_string in date_strings:
        for date in date_range:
            date_string = date.strftime('%d/%m/%Y')
            if date_string != start_date_string:
                contatore+=dailyBudget
                
        saldo_finale=cumulative_balances[start_date_string]+contatore
        
        # st.write(f"Date: {formatted_date}, Cumulative Balance: {saldo_finale} euros")
        if saldo_finale>=0:
            st.success(f"Stai andando bene! Il tuo saldo è di {saldo_finale} euro", icon="✅")
        else:
            st.error(f"Stai andando male! Il tuo saldo è di {saldo_finale} euro", icon="🚨")
            
        
    st.text("3. Visualizza spese")
    records = []
    for data in st.session_state:
        for elem in st.session_state[data]:
            if elem!=[0]:
                row={}
                row["Data"] = data
                number = elem[0]
                formatted_number = f"{number:.2f}"
                row["Spesa"] = formatted_number
                row["Categoria"] = elem[1]
                records.append(row)
                
    # Create a DataFrame from the new records
    df = pd.DataFrame(records)
    st.table(df)

if __name__ == '__main__':
    st.title("Budget :sun_with_face: :money_with_wings:")
    st.divider()
    main()
