'''
***Simple Linear Regression***
With Gradient Descent

Author :
Pranath Reddy
2016B5A30572H
'''
import csv
import math 
import numpy as np
from sklearn.model_selection import train_test_split

# A function to return the column at specified index
def getcol(data,c):
    col = []
    for i in range(len(data)):
        col.append(data[i][c])
    return col

# A function to return root mean square error
def rmse(x,y,m,c):
    yp = [0 for i in range(len(x))]
    for i in range(len(x)):
        yp[i] = (m*x[i]) + c
    rmse = 0
    for i in range(len(y)):
        rmse = rmse + (yp[i]-y[i])**2
    rmse = math.sqrt(rmse/len(y))
    return rmse

# A function to return mean-magnitude relative error
def mmre(x,y,m,c):
    yp = [0 for i in range(len(x))]
    for i in range(len(x)):
        yp[i] = (m*x[i]) + c
    mmre = 0
    for i in range(len(y)):
        mmre = mmre + (abs(y[i]-yp[i])/(y[i]+0.005))
    mmre = mmre/len(y)
    return mmre

# A function to return the updated values of m,c after one iteration of gradient descent
def wtupdate(m,c,x,y):
    sumvm = 0
    sumvc = 0
    yp = [0 for i in range(len(x))]
    for i in range(len(x)):
        yp[i] = (m*x[i]) + c
        sumvm = sumvm + (-2/len(x))*(y[i]-yp[i])*x[i]
        sumvc = sumvc + (-2/len(x))*(y[i]-yp[i])
    m = m - 0.001*sumvm
    c = c - 0.001*sumvc
    return m, c

# A function to return the slope and intercept of y^
def linreg(x,y):
    m = 0
    c = 0
    iters = 1000
    i = 0
    while(i<iters):
        m, c = wtupdate(m,c,x,y)
        i = i+1
    return m, c

# A function to implement min-max normalization
def norm(data):
    ndata = data
    for i in range(21):
        maxval = max(getcol(data,i))
        minval = min(getcol(data,i))
        for j in range(len(data)):
            ndata[j][i] = (data[j][i]-minval)/((maxval-minval)+0.005)
    return ndata

slope = [[0 for i in range(20)] for j in range(56)]
intercept = [[0 for i in range(20)] for j in range(56)]
RMSE = [[0 for i in range(20)] for j in range(56)]
MMRE = [[0 for i in range(20)] for j in range(56)]
for i in range(56):
    data = []
    # import the data
    with open(str(i+1)+".csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) 
        for row in reader: 
            data.append(row)

    # normalize the data
    data = norm(data)
    data = np.asarray(data)
    # split into dependent and independent variables
    x = data[:,:-1]
    y = data[:,-1]

    # split into testing and training sets
    x_tr, x_ts, y_tr, y_ts = train_test_split(x, y, test_size=0.3)
    for j in range(20):
        x = getcol(x_tr,j)
        x_ts1 = getcol(x_ts,j)
        y = y_tr
        m, c = linreg(x,y)
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
