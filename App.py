
import dash
from dash.dependencies import Input, Output, State

import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt
import pandas as pd
import plotly.express as px
import json
import numpy as np
import plotly.graph_objects as go
import sklearn as sk


import dash
import dash_html_components as html


# Loading dataset "House Sales":
sales = pd.read_csv('raw_sales.csv')

# Data Manipulation here: 
# We artifficially add some variables to give some complexity 
sales["Bathrooms"] = sales["bedrooms"]/2 
sales["Bathrooms"] = sales["Bathrooms"].round()
sales["rooms"] = (sales["Bathrooms"] + 0.3 + sales["bedrooms"]*1.2).round()


# 
app.layout = html.H1(app.title) 
# 
if __name__ == '__main__':
# app.server.run() 

#
app = dash.Dash(__name__, title = "My Dashboard")

import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# App layout

import datetime as dt
dcc.Input(
    id='startdate-input',
    type='Date',
    value=dt.date.today() - dt.timedelta(days=60)
)

app.layout = html.Div([
  html.H1("Data Visualisation", style = {'text-align': 'center'}),
  
  dcc.Dropdown(id = "slct_year",
                 options = [
                     {"label": "Price", "value": 2015},
                     {"label": "Number of bathrooms", "value": 2016},
                     {"label": "Number of bedrooms", "value": 2017},
                     {"label": "Number of rooms", "value": 2018}],
                 multi = False,
                 value=2015,
                 style={'width': "40%"}
                 ),
    
    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})
    
    dcc.Input(
    id='startdate-input',
    type='Date',
    value=dt.date.today() - dt.timedelta(days=60)
)

])
                
if __name__ == '__main__':
    app.server.run() 
    app.server.run(debug=False)






df = px.data.tips()
# create the bins
df = sales
counts, bins = np.histogram(df.rooms, bins=range(0, 7, 1))
bins = (0.5 * (bins[:-1] + bins[1:])).round()

fig = px.bar(x=bins, y=counts, labels={'x':'total_bill', 'y':'count'})
fig.show()
