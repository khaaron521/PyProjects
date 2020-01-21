
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.subplots
from dash.dependencies import Input, Output, State
from alpha_vantage.timeseries import TimeSeries


app = dash.Dash(__name__)


ts = TimeSeries(key='BV1I5C1GWLRD5W5R', output_format='pandas')


app.layout = html.Div(
    [
        dcc.Textarea(id="input1",
                     rows='8',
                     style={'width':'100%'}),
        html.Button(id='button3',
                    children='Get Daily'
                    ),
        dcc.Graph(id='eq_graph_daily')
    ],
)


# -------------------------- Function to Update Daily Graph ----------------------------
# def update_graph_daily(eq):
#     df, meta_data = ts.get_daily(symbol=eq, outputsize='compact')
#     df['index1'] = df.index
#
#     return html.Div([
#         html.H5(eq),
#         dcc.Graph(
#             figure={
#                 'data': [
#                     {
#                         'x': df['index1'],
#                         'y': df['4. close'],
#                         'name': 'Prices at Close',
#                         'type': 'scatter',
#                         'mode': 'line',
#                     },
#                     {
#                         'x': df['index1'],
#                         'y': df['5. volume'],
#                         'name': 'Volume',
#                         'type': 'bar',
#                         'yaxis': 'y2',
#                     },
#                 ],
#                 'layout': go.Layout(
#                     title='Daily Closing Prices and Volume',
#                     xaxis={'title': 'Time'},
#                     yaxis={'title': 'Closing Price'},
#                     yaxis2={'title': 'Volume', 'side': 'right'},
#                     # margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
#                     legend={'x': 0, 'y': 1},
#                     hovermode='closest'
#                 )
#             }
#         ),
#     ])


# -------------------------- Callback to Update Daily Graph ----------------------------
@app.callback(
    Output('eq_graph_daily', 'figure'),
    [Input('button3', 'n_clicks')],
    [State('input1', 'value')])
def update_output(n_clicks, input1):
    if n_clicks:
        eq = input1
        df, meta_data = ts.get_daily(symbol=eq, outputsize='compact')
        df['index1'] = df.index

        time = df['index1']
        close = df['4. close']
        volume = df['5. volume']

        fig = plotly.subplots.make_subplots(rows=2, cols=1,
                                            shared_xaxes=True,
                                            vertical_spacing=0.009,
                                            horizontal_spacing=0.009)
        fig['layout']['margin'] = {'l': 30, 'r': 10, 'b': 50, 't': 25}

        fig.append_trace({'x': time, 'y': close,'type':'scatter','name':'Price', 'mode': 'lines'},1,1)
        fig.append_trace({'x': time, 'y': volume,'type':'scatter','name':'Volume', 'mode': 'lines'},2,1)

        fig['layout'].update(title='Price and Volume')
        return fig


if __name__ == '__main__':
    app.run_server()