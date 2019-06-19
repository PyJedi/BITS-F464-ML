'''
*** Information gain with binary split ***

Author :
Pranath Reddy
2016B5A30572H
'''
import csv
import cmath as math 

def col(array, i):
    return [row[i] for row in array]

def mean(col): 
    return sum(col) / len(col)

def entropy_parent(data,mean):
    nf = len([i for (i, val) in enumerate(data) if val >= mean])
    nnf = len([i for (i, val) in enumerate(data) if val < mean])
    return -((float(nf)/float(len(data)))*(math.log(float(nf)/float(len(data)),2)))-((float(nnf)/float(len(data)))*(math.log(float(nnf)/float(len(data)),2)))

def entropy_node(data):
    nf = len([i for (i, val) in enumerate(data) if val > 0])
    nnf = len([i for (i, val) in enumerate(data) if val == 0])
    if len(data) != 0:
        return -((float(nf)/float(len(data)))*(math.log(float(nf)/float(len(data)),2)))-((float(nnf)/float(len(data)))*(math.log(float(nnf)/float(len(data)),2)))
    else:
        return 0

infogain_values = []
for i in range(56):
    data = []
    with open(str(i+1)+".csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) 
        for row in reader: 
            data.append(row)
    infogain_row = []
    for j in range(20):
        coldata = col(data,j)
        m = mean(coldata)
        in1 = [i for (i, val) in enumerate(coldata) if val >= m]
        in2 = [i for (i, val) in enumerate(coldata) if val < m]
        nlen = len(in1) + len(in2)
        entro_p = entropy_parent(coldata,m)
        entro_p = entro_p.real
        part1 = [data[i][20] for i in in1]
        part2 = [data[i][20] for i in in2]
        entro_n1 = entropy_node(part1)
        entro_n1 = entro_n1.real
        entro_n2 = entropy_node(part2)
        entro_n2 = entro_n2.real
        infogain = entro_p - ((float(len(in1))/float(nlen))*entro_n1) - ((float(len(in2))/float(nlen))*entro_n2)
        infogain_row.append(infogain)
    infogain_values.append(infogain_row)

csvfile = "./2016B5A30572H_infogain.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(infogain_values)


    





