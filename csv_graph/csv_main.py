import graph
import pandas as pd

filename = 'zenkoku.csv'
data = pd.read_csv(filename, encoding="shift-jis")

month = data['month'].values.tolist()

kyoto_temp = data['kyoto_temp'].values.tolist()
naha_temp = data['naha_temp'].values.tolist()
asahikawa_temp = data['asahikawa_temp'].values.tolist()

temp = [kyoto_temp, naha_temp, asahikawa_temp]
colors = ['red', 'blue', 'green']

graph.temp_comp(month, temp, colors)
