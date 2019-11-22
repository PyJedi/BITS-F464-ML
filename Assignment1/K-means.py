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

# A function to calculate the mean of an array
def mean(val): 
    if len(val) == 0:
        return 0
    else:
        return sum(val) / len(val)

# A function to return a column of the data at the specified index
def col(array, i):
    return [row[i] for row in array]

# A function to return the max of two values
def higher(x,y):
    if x>y:
        return x
    else:
        return y

# A function to calculate the distance between two points
def dist(x,y):
    sum = 0
    for a in range(20):
        sum = sum + (x[a]-y[a])**2
    return (math.sqrt(sum)).real

# A function to calculate the distances from initialized centroids
def distcen_init(data,cen):
    distc1 = [0 for x in range(len(data))]
    distc2 = [0 for x in range(len(data))]
    for k in range(len(data)):
        distc1[k] = (dist(data[k],data[cen[0]]))
        distc2[k] = (dist(data[k],data[cen[1]]))
    return distc1, distc2

# A function to calculate the distances from centroids
def distcen(data,cen):
    distc1 = [0 for x in range(len(data))]
    distc2 = [0 for x in range(len(data))]
    for k in range(len(data)):
        distc1[k] = (dist(data[k],cen[0]))
        distc2[k] = (dist(data[k],cen[1]))
    return distc1, distc2

# A function to calculate the distance matric of the data
def distmatrix(data):
    distmatrix = [[0 for i in range(len(data))] for j in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data)):
            distmatrix[i][j] = dist(data[i],data[j])
    return distmatrix

def getcol(data,c):
    col = []
    for i in range(len(data)):
        col.append(data[i][c])
    return col
    
# A function to implement min-max normalization
def norm(data):
    ndata = data
    for i in range(20):
        maxval = max(getcol(data,i))
        minval = min(getcol(data,i))
        for j in range(len(data)):
            ndata[j][i] = (data[j][i]-minval)/(maxval-minval)
    return ndata

SSElist = [] # create an empty array to hold all SSE values
SILlist = [] # create an empty array to hold all Silhouette values
performance = [[0 for i in range(2)] for j in range(56)] # initiate our final output array
for i in range(56):
    data = []
    # input the data csv
    with open(str(i+1)+".csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) 
        for row in reader: 
            data.append(row)

    # to normalize the data
    #data = norm(data) 

    # initiate the centroids
    randindex = [randint(0, len(data)) for b in range(2)] 
    dsvc1, dsvc2 = distcen_init(data,randindex)

    for j in range(50):
        # assign cluster indexes
        cval = [1 for x in range(len(data))]
        for l in range(len(data)):
            if dsvc2[l]<dsvc1[l]:
                cval[l] = 2
        # divide into clusters using cluster indexes found above
        clist1 = []
        clist2 = []
        for m in range(len(data)):
            if cval[m] == 1:
                clist1.append(data[m])
            else:
                clist2.append(data[m])
        # update the centroids
        c1 = []
        c2 = []
        for n in range(20):
            c1.append(mean(col(clist1,n)))
            c2.append(mean(col(clist2,n)))
        cen = [c1,c2]
        # update the distances from centroids
        dsvc1, dsvc2 = distcen(data,cen)


    # To Export clustering information 
    '''
    cval2 = [[0 for a in range(1)] for b in range(len(cval))]
    for k in range(len(cval)):
        cval2[k] = [cval[k]]

    csvfile1 = "clusters" + str(i+1) + ".csv"
    with open(csvfile1, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(cval2)
    '''
    
    # find SSE of the final clusters
    SSE = 0
    for p in range(len(clist1)):
        SSE = SSE + (dist(clist1[p],c1)*dist(clist1[p],c1))
    for q in range(len(clist2)):
        SSE = SSE + (dist(clist2[q],c2)*dist(clist2[q],c2))
    SSElist.append(SSE)

    # calculate the distance matrix
    d = distmatrix(data)

    # get indexes of all points in each centroid
    in1 = []
    in2 = []
    for x in range(len(cval)):
        if cval[x] == 1:
            in1.append(x)
        else:
            in2.append(x)

    # sepatarate the rows of the distance matrix that correspond to each cluster
    d1 = []
    d2 = []
    for h in range(len(in1)):
        d1.append(d[in1[h]])
    for j in range(len(in2)):
        d2.append(d[in2[j]])

    # calculate the silhouette value
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

    # export the final output as csv
    csvfile2 = "./2016B5A30572H_performance.csv"
    with open(csvfile2, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(performance)

    print("CSV-" + str(i+1) + " Done!")
