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
value_yrange = [0, 1000]
xx = [0]
yy = [0]
nameDict = {"Asparagus officinalis": "Asparagus_officinalis", "Coix lacryma-jobi": "Coix_lacryma-jobi"}
names = list(nameDict.keys())
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button("Search", color="primary", className="ml-2"),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)
app.layout = html.Div([
dbc.Navbar(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="https://i.imgur.com/gMvkB5k.jpg")),
                        dbc.Col(dbc.NavbarBrand("Navbar", className="ml-2"))],
                    align = "center",
                    no_gutters = True,

                ),
             ),
            dbc.NavbarToggler(id = "navbar-toggler"),
            dbc.Collapse(search_bar, id = "navbar-collapse", navbar = True),
        ],
        color = "dark",
        dark = True

    ),
    html.Button(
        id='button',
        style={"width": "20%", "display": "inline-block"},
        children='Update',
        n_clicks=0,

    ),
    dcc.Input(
        id="input",
        type='text',
        value='',
    ),
    html.Div(
        id = "data",
        style = {"display": "none"},

    ),
    html.Div(
        "",
        id = "space"
    ),
    dtc.ThemeToggle(
        bg_color_dark='#232323',
        icon_color_dark='#EDC575',
        bg_color_light='#07484E',
        icon_color_light='#C8DBDC',
        tooltip_text='Toggle light/dark theme'
    ),
    dcc.Dropdown(
        id = "dropmenu",
        options =[{'label': name, 'value': nameDict[name]}for name in names],
        value = ""
    ),
    html.Div(
        children="Binomial name:",
        style={"width": "7%", "display": "inline-block"},
        id="binomialprev",
    ),

    html.Div(
        children="Binomial Placeholder",
        style={"width": "8%", "display": "inline-block"},
        id="Binomial name",
    ),

    html.Div(
        children="Genus name:",
        style={"width": "7%", "display": "inline-block"},
        id="genusprev",
    ),
    html.Div(
        children="Genus Placeholder",
        style={"width": "8%", "display": "inline-block"},
        id="Genus",
    ),
    dcc.ConfirmDialog(
        children = "",
        id = "output-confirm",
        message = "Is this the correct plant? (Okay for yes, cancel for no)",

    ),
    dcc.Graph(
        id='graph',
        style = {"width": "60%", "float": "right", "display": "none" },
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
                'title': 'Water graph',
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

@app.callback([Output("Binomial name", "children"), Output("Genus", "children")], Output("data", "children"), Output("graph", "figure"), [Input("dropmenu", "value")])
def update_page(value):
        dtc.ThemeToggle()
        print(value)
        URL = "https://practicalplants.org/wiki/" + value
        String = main.parse_plant(URL)
        String = io.StringIO(String)
        predata = String
        data = pandas.read_csv(String, sep = ",")
        xx = [0,12,24]
        if (data["Water"].item() == "moderate"):
            yy = [500,500,500]
        else:
            yy = [250,250,250]
        figure = {
            'data': [
                go.Scatter(
                    x=xx,
                    y=yy,
                    mode='lines+markers',
                    marker=dict(size=15, color='orange'),
                    opacity=0.7,
                ),
            ], 'layout': {
                'title': (data["Binomial name"].item() + ' water graph'),
                "xaxis": {"range": value_range},
                "yaxis": {"range": value_yrange}
            }
        }
        return list(data["Binomial name"]), list(data["Genus"]), data["Genus"], figure

@app.callback([Output("graph", "figure")],[Input("id_1", "n_clicks"), Input("id_2", "n_clicks"), Input("id_3", "n_clicks"), Input("id_4", "n_clicks"), Input("id_5", "n_clicks")], [State("data", "children")])
def update_graph(children, input1, input2, input3, input4, input5):
    print(children)
    print("Yes")

# @app.callback([Output("Binomial name", "children"), Output("Genus", "children")], [Input("button", "n_clicks")], [State("input", "value")])
# def update_page(n_clicks, value):
#     if (n_clicks != 0):
#         results = main.search(value)
#         for i in range(len(results)):
#             result = popup_spawn(results[i+1])
#             if (result == True):
#                 String = results[i+1]
#         URL = "https://practicalplants.org/wiki/" + results[0]
#         String = main.parse_plant(URL)
#         String = io.StringIO(String)
#         data = pandas.read_csv(String, sep = ",")
#         return list(data["Binomial name"]), list(data["Genus"])
#
#
#
# @app.callback([Output("Binomial name", "children")],[Input("output-confirm", "submit_n_clicks"), State("output-confirm", "message")])
# def popup_mainsearch(submit_n_clicks, message):
#     if (submit_n_clicks):
#         return message
#     return False

if __name__ == '__main__':
    app.run_server(debug=True)
