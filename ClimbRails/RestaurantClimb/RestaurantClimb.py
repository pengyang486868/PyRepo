import pandas as pd
import numpy as np
import time
import re
from bs4 import BeautifulSoup
import requests

#一级目录url
def get_results(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('li',attrs={'class': 'regular-search-result'})
    return results

#二级目录url
def get_all_url_single_page(results):
    BizURL=[]
    for result in results:
        bizurl=str(result.find('a'))
        bizurl_='https://www.yelp.com' + bizurl.split('>')[0].split(' ')[-1][6:-2]
        BizURL.append(bizurl_)
    return BizURL

# res = []
URLs = [] # 1级目录url
for i in range(10):
    url = 'https://www.yelp.com/search?find_desc=Restaurants&start={}&l=g:-73.9766979218,40.7982170258,-73.9511203766,40.8177067094'.format(str(i*30))
    #print(url)
    results = get_results(url)
    URLs.extend(get_all_url_single_page(results))
    time.sleep(15) #yelp貌似有反爬虫，一定要sleep，不然后面循环到后面几个网页就不给我扒了
    #print(URLs[0],len(URLs))

#当然sleep了也没有用，还是有若干个网页没给我扒，于是我在这里逐一补了一遍，总共有292个餐厅
for i in [240]:
    url = 'https://www.yelp.com/search?find_desc=Restaurants&start={}&l=g:-73.9766979218,40.7982170258,-73.9511203766,40.8177067094'.format(str(i))
    print(url)
    results = get_results(url)
    URLs.extend(get_all_url_single_page(results))
#     res.extend(results)
    time.sleep(1)
    print(URLs[-1],len(URLs))

print('--------------')
for u in URLs:
    print(u)



#然后就开始扒292个二级餐厅页面里的时间，评论者来源地和评论本身，但是一共有292个我也没看效果，也不知道怎么把他们存成dataframe.......
#但我突然意识到，一级网页似乎不用扒了，因为二级网页里面餐厅的名字啊这些都有。。。。。。。。

for url in URLs:
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    hours= soup.find('div', attrs={'class':'ywidget biz-hours'})
    hours_splited = hours.text.split("</span>")[0].split('\n')
    hour_dic = {}
    for hour in hours_splited:
        if not hour:
            continue
        else:
            if hour in ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']:
                last = hour
            elif hour[0].isdigit():
                hour_dic[last] = hour
    # hour_dic, {Mon: time}
    print(hour_dic)
    review = soup.find('ul', attrs={'class':'ylist ylist-bordered reviews'})
    for review1 in review.findAll('div',attrs={'class':'review review--with-sidebar'}):
        location = review1.find('li',attrs={'class':'user-location responsive-hidden-small'}).text.split('</b>')[0].strip()
        comment = review1.find('p').text.split("</p>")[0]
        # location,comment
        print(location)
        print(comment)


