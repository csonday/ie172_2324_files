import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

import webbrowser

from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import casefunctions

app = dash.Dash(__name__, external_stylesheets = ['assets/bootstrap.css'])

# we set the app title
app.title = "First Dash App"

app.layout = html.Div(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    html.H3(
                        "First Dash App", 
                        style={'fontWeight':'bold'}
                    )
                ),
                dbc.CardBody(
                    [
                        dbc.InputGroup(
                            [
                                dbc.InputGroupText("Input"), 
                                dbc.Input(id='input_value', value=None) #text box
                            ]
                        ),
                        html.Br(),
                        dbc.InputGroup(
                            [
                                dbc.InputGroupText("Process"), 
                                dbc.Select(
                                    id="process_type",
                                    options=[
                                        {"label": "Factorial", "value": "1"},
                                        {"label": "Palindrome Checker", "value": "2"},
                                        {"label": "Greeter", "value": "3"},
                                    ],
                                )
                            ]
                        ),
                        html.Br(),
                        dbc.Button(
                            "Calculate", 
                            size="lg", 
                            className="me-1", 
                            color='success',
                            id='confirm_process',
                            n_clicks=0
                        ),
                        html.Div(
                            "Output area",
                            id='output_container',
                            style={
                                'border':'2px dotted red',
                                'border-radius': '0.375em',
                                'padding': '1em',
                                'margin-top': '.5em'
                            }
                        )
                    ]
                )
            ]
        )
    ]
)


@app.callback(
    [ # outputs/updated elements
        Output('output_container', 'children')
    ],
    [ # triggers
        Input('confirm_process', 'n_clicks'),
    ],
    [ # additional inputs that are not triggers
        State('input_value', 'value'),
        State('process_type', 'value'),
    ]
)
def calculate(btnclick, input_value, process_type):
    if btnclick>0:
        if process_type == '1':
            outputvalue = casefunctions.get_factorial(input_value)
        elif process_type == '2':
            # replace output with the is_palindrome() function from casefunctions
            outputvalue = 'output 2'
        elif process_type == '3':
            # replace output with the greeter() function from casefunctions
            outputvalue = 'output 3'
        else:
            outputvalue = 'Select a valid process'
        
        return [outputvalue]
    else:
        raise PreventUpdate
    


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/', autoraise=True)
    app.run_server(debug=False)