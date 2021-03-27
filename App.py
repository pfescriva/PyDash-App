
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

app = dash.Dash(__name__, title = "My Dashboard")

# Loading dataset "House Sales":
sales = pd.read_csv('raw_sales.csv')

# Data Manipulation here: 

# PyDash is in a way similar to RShinny. Instead of the UI, you have to append to the App.layout 
# app.layout: the layout part of the app, and you create there the .html components 


import dash
import dash_html_components as html

app = dash.Dash(__name__, title="2021 (Mis cojones) Dash Python App")
# 
app.layout = html.H1(app.title) 
# 
if __name__ == '__main__':
# app.server.run() 







