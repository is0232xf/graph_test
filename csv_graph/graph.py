import numpy as np
import matplotlib.pyplot as plt

def temp_comp(month, temp_list, colors):
    for i in range(len(temp_list)):
        plt.plot(month, temp_list[i], colors[i])
    plt.grid()
    plt.show()

def line(x, y, color='black'):
    plt.plot(x, y, color)
    plt.show()

def bar(x, y, color='black'):
    plt.bar(x, y, color=color)
    plt.show()

def barh(x, y, color='black'):
    plt.xticks(x)
    plt.barh(x, y, color=color)
    plt.show()

def scatter(x, y, color='black'):
    plt.xticks(x)
    plt.scatter(x, y, c=color)
    plt.show()

def circle(label, p, sorted=False):
    if sorted==True:
        p, label = circle_sort(p, label)
    plt.pie(p, labels=label, autopct="%1.1f%%", startangle=90, counterclock=False)
    plt.show()

def histgram(x, color):
    plt.xticks(x)
    plt.hist(x, color=color)
    plt.show()

def circle_sort(p, label):
    label_index_list = []
    sorted_label = []
    sorted_p = sorted(p, reverse=True)
    for i in sorted_p:
        label_index_list.append(p.index(i))
    for j in label_index_list:
        sorted_label.append(label[j])
    return sorted_p, sorted_label