# -*- coding: utf-8 -*-

import datetime
import requests
import pathlib
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State



app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
app.css.append_css({'external_url': '/assets/style.css'})
app.server.static_folder = 'static'

server = app.server

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()


# Currency pairs
currencies = ["EURUSD", "USDCHF", "USDJPY", "GBPUSD"]

# API Requests for news div
googleau_news_requests = requests.get(
    "https://newsapi.org/v2/top-headlines?sources=google-news-au&pageSize=100&apiKey=da8e2e705b914f9f86ed2e9692e66012"
)

# API Requests for news div
au_news_requests = requests.get(
    "https://newsapi.org/v2/top-headlines?country=au&pageSize=100&category=business&apiKey=da8e2e705b914f9f86ed2e9692e66012"
)

wsj_news_requests = requests.get(
    "https://newsapi.org/v2/top-headlines?sources=the-wall-street-journal&pageSize=100&apiKey=da8e2e705b914f9f86ed2e9692e66012"
)

afr_news_requests = requests.get(
    "https://newsapi.org/v2/top-headlines?sources=australian-financial-review&pageSize=100&apiKey=da8e2e705b914f9f86ed2e9692e66012"
)

abcau_news_requests = requests.get(
    "https://newsapi.org/v2/top-headlines?sources=abc-news-au&pageSize=100&apiKey=da8e2e705b914f9f86ed2e9692e66012"
)

arstechnica_news_requests = requests.get(
    "https://newsapi.org/v2/top-headlines?sources=ars-technica&pageSize=100&apiKey=da8e2e705b914f9f86ed2e9692e66012"
)

googlenews_news_requests = requests.get(
    "https://newsapi.org/v2/top-headlines?sources=google-news&pageSize=100&apiKey=da8e2e705b914f9f86ed2e9692e66012"
)

reddit_news_requests = requests.get(
    "https://newsapi.org/v2/top-headlines?sources=reuters&pageSize=100&apiKey=da8e2e705b914f9f86ed2e9692e66012"
)


# API Call to update news
def update_news():
    json_data = googleau_news_requests.json()["articles"]
    df = pd.DataFrame(json_data)
    df = pd.DataFrame(df[["title", "url"]])
    max_rows = 50
    return html.Div(
        children=[
            html.P(className="p-news", children="AU Google News API",
                   style={'display': 'inline-block'}),
            html.P(
                className="p-news float-right",
                children="Last Updated : "
                         + datetime.datetime.now().strftime("%H:%M:%S"),
                style={'display': 'inline-block', 'text-align': 'justify'}
            ),
            html.Table(
                className="table-news",
                children=[
                    html.Tr(
                        children=[
                            html.Td(
                                children=[
                                    html.A(
                                        className="td-link",
                                        children=df.iloc[i]["title"],
                                        href=df.iloc[i]["url"],
                                        target="_blank",
                                    )
                                ]
                            )
                        ]
                    )
                    for i in range(min(len(df), max_rows))
                ],
            ),
        ]
    )


# API Call to update Australian News
def update_aus():
    json_data = au_news_requests.json()["articles"]
    df = pd.DataFrame(json_data)
    df = pd.DataFrame(df[["title", "url"]])
    max_rows = 50
    return html.Div(
        children=[
            html.P(className="p-news", children="Australian News API",
                   style={'display': 'inline-block'}),
            html.P(
                className="p-news float-right",
                children="Last Updated : "
                         + datetime.datetime.now().strftime("%H:%M:%S"),
                style={'display': 'inline-block', 'margin-right': 0}
            ),
            html.Table(
                className="table-news",
                children=[
                    html.Tr(    # html table row
                        children=[
                            html.Td(    # html table cell
                                children=[
                                    html.A( # html links
                                        className="td-link",
                                        children=df.iloc[i]["title"],
                                        href=df.iloc[i]["url"],
                                        target="_blank",
                                    )
                                ]
                            )
                        ]
                    )
                    for i in range(min(len(df), max_rows))
                ],
            ),
        ]
    )


# API Call to update Wall Street Journal
def update_wsj():
    json_data = wsj_news_requests.json()["articles"]
    df = pd.DataFrame(json_data)
    df = pd.DataFrame(df[["title", "url"]])
    max_rows = 50
    return html.Div(
        children=[
            html.P(className="p-news", children="WSJ API",
                   style={'display': 'inline-block'}),
            html.P(
                className="p-news float-right",
                children="Last Updated : "
                         + datetime.datetime.now().strftime("%H:%M:%S"),
                style={'display': 'inline-block', 'margin-right': 0}
            ),
            html.Table(
                className="table-news",
                children=[
                    html.Tr(    # html table row
                        children=[
                            html.Td(    # html table cell
                                children=[
                                    html.A( # html links
                                        className="td-link",
                                        children=df.iloc[i]["title"],
                                        href=df.iloc[i]["url"],
                                        target="_blank",
                                    )
                                ]
                            )
                        ]
                    )
                    for i in range(min(len(df), max_rows))
                ],
            ),
        ]
    )


# API Call to update AFR
def update_afr():
    json_data = afr_news_requests.json()["articles"]
    df = pd.DataFrame(json_data)
    df = pd.DataFrame(df[["title", "url"]])
    max_rows = 50
    return html.Div(
        children=[
            html.P(className="p-news", children="AFR API",
                   style={'display': 'inline-block'}),
            html.P(
                className="p-news float-right",
                children="Last Updated : "
                         + datetime.datetime.now().strftime("%H:%M:%S"),
                style={'display': 'inline-block', 'margin-right': 0}
            ),
            html.Table(
                className="table-news",
                children=[
                    html.Tr(    # html table row
                        children=[
                            html.Td(    # html table cell
                                children=[
                                    html.A( # html links
                                        className="td-link",
                                        children=df.iloc[i]["title"],
                                        href=df.iloc[i]["url"],
                                        target="_blank",
                                    )
                                ]
                            )
                        ]
                    )
                    for i in range(min(len(df), max_rows))
                ],
            ),
        ]
    )

# API Call to update AFR
def update_abcau():
    json_data = abcau_news_requests.json()["articles"]
    df = pd.DataFrame(json_data)
    df = pd.DataFrame(df[["title", "url"]])
    max_rows = 50
    return html.Div(
        children=[
            html.P(className="p-news", children="ABC AU API",
                   style={'display': 'inline-block'}),
            html.P(
                className="p-news float-right",
                children="Last Updated : "
                         + datetime.datetime.now().strftime("%H:%M:%S"),
                style={'display': 'inline-block', 'margin-right': 0}
            ),
            html.Table(
                className="table-news",
                children=[
                    html.Tr(    # html table row
                        children=[
                            html.Td(    # html table cell
                                children=[
                                    html.A( # html links
                                        className="td-link",
                                        children=df.iloc[i]["title"],
                                        href=df.iloc[i]["url"],
                                        target="_blank",
                                    )
                                ]
                            )
                        ]
                    )
                    for i in range(min(len(df), max_rows))
                ],
            ),
        ]
    )


# API Call to update AFR
def update_arstechnica():
    json_data = arstechnica_news_requests.json()["articles"]
    df = pd.DataFrame(json_data)
    df = pd.DataFrame(df[["title", "url"]])
    max_rows = 50
    return html.Div(
        children=[
            html.P(className="p-news", children="ARS Technica API",
                   style={'display': 'inline-block'}),
            html.P(
                className="p-news float-right",
                children="Last Updated : "
                         + datetime.datetime.now().strftime("%H:%M:%S"),
                style={'display': 'inline-block', 'margin-right': 0}
            ),
            html.Table(
                className="table-news",
                children=[
                    html.Tr(    # html table row
                        children=[
                            html.Td(    # html table cell
                                children=[
                                    html.A( # html links
                                        className="td-link",
                                        children=df.iloc[i]["title"],
                                        href=df.iloc[i]["url"],
                                        target="_blank",
                                    )
                                ]
                            )
                        ]
                    )
                    for i in range(min(len(df), max_rows))
                ],
            ),
        ]
    )


# API Call to update AFR
def update_gnews():
    json_data = googlenews_news_requests.json()["articles"]
    df = pd.DataFrame(json_data)
    df = pd.DataFrame(df[["title", "url"]])
    max_rows = 50
    return html.Div(
        children=[
            html.P(className="p-news", children="Google News API",
                   style={'display': 'inline-block'}),
            html.P(
                className="p-news float-right",
                children="Last Updated : "
                         + datetime.datetime.now().strftime("%H:%M:%S"),
                style={'display': 'inline-block', 'margin-right': 0}
            ),
            html.Table(
                className="table-news",
                children=[
                    html.Tr(    # html table row
                        children=[
                            html.Td(    # html table cell
                                children=[
                                    html.A( # html links
                                        className="td-link",
                                        children=df.iloc[i]["title"],
                                        href=df.iloc[i]["url"],
                                        target="_blank",
                                    )
                                ]
                            )
                        ]
                    )
                    for i in range(min(len(df), max_rows))
                ],
            ),
        ]
    )


# API Call to update AFR
def update_reuters():
    json_data = reddit_news_requests.json()["articles"]
    df = pd.DataFrame(json_data)
    df = pd.DataFrame(df[["title", "url"]])
    max_rows = 50
    return html.Div(
        children=[
            html.P(className="p-news float-left", children="Reuters API",
                   style={'display': 'inline-block'}),
            html.P(
                className="p-news float-right",
                children="Last Updated : "
                         + datetime.datetime.now().strftime("%H:%M:%S"),
                style={'display': 'inline-block', 'margin-right': 0}
            ),
            html.Table(
                className="table-news",
                children=[
                    html.Tr(    # html table row
                        children=[
                            html.Td(    # html table cell
                                children=[
                                    html.A( # html links
                                        className="td-link",
                                        children=df.iloc[i]["title"],
                                        href=df.iloc[i]["url"],
                                        target="_blank",
                                    )
                                ]
                            )
                        ]
                    )
                    for i in range(min(len(df), max_rows))
                ],
            ),
        ]
    )


# Dash App Layout
app.layout = html.Div(
    className="row",
    children=[
        # Interval component for live clock
        dcc.Interval(id="interval", interval=1 * 1000, n_intervals=0),
        # Interval component for ask bid updates
        dcc.Interval(id="i_bis", interval=1 * 2000, n_intervals=0),
        # Interval component for graph updates
        dcc.Interval(id="i_tris", interval=1 * 5000, n_intervals=0),
        # Interval component for graph updates
        dcc.Interval(id="i_news", interval=1 * 60000, n_intervals=0),
        # Left Panel Div
        # Div for App Info
        html.Div(
            className="div-info",
            children=[
                html.H3(className="title-header", children="Newsfeed"),
            ],
        ),
        html.Div(
            className="div-main-panel",
            children=[
                # Div for News Headlines
                html.Div(
                    className="three columns div-news",
                    children=[html.Div(id="news", children=update_news())],
                    style={'display': 'inline-block'}
                ),
                html.Div(
                    className="three columns div-news",
                    children=[html.Div(id="australia", children=update_aus())],
                    style={'display': 'inline-block'}
                ),
                html.Div(
                    className="three columns div-news",
                    children=[html.Div(id="wsj", children=update_wsj())],
                    style={'display': 'inline-block'}
                ),
                html.Div(
                    className="three columns div-news",
                    children=[html.Div(id="afr", children=update_afr())],
                    style={'display': 'inline-block'}
                ),
            ],
        ),
        html.Div(
            className="div-main-panel",
            children=[
                # Div for News Headlines
                html.Div(
                    className="three columns div-news",
                    children=[html.Div(id="abc_news_au", children=update_abcau())],
                    style={'display': 'inline-block'}
                ),
                html.Div(
                    className="three columns div-news",
                    children=[html.Div(id="ars_technica", children=update_arstechnica())],
                    style={'display': 'inline-block'}
                ),
                html.Div(
                    className="three columns div-news",
                    children=[html.Div(id="google_news", children=update_gnews())],
                    style={'display': 'inline-block'}
                ),
                html.Div(
                    className="three columns div-news",
                    children=[html.Div(id="reuters", children=update_reuters())],
                    style={'display': 'inline-block'}
                ),
            ],
        ),
    ]
)

# Dynamic Callbacks


# Callback to update news
@app.callback(Output("news", "children"), [Input("i_news", "n_intervals")])
def update_news_div(n):
    return update_news()


# Callback to update WSJ
@app.callback(Output("wsj", "children"), [Input("i_news", "n_intervals")])
def update_news_div(n):
    return update_wsj()

# Callback to update aus news
@app.callback(Output("australia", "children"), [Input("i_news", "n_intervals")])
def update_news_div(n):
    return update_aus()

# Callback to update AFR
@app.callback(Output("afr", "children"), [Input("i_news", "n_intervals")])
def update_news_div(n):
    return update_afr()

# Callback to update AFR
@app.callback(Output("abc_news_au", "children"), [Input("i_news", "n_intervals")])
def update_news_div(n):
    return update_abcau()

# Callback to update ABC AU
@app.callback(Output("ars_technica", "children"), [Input("i_news", "n_intervals")])
def update_news_div(n):
    return update_arstechnica()

# Callback to update AFR
@app.callback(Output("google_news", "children"), [Input("i_news", "n_intervals")])
def update_news_div(n):
    return update_gnews()

# Callback to update AFR
@app.callback(Output("reuters", "children"), [Input("i_news", "n_intervals")])
def update_news_div(n):
    return update_reuters()

if __name__ == "__main__":
    # host = '120.18.29.220'
    # app.run_server(host=host, port=8051)           # http://10.99.102.60:8051/
    app.run_server(debug=False)
