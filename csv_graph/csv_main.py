import graph
import pandas as pd

filename = 'otsu_temp.csv'
data = pd.read_csv(filename)

month = data['month'].values.tolist()
temp = data['temp'].values.tolist()

graph.line(month, temp)