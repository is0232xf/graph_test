import graph
import pandas as pd

filename = 'zenkoku.csv' # 使うファイル名を指定する
data = pd.read_csv(filename, encoding="shift-jis", sep='\t')

# ここから各データをリスト化
month = data['month'].values.tolist()

kyoto_temp = data['kyoto_temp'].values.tolist()
naha_temp = data['naha_temp'].values.tolist()
asahikawa_temp = data['asahikawa_temp'].values.tolist()
tokyo_temp = data['tokyo_temp'].values.tolist()
nagoya_temp = data['nagoya_temp'].values.tolist()
kanazawa_temp = data['kanazawa_temp'].values.tolist()
takamatsu_temp = data['takamatsu_temp'].values.tolist()
fukuoka_temp = data['fukuoka_temp'].values.tolist()
sendai_temp = data['sendai_temp'].values.tolist()
hiroshima_temp = data['hiroshima_temp'].values.tolist()
kagoshima_temp = data['kagoshima_temp'].values.tolist()

kyoto_rain = data['kyoto_rain'].values.tolist()
naha_rain = data['naha_rain'].values.tolist()
asahikawa_rain = data['asahikawa_rain'].values.tolist()
tokyo_rain = data['tokyo_rain'].values.tolist()
nagoya_rain = data['nagoya_rain'].values.tolist()
kanazawa_rain = data['kanazawa_rain'].values.tolist()
takamatsu_rain = data['takamatsu_rain'].values.tolist()
fukuoka_rain = data['fukuoka_rain'].values.tolist()
sendai_rain = data['sendai_rain'].values.tolist()
hiroshima_rain = data['hiroshima_rain'].values.tolist()
kagoshima_rain = data['kagoshima_rain'].values.tolist()
# ここまで

# ここからグラフの描画
# 使い方：引数に(month, 描画したいデータ, "色")を追加する
# サンプルではgraph.line()とgraph.bar()が使える
graph.line(month, kyoto_temp, "red")
graph.line(month, naha_temp, "blue")