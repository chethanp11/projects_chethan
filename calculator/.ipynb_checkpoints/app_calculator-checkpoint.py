import streamlit as st
from main_calculator import Calculator

def main():
    st.title("Enhanced Calculator")

    calc = Calculator()

    operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide", "Power", "Modulus", "Square Root", "Factorial"])

    if operation in ["Add", "Subtract", "Multiply", "Divide", "Power", "Modulus"]:
        num1 = st.number_input("Enter first number", value=0.0)
        num2 = st.number_input("Enter second number", value=0.0)

        if st.button("Calculate"):
            try:
                if operation == "Add":
                    result = calc.add(num1, num2)
                elif operation == "Subtract":
                    result = calc.subtract(num1, num2)
                elif operation == "Multiply":
                    result = calc.multiply(num1, num2)
                elif operation == "Divide":
                    result = calc.divide(num1, num2)
                elif operation == "Power":
                    result = calc.power(num1, num2)
                elif operation == "Modulus":
                    result = calc.modulus(num1, num2)
                st.success(f"Result: {result}")
            except Exception as e:
                st.error(f"Error: {e}")

    elif operation == "Square Root":
        num = st.number_input("Enter number", value=0.0)
        if st.button("Calculate"):
            try:
                result = calc.square_root(num)
                st.success(f"Result: {result}")
            except Exception as e:
                st.error(f"Error: {e}")

    elif operation == "Factorial":
        num = st.number_input("Enter number", value=0, step=1, format="%d")
        if st.button("Calculate"):
            try:
                result = calc.factorial(int(num))
                st.success(f"Result: {result}")
            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    main()