import functools
import csv

def getdata(str):
    path = r'data.csv'

    with open(path) as file:
        reader = csv.DictReader(file)
        a = []
        for r in reader:
            if (r['Mean Scale Score'] != 's') & (r['Category'] == str):
                a.append(r)
        return a

def cmp(x,y):
    if (x[1] + x[4]) / (x[2] + x[3]) > (y[1] + y[4]) / (y[2] + y[3]):
        return 1
    if (x[1] + x[4]) / (x[2] + x[3]) < (y[1] + y[4]) / (y[2] + y[3]):
        return -1
    return 0

# main process
data = getdata('All Students')
stat = []
global find
for r in data:
    find = False
    for s in stat:
        if s[0] == r['School Name']:
            s[1]+=int(r['# Level 1'])
            s[2]+=int(r['# Level 2'])
            s[3]+=int(r['# Level 3'])
            s[4]+=int(r['# Level 4'])
            find = True
    if find == False:
        stat.append([r['School Name'],0,0,0,0])

print('-----------sorted [big/small vs middle]-------------')
#for line in stat:
#    print(line)
srt = sorted(stat,key=functools.cmp_to_key(cmp))
srt.reverse()
for line in srt:
    print(line)

