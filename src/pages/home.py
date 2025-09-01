import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

layout = html.Div(
    dbc.Container([
        # Top tab with navy background
        html.Div([
            html.H6("BEST PRACTICE GUIDELINES", style={
                'text-align': 'center',
                'font-weight': 'normal',
                'color': '#fff',
                'font-size': '16px',
                'margin': '0',
                'padding-top': '0px',
                'padding-bottom': '0px',
                'font-family': 'Arial, sans-serif'
            }),
            html.H1("Care advice for professionals.", style={
                'text-align': 'center',
                'font-family': 'Lato, Arial, sans-serif',
                'font-weight': 'bold',
                'color': '#fff',
                'font-size': '36px',
                'margin': '0',          # remove margin to avoid gaps
                'padding-bottom': '20px'
            }),
        ],
        style={
            'backgroundColor': '#001f3f',  # navy blue
            'padding': '20px 0',           # vertical padding for some breathing room
            'border-radius': '0',
            'margin-bottom': '0',
        }),

        # Cards below the top tab
        html.Div([
            dbc.Row([
                dbc.Col(
                    html.A(
                        dbc.Card(
                            dbc.CardBody([
                                html.Div("About", style={'text-align': 'center'})
                            ]),
                            style={
                                'height': '150px',
                                'cursor': 'pointer',
                                'border': '1px solid black'
                            }
                        ),
                        href='/about'
                    ),
                    width=5,
                    style={'padding': '0 5px'}  # reduce column padding
                ),
                dbc.Col(
                    html.A(
                        dbc.Card(
                            dbc.CardBody([
                                html.Div("The Basics", style={'text-align': 'center'})
                            ]),
                            style={
                                'height': '150px',
                                'cursor': 'pointer',
                                'border': '1px solid black'
                            }
                        ),
                        href='/basics'
                    ),
                    width=5,
                    style={'padding': '0px'}
                )
            ], justify='center', className='mb-3', style={'margin': '0'}),

            dbc.Row([
                dbc.Col(
                    html.A(
                        dbc.Card(
                            dbc.CardBody([
                                html.Div("The BPGs", style={'text-align': 'center'})
                            ]),
                            style={
                                'height': '160px',
                                'cursor': 'pointer',
                                'border': '0px solid black'
                            }
                        ),
                        href='/bpgs'
                    ),
                    width=10,
                    style={'padding': '0 5px'}
                )
            ], justify='center', className='mb-3', style={'margin': '0'}),
        ], style={'padding': '0', 'margin': '0'}),

    ],
    style={'padding': '0', 'margin': '0', 'maxWidth': '900px'}),  # Container style

    style={
        'height': '100vh',
        'display': 'flex',
        'justify-content': 'center',
        'align-items': 'center',
        'flex-direction': 'column',
        'backgroundColor': '#001f3f',  # navy blue background
        'margin': '0',
        'padding': '0',
    }
)

if __name__ == '__main__':
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = layout
    app.run_server(debug=True)
