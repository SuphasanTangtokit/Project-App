from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from figures import bar_chart,pie_chart,line_chart,heatmap
from pathlib import Path
import pandas as pd
from dash import dash_table
#data = Path(__file__).parent.parent.joinpath("data", "prepared6.csv")
#df = pd.read_csv(data)
data = Path(__file__).parent.parent.joinpath("data", "prepared.csv")
dataset_2016 = pd.read_csv(data)
data1 = Path(__file__).parent.parent.joinpath("data", "prepared1.csv")
dataset_2017 = pd.read_csv(data1)
data2 = Path(__file__).parent.parent.joinpath("data", "prepared2.csv")
dataset_2018 = pd.read_csv(data2)
data3 = Path(__file__).parent.parent.joinpath("data", "prepared3.csv")
dataset_2019 = pd.read_csv(data3)
data4 = Path(__file__).parent.parent.joinpath("data", "prepared4.csv")
dataset_2020 = pd.read_csv(data4)
data5 = Path(__file__).parent.parent.joinpath("data", "prepared5.csv")
dataset_2021 = pd.read_csv(data5)
data6 = Path(__file__).parent.parent.joinpath("data", "prepared6.csv")
dataset_2022 = pd.read_csv(data6)

all_data = pd.concat([dataset_2016,dataset_2017,dataset_2018,dataset_2019,dataset_2020, dataset_2021], ignore_index=True)


year_datasets = {
    '2015/16': dataset_2016,
    '2016/17': dataset_2017,
    '2017/18': dataset_2018,
    '2018/19': dataset_2019,
    '2019/20': dataset_2020,
    '2020/21': dataset_2021,
    '2021/22': dataset_2022
}
first_value = dataset_2022.iloc[8]['HE provider']
bar = bar_chart([1,9],'2015/16')
pie = pie_chart(first_value,'2015/16')
line = line_chart(['University College London'])
heat = heatmap(['The University of Greenwich'])
column_values = dataset_2022['HE provider'].unique()

dropdown_options = [{'label': value, 'value': value} for value in column_values]

checklist = dbc.RadioItems(id = 'checklist',
                          options = [{"label": "2015/16", "value": "2015/16"},
                                    {"label": "2016/17", "value": "2016/17"},
                                    {"label": "2017/18", "value": "2017/18"},
                                    {"label": "2018/19", "value": "2018/19"},
                                    {"label": "2019/20", "value": "2019/20"},
                                    {"label": "2020/21", "value": "2020/21"},
                                    {"label": "2021/22", "value": "2021/22"}],
                          value = ["2015/16"],
                          inline = True,
                          style={#'background-color': '#2ecc71',
                             'color': 'teal',
                             'border-radius':'5px',
                             'padding':'10px 40px',
                             'border':'none',
                             'cursor':'pointer'}
                          #type= 'radio'
)
Stats = {'Max_cycle_spaces': dataset_2022["cycle_spaces"].max(),
         'Max_car_spaces': dataset_2022["car_spaces"].max(),
         'Max_energy': dataset_2022["energy"].max()}

Table =  dash_table.DataTable(
            columns=[
                {"name": "", "id": "row-label"}  # Row label column
                for i in range(len(dataset_2022.columns))  # Numerical data columns
            ] + [{"name": i, "id": i} for i in dataset_2022.columns],
            data=[
                {"row-label": i} | dict(zip(dataset_2022.columns, row))  # Combine row label and data
                for i, row in dataset_2022.iterrows()
            ],
            merge_duplicate_headers=True,  # Merge top-level headers
            style_cell={"textAlign": "left"},
            style_header={"fontWeight": "bold"},
        )

"""Table  = dash_table.DataTable(
        id='table',
        columns=[{'name': col, 'id': col} for col in Stats.keys()],
        data=[Stats],
        style_table={'overflowX': 'auto','float': 'left', 'margin-right': '50px'},
        style_header={
            'writing-mode': 'vertical-rl',  # Rotate text vertically
            'text-orientation': 'mixed',  # Ensure text orientation is applied in all browsers
            'white-space': 'nowrap'  # Prevent text wrapping
        }
    )"""

dropdown = dcc.Dropdown(id = 'dropdown',
                      #options = dropdown_options,
                      value='',
                      placeholder='Select HE provider',
                      #search=True, 
                      #clearable=True
)

dropdown2 = dcc.Dropdown(
        id='provider-dropdown',
        options=[{'label': provider, 'value': provider} for provider in list(all_data['HE provider'].unique())],
        value=list(all_data['HE provider'].unique()[8]),  # Default selected provider
        multi= True
    )

slider = dcc.Slider(
        id='bar-slider',
        min=1,
        max=len(dataset_2022),  # Set the maximum value of the slider to the number of bars
        #step=1,
        value=5,  # Default value is the total number of bars
        #marks={i: str(i) for i in range(1, len(df) + 1)}  # Mark every integer from 1 to the number of bars
        #marks = {} # Dictionary
    )

range_slider = dcc.RangeSlider(
            id="he-provider-slider",
            min=1,
            max=len(all_data['HE provider'].unique()),
            value=[89, 97],  # Default to show all providers
            #marks={str(i): i for i in range(min, max + 1)},
            tooltip={"placement": "bottom"},
        )
row_one = html.Div(
    dbc.Row([
        dbc.Col(children=[html.H1("TRANSPORT AND ENVIRONMENT METRICS AT VARIOUS HIGHER EDUCATION PROVIDERS")
                 ], width=9,style={'font':'Lato','background-color': '#1a202c','color': '#4fd1c5'}),
        dbc.Col(children=[
            html.Img(src='/assets/logo.jpg', style={'top': '10px', 'right': '10px','width': '200px', 'height': '200px'}),
        ], width=3)
                
    ])
)
row_four = html.Div(
    dbc.Row([
        dbc.Col(children=[
            dbc.Input(id='search-input', type='text', placeholder='Enter search term'),
            html.Div(id='search-output')
        ], width=3),
    ])
)

row_five = html.Div(
    dbc.Row([dbc.Col(children=[
            dcc.Graph(id='bar', figure = bar)
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=12),
             ])
    )
row_two = html.Div(
    dbc.Row([dbc.Col(children=[range_slider
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=12),])
    ) 
row_three = html.Div(
    dbc.Row([dbc.Col(children=[dropdown
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=6),
             dbc.Col(children=[
                 checklist,
    ], width =5)])) 

row_nine = html.Div(
    dbc.Row([dbc.Col(children=[],width=12)]))


row_ten = html.Br()


row_six = html.Div(
    dbc.Row([dbc.Col(children=[],width=1),dbc.Col(children=[
        dcc.Graph(id='pie', figure = pie)], width=10
        ),#{"size": 4, "offset": 4}),
             #dbc.Col(children=[Table], width=5)
        dbc.Col(children=[],width=1)])
    )

row_seven = html.Div(
    dbc.Row([dbc.Col(children=[dcc.Graph(id='line', figure = line)
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=12)])) 
row_eleven = html.Div(dbc.Row([dbc.Col(children=[dcc.Graph(id='heat', figure = heat)
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=12)]))
row_eight = html.Div(
    dbc.Row([dbc.Col(children=[dropdown2
            #html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid"),
        ], width=12)])) 

"""row_six = html.Div([
    dcc.Dropdown(
        id='category-filter',
        options=[],
        value='',  # Default value
        searchable=True,  # Enable search functionality
        clearable=True
    ),
    dcc.Graph(id='pie',figure = pie)
])"""
