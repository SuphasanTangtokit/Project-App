import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

layout = html.Div([

    # Page header with navigation buttons
    html.Div([
        html.H2("THE BASICS", style={"marginBottom": "30px", "color": "white", "fontSize": "40px"}),
        html.Div([
            html.A("What Are the BPGs?", href="#what", className="about-btn"),
            html.A("Evidence-Based Practice", href="#evidence", className="about-btn"),
        ], style={"display": "flex", "gap": "20px", "justifyContent": "center"})
    ], style={
        "textAlign": "center",
        "padding": "60px 20px 40px",
        "backgroundColor": "#001f3f"  # navy blue
    }),

    # Content sections in cards
    dbc.Container([

        # Section 1
        dbc.Row(
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H3("What Are the BPGs?", className="card-title", style={"marginBottom": "20px"}),
                        html.P("Best practice guidelines (BPGs) are meticulously crafted, evidence-based documents that "
                               "encapsulate research findings and offer recommendations to healthcare providers, leaders, "
                               "policymakers, patients, and families concerning a specific clinical or healthcare issue."),
                    ])
                ], className="shadow-lg p-4", style={"borderRadius": "15px"})
            , width=8), justify="center", id="what", style={"padding": "80px 0"}),

        ## Section 2 (Evidence-Based Practice + Subsection)
        dbc.Row(
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H3("Evidence-Based Practice", className="card-title", style={"marginBottom": "20px"}),
                        html.P("The Best Practice Guidelines are informed by evidence."),
                        html.P("This indicates that the recommendations offered are grounded in expert opinion and a thorough " \
                        "examination of data gathered from scientific research. They are created by groups of researchers, " \
                        "clinicians, and educators who possess specialized knowledge in the subject matter of each particular BPG. " \
                        "These teams are frequently interprofessional, resulting in a diverse array of knowledge and clinical " \
                        "proficiency."),
                        # Subsection
                        html.Div([
                            html.H4("How the BPGs are Developed", style={"marginTop": "30px", "marginBottom": "15px"}),

                            html.Ol([  # Ordered list for steps
                                html.Li([
                                    html.Span("Step 1: Conduct Literature Review", style={"fontWeight": "bold"}),
                                    html.P("The team conducts a literature review. This involves collecting and reviewing "
                                        "academic publications that provide evidence for approaches and procedures within "
                                        "clinical practice.", style={"marginLeft": "15px"})
                                ]),
                                html.Li([
                                    html.Span("Step 2: Evaluate Evidence", style={"fontWeight": "bold"}),
                                    html.P("After gathering information from academic sources, the team evaluates the evidence "
                                        "based on strength and merit. For example, research that's backed by a lot of data "
                                        "is given greater weight.", style={"marginLeft": "15px"})
                                ]),
                                html.Li([
                                    html.Span("Step 3: Synthesize & Summarize", style={"fontWeight": "bold"}),
                                    html.P("The evidence is then summarized and synthesized into a series of recommendations "
                                        "for how to approach clinical situations.", style={"marginLeft": "15px"})
                                ]),
                                html.Li([
                                    html.Span("Step 4: Review Recommendations", style={"fontWeight": "bold"}),
                                    html.P("The recommendations are reviewed by an external panel of experts. The panel determines "
                                        "what changes need to be made to the recommendations, working until they reach a consensus.",
                                        style={"marginLeft": "15px"})
                                ]),
                            ], style={"lineHeight": "2"})
                        ])
                    ])
                ], className="shadow-lg p-4", style={"borderRadius": "15px"})
            , width=8), justify="center", id="evidence", style={"padding": "80px 0"}),

    ], fluid=True, style={"backgroundColor": "#001f3f"})  # navy background for entire page
])
