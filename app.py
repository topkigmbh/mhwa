from dash import Dash, dcc, html, Input, Output
import os


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H2('Hier war mal ein Schweinepriester App'),
    dcc.Dropdown(['Kinder', 'tote', 'Tiere'],
        'Tiere',
        id='dropdown'
    ),
    html.Div(id='display-value')
])

@app.callback(Output('display-value', 'children'),
                [Input('dropdown', 'value')])
def display_value(value):
    return f'Sie haben folgendes gewählt {value}'

if __name__ == '__main__':
    app.run_server(debug=True)