'''
from pathlib import Path
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px



try:
    
    data = Path(__file__).parent.parent.joinpath("src\data", "prepared.csv")
    dataset_2016 = pd.read_csv(data)
    print("File successfully loaded.")
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("Error:", e)
dataset_2016['Year'] = 2016
data1 = Path(__file__).parent.parent.joinpath("src\data", "prepared1.csv")
dataset_2017 = pd.read_csv(data1)
dataset_2017['Year'] = 2017
data2 = Path(__file__).parent.parent.joinpath("src\data", "prepared2.csv")
dataset_2018 = pd.read_csv(data2)
dataset_2018['Year'] = 2018
data3 = Path(__file__).parent.parent.joinpath("src\data", "prepared3.csv")
dataset_2019 = pd.read_csv(data3)
dataset_2019['Year'] = 2019
data4 = Path(__file__).parent.parent.joinpath("src\data", "prepared4.csv")
dataset_2020 = pd.read_csv(data4)
dataset_2020['Year'] = 2020
data5 = Path(__file__).parent.parent.joinpath("src\data", "prepared5.csv")
dataset_2021 = pd.read_csv(data5)
dataset_2021['Year'] = 2021
data6 = Path(__file__).parent.parent.joinpath("src\data", "prepared6.csv")
dataset_2022 = pd.read_csv(data6)
dataset_2022['Year'] = 2022

all_data = pd.concat([dataset_2016,dataset_2017,dataset_2018,dataset_2019,dataset_2020, dataset_2021,dataset_2022], ignore_index=True)


year_datasets = {
    '2015/16': dataset_2016,
    '2016/17': dataset_2017,
    '2017/18': dataset_2018,
    '2018/19': dataset_2019,
    '2019/20': dataset_2020,
    '2020/21': dataset_2021,
    '2021/22': dataset_2022
}



def bar_chart(num_charts,selected_year):
    
    """
    Generate a bar chart comparing car parking spaces and cycle spaces for different Higher Education Providers.

    Args:
        num_charts (list): A list containing two integers representing the range of data to be plotted.
        selected_year (str): The selected year for which data will be plotted.

    Returns:
        plotly.graph_objs._figure.Figure: The generated bar chart figure.
    
    
    """
    
    if isinstance(selected_year, list):
        selected_year = selected_year[0]
    
    filtered_data = year_datasets[selected_year]
    

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=filtered_data['HE provider'][num_charts[0]:num_charts[1]],
        y=filtered_data['Total number of cycle spaces'][num_charts[0]:num_charts[1]],
        name='cycle_spaces'
    ))
    fig.add_trace(go.Bar(
        x=filtered_data['HE provider'][num_charts[0]:num_charts[1]],
        y=filtered_data['Total number of car parking spaces'][num_charts[0]:num_charts[1]],
        name='car_spaces',
        #marker=dict(color=['teal','cyan'])
    ))
    fig.update_layout(title='How does car parking spaces compare to cycle spaces for different Higher Education Providers?',
        #template="simple_white",
        barmode= 'group',height = 800,paper_bgcolor='#FFFFFF')
    fig.update_traces(marker_line_width=0.01)
    fig.update_xaxes(ticklen=0,tickfont=dict(size=16,color='teal'))
    return fig

def pie_chart(selected_provider,selected_year):
    
    """
    Generate a pie chart showing the distribution of cycle spaces and car parking spaces for a selected provider and year.

    Args:
        selected_provider (str): The name of the provider for which the pie chart is generated.
        selected_year (str): The selected year for which data will be plotted.

    Returns:
        plotly.graph_objs._figure.Figure: The generated pie chart figure
    
    """

    if isinstance(selected_year, list):
        selected_year = selected_year[0]
    filtered_data = year_datasets[selected_year]
    if selected_provider:
        filtered_data = filtered_data[filtered_data['HE provider'] == selected_provider]
    cycle_spaces = filtered_data['Total number of cycle spaces'].values[0]
    car_spaces = filtered_data['Total number of car parking spaces'].values[0]
    labels = ['Cycle Spaces', 'Car Spaces']
    colors = ['gold', 'lightgreen']
    values = [cycle_spaces,car_spaces]
    figure = go.Figure(data=[go.Pie(labels=labels, values=values,title=dict(text = f'Pie Chart for {selected_provider} ({selected_year})',font=dict(size=16,color="red")))]).update_layout(height= 600,margin=dict(b=1,t=5,r=4,l=40),
    paper_bgcolor='rgba(0,0,0,0)',  # Set plot background color to transparent paper_bgcolor='powderblue'
    legend=dict(x=0.8,y=0.9,font=dict(size=16,color='red'),# Show legend box
        bgcolor='rgba(0,0,0,0)',  # Set background transparent
        bordercolor="gray",  # Add border for visual separation
        borderwidth=1)                                            )
    figure.update_traces(textinfo='percent+label', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    return figure
    
def line_chart(selected_providers):
    
    """
    Generate a line chart showing the energy generated over the years for the selected providers.

    Args:
        selected_providers (list): A list of provider names for which the line chart is generated.

    Returns:
        plotly.graph_objs._figure.Figure: The generated line chart figure.
    """
    
    filtered_data = all_data[all_data['HE provider'].isin(selected_providers)]
    
    # Create line chart
    fig = go.Figure()
    for provider in selected_providers:
        provider_data = filtered_data[filtered_data['HE provider'] == provider]
        fig.add_trace(go.Scatter(x=provider_data['Year'], y=provider_data['Total renewable energy generated onsite or offsite (kWh)'], mode='lines+markers', name=provider,
                                 line=dict(width=1,shape='spline',smoothing=1.3),
                                 marker=dict(size=10)))
    fig.update_layout(title='Energy Over Years for Selected HE Providers',
                      xaxis_title='Year',
                      yaxis_title='Energy',
                      legend=dict(font=dict(size=13),orientation='h', xanchor='center', x=0.5, y=-0.2),height= 700,margin=dict(r=4,l=40),paper_bgcolor= '#FFFFFF')#'#3498db')
    return fig


def heatmap(selected_providers):
    
    """
    Generate a heatmap showing the energy generated over the years for the selected providers.

    Args:
        selected_providers (list): A list of provider names for which the heatmap is generated.

    Returns:
        plotly.graph_objs._figure.Figure: The generated heatmap figure.
    """
    filtered_data = all_data[all_data['HE provider'].isin(selected_providers)]
    filtered_data  = filtered_data.pivot(index='HE provider',columns='Year',values='Total renewable energy generated onsite or offsite (kWh)') 

    fig = px.imshow(filtered_data,color_continuous_scale=px.colors.sequential.Oranges)
    fig.update_layout(title='Distribution of Renewable Energy over years for different HE providers',height= 700)
    return fig
'''



    