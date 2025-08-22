from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from pathlib import Path
import pandas as pd

# Load CSV
data_path = Path(__file__).parent.parent.joinpath("data", "BPG.csv")
df = pd.read_csv(data_path, encoding="utf-8-sig").dropna(subset=['BPG'])

Date_of_publication = "Date of publication"
Status_col = "Status"
organisation_col = "organisation"

df[Date_of_publication] = pd.to_datetime(df[Date_of_publication], errors='coerce', dayfirst=True)


# 🔧 Normalise organisation column (fixes UKNEQAS issue)
df[organisation_col] = df[organisation_col].str.strip().str.upper()

# Organisation → Colour mapping
ORG_COLOURS = {
    "ACGS": "#1f77b4",   # Blue
    "EMQN": "#2ca02c",   # Green
    "GENQA": "#9467bd",  # Purple
    "UKNEQAS": "#ff0000" # Red
}

# Legend
legend = html.Div(
    [
        html.Span("ACGS", style={"color": ORG_COLOURS["ACGS"], "margin-right": "15px", "font-weight": "bold"}),
        html.Span("EMQN", style={"color": ORG_COLOURS["EMQN"], "margin-right": "15px", "font-weight": "bold"}),
        html.Span("GENQA", style={"color": ORG_COLOURS["GENQA"], "margin-right": "15px", "font-weight": "bold"}),
        html.Span("UKNEQAS", style={"color": ORG_COLOURS["UKNEQAS"], "margin-right": "15px", "font-weight": "bold"}),
    ],
    style={"text-align": "center", "margin-bottom": "15px"}
)

layout = dbc.Container([
    html.H2("THE BPGs", style={'text-align': 'center', 'margin-top': '20px'}),

    legend,  # Insert legend here

    # Controls row
    dbc.Row([
        dbc.Col(
            dbc.Checklist(
                options=[{"label": "Sort A-Z", "value": "sort"}],
                value=[],
                id="sort-checkbox",
                inline=True
            ),
            width="auto"
        ),
        dbc.Col(
            dbc.Checklist(
                options=[
                    {"label": "Oldest → Newest", "value": "oldest"},
                    {"label": "Newest → Oldest", "value": "newest"}
                ],
                value=[],
                id="date-sort-checkbox",
                inline=True
            ),
            width="auto"
        ),
        dbc.Col(
            dcc.DatePickerRange(
                id='date-picker-range',
                start_date_placeholder_text="Start date",
                end_date_placeholder_text="End date",
                display_format='DD/MM/YYYY',
                min_date_allowed=df[Date_of_publication].min(),
                max_date_allowed=df[Date_of_publication].max(),
                start_date=df[Date_of_publication].min(),
                end_date=df[Date_of_publication].max(),
                style={"margin-left": "10px"}
            ),
            width="auto"
        ),
        dbc.Col(
            dcc.Dropdown(
                id='status-dropdown',
                options=[
                    {"label": status, "value": status}
                    for status in sorted(df[Status_col].dropna().unique())
                ],
                placeholder="Filter by Status...",
                multi=True,
                clearable=True,
                style={"width": "250px"}
            ),
            width="auto"
        ),
        dbc.Col(
            dcc.Dropdown(
                id='organisation-dropdown',
                options=[
                    {"label": organisation, "value": organisation}
                    for organisation in sorted(df[organisation_col].dropna().unique())
                ],
                placeholder="Filter by Organisation...",
                multi=True,
                clearable=True,
                style={"width": "250px"}
            ),
            width="auto"
        ),
    ], align="center", justify="between", style={"margin-bottom": "15px"}),

    # Name search
    dbc.Input(
        id="search-input",
        placeholder="Search BPG...",
        type="text",
        debounce=True,
        style={"margin-bottom": "15px"}
    ),

    html.Div(id="alphabet-bar", style={
        "display": "flex",
        "flex-wrap": "wrap",
        "gap": "10px",
        "margin-bottom": "15px"
    }),

    html.Ul(id="bpg-list", style={'cursor': 'pointer', 'padding': 0}),
    html.Hr(),
    html.Div(id="bpg-details", style={"whiteSpace": "pre-line", "margin-top": "20px"})
], fluid=True)


@callback(
    Output("bpg-list", "children"),
    Output("alphabet-bar", "children"),
    Input("sort-checkbox", "value"),
    Input("search-input", "value"),
    Input("date-sort-checkbox", "value"),
    Input("date-picker-range", "start_date"),
    Input("date-picker-range", "end_date"),
    Input("status-dropdown", "value"),
    Input("organisation-dropdown", "value")
)
def update_bpg_list(sort_value, search_term, date_sort, start_date, end_date, status_filter, organisation_filter):
    df_copy = df.copy()

    # Name search
    if search_term:
        df_copy = df_copy[df_copy['BPG'].str.contains(search_term, case=False, na=False)]

    # Status filter
    if status_filter and len(status_filter) > 0:
        df_copy = df_copy[df_copy[Status_col].isin(status_filter)]

    # Organisation filter
    if organisation_filter and len(organisation_filter) > 0:
        df_copy = df_copy[df_copy[organisation_col].isin(organisation_filter)]

    # Date range filter
    if start_date:
        try:
            df_copy = df_copy[df_copy[Date_of_publication] >= pd.to_datetime(start_date)]
        except:
            pass
    if end_date:
        try:
            df_copy = df_copy[df_copy[Date_of_publication] <= pd.to_datetime(end_date)]
        except:
            pass

    # Date sorting
    if date_sort:
        if "oldest" in date_sort:
            df_copy = df_copy.sort_values(Date_of_publication, ascending=True)
        elif "newest" in date_sort:
            df_copy = df_copy.sort_values(Date_of_publication, ascending=False)

    # Keep BPG + organisation for colouring
    bpg_list_filtered = df_copy[['BPG', organisation_col]].values.tolist()

    # Alphabetical grouping
    if "sort" in sort_value:
        bpg_list_filtered.sort(key=lambda x: x[0])  # sort by BPG name
        grouped_items = []
        current_letter = ""
        available_letters = []

        for bpg, org in bpg_list_filtered:
            first_letter = bpg[0].upper()
            if first_letter != current_letter:
                grouped_items.append(html.H4(first_letter, id=f"letter-{first_letter}", style={"margin-top": "10px"}))
                available_letters.append(first_letter)
                current_letter = first_letter

            colour = ORG_COLOURS.get(org, "red")  # fallback if org missing
            grouped_items.append(
                html.Li(
                    dcc.Link(bpg, href=f"/bpgs/{bpg}",
                             style={"font-size": "16px", "text-decoration": "none", "color": colour}),
                    style={"list-style-type": "none", "margin-bottom": "5px", "cursor": "pointer"}
                )
            )

        alphabet_links = [
            html.A(letter, href=f"#letter-{letter}",
                   style={"text-decoration": "none", "font-weight": "bold", "color": "blue", "margin-right": "5px"})
            for letter in available_letters
        ]
        return grouped_items, alphabet_links

    # No alphabetical grouping
    unsorted_list = [
        html.Li(
            dcc.Link(bpg, href=f"/bpgs/{bpg}",
                     style={"font-size": "16px", "text-decoration": "none",
                            "color": ORG_COLOURS.get(org, "red")}),
            style={"list-style-type": "none", "margin-bottom": "5px", "cursor": "pointer"}
        )
        for bpg, org in bpg_list_filtered
    ]
    return unsorted_list, []
