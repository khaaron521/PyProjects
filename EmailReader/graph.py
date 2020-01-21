import dash, requests, pandas as pd
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly.tools as tls
import plotly.subplots
from io import StringIO
from alpha_vantage.timeseries import TimeSeries



app = dash.Dash(__name__)
ts = TimeSeries(key='BV1I5C1GWLRD5W5R', output_format='pandas')

app.layout = html.Div([
    html.Div(['Name : ',
              dcc.Input(id='input',value='ACC',type='text')
              ]),
    dcc.Graph(id='price_volume')
])


@app.callback(
    Output('price_volume', 'figure'),
    [Input(component_id='input', component_property = 'value')]
)
def update_graph(in_data):
    df, meta_data = ts.get_daily(symbol=in_data, outputsize='compact')
    df['index1'] = df.index

    fig = plotly.subplots.make_subplots(rows=2, cols=1, shared_xaxes=True,
                                        vertical_spacing=0.009,
                                        horizontal_spacing=0.009)
    fig['layout']['margin'] = {'l': 30, 'r': 10, 'b': 50, 't': 25}

    fig.append_trace({'x':df.index,'y':df['4. close'],
                      'type':'scatter','name':'Price'},1,1)
    # fig.append_trace({'x':df.index,'y':df['4. close'],
    #                   'type':'scatter','name':'MMA30'},1,1)
    fig.append_trace({'x':df.index,'y':df['5. volume'],
                      'type':'bar','name':'Volume'},2,1)

    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='Black')
    fig['layout'].update(title='Plot of '+in_data,
                         plot_bgcolor='rgba(0,0,0,0)')
    return fig


if __name__ == '__main__':
    app.run_server()