#coding=utf-8
import os
os.system('cls')
import urllib.request
import csv
import re
import pandas as pd

with open('urls.csv', 'r', newline='') as f:
    rawlist = f.readlines()

restau_raw = []
for r in rawlist:
    restau_raw.append(r[:-3])

#print(restau_raw)
review_str = r'"description": "(.+?)", "author": "(.+?)"}'
location_str = r'id="dropdown_user-name">(.+?)</a>\n        </li>\n        <li class="user-location responsive-hidden-small">\n            <b>(.+?)</b>\n        </li>\n    </ul>'
time_str = r'<th scope="row">(.+?)</th>\n        <td>\n            <span class="nowrap">(.+?)</span>(.+?)<span class="nowrap">(.+?)</span>\n        </td>\n        <td class="extra">\n        </td>\n    </tr>'
address_str = r'"name": "(.+?)", "address": {"addressLocality": "(.+?)", "addressRegion": "(.+?)", "streetAddress": "(.+?)", "postalCode": "(.+?)"'

review_comp = re.compile(review_str)
location_comp = re.compile(location_str)
time_comp = re.compile(time_str)
address_comp = re.compile(address_str)

uniqueidSeries = []
nameSeries = []
addressSeries = []
zipSeries = []
timeSeries = []
reviewSeries = []

fp = open('main_info.csv', 'w', newline='')
fr = open('reviews.csv', 'w', newline='')

for raw in restau_raw:
    url = r'https://www.yelp.com/biz/' + raw + r'?osq=Restaurants'
    data = urllib.request.urlopen(url)
    datastr = data.read().decode()
    reviewinfo = review_comp.findall(datastr)
    locationdic = location_comp.findall(datastr)
    timedic = time_comp.findall(datastr)
    addressinfo = address_comp.findall(datastr)

    uniqueid = raw
    uniqueidSeries.append(uniqueid)

    name = addressinfo[0][0]
    nameSeries.append(name)

    addr = addressinfo[0][3]
    addressSeries.append(addr)

    zip = addressinfo[0][4]
    zipSeries.append(zip)
    
    timearray = []
    time = ''
    for d in timedic:
        timearray.append([d[0],d[1] + d[2] + d[3]])
        time = time + '/' + d[0] + ':' + d[1] + d[2] + d[3]
    timeSeries.append(timearray)

    revarray = []
    for rev in reviewinfo:
        for loc in locationdic:
            if rev[1] == loc[0]:
                rev_complete = []
                rev_complete.append(rev[0])
                rev_complete.append(rev[1])
                rev_complete.append(loc[1])
                revarray.append(rev_complete)
                fr.write(uniqueid + ',' + rev[0] + ',' + rev[1] + ',' + loc[1] + '\n')
    reviewSeries.append(revarray)
    
    fp.write(uniqueid + ',' + name + ',' + addr + ',' + zip + ',' + time + '\n')
    print("")

df = pd.DataFrame({'key':uniqueidSeries,'name':nameSeries,'address':addressSeries,'zip':zipSeries,'time':timeSeries,'review':reviewSeries})
fp.close()
fr.close()

