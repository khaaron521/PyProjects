
import matplotlib.pyplot as plt
import dash
import dash_table as dt
import dash_core_components as dcc
import dash_html_components as html
import plotly
import pandas as pd
from dash.dependencies import Input, Output, State
from plotly.tools import mpl_to_plotly
from alpha_vantage.timeseries import TimeSeries
import datetime
import csv


ts = TimeSeries(key='BV1I5C1GWLRD5W5R', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')
col_names = [row[0] for row in data]

current_datetime = datetime.datetime.now()
datetime_string = current_datetime.strftime('%m-%d-%Y_%Hh%Mm%Ss.csv')

print(data)
print('---------------------------------------------------')
print(meta_data)

graph = data['4. close'].plot()


# csvData = data
# with open(datetime_string, 'w', newline='') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerow(col_names)
#     writer.writerows(meta_data)
#     writer.writerows(csvData)
#
#     csvFile.close()

# data['4. close'].plot()
# plt.title('Intraday Times Series for the MSFT stock (1 min)')
# plt.show()