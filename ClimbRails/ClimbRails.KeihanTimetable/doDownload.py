import socket
import urllib.request

def downloadOneFile(url,path):
    maxTimeout = 5
    maxTimes = 10
    socket.setdefaulttimeout(maxTimeout)
    print(path)

    # create file first
    fp = open(path,'a')
    fp.close()

    try:
        urllib.request.urlretrieve(url,path)
    except socket.timeout:
        count = 1
        while count <= maxTimes:
            try:
                urllib.request.urlretrieve(url,path)
                break
            except socket.timeout:
                err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
                print(err_info)
                count += 1
        if count > maxTimes:
            print("downloading failed! " + path)
