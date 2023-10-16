from dash import dcc
from dash import html

main_layout = html.Div([
    html.H1('Predicciones con Modelos ARIMA'),

    # Dropdown para la selección del año
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': 'Todos los años', 'value': 'all'}] + [{'label': str(year), 'value': year} for year in range(2020, 2023)],
        value='all'  # Valor por defecto
    ),
    dcc.Graph(id='forecast-graph-1', style={'margin-bottom': '50px'}),
    dcc.Graph(id='forecast-graph-2'),
])
