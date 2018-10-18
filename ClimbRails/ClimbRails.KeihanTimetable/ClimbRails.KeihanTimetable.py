#coding=utf-8
import os
os.system('cls')
import urllib.request
import re
import sys
import makeUrl
import doDownload

startwith = 120

base = makeUrl.base()
infobase = makeUrl.infobase()

title_str = r'<title>(.+?)｜電車・駅のご'
title_comp = re.compile(title_str)

timetable_str = r'<li><span>(.+?)</span><a href="(.+?)" target="_blank"><img src="img/timetable_weekday.gif" alt="(.+?)（PDF）"  ??width="85" height="21" ??/></a><a href="(.+?)" target="_blank"><img src="img/timetable_holiday.gif" alt="(.+?)（PDF'
timetable_comp = re.compile(timetable_str)

struct_str = r'<p><a href="(.+?)" target="_blank"><.+? alt="駅構内図'
struct_comp = re.compile(struct_str)

for id in range(startwith,300):
    url = makeUrl.makefromint(id)
    try:
        data = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        continue

    datastr = data.read().decode()

    title = title_comp.findall(datastr)
    timetables = timetable_comp.findall(datastr)
    struct = struct_comp.findall(datastr)

    #print(title)
    #print(timetables)
    #print(struct)
    #print(struct[0])
    #print(timetables[0][1])

    folder = "E:\\keihan\\" + str(id) + title[0]
    os.mkdir(folder)
    
    for tableIndex in range(0,len(timetables)):
        direction = timetables[tableIndex][0]
        doDownload.downloadOneFile(base + timetables[tableIndex][1],folder + "\\" + direction + "-" + timetables[tableIndex][2] + ".pdf")
        doDownload.downloadOneFile(base + timetables[tableIndex][3],folder + "\\" + direction + "-" + timetables[tableIndex][4] + ".pdf")
    doDownload.downloadOneFile(infobase + struct[0],folder + "\\struct.pdf")


