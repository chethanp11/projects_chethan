Below are the two Python files for building an NPV (Net Present Value) calculator using Streamlit for the UI.

:

def calculate_npv(rate, cash_flows):
    """
    Calculate the Net Present Value (NPV) of a series of cash flows.

    :param rate: The discount rate as a decimal (e.g., 0.1 for 10%)
    :param cash_flows: A list of cash flows, where the first element is the initial investment (negative value)
                       and the subsequent elements are the cash inflows.
    :return: The NPV value.
    """
    npv = 0
    for i, cash_flow in enumerate(cash_flows):
        npv += cash_flow / ((1 + rate) ** i)
    return npv