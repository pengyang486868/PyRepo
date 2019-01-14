import csv
import numpy as np

def read(path):
    path = 'E:\\work\\TF\\data\\' + path
    #path = 'D:\\tf\\data\\' + path
    with open(path) as file:
        reader = csv.reader(file)
        a = []
        for r in reader:
                a.append(r)
        return np.asarray(a,dtype=float)

def toonehot(lst):
    hundred = []
    ten = []
    one = []
    for i in range(3):
        hundred.append(0)
    for i in range(10):
        ten.append(0)
        one.append(0)
    hundred[int(lst[0])] = 1
    ten[int(lst[1])] = 1
    one[int(lst[2])] = 1
    return np.hstack((hundred,ten,one))

def input(str):
    return read(str + '_input.csv')

#def output(str):
#    all = read(str + '_output.csv')
#    result = []
#    for n in all:
#        result.append(toonehot(n))
#    return np.asarray(result)

def output(str):
    return read(str + '_output.csv')



