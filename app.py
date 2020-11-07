import io

import dash
import plotly
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go
import plotly.graph_objects as go
from dash.dependencies import Input, Output
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
        children='Update',
        n_clicks=0
    ),
    dcc.Input(
        type='text',
        value=''
    ),

    dcc.Graph(
        id='graph',
        figure={
            'data': [
                go.Scatter(
                    x=xx,
                    y=yy,
                    # text='name',
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

@app.callback(Output('graph', 'figure'), [Input('button', 'n_clicks')])
def update_graph(n_clicks):
    if n_clicks == 0:
        raise no_update
    out = io.StringIO(main.main())
    data = pandas.read_csv(out, sep = ",")
    if "no shade" in (data["Sun"]):
        print("hello")

    return {

        'data': [{
            'x': x[0],
            'y': y[0],

        }],
        'layout': {
            'title': ('graph ' + str(n_clicks + 1)),
            "xaxis": {"range": [0, (value_range[1] + 24*n_clicks)]},
        }
    }


if __name__ == '__main__':
    app.run_server(debug=True)