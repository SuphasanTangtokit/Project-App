import dash
from dash import Dash, html, dcc, Output, Input
import urllib.parse
import unicodedata
import dash_bootstrap_components as dbc
import pandas as pd
from pathlib import Path
from pages import bpgs, home, aboutpage, thebasics
import requests
import json

data_path = Path(__file__).parent.joinpath("data", "BPG.csv")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def clean_column_name(col):
    col = unicodedata.normalize("NFKC", col)
    col = col.replace("\xa0", " ").replace("\u202f", " ")
    col = col.strip()
    col = " ".join(col.split())
    return col

df = pd.read_csv(data_path, encoding="utf-8-sig").dropna(subset=["BPG"])

df.columns = [clean_column_name(c) for c in df.columns]

# Clean string values elementwise
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)




# Shared top navbar (full-width)
navbar = dbc.Navbar(
    dbc.Container([
        dbc.NavbarBrand("Masters BPG Map", href="/", className="ms-2"),
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("About", href="/about")),
                dbc.NavItem(dbc.NavLink("The Basics", href="/basics")),
                dbc.NavItem(dbc.NavLink("BPG Maps", href="/bpgs")),
            ],
            className="ms-auto",
            navbar=True
        ),
    ], fluid=True),  # makes navbar span entire screen
    color="dark",
    dark=True,
    sticky="top",
    className="p-2"
)

# App layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content', style={'margin-top': '20px'}),
    html.A('Go to top', href='#top', id='top-link',
           style={'background-color': 'gray', 'color': 'white', 'padding': '10px', 'position': 'fixed', 'bottom': '20px', 'right': '20px'})
])



def bpg_detail_layout(bpg_name):
    # Decode name from URL
    decoded_name = urllib.parse.unquote(bpg_name).strip()

    # Case-insensitive match + strip any extra spaces
    match = df[df['BPG'].str.strip().str.lower() == decoded_name.lower()]

    if match.empty:
        return html.Div(f"No details found for {decoded_name}", style={'textAlign': 'center', 'marginTop': '50px'})

    row_data = match.iloc[0].fillna("N/A").to_dict()

    # Columns to display
    desired_columns = [
        "New Category",
        "New Category_Subgroup",
        "Old Category",
        "Date of publication",
        "Status",
        "Version",
        "comments",
        "organisation",
        "WG lead",
        "WG lead email",
        "WG members",
        "Justification"
    ]

    # Build table rows
    rows = []
    for col in desired_columns:
        value = row_data.get(col, "N/A")
        rows.append(html.Tr([html.Th(col), html.Td(str(value))]))

    return dbc.Container([
        html.H2(f"BPG Detail: {decoded_name}", style={'textAlign': 'center', 'marginTop': '20px'}),
        dbc.Table([
            html.Thead(html.Tr([html.Th("Field"), html.Th("Value")])),
            html.Tbody(rows)
        ], bordered=True, striped=True),
        html.Br(),
        dcc.Link("Back to BPG list", href="/bpgs")
    ], fluid=True)

# Page routing
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if not pathname or pathname == '/':
        return home.layout
    elif pathname == '/about':
        return aboutpage.layout
    elif pathname == '/basics':
        return thebasics.layout
    elif pathname == '/bpgs':
        return bpgs.layout
    elif pathname.startswith('/bpgs/'):
        bpg_name = pathname.split('/bpgs/')[1]
        return bpg_detail_layout(bpg_name)
    else:
        return html.Div("404 - Page not found", style={'textAlign': 'center', 'padding': '50px'})

# Hide "go to top" link only on homepage
@app.callback(
    Output('top-link', 'style'),
    [Input('url', 'pathname')]
)
def update_top_link_style(pathname):
    if pathname == '/' or pathname == '/home':
        return {'display': 'none'}
    return {'background-color': 'gray', 'color': 'white', 'padding': '10px',
            'position': 'fixed', 'bottom': '20px', 'right': '20px'}

if __name__ == '__main__':
    app.run(debug=True)


