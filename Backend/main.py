import csv
import os

# get current working directory
cwd = os.getcwd()

#get files in directory
files = os.listdir(cwd) 

print(files)

with open('GM.csv') as f:
    reader = csv.reader(f)
    GM = list(reader)

with open('Ford.csv') as f:
    reader = csv.reader(f)
    Ford = list(reader)

GM_key = GM[0]
GM = GM[1:]
GM_len = len(GM) - 1
Ford_key = Ford[0]
Ford = Ford[1:]
Ford_len = len(Ford) - 1
