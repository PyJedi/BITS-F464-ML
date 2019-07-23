'''
***Simple Linear Regression***
with Scipy

Author :
Pranath Reddy
2016B5A30572H
'''
import csv
import math 
from scipy import stats
import numpy as np
from sklearn.model_selection import train_test_split

def getcol(data,c):
    col = []
    for i in range(len(data)):
        col.append(data[i][c])
    return col

def rmse(x,y,m,c):
    yp = [0 for i in range(len(x))]
    for i in range(len(x)):
        yp[i] = (m*x[i]) + c
    rmse = 0
    for i in range(len(y)):
        rmse = rmse + (yp[i]-y[i])**2
    rmse = math.sqrt(rmse/len(y))
    return rmse

def mmre(x,y,m,c):
    yp = [0 for i in range(len(x))]
    for i in range(len(x)):
        yp[i] = (m*x[i]) + c
    mmre = 0
    for i in range(len(y)):
        mmre = mmre + (abs(y[i]-yp[i])/(y[i]+0.05))
    mmre = mmre/len(y)
    return mmre

def norm(data):
    ndata = data
    for i in range(21):
        maxval = max(getcol(data,i))
        minval = min(getcol(data,i))
        for j in range(len(data)):
            ndata[j][i] = (data[j][i]-minval)/((maxval-minval)+0.05)
    return ndata

slope = [[0 for i in range(20)] for j in range(56)]
intercept = [[0 for i in range(20)] for j in range(56)]
RMSE = [[0 for i in range(20)] for j in range(56)]
MMRE = [[0 for i in range(20)] for j in range(56)]
for i in range(56):
    data = []
    with open(str(i+1)+".csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) 
        for row in reader: 
            data.append(row)

    data = norm(data)
    data = np.asarray(data)
    x = data[:,:-1]
    y = data[:,-1]

    x_tr, x_ts, y_tr, y_ts = train_test_split(x, y, test_size=0.3)
    for j in range(20):
        x = getcol(x_tr,j)
        x_ts1 = getcol(x_ts,j)
        y = y_tr
        m, c, r_value, p_value, std_err = stats.linregress(x,y)
        slope[i][j] = m
        intercept[i][j] = c
        RMSE[i][j] = rmse(x_ts1,y_ts,m,c)
        MMRE[i][j] = mmre(x_ts1,y_ts,m,c)

    csvfile2 = "./2016B5A30572H_slope.csv"
    with open(csvfile2, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(slope)

    csvfile3 = "./2016B5A30572H_intercept.csv"
    with open(csvfile3, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(intercept)

    csvfile4 = "./2016B5A30572H_RMSE.csv"
    with open(csvfile4, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(RMSE)

    csvfile5 = "./2016B5A30572H_MMRE.csv"
    with open(csvfile5, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(MMRE)

    print("CSV-" + str(i+1) + " Done!")
