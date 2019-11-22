'''
*** Information gain with binary split ***

Author :
Pranath Reddy
2016B5A30572H
'''
import csv
import cmath as math 

# A function to return the column at specified index
def col(array, i):
    return [row[i] for row in array]

# A function to calculate the mean of an array
def mean(col): 
    return float(sum(col)) / float(len(col))

# A function to calculate the entropy
def entropy_node(data):
    nf = len([i for (i, val) in enumerate(data) if val != 0])
    nnf = len([i for (i, val) in enumerate(data) if val == 0])
    if len(data) != 0:
        if nf == 0 and nnf == 0:
            return 0
        elif nf == 0:
            return -((float(nnf)/float(len(data)))*(math.log(float(nnf)/float(len(data)),2)))
        elif nnf == 0:
            return -((float(nf)/float(len(data)))*(math.log(float(nf)/float(len(data)),2)))
        else:
            return -((float(nf)/float(len(data)))*(math.log(float(nf)/float(len(data)),2)))-((float(nnf)/float(len(data)))*(math.log(float(nnf)/float(len(data)),2)))
    else:
        return 0

infogain_values = [] # initiate an array to hold all information gain values
for i in range(56):
    data = []
    # input data
    with open(str(i+1)+".csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) 
        for row in reader: 
            data.append(row)
    infogain_row = []
    # calculate entropy of parent node
    entro_p = entropy_node(col(data,20))
    entro_p = entro_p.real
    for j in range(20):
        # get the attribute array
        coldata = col(data,j)
        # find mean of the attribute array
        m = mean(coldata)
        # get the index of rows after splitting w.r.t mean
        in1 = [i for (i, val) in enumerate(coldata) if val > m]
        in2 = [i for (i, val) in enumerate(coldata) if val <= m]
        nlen = len(in1) + len(in2)
        # separate the parent array into two child arrays based on the indexes obtained above 
        part1 = [data[i][20] for i in in1]
        part2 = [data[i][20] for i in in2]
        # calculate the entropy of child node 1
        entro_n1 = entropy_node(part1)
        entro_n1 = entro_n1.real
        # calculate the entropy of child node 2
        entro_n2 = entropy_node(part2)
        entro_n2 = entro_n2.real
        # find the information gain
        infogain = entro_p - ((float(len(in1))/float(nlen))*entro_n1) - ((float(len(in2))/float(nlen))*entro_n2)
        infogain_row.append(infogain)
    infogain_values.append(infogain_row)

# export the information gain as a csv file
csvfile = "./2016B5A30572H_infogain2.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(infogain_values)


    





