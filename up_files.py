import csv
file = open('EPL_2018_2019.csv', mode='r', encoding='utf-8')
data = csv.DictReader(file)
file.close()