'''
***Average value of RMSE and MMRE***
to find the average value of rmse and mmre after k-runs of linear regression

Author :
Pranath Reddy
2016B5A30572H
'''
import csv
import math 
import numpy as np

# A function to calculate the mean of an array
def mean(col): 
    return float(sum(col)) / float(len(col))

# A function to return the column at specified index
def getcol(data,c):
    col = []
    for i in range(len(data)):
        col.append(data[i][c])
    return col

RMSE = [[0 for i in range(20)] for j in range(56)]
MMRE = [[0 for i in range(20)] for j in range(56)]
k = 5 # number of sets of linear regression outputs available
for a in range(k):
    datar = []
    datam = []
    # import the data
    with open("2016B5A30572H_RMSE_"+str(a+1)+".csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) 
        for row in reader: 
            datar.append(row)

    with open("2016B5A30572H_MMRE_"+str(a+1)+".csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) 
        for row in reader: 
            datam.append(row)

    for i in range(56):
        for j in range(20):
            RMSE[i][j] = RMSE[i][j] + datar[i][j]
            MMRE[i][j] = MMRE[i][j] + datam[i][j]

for i in range(56):
    for j in range(20):
        RMSE[i][j] = float(RMSE[i][j])/5.0
        MMRE[i][j] = float(MMRE[i][j])/5.0
    
csvfile4 = "./2016B5A30572H_RMSE.csv"
with open(csvfile4, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(RMSE)

csvfile5 = "./2016B5A30572H_MMRE.csv"
with open(csvfile5, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(MMRE)
