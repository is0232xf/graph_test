#coding: UTF-8
import random
import graph
import numpy as np

def linear_conv(x):
  k = 1.5
  i = random.randint(1,20)
  y = k*x + i
  return y

# 折れ線グラフ，棒グラフ用
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
temp = [9, 10, 14, 20, 25, 28, 32, 33, 29, 23, 17, 11]
rain = [49.2, 69.8, 109.4, 140.9, 140.0, 227.5, 223.2, 147.9, 210.7, 123.0, 76.3, 52.5]

# 散布図用
x = range(0, 100)
y = []
for j in x:
  i = linear_conv(j)
  y.append(i)

# 円グラフ用
label = ['A', 'B', 'C', 'D', 'E']
p = [5, 30, 25, 14, 9]

# ヒストグラム用
# 引数：(平均，標準偏差，サンプル数)
score = np.random.normal(50, 10, 1000)

# colorは色を表す．red, green, blue, orangeなど，好きな色に変更することができる
# xとyの[]内に描画するグラフの値を書く
# graph.line(month, temp, color='blue')
# graph.bar(month, rain, color='blue')
# graph.barh(x, y, color='magenta')
# graph.scatter(x, y, color='green')
# graph.circle(label, p, True)
graph.histgram(score, color='purple')
