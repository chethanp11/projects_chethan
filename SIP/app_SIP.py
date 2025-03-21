import streamlit as st
from main_SIP import calculate_sip

def main():
    st.title("SIP Calculator")

    st.sidebar.header("Input Parameters")
    monthly_investment = st.sidebar.number_input("Monthly Investment Amount", min_value=0.0, value=1000.0, step=100.0)
    annual_rate = st.sidebar.number_input("Expected Annual Return Rate (%)", min_value=0.0, value=12.0, step=0.1)
    years = st.sidebar.number_input("Investment Duration (Years)", min_value=1, value=10, step=1)

    if st.sidebar.button("Calculate"):
        future_value = calculate_sip(monthly_investment, annual_rate, years)
        st.subheader("Results")
        st.write(f"Future Value of Investment: ₹{future_value:,.2f}")

if __name__ == "__main__":
    main()


To run the Streamlit application, make sure both files are in the same directory and execute the following command in your terminal:

streamlit run