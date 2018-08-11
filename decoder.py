import pickle

import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://www.pythonchallenge.com/pc/def/banner.p')
a = pickle.loads(r.data)
for l in a:
    for t in l:
        for i in range(t[1]):
            print(t[0], end='')
    print()