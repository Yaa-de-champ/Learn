#%%
import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc

# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                'Div2Airport': str, 'Div2TailNum': str})

# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)

# Pie Chart Creation
fig = px.pie(data, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')

# Create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.
app.layout = html.Div(children=[html.H1('Airline Dashboard', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
                                html.P('Proportion of distance group (250 mile distance interval group) by flights.', style={'textAlign':'center', 'color': '#F57241'}),
                                dcc.Graph(figure=fig),
                                        ])

# Run the application                   
if __name__ == '__main__':
    app.run_server()



# %%
# Import required libraries
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

# Read the airline data into the pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                'Div2Airport': str, 'Div2TailNum': str})
# Create a dash application
app = dash.Dash(__name__)
                            
app.layout = html.Div(children=[ html.H1('Airline Performance Dashboard',style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
                                html.Div(["Input Year: ", dcc.Input(id='input-year', value='2010', 
                                type='number', style={'height':'50px', 'font-size': 35}),], 
                                style={'font-size': 40}),
                                html.Br(),
                                html.Br(),
                                html.Div(dcc.Graph(id='line-plot')),
                                ])

# add callback decorator
@app.callback( Output(component_id='line-plot', component_property='figure'),
            Input(component_id='input-year', component_property='value'))

# Add computation to callback function and return graph
def get_graph(entered_year):
    # Select 2019 data
    df =  airline_data[airline_data['Year']==int(entered_year)]
    
    # Group the data by Month and compute average over arrival delay time.
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()

    fig = go.Figure(data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
    fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
# %%
import pandas as pd

import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update

app = dash.Dash(__name__)

# REVIEW1: Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True

# Read the automobiles data into pandas dataframe
auto_data =  pd.read_csv('automobileEDA.csv', 
                            encoding = "ISO-8859-1",
                            )

#Layout Section of Dash

app.layout = html.Div(children=[html.H1('Car Automobile Components', 
                                style={'textAlign': 'center', 'color': '#503D36',
                                'font-size': 24}),

    #outer division starts
        html.Div([
            # First inner divsion for  adding dropdown helper text for Selected Drive wheels
                    html.Div(
                            html.H2('Drive Wheels Type:', style={'margin-right': '2em'}),
                    ),
                    #Second Inner division for adding 2 inner divisions for 2 output graphs 

                        dcc.Dropdown(
                            id='demo-dropdown',
                        options=[
                        {'label': 'Rear Wheel Drive', 'value': 'rwd'},
                            {'label': 'Front Wheel Drive', 'value': 'fwd'},
                            {'label': 'Four Wheel Drive', 'value': '4wd'}
        ],
        value='rwd'
        ),
                    #Second Inner division for adding 2 inner divisions for 2 output graphs 

                    html.Div([
                
                        html.Div([ ], id='plot1'),
                        html.Div([ ], id='plot2')

                        
                    ], style={'display': 'flex'}),

    ])
    #outer division ends

])
#layout ends

#Place to add @app.callback Decorator
@app.callback([Output(component_id='plot1', component_property='children'),
        Output(component_id='plot2', component_property='children')],
        Input(component_id='demo-dropdown', component_property='value'))


#Place to define the callback function .
def display_selected_drive_charts(value):



        filtered_df = auto_data[auto_data['drive-wheels']==value].groupby(['drive-wheels','body-style'],as_index=False). \
            mean()
        
        filtered_df = filtered_df

        fig1 = px.pie(filtered_df, values='price', names='body-style', title="Pie Chart")
        fig2 = px.bar(filtered_df, x='body-style', y='price', title='Bar Chart')
    
        return [dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2) ]



if __name__ == '__main__':
    app.run_server()
    
