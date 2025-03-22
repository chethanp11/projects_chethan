import pandas as pd
import plotly.express as px

def read_data(uploaded_file):
    if uploaded_file.name.endswith('.csv'):
        return pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        return pd.read_excel(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Please upload CSV or Excel.")

def determine_chart_type(data):
    numeric_columns = data.select_dtypes(include='number').columns
    if len(numeric_columns) >= 2:
        return 'line'
    elif len(numeric_columns) == 1:
        return 'bar'
    else:
        return 'pie'

def generate_chart(data, chart_type):
    numeric_cols = data.select_dtypes(include='number').columns
    non_numeric_cols = data.select_dtypes(exclude='number').columns

    if len(numeric_cols) == 0 or len(non_numeric_cols) == 0:
        raise ValueError("Need at least one numeric and one non-numeric column.")

    x = non_numeric_cols[0]
    y = numeric_cols[0]

    if chart_type == 'bar':
        fig = px.bar(data, x=x, y=y, title=f"Bar Chart: {y} by {x}")
    elif chart_type == 'line':
        fig = px.line(data, x=x, y=y, title=f"Line Chart: {y} over {x}")
    elif chart_type == 'pie':
        fig = px.pie(data, names=x, values=y, title=f"Pie Chart of {y}")
    else:
        raise ValueError(f"Unsupported chart type: {chart_type}")

    fig.update_traces(hoverinfo='label+percent+value', textinfo='label+percent')
    fig.update_layout(hovermode='x unified', template='plotly_white')

    return fig