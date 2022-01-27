import csv

filename = 'kyoto_temp_rain.csv'
f = open(filename, 'a', newline='')
csvWriter = csv.writer(f)
csvWriter.writerow(['month', 'temp', 'rain'])

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
temp = [9, 10, 14, 20, 25, 28, 32, 33, 29, 23, 17, 11]
rain = [49.2, 69.8, 109.4, 140.9, 140.0, 227.5, 223.2, 147.9, 210.7, 123.0, 76.3, 52.5]

for i in range(len(month)):
    csvWriter.writerow([month[i], temp[i], rain[i]])
f.close()