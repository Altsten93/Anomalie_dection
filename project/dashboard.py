
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# 1. Load Data
try:
    df = pd.read_csv('simulated_data.csv')
    # For the purpose of this demo, let's rename the columns
    df.rename(columns={
        'price_volatile': 'Urban Market',
        'price_stable': 'Suburban Market',
        'price_spiky': 'Rural Market'
    }, inplace=True)
    # Create a time index for the line chart
    df['Date'] = pd.to_datetime(pd.date_range(start='2023-01-01', periods=len(df), freq='D'))
except FileNotFoundError:
    # Create a dummy dataframe if the file is not found
    df = pd.DataFrame({
        'Urban Market': [0], 'Suburban Market': [0], 'Rural Market': [0], 'Date': [pd.to_datetime('2023-01-01')]
    })

# 2. Initialize the Dash App
app = dash.Dash(__name__)
app.title = "House Price Simulation Dashboard"

# 3. Define the App Layout
app.layout = html.Div(style={'fontFamily': 'Arial, sans-serif', 'padding': '20px', 'backgroundColor': '#f4f4f4'}, children=[
    html.H1(
        children='House Price Simulation Dashboard',
        style={'textAlign': 'center', 'color': '#333'}
    ),

    html.Div(
        children='An interactive dashboard to visualize simulated house price data for different markets.',
        style={'textAlign': 'center', 'color': '#555', 'marginBottom': '30px'}
    ),

    html.Div(children=[
        html.Div(children=[
            html.Label('Select Housing Market:', style={'fontWeight': 'bold'}),
            dcc.Dropdown(
                id='market-dropdown',
                options=[{'label': col, 'value': col} for col in ['Urban Market', 'Suburban Market', 'Rural Market']],
                value='Urban Market', # Default value
                clearable=False,
                style={'marginBottom': '20px'}
            ),
        ], style={'padding': '10px'}),
    ]),

    html.Div(children=[
        html.Div(children=[
            dcc.Graph(id='price-line-chart')
        ], style={'padding': '10px'}),
    ]),

    html.Div(children=[
        html.Div(children=[
            dcc.Graph(id='price-histogram')
        ], style={'padding': '10px'}),
    ])
])

# 4. Define the Callbacks
@app.callback(
    [Output('price-line-chart', 'figure'),
     Output('price-histogram', 'figure')],
    [Input('market-dropdown', 'value')]
)
def update_charts(selected_market):
    # Line Chart
    line_fig = px.line(
        df,
        x='Date',
        y=selected_market,
        title=f'Simulated Prices for {selected_market}',
        labels={'value': 'Price (in thousands)', 'Date': 'Date'}
    )
    line_fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_color='#333'
    )

    # Histogram
    hist_fig = px.histogram(
        df,
        x=selected_market,
        nbins=50,
        title=f'Price Distribution for {selected_market}',
        labels={'x': 'Price Bins', 'y': 'Count'}
    )
    hist_fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_color='#333',
        bargap=0.1
    )

    return line_fig, hist_fig

# 5. Run the App
if __name__ == '__main__':
    app.run_server(debug=True)
