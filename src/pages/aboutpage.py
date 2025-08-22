from dash import html
import dash_bootstrap_components as dbc

layout = html.Div([

    # Page header
    html.Div([
        html.H2("ABOUT", style={"marginBottom": "30px", "color": "white", "fontSize": "40px"}),
        html.Div([
            html.A("Project Scope & Goals", href="#scope", className="about-btn"),
            html.A("The Team", href="#team", className="about-btn"),
            html.A("Impact of the BPGs", href="#impact", className="about-btn"),
        ], style={"display": "flex", "gap": "20px", "justifyContent": "center"})
    ], style={
        "textAlign": "center",
        "padding": "60px 20px 40px",
        "backgroundColor": "#001f3f"  # navy blue
    }),

    # Sections with centered boxes
    dbc.Container([

        # Project Scope & Goals
        dbc.Row(
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H3("Project Scope & Goals", className="card-title", style={"marginBottom": "20px"}),
                        html.P("This website was developed by a MSc Genomic Medicine student "
                               "from Imperial College London."),
                        html.P("Our goal with the site was to make the Best Practice Guidelines more "
                               "accessible and easier to understand by providing supplementary resources for nurses."),
                        html.P("On this site, you’ll find a list of all the BPGs organized into categories, "
                               "practice recommendation summaries, case studies and point-of-care resources "
                               "for helping nurses make evidence-based decisions during care moments.")
                    ])
                ], className="shadow-lg p-4", style={"borderRadius": "15px"})
            , width=8), justify="center", id="scope", style={"padding": "80px 0"}),

        # Team
        dbc.Row(
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H3("The Team", className="card-title", style={"marginBottom": "20px"}),

                         # Mary
                        dbc.Row([
                            dbc.Col([
                                html.H4("Mary Alikian", style={"color": "#001f3f", "fontWeight": "bold"}),
                                html.H6("Project Lead", className="card-subtitle"),
                                html.P("Imperial College London", className="card-text")
                            ], width=4),
                            dbc.Col([
                                html.P("Leads the overall project, supervises the MSc student and ensures successful "
                                       "completion of deliverables.")
                            ], width=8)
                        ], style={"marginBottom": "30px"}),

                        # Abdullah
                        dbc.Row([
                            dbc.Col([
                                html.H4("Abdullah Al Saud", style={"color": "#001f3f", "fontWeight": "bold"}),
                                html.H6("MSc Student", className="card-subtitle"),
                                html.P("Imperial College London", className="card-text")
                            ], width=4),
                            dbc.Col([
                                html.P("Responsible for analyzing survey data, preparing the final gap analysis report, "
                                       "and assisting in the organization of the workshop.")
                            ], width=8)
                        ], style={"marginBottom": "30px"}),

                        # Omar
                        dbc.Row([
                            dbc.Col([
                                html.H4("Omar Bashir", style={"color": "#001f3f", "fontWeight": "bold"}),
                                html.H6("MSc Student", className="card-subtitle"),
                                html.P("Imperial College London", className="card-text")
                            ], width=4),
                            dbc.Col([
                                html.P("Responsible for developing and administering the surveys to support "
                                       "the gap analysis of BPGs in genomic testing.")
                            ], width=8)
                        ], style={"marginBottom": "30px"}),

                        # Suphasan
                        dbc.Row([
                            dbc.Col([
                                html.H4("Suphasan Tangtokit", style={"color": "#001f3f", "fontWeight": "bold"}),
                                html.H6("MSc Student", className="card-subtitle"),
                                html.P("Imperial College London", className="card-text")
                            ], width=4),
                            dbc.Col([
                                html.P("Responsible for implementing the master BPG map and API to improve "
                                       "stakeholder engagement and facilitate data dissemination.")
                            ], width=8)
                        ])
                    ])
                ], className="shadow-lg p-4", style={"borderRadius": "15px"})
            , width=10), justify="center", id="team", style={"padding": "80px 0"}),

        # Impact
        dbc.Row(
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H3("The Impact of the BPGs", className="card-title", style={"marginBottom": "20px"}),
                        html.P("The Best Practice Guidelines use evidence-based research to develop structured approaches to "
                               "patient-centred care. Health care organizations that have implemented the BPGs, have seen improvements "
                               "in patient health, increases in the quality of care provided, and reduced health care costs."),
                    ])
                ], className="shadow-lg p-4", style={"borderRadius": "15px"})
            , width=8), justify="center", id="impact", style={"padding": "80px 0"}),

    ], fluid=True, style={"backgroundColor": "#001f3f"})  # navy background for entire page
])
