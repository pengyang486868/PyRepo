def infobase():
    url = 'https://www.keihan.co.jp/traffic/station/stationinfo/'
    return url

def makefromint(n):
    if n < 10:
        return 'https://www.keihan.co.jp/traffic/station/stationinfo/' + '00' + str(n) + '.html'
    if n < 100:
        return 'https://www.keihan.co.jp/traffic/station/stationinfo/' + '0' + str(n) + '.html'
    return 'https://www.keihan.co.jp/traffic/station/stationinfo/' + str(n) + '.html'

def base():
    return 'https://www.keihan.co.jp'
