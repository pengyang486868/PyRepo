#coding=utf-8
import os
os.system('cls')
import urllib.request
import csv
import re

with open('urls.csv', 'r', newline='') as f:
    rawlist = f.readlines()

restau_raw = []
for r in rawlist:
    restau_raw.append(r[:-2])

#print(restau_raw)
review_str = r'"description": "(.+?)", "author": "(.+?)"}'
location_str = r'id="dropdown_user-name">(.+?)</a>\n        </li>\n        <li class="user-location responsive-hidden-small">\n            <b>(.+?)</b>\n        </li>\n    </ul>'
time_str = r'<th scope="row">(.+?)</th>\n        <td>\n            <span class="nowrap">(.+?)</span>(.+?)<span class="nowrap">(.+?)</span>\n        </td>\n        <td class="extra">\n        </td>\n    </tr>'
address_str = r'"name": "(.+?)", "address": {"addressLocality": "(.+?)", "addressRegion": "(.+?)", "streetAddress": "(.+?)", "postalCode": "(.+?)"'

review_comp = re.compile(review_str)
location_comp = re.compile(location_str)
time_comp = re.compile(time_str)
address_comp = re.compile(address_str)

for raw in restau_raw:
    curReview = []
    url = r'https://www.yelp.com/biz/' + raw + r'?osq=Restaurants'
    data = urllib.request.urlopen(url)
    datastr = data.read().decode()
    reviewinfo = review_comp.findall(datastr)
    locationdic = location_comp.findall(datastr)
    timedic = time_comp.findall(datastr)
    addressinfo=address_comp.findall(datastr)
    curReview.append(reviewinfo)


