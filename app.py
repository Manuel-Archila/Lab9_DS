import dash
from dash.dependencies import Input, Output
from layouts.main_layout import main_layout
from callbacks.update_graph import register_callbacks

# Inicializa la aplicación
app = dash.Dash(__name__)
server = app.server

app.layout = main_layout
register_callbacks(app)

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
