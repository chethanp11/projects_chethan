import streamlit as st
from main_SWP import SWPCalculator
import pandas as pd

def main():
    st.title("Systematic Withdrawal Plan (SWP) Calculator")

    initial_investment = st.number_input("Initial Investment", min_value=0.0, value=100000.0, step=1000.0)
    annual_withdrawal = st.number_input("Annual Withdrawal", min_value=0.0, value=10000.0, step=500.0)
    annual_return_rate = st.number_input("Annual Return Rate (%)", min_value=0.0, value=5.0, step=0.1) / 100
    years = st.number_input("Number of Years", min_value=1, value=10, step=1)

    if st.button("Calculate"):
        calculator = SWPCalculator(initial_investment, annual_withdrawal, annual_return_rate, years)
        balances = calculator.calculate_yearly_balances()
        
        df_balances = pd.DataFrame(balances)
        st.subheader("Yearly Balances")
        st.dataframe(df_balances.style.format({
            'Starting Balance': '{:,.2f}',
            'Interest Earned': '{:,.2f}',
            'Annual Withdrawal': '{:,.2f}',
            'End of Year Balance': '{:,.2f}'
        }))

if __name__ == "__main__":
    main()