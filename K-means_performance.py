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

def higher(x,y):
    if x>y:
        return x
    else:
        return y

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

def distmatrix(data):
    distmatrix = [[0 for i in range(len(data))] for j in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data)):
            distmatrix[i][j] = dist(data[i],data[j])
    return distmatrix

SSElist = []
SILlist = []
performance = [[0 for i in range(2)] for j in range(56)]
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

    SSE = 0
    for p in range(len(clist1)):
        SSE = SSE + dist(clist1[p],c1)
    for q in range(len(clist2)):
        SSE = SSE + dist(clist2[q],c2)
    SSElist.append([SSE])

    d = distmatrix(data)
    in1 = []
    in2 = []
    for x in range(len(cval)):
        if cval[x] == 1:
            in1.append(x)
        else:
            in2.append(x)

    d1 = []
    d2 = []
    for h in range(len(in1)):
        d1.append(d[in1[h]])
    for j in range(len(in2)):
        d2.append(d[in2[j]])
    silval = []
    for y in range(len(data)):
        if cval[y] == 1:
            if len(col(d1,y))-1 == 0:
                ai = 0
            else:
                ai = sum(col(d1,y))/(len(col(d1,y))-1)
            bi = mean(col(d2,y))
            si = (bi-ai)/higher(bi,ai)
        else:
            if len(col(d2,y))-1 == 0:
                ai = 0
            else:
                ai = sum(col(d2,y))/(len(col(d2,y))-1)
            bi = mean(col(d1,y))
            si = (bi-ai)/higher(bi,ai)
        silval.append(si)

    SILlist.append(mean(silval))

    for d in range(len(SILlist)):    
        performance[d] = [SILlist[d],SSElist[d]]

    csvfile = "./2016B5A30572H_performance.csv"
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(performance)

    print("CSV-" + str(i+1) + " Done!")
