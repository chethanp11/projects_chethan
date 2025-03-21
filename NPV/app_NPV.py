:

import streamlit as st
from main_NPV import calculate_npv

def main():
    st.title("NPV Calculator")

    st.sidebar.header("Input Parameters")
    
    # Input for discount rate
    rate = st.sidebar.number_input("Discount Rate (as a %)", min_value=0.0, max_value=100.0, value=10.0)
    rate = rate / 100  # Convert percentage to a decimal

    # Input for cash flows
    cash_flows_str = st.sidebar.text_area("Cash Flows (comma separated)", "-1000, 200, 300, 400, 500")
    cash_flows = list(map(float, cash_flows_str.split(',')))

    # Calculate NPV
    if st.sidebar.button("Calculate NPV"):
        npv = calculate_npv(rate, cash_flows)
        st.write(f"The Net Present Value (NPV) is: {npv:.2f}")

if __name__ == "__main__":
    main()


To run the application, ensure you have Streamlit installed and execute the following command in your terminal:
bash
streamlit run