#%%
import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc

#reading the airline data into pandas dataframe
airline_dataset = pd.read_csv('airline_data.csv', encoding='ISO-8859-1', dtype={'Div1Airport':str, 'Div1TailNum':str, 'Div2Airport':str, 'Div2TailNum':str})

#randomly sample 500 data points. 
data = airline_dataset.sample(n=500, random_state=42)

#creating a pie chart
fig = px.pie(data, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')

#creating a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.
app.layout = html.Div(children=[html.H1('Airline On-time Performance Dashboard',
                                            style={'textAlign':'center', 
                                                'color':'#503D36', 
                                                'font-size': 50}), 
                                html.P('Proportion of distance group(250 mile distance interval flights',
                                        style={'textAlign':'center', 'color':'#F57241'}), 
                                dcc.Graph(figure=fig)])

#running the application
if __name__ == '__main__':
    app.run()







# %%
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

#The file is encoded using ISO-8859-1 character encoding, which is a standard way of representing characters in the file.
#We defined data type of specific columns such as (Div1Airport, Div1TailNum, Div2Airport, and Div2TailNum) to be strings, which ensures that these columns are read as text instead of numbers.
airline_dataset = pd.read_csv('airline_data.csv',
                                encoding='ISO-8859-1',
                                dtype={'Div1Airport':str, 'Div1TailNum':str, 'Div2Airport':str, 'Div2TailNum':str})

#create a dash aplication layout
app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('Airline Performance Dashboard',
                                        style={'textAlign':'center','color':'#503D36', 'font-size':40}),
                                html.Div(['Input Year: ', dcc.Input(id = 'input-year', value='2010',
                                                                    type='number', style={'height':'50px', 'font-size':35}),],
                                style={'font-size':40}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id = 'line-plot')),
                                ])

#adding callback decorator
@app.callback( Output(component_id='line-plot', component_property='figure'), 
                Input(component_id='input-year', component_property='value'))

#add computation to callback function and return graph
def get_graph(entered_year):

    #select data based on the entered year
    df = airline_dataset[airline_dataset['Year']==int(entered_year)]
    
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()

    #group the data by month and compute average over arrival delay time.
    fig = go.Figure(data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
    fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
    return fig

#run the app
if __name__ == '__main__':
    app.run()


# %%
