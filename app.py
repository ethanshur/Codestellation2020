import io

import dash
import plotly
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
from dash.dash import no_update
import pandas
import dash_trich_components as dtc
import main

value_range = [0,24]
value_yrange = [0, 800]
xx = [0]
yy = [0]
nameDict = {"Asparagus officinalis": "Asparagus_officinalis", "Coix lacryma-jobi": "Coix_lacryma-jobi"}
names = list(nameDict.keys())
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([
        dbc.Navbar(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="https://i.imgur.com/qXfTTbl.png")),
                        dbc.Col(dbc.NavbarBrand("botNy", className="ml-2"))],
                    align = "center",
                    no_gutters = True,

                ),
             ),
            dbc.NavbarToggler(id = "navbar-toggler"),
        ],
        color = "dark",
        dark = True

    ),
    #html.Img(
     #   id = "logo",
     #   src = "https://i.imgur.com/qXfTTbl.png",
     #   style = {"position": "fixed", "top": 0, "right": 0},
     #   width = "10%",
     #   height = "10%",
#),
    html.Button(
        id='button',
        style={"width": "10%", "display": "inline-block"},
        children='Update',
        n_clicks=0,
    ),
    dcc.Input(
        id="input",
        type='text',
        style={"width": "30%"},
        value='',
    ),

    html.Button(
        id = "input-button",
        style={"width": "10%","left": 0, "display": "inline-block"},
        children = "Import",
        n_clicks = 0,
    ),
    html.Div(
        id = "data",
        style = {"display": "none"},
    ),
    dcc.Dropdown(
        id = "dropmenu",
        options =[{'label': name, 'value': nameDict[name]}for name in names],
        value = ""
    ),
    html.Div(
        children="Binomial name:",
        style={"position":"relative", "width": "7%", "display": "inline-block"},
        id="binomialprev",
    ),

    html.Div(
        children="Binomial Placeholder",
        style={"position":"relative", "width": "93%", "display": "inline-block"},
        id="Binomial name",
    ),

    html.Div(
        children="Genus name:",
        style={"position":"relative","width": "7%", "display": "inline-block"},
        id="genusprev",
    ),
    html.Div(
        children="Genus Placeholder",
        style={"position":"relative","width": "93%", "display": "inline-block"},
        id="Genus",
    ),

    html.Div(
        children= "Family name:",
        style={"position":"relative","width": "7%", "display": "inline-block"},
        id = "familyprev",
    ),
    html.Div(
        children = "Family Placeholder:",
        style={"position":"relative","width": "93%", "display": "inline-block"},
        id = "Family",
    ),

    html.Div(
        children = "Soil pH:",
        style={"position":"relative","width": "7%", "display": "inline-block"},
        id = "phprev",
    ),
    html.Div(
        children = "pH Placeholder",
        style={"position":"relative","height": "93%", "display": "inline-block"},
        id = "pH",
    ),
    html.Div(
        children = "Special thanks to Jacob Smith for providing us a new sensor when ours broke",
        style = {"position": "fixed", "bottom": 0, "left": 0, "width": "300px", "border": "3px solid"},
    ),
    dcc.Graph(
        id='sungraph',
        style = {"width": "60%", "float": "right", "display": "none", "position": "static" },
        figure={
            'data': [
                go.Scatter(
                    x=xx,
                    y=yy,
                    mode='markers',
                    marker=dict(size=15, color='orange'),
                    opacity=0.7,
                ),
            ], 'layout': {
                'title': 'Sunlight graph',
                "xaxis": {"range": value_range},
                "yaxis": {"range": value_yrange}
            }
        }),
    dcc.Graph(
        id='tempgraph',
        style = {"width": "60%", "float": "right", "display": "none", "position": "static" },
        figure={
            'data': [
                go.Scatter(
                    x=xx,
                    y=yy,
                    mode='markers',
                    marker=dict(size=15, color='orange'),
                    opacity=0.7,
                ),
            ], 'layout': {
                'title': 'Temperature graph',
                "xaxis": {"range": value_range},
                "yaxis": {"range": value_yrange}
            }
        }),
    dcc.Graph(
        id='humiditygraph',
        style = {"width": "60%", "float": "right", "display": "none", "position": "static" },
        figure={
            'data': [
                go.Scatter(
                    x=xx,
                    y=yy,
                    mode='markers',
                    marker=dict(size=15, color='orange'),
                    opacity=0.7,
                ),
            ], 'layout': {
                'title': 'Humidity graph',
                "xaxis": {"range": value_range},
                "yaxis": {"range": value_yrange}
            }
        }),
])


@app.callback([Output("dropmenu", "options"), Output("dropmenu", "value")], [Input("button", "n_clicks")], [State("input", "value"), State("dropmenu", "options")],)
def update_page(n_clicks, value, options):
    if (n_clicks != 0):
        results = main.search(value)
        noptions = options
        for i in results:
            noptions.append({"label": i, "value": i})
        print(noptions)
        return noptions, noptions[0]["label"]

    #[{'label': name, 'value': nameDict[name]} for name in names],

# @app.callback([Output("Binomial name", "children")],[Input("output-confirm", "submit_n_clicks"), State("output-confirm", "message")])
# def popup_mainsearch(submit_n_clicks, message):
#     if (submit_n_clicks):
#         return message
#     return False

@app.callback([Output("Binomial name", "children"), Output("Genus", "children"), Output("Family", "children"), Output("pH", "children"), Output("sungraph", "style"), Output("sungraph", "figure"), Output("tempgraph", "style"), Output("humiditygraph", "style")], [Input("dropmenu", "value")])
def update_page(value):
        dtc.ThemeToggle()
        URL = "https://practicalplants.org/wiki/" + value
        style = {"width": "60%", "float": "right", "position": "relative"}
        String = main.parse_plant(URL)
        String = io.StringIO(String)
        predata = String
        data = pandas.read_csv(String, sep = ",")
        xx = [0,12,24]

        if (data["Sun"].item() == "full sun"):
            yy = [650]
            for i in range(len(xx)):
                yy.append(yy[0])
            print(yy)

        elif (data["Sun"].item == "partial sun"):
            yy = [500]
            for i in range(len(xx)):
                yy.append(yy[0])
            print(yy)
        else:
            yy = [300]
            for i in range(len(xx)):
                yy.append(yy[0])
            print(yy)
        print(data["Sun"].item)
        print(data["Native Climate Zones"].item)
        figure_sun = {
            'data': [
                go.Scatter(
                    x=xx,
                    y=yy,
                    mode='lines+markers',
                    marker=dict(size=15, color='orange'),
                    opacity=0.7,
                ),
            ], 'layout': {
                'title': (data["Binomial name"].item() + ' Sun Graph'),
                "xaxis": {"range": value_range},
                "yaxis": {"range": value_yrange}
            }
        }
        return list(data["Binomial name"]), list(data["Genus"]), list(data["Family"]), list(data["Soil PH"]), style, figure_sun,style,style
@app.callback([Output("sungraph", "style"), Output("sungraph", "figure"), Output("tempgraph", "style"), Output("humiditygraph", "style")], [Input("input-button", "n_clicks")])
def import_data(n_clicks):
    if n_clicks != 0:

if __name__ == '__main__':
    app.run_server(debug=True)
