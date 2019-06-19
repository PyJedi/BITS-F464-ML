'''
*** K-means clustering ***
two clusters

Author :
Pranath Reddy
2016B5A30572H
'''
import csv
import cmath as math 
from random import randint

def mean(val): 
    if len(val) == 0:
        return 0
    else:
        return sum(val) / len(val)

def col(array, i):
    return [row[i] for row in array]

def dist(x,y):
    sum = 0
    for a in range(20):
        sum = sum + (x[a]-y[a])**2
    return (math.sqrt(sum)).real

def distcen_init(data,cen):
    distc1 = [0 for x in range(len(data))]
    distc2 = [0 for x in range(len(data))]
    for k in range(len(data)):
        distc1[k] = (dist(data[k],data[cen[0]]))
        distc2[k] = (dist(data[k],data[cen[1]]))
    return distc1, distc2

def distcen(data,cen):
    distc1 = [0 for x in range(len(data))]
    distc2 = [0 for x in range(len(data))]
    for k in range(len(data)):
        distc1[k] = (dist(data[k],cen[0]))
        distc2[k] = (dist(data[k],cen[1]))
    return distc1, distc2

for i in range(56):
    data = []
    with open(str(i+1)+".csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) 
        for row in reader: 
            data.append(row)

    randindex = [randint(0, len(data)) for b in range(2)]
    dsvc1, dsvc2 = distcen_init(data,randindex)

    for j in range(50):
        cval = [1 for x in range(len(data))]
        for l in range(len(data)):
            if dsvc2[l]<dsvc1[l]:
                cval[l] = 2
        clist1 = []
        clist2 = []
        for m in range(len(data)):
            if cval[m] == 1:
                clist1.append(data[m])
            else:
                clist2.append(data[m])
        c1 = []
        c2 = []
        for n in range(20):
            c1.append(mean(col(clist1,n)))
            c2.append(mean(col(clist2,n)))
        cen = [c1,c2]
        dsvc1, dsvc2 = distcen(data,cen)

    cval2 = [[0 for a in range(1)] for b in range(len(cval))]
    for k in range(len(cval)):
        cval2[k] = [cval[k]]

    csvfile = "clusters" + str(i+1) + ".csv"
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(cval2)

    print("CSV-" + str(i+1) + " Done!")
