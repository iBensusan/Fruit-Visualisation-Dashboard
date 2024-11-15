import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Sample data
data = {
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Strawberries'],
    'Amount': [4, 1, 2, 5, 3],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Fruit Visualization Dashboard"),
    dcc.Dropdown(
        id='fruit-dropdown',
        options=[{'label': fruit, 'value': fruit} for fruit in df['Fruit']],
        value='Apples'
    ),
    dcc.Graph(id='fruit-bar-chart'),
])

# Define the callback to update the graph
@app.callback(
    Output('fruit-bar-chart', 'figure'),
    Input('fruit-dropdown', 'value')
)
def update_graph(selected_fruit):
    # Filter data based on selected fruit
    filtered_df = df[df['Fruit'] == selected_fruit]
    fig = px.bar(
        filtered_df,
        x='Fruit',
        y='Amount',
        title=f"Amount of {selected_fruit}",
        color='Fruit'
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
