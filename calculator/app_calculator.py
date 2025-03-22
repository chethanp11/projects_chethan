import streamlit as st
from main_calculator import GeometryCalculator, ArithmeticCalculator, AstronomyCalculator
from datetime import datetime

def main():
    st.title("Comprehensive Calculator")

    geo_calc = GeometryCalculator()
    arith_calc = ArithmeticCalculator()
    astro_calc = AstronomyCalculator()

    calc_type = st.radio("Select Calculator Type", ["Geometric", "Arithmetic", "Astronomy"])

    if calc_type == "Geometric":
        handle_geometric_calculations(geo_calc)
    elif calc_type == "Arithmetic":
        handle_arithmetic_calculations(arith_calc)
    elif calc_type == "Astronomy":
        handle_astronomy_calculations(astro_calc)

def handle_geometric_calculations(geo_calc):
    operation = st.selectbox("Select Operation", [
        "Circle Area", "Circle Perimeter", "Rectangle Area", "Rectangle Perimeter",
        "Distance Between Points", "Triangle Area", "Triangle Perimeter"])

    if operation == "Circle Area":
        radius = st.number_input("Enter radius", value=0.0)
        if st.button("Calculate"):
            result = geo_calc.circle_area(radius)
            st.success(f"Area: {result}")

    elif operation == "Circle Perimeter":
        radius = st.number_input("Enter radius", value=0.0)
        if st.button("Calculate"):
            result = geo_calc.circle_perimeter(radius)
            st.success(f"Perimeter: {result}")

    elif operation == "Rectangle Area":
        length = st.number_input("Enter length", value=0.0)
        width = st.number_input("Enter width", value=0.0)
        if st.button("Calculate"):
            result = geo_calc.rectangle_area(length, width)
            st.success(f"Area: {result}")

    elif operation == "Rectangle Perimeter":
        length = st.number_input("Enter length", value=0.0)
        width = st.number_input("Enter width", value=0.0)
        if st.button("Calculate"):
            result = geo_calc.rectangle_perimeter(length, width)
            st.success(f"Perimeter: {result}")

    elif operation == "Distance Between Points":
        x1 = st.number_input("Enter x1", value=0.0)
        y1 = st.number_input("Enter y1", value=0.0)
        x2 = st.number_input("Enter x2", value=0.0)
        y2 = st.number_input("Enter y2", value=0.0)
        if st.button("Calculate"):
            result = geo_calc.distance_between_points(x1, y1, x2, y2)
            st.success(f"Distance: {result}")

    elif operation == "Triangle Area":
        base = st.number_input("Enter base", value=0.0)
        height = st.number_input("Enter height", value=0.0)
        if st.button("Calculate"):
            result = geo_calc.triangle_area(base, height)
            st.success(f"Area: {result}")

    elif operation == "Triangle Perimeter":
        a = st.number_input("Enter side a", value=0.0)
        b = st.number_input("Enter side b", value=0.0)
        c = st.number_input("Enter side c", value=0.0)
        if st.button("Calculate"):
            result = geo_calc.triangle_perimeter(a, b, c)
            st.success(f"Perimeter: {result}")

def handle_arithmetic_calculations(arith_calc):
    operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])

    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    if operation == "Addition":
        if st.button("Calculate"):
            result = arith_calc.add(num1, num2)
            st.success(f"Result: {result}")

    elif operation == "Subtraction":
        if st.button("Calculate"):
            result = arith_calc.subtract(num1, num2)
            st.success(f"Result: {result}")

    elif operation == "Multiplication":
        if st.button("Calculate"):
            result = arith_calc.multiply(num1, num2)
            st.success(f"Result: {result}")

    elif operation == "Division":
        if st.button("Calculate"):
            try:
                result = arith_calc.divide(num1, num2)
                st.success(f"Result: {result}")
            except ValueError as e:
                st.error(e)

def handle_astronomy_calculations(astro_calc):
    operation = st.selectbox("Select Operation", ["UTC to Julian Date", "Julian Date to UTC", "Celestial Position", "Equatorial to Horizontal"])

    if operation == "UTC to Julian Date":
        utc_time = st.date_input("Select UTC Date", value=datetime.utcnow())
        if st.button("Calculate"):
            result = astro_calc.utc_to_julian_date(utc_time)
            st.success(f"Julian Date: {result}")

    elif operation == "Julian Date to UTC":
        julian_date = st.number_input("Enter Julian Date", value=0.0)
        if st.button("Calculate"):
            result = astro_calc.julian_date_to_utc(julian_date)
            st.success(f"UTC Date: {result}")

    elif operation == "Celestial Position":
        ra = st.number_input("Enter Right Ascension", value=0.0)
        dec = st.number_input("Enter Declination", value=0.0)
        observer_lat = st.number_input("Enter Observer Latitude", value=0.0)
        observer_lon = st.number_input("Enter Observer Longitude", value=0.0)
        if st.button("Calculate"):
            result = astro_calc.calculate_celestial_position(ra, dec, observer_lat, observer_lon)
            st.success(f"Position: Azimuth {result['azimuth']}, Altitude {result['altitude']}")

    elif operation == "Equatorial to Horizontal":
        ra = st.number_input("Enter Right Ascension", value=0.0)
        dec = st.number_input("Enter Declination", value=0.0)
        observer_lat = st.number_input("Enter Observer Latitude", value=0.0)
        observer_lon = st.number_input("Enter Observer Longitude", value=0.0)
        time = st.date_input("Select Date and Time", value=datetime.utcnow())
        if st.button("Calculate"):
            result = astro_calc.convert_equatorial_to_horizontal(ra, dec, observer_lat, observer_lon, time)
            st.success(f"Converted: Azimuth {result['azimuth']}, Altitude {result['altitude']}")

if __name__ == "__main__":
    main()