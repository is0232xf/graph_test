#coding: UTF-8
import random
import graph
import numpy as np

# �܂���O���t�C�_�O���t�p
month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
temp = [9, 10, 14, 20, 25, 28, 32, 33, 29, 23, 17, 11]
rain = [49.2, 69.8, 109.4, 140.9, 140.0, 227.5, 223.2, 147.9, 210.7, 123.0, 76.3, 52.5]

# �U�z�}�p
x = range(0, 10)
y = []
for k in range(len(x)):
  i = random.randint(1,100)
  y.append(i)

# �~�O���t�p
label = ['A', 'B', 'C', 'D', 'E']
p = [5, 30, 25, 14, 9]

# �q�X�g�O�����p
data = np.random.normal(10, 10, 1000)

# color�͐F��\���Dred, green, blue, orange�ȂǁC�D���ȐF�ɕύX���邱�Ƃ��ł���
# x��y��[]���ɕ`�悷��O���t�̒l������
# graph.line(month, temp, color='orange')
graph.bar(month, rain, color='blue')
# graph.barh(x, y, color='magenta')
# graph.scatter(x, y, color='cyan')
# graph.histgram(data, color='green')
