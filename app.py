import io

import dash
import plotly
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
from dash.dash import no_update
import pandas

import main

value_range = [0, 24]
value_yrange = [0, 1000]
xx = [24]
yy = [1000]
app = dash.Dash(__name__)
app.layout = html.Div([
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
        "",
        id = "space"
    ),

    html.Div(
        children="Binomial name:",
        style={"width": "7%", "display": "inline-block"},
        id="binomialprev",
    ),

    html.Div(
        children = "Binomial Placeholder",
        style = {"width": "8%", "display": "inline-block"},
        id = "Binomial name",
    ),

html.Div(
        children="Genus name:",
        style={"width": "7%", "display": "inline-block"},
        id="genusprev",
    ),
    html.Div(
        children = "Genus Placeholder",
        style={"width": "8%", "display": "inline-block"},
        id = "Genus",
    ),
    dcc.Graph(
        id='graph',
        figure={
            'data': [
                go.Scatter(
                    x=xx,
                    y=yy,
                    mode='markers',
                    marker=dict(size=15, color='orange'),
                    opacity=0.7,
                    # line=dict(width=2, color="red"),

                    # name=i
                ),  # for i in df.continent.unique()
            ], 'layout': {
                'title': 'graph-1',
                "xaxis": {"range": value_range},
                "yaxis": {"range": value_yrange}
            }
        })
])

x = xx
y = yy


# @app.callback(Output('graph', 'figure'), [Input('button', 'n_clicks')], [Input("input", "value")])
# def update_graph(n_clicks):
#     if n_clicks == 0:
#         raise no_update
#     #out = io.StringIO(main.search(input))
#     #data = pandas.read_csv(out, sep=",")
#     #if "no shade" in (data["Sun"]):
#        # print("hello")
#     return {
#         'data': [{
#             'x': x[0],
#             'y': y[0],
#         }],
#         'layout': {
#             'title': ('graph ' + str(n_clicks)),
#             "xaxis": {"range": [0, (value_range[1] + (24 * int(n_clicks)))]},
#         }
#     }
# def update_text(value):
#     return "input: {}".format(value)

@app.callback([Output("Binomial name", "children"), Output("Genus", "children")], [Input("button", "n_clicks")], [State("input", "value")])
def update_page(n_clicks, value):
    if (n_clicks != 0):
        String = main.search(value)
        String = io.StringIO(String)
        data = pandas.read_csv(String, sep = ",")
        return list(data["Binomial name"]), list(data["Genus"])




if __name__ == '__main__':
    app.run_server(debug=True)
