Below are the two Python files for a simple SIP (Systematic Investment Plan) calculator application using Streamlit.



def calculate_sip(monthly_investment, annual_rate, years):
    """
    Calculate the future value of a series of monthly investments (SIP).

    Parameters:
    - monthly_investment: The amount invested every month.
    - annual_rate: The annual interest rate (in percentage).
    - years: The number of years the investment is held.

    Returns:
    - The future value of the investments.
    """
    months = years * 12
    monthly_rate = annual_rate / 12 / 100
    future_value = 0

    for month in range(1, months + 1):
        future_value = future_value * (1 + monthly_rate) + monthly_investment

    return future_value