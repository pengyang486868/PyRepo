#!/usr/bin/python
#coding:utf-8
 
import urllib.request
import math
import re
 
pattern_x = re.compile(r'"x":(".+?")')
pattern_y = re.compile(r'"y":(".+?")')
 
def mercator2wgs84(mercator):
    #key1=mercator.keys()[0]
    #key2=mercator.keys()[1]
    point_x = mercator[0]
    point_y = mercator[1]
    x = point_x / 20037508.3427892 * 180
    y = point_y / 20037508.3427892 * 180
    y = 180 / math.pi * (2 * math.atan(math.exp(y * math.pi / 180)) - math.pi / 2)
    return (x,y)
 
def get_mercator(addr):
    quote_addr = urllib.request.quote(addr.encode('utf8'))
    #city = urllib.request.quote(u'齐齐哈尔市龙'.encode('utf8'))
    #province = urllib.request.quote(u'黑龙江省'.encode('utf8'))
    #if quote_addr.startswith(city) or quote_addr.startswith(province):
    #    pass
    #else:
        #quote_addr = city + quote_addr
    s = urllib.request.quote(u'北京市'.encode('utf8'))
    api_addr = "http://api.map.baidu.com/?qt=gc&wd=%s&cn=%s&ie=utf-8&oue=1&fromproduct=jsapi&res=api&callback=BMap._rd._cbk62300" % (quote_addr
,s)
    data = urllib.request.urlopen(api_addr)
    content = data.read().decode()
    #content = req.content
    x = re.findall(pattern_x,content)
    y = re.findall(pattern_y,content)
    if x:
        x = x[0]
        y = y[0] 
        x = x[1:-1]
        y = y[1:-1]
        x = float(x)
        y = float(y)
        location = (x,y)
    else:
        location = ()
    return location
 
def run():
    #data=xlrd.open_workbook('Book2.xls')
    #rtable=data.sheets()[0]
    #nrows=rtable.nrows
    #values=rtable.col_values(0)
     
    #workbook=xlwt.Workbook()
    #wtable=workbook.add_sheet('data',cell_overwrite_ok=True)
    #row=0
    #for value in values:
    #    mercator=get_mercator(value)
    #    if mercator:
    #        wgs=mercator2wgs84(mercator)
    #    else:
    #        wgs=('NotFound','NotFound')
    #    wtable.write(row,0,value)
    #    wtable.write(row,1,wgs[0])
    #    wtable.write(row,2,wgs[1])
    #    row=row+1
 
    #workbook.save('data.xls')
    mercator = get_mercator("常州市戚墅堰区")
    wgs=mercator2wgs84(mercator)
    print("")
 
if __name__ == '__main__':
    run()
