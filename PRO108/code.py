import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv('mobile_rating.csv')

fig = ff.create_distplot( [df["Avg Rating"].tolist()], ["Average Ratings"])
fig.show()