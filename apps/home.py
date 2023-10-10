# Usual Dash dependencies
import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc, html
from dash.exceptions import PreventUpdate

# Let us import the app object in case we need to define
# callbacks here
from app import app

# store the layout objects into a variable named layout
layout = html.Div(
    [
        html.H2('Welcome to our app!'),
        html.Hr(),
        html.Div(
            [
                html.Span(
                    "Thru this app, you can manage a database of movies that are classified according to genres.",
                ),
                html.Br(),
                html.Br(),
                html.Span(
                    "Contact the owner if you need assistance!",
                    style={'font-style':'italic'}
                ),
            ]
        )
    ]
)
