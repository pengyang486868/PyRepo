#coding=utf-8
import os
os.system('cls')
import urllib.request
import re
import sys
import time

suburl_str = r'href="/biz/(.+?)osq=Restaurants"'
suburl_comp = re.compile(suburl_str)

URLs = [] # url for all rests
for i in range(10):
    time.sleep(1)
    url = 'https://www.yelp.com/search?find_desc=Restaurants&start={}&l=g:-73.9766979218,40.7982170258,-73.9511203766,40.8177067094'.format(str(i * 30))
    
    data = urllib.request.urlopen(url)
    datastr = data.read().decode()
    surl = suburl_comp.findall(datastr)
    curCount = 0
    for u1 in surl:
        if not(u1 in URLs) and u1[-1] == '?' and len(u1) < 100:
            URLs.append(u1)
            curCount = curCount + 1
    if curCount < 30:
        data = urllib.request.urlopen(url) 
        datastr = data.read().decode()
        surl = suburl_comp.findall(datastr)
        curCount = 0
        for u1 in surl:
            if not(u1 in URLs) and u1[-1] == '?' and len(u1) < 100:
                URLs.append(u1)

print(len(URLs))

with open('urls.csv', 'w', newline='') as f:
    for row in URLs:
        f.write(row + '\n')


