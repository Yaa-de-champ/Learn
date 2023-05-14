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
import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output


# Add Dataframe
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "MTL", "NYC"]
})
# Add a bar graph figure
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(
        children='Dashboard',
        style={
            'textAlign': 'center'
        }
    ),
    
    # Create dropdown
    dcc.Dropdown(options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC' # Providing a vallue to dropdown
        ),
    # Bar graph    
    dcc.Graph(id='example-graph-2',figure=fig)

    ])
# Run Application
if __name__ == '__main__':
    app.run()

    
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

app.layout = html.Div(children=[#TASK 3A
                                html.H1('Car Automobile Components', style={'textAlign':'center', 'color':'#503D36', 'font-size': 24}),


        #outer division starts
        html.Div([
                    # First inner divsion for  adding dropdown helper text for Selected Drive wheels
                    html.Div(
                            #TASK 3B
                            [
                            html.H2('Drive Wheels Type:', style={'margin-right':'2em'}) #value 2em which means 2 times the size of the current font.
                                ]
                    ),
                    

                    #TASK 3C
                    dcc.Dropdown(id='demo-dropdown',
                                    options=[
                                        {'label': 'Rear Wheel Drive', 'value': 'rwd'},
                                        {'label': 'Front Wheel Drive', 'value': 'fwd'},
                                        {'label': 'Four Wheel Drive', 'value': '4wd'}
                                    ],
                                    value='rwd'
                                    ),

                    #Second Inner division for adding 2 inner divisions for 2 output graphs 
                    html.Div([
                
                        #TASK 3D
                        html.Div([ ], id='plot1'),
                        html.Div([ ], id='plot2')
                        
                ], style={'display': 'flex'}),

    ])
    #outer division ends

])
#layout ends

#Place to add @app.callback Decorator
#TASK 3E
@app.callback([Output(component_id='plot1', component_property='children'),
                Output(component_id='plot2', component_property='children')],
                Input(component_id='demo-dropdown', component_property='value'))

#Place to define the callback function .
#TASK 3F
def display_selected_drive_charts(value):


    filtered_df = auto_data[auto_data['drive-wheels']==value].groupby(['drive-wheels','body-style'],as_index=False). \
            mean() #The function first filters our dataframe auto_data by the selected value of the drive-wheels from the dropdown as follows
                        #The backslash allows you to break the statement into multiple lines without causing a syntax error.
                        #  as_index=False to make sure that the resulting DataFrame has the grouped columns as regular columns rather than as an index.
                        #.mean() calculates the mean of all the numeric columns in the resulting grouped DataFrame.
                        #The final output is a new DataFrame that shows the mean values of all the numeric columns for each unique combination of 'drive-wheels' and 'body-style' in the filtered DataFrame. This can be useful for analyzing how different car models with different body styles and drive wheels compare in terms of their mean values for various attributes.

                        
    filtered_df = filtered_df

    fig1 = px.pie(filtered_df, values='price', names='body-style', title="Pie Chart")
    fig2 = px.bar(filtered_df, x='body-style', y='price', title='Bar Chart')
        
    return [dcc.Graph(figure=fig1),
                dcc.Graph(figure=fig2) ]



if __name__ == '__main__':
    app.run_server()
    

# %%
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px



airline_dataset = pd.read_csv('airline_data.csv', encoding='ISO-8859-1', dtype={'Div1Airport':str, 'Div1TailNum':str, 'Div2Airport':str, 'Div2TailNum':str})

# Create a dash application
app = dash.Dash(__name__)


# Build dash app layout
app.layout = html.Div(children=[ html.H1('Flight Details Statistics Dashboard', 
                                style={'textAlign': 'center', 'color': '#503D36',
                                'font-size': 35}),
                                
                                #input component.
                                html.Div(["Input Year: ", dcc.Input(id='input-year', value='2010', 
                                type='number', style={'height':'35px', 'font-size': 30}),], 
                                style={'font-size': 30}),
                                html.Br(),
                                html.Br(), 

                                # Output component-Segment 1
                                html.Div([
                                        html.Div(dcc.Graph(id='carrier-plot')),
                                        html.Div(dcc.Graph(id='weather-plot'))
                                ], style={'display': 'flex'}),
                                # Output component-Segment 2
                                html.Div([
                                        html.Div(dcc.Graph(id='nas-plot')),
                                        html.Div(dcc.Graph(id='security-plot'))
                                ], style={'display': 'flex'}),
                                # Output component-Segment 3
                                html.Div(dcc.Graph(id='late-plot'), style={'width':'65%'})
                                ])


""" Compute_info function description
This function takes in airline data and selected year as an input and performs computation for creating charts and plots.
Arguments:
    airline_data: Input airline data.
    entered_year: Input year for which computation needs to be performed.
    
Returns:
    Computed average dataframes for carrier delay, weather delay, NAS delay, security delay, and late aircraft delay.
"""


def compute_info(airline_data, entered_year):
    # Select data
    df =  airline_data[airline_data['Year']==int(entered_year)]
    # Compute delay averages
    avg_car = df.groupby(['Month','Reporting_Airline'])['CarrierDelay'].mean().reset_index() #the resulting avg_car dataframe contains the average 'CarrierDelay' time (in minutes) for each combination of month and airline in the original dataset.
    avg_weather = df.groupby(['Month','Reporting_Airline'])['WeatherDelay'].mean().reset_index()
    avg_NAS = df.groupby(['Month','Reporting_Airline'])['NASDelay'].mean().reset_index()
    avg_sec = df.groupby(['Month','Reporting_Airline'])['SecurityDelay'].mean().reset_index()
    avg_late = df.groupby(['Month','Reporting_Airline'])['LateAircraftDelay'].mean().reset_index()
    return avg_car, avg_weather, avg_NAS, avg_sec, avg_late

#Task : Try to understand the function and importance of 'reset_index method"

"""Callback Function
Function that returns fugures using the provided input year.
Arguments:
    entered_year: Input year provided by the user.
    
Returns:
    List of figures computed using the provided helper function `compute_info`.
"""



# Callback decorator
@app.callback( [
                Output(component_id='carrier-plot', component_property='figure'),
                Output(component_id='weather-plot', component_property='figure'),
                Output(component_id='nas-plot', component_property='figure'),
                Output(component_id='security-plot', component_property='figure'),
                Output(component_id='late-plot', component_property='figure')
                ],
                Input(component_id='input-year', component_property='value'))


# Computation to callback function and return graph
def get_graph(entered_year):
    
    # Compute required information for creating graph from the data
    avg_car, avg_weather, avg_NAS, avg_sec, avg_late = compute_info(airline_dataset, entered_year)
            
    # Line plot for carrier delay
    carrier_fig = px.line(avg_car, x='Month', y='CarrierDelay', color='Reporting_Airline', title='Average carrrier delay time (minutes) by airline')
    # Line plot for weather delay
    weather_fig = px.line(avg_weather, x='Month', y='WeatherDelay', color='Reporting_Airline', title='Average weather delay time (minutes) by airline')
    # Line plot for nas delay
    nas_fig = px.line(avg_NAS, x='Month', y='NASDelay', color='Reporting_Airline', title='Average NAS delay time (minutes) by airline')
    # Line plot for security delay
    sec_fig = px.line(avg_sec, x='Month', y='SecurityDelay', color='Reporting_Airline', title='Average security delay time (minutes) by airline')
    # Line plot for late aircraft delay
    late_fig = px.line(avg_late, x='Month', y='LateAircraftDelay', color='Reporting_Airline', title='Average late aircraft delay time (minutes) by airline')

            
    return[carrier_fig, weather_fig, nas_fig, sec_fig, late_fig]


# Run the app
if __name__ == '__main__':
    app.run()

# %%
