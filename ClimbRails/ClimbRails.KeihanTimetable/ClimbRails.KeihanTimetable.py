#coding=utf-8
import os
os.system('cls')
import urllib.request
import re
import sys
import makeUrl

# redist
print('------------------------------')

base = makeUrl.base()
url = makeUrl.makefromint(40)
print(url)

try:
    data = urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    print(e)
    sys.exit()

datastr = data.read().decode()

l = len(datastr)
if l > 0:
    print(l)
#print(datastr)
title_str = r'<title>(.+?)｜電車・駅のご'
title_comp = re.compile(title_str)

timetable_str = r'<li><span>(.+?)</span><a href="(.+?)" target="_blank"><img src="img/timetable_weekday.gif" alt="(.+?)（PDF）" width="85" height="21" /></a><a href="(.+?)" target="_blank"><img src="img/timetable_holiday.gif" alt="(.+?)（PDF'
timetable_comp = re.compile(timetable_str)

struct_str = r'<p><a href="(.+?)" target="_blank"><.+? alt="駅構内図'
struct_comp = re.compile(struct_str)

title = title_comp.findall(datastr)
timetables = timetable_comp.findall(datastr)
struct = struct_comp.findall(datastr)

print(title)
for r in timetables:
    print(r)
print(struct)
print(struct[0])
print(timetables[0][2])

os.mkdir(r'E:\keihan\kkk')
fpath = r'E:\keihan\try.pdf'
fp = open(fpath,'w')
fp.close()
urllib.request.urlretrieve(base + timetables[0][1],fpath)
urllib.request.urlretrieve(base + timetables[0][1],'xx.pdf')


