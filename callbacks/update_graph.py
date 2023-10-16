import numpy as np
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from joblib import load

# Cargar los datos
forecast_df = load('data/forecast_df.pkl')
historical = load('data/historical.pkl')
df_test_transformed = load('data/df_test_transformed.pkl')
forecast_df2 = load('data/forecast_df1.pkl')
historical2 = load('data/historical1.pkl')
df_test_transformed2 = load('data/df_test_transformed1.pkl')

print(df_test_transformed2.head())
print(forecast_df2.head())



def register_callbacks(app):

    # Devolución de llamada para el primer gráfico
    @app.callback(
        Output('forecast-graph-1', 'figure'),
        [Input('forecast-graph-1', 'id'),
         Input('year-dropdown', 'value')]
    )
    def update_graph_1(_, selected_year):
         # Si se seleccionó 'all', no filtrar datos
        if selected_year == 'all':
            filtered_historical = historical
            filtered_forecast = forecast_df
            filtered_test = df_test_transformed
        else:
            # Filtrar datos por el año seleccionado
            filtered_historical = historical[historical.index.year == selected_year]
            filtered_forecast = forecast_df[forecast_df.index.year == selected_year]
            filtered_test = df_test_transformed[df_test_transformed.index.year == selected_year]

        fig1 = go.Figure()

        fig1.add_trace(go.Scatter(x=filtered_historical.index, y=filtered_historical.values,
                                  mode='lines', name='Datos historicos', line=dict(color='green')))
        fig1.add_trace(go.Scatter(x=filtered_forecast.index, y=filtered_forecast['Forecast'].values,
                                  mode='lines', name='Prediccion', line=dict(color='red')))
        fig1.add_trace(go.Scatter(x=filtered_test.index, y=filtered_test.values,
                                  mode='lines', name='Valores reales', line=dict(color='blue')))

        fig1.update_layout(title='Predicción de Importación de Gasolina Regular', xaxis_title='Date', yaxis_title='Importaciones de gasolina regular')
        
        return fig1

    # Devolución de llamada para el segundo gráfico
    @app.callback(
        Output('forecast-graph-2', 'figure'),
        [Input('forecast-graph-2', 'id'),
         Input('year-dropdown', 'value')]
    )
    def update_graph_2(_, selected_year):
        # Si se seleccionó 'all', no filtrar datos
        if selected_year == 'all':
            filtered_historical2 = historical2
            filtered_forecast2 = forecast_df2
            filtered_test2 = df_test_transformed2
        else:
            # Filtrar datos por el año seleccionado
            filtered_historical2 = historical2[historical2.index.year == selected_year]
            filtered_forecast2 = forecast_df2[forecast_df2.index.year == selected_year]
            filtered_test2 = df_test_transformed2[df_test_transformed2.index.year == selected_year]

        fig2 = go.Figure()

        fig2.add_trace(go.Scatter(x=filtered_historical2.index, y=filtered_historical2.values, mode='lines', name='Datos historicos', line=dict(color='green')))
        fig2.add_trace(go.Scatter(x=filtered_forecast2.index, y=filtered_forecast2['Forecast'].values, mode='lines', name='Prediccion', line=dict(color='red')))
        fig2.add_trace(go.Scatter(x=filtered_test2.index, y=filtered_test2["Diesel_conjunto"].values, mode='lines', name='Valores reales', line=dict(color='blue')))

        fig2.update_layout(title='Predicción del Consumo de Diesel', xaxis_title='Date', yaxis_title='Consumo de Diesel')
        
        return fig2
