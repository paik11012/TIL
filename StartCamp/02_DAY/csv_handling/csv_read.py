# 1. split
with open('dinner.csv','r',encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        #delete empty lines
        print(line.strip().split(',')) #split with ,

# 2. csv_reader
import csv
with open('dinner.csv','r',encoding='utf-8') as f: #no empty lines
    items = csv.reader(f)
    for item in items:
        print(item)