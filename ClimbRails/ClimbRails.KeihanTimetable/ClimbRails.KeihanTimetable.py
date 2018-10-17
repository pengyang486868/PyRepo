#coding=utf-8
import os
os.system('cls')
import urllib.request
import re
import sys
import makeUrl
import csv
import socket

print('------------------------------')

path = r'tl.csv'

with open(path) as file:
    reader = csv.DictReader(file)
    a = []
    for r in reader:
            a.append(r['tl'])

for t in a:
    print(t)
    socket.setdefaulttimeout(5)
    #解决下载不完全问题且避免陷入死循环
    try:
        urllib.request.urlretrieve('http://onuma.com/transfer/SEPS/' + t,t)
    except socket.timeout:
        count = 1
        while count <= 10:
            try:
                urllib.request.urlretrieve('http://onuma.com/transfer/SEPS/' + t,t)                                                
                break
            except socket.timeout:
                err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
                print(err_info)
                count += 1
        if count > 5:
            print("downloading failed!")

url=makeUrl.makefromint(40)
print(url)

try:
    data=urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    print(e)
    sys.exit()

datastr=data.read().decode()

l=len(datastr)
if l>0:
    print(l)
#print(datastr)

title_str=r'<title>(.+?)｜電車・駅のご'
title_comp=re.compile(title_str)

timetable_str=r'<li><span>(.+?)</span><a href="(.+?)" target="_blank"><img src="img/timetable_weekday.gif" alt="(.+?)（PDF）" width="85" height="21" /></a><a href="(.+?)" target="_blank"><img src="img/timetable_holiday.gif" alt="(.+?)（PDF'
timetable_comp=re.compile(timetable_str)

struct_str=r'<p><a href="(.+?)" target="_blank"><.+? alt="駅構内図'
struct_comp=re.compile(struct_str)

title=title_comp.findall(datastr)
timetables=timetable_comp.findall(datastr)
struct=struct_comp.findall(datastr)

print(title)
for r in timetables:
    print(r)
print(struct)

