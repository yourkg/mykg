#-*- coding:utf-8 -*-
import re
import urllib.request
import time
xx=0

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
           	}

#path='https://www.baidu.com/s?&wd=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&ie=utf-8'
path='https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD'

with open('content1.txt','r',encoding='utf-8') as f:
  content1 = f.read()
with open('content2.txt','r',encoding='utf-8') as f:
  content2 = f.read()



starttime = time.time()
def fab():
    print('\r用时:', round(time.time() - starttime, 2),'     秒          ',end="")
    if round(time.time() - starttime, 2)>100:
           print("not")
           return
    a=urllib.request.Request(url=path, headers=headers)
    b=urllib.request.urlopen(a).read().decode('utf-8')
    #zz=r'"sp_realtime_bigpic5"(.*?)"se_com_default"'
    zz=r'"content_left"(.*?)"gotoPage"'
    zzx=re.compile(zz,re.DOTALL)
    ulist=zzx.findall(b)
    #print(b)

    try:
        with open("index.html", "w", encoding='utf-8') as f:
            #f.write(ulist[0][200:-150])
            #f.write("<div id='content_left'"+ulist[0][:-10])
            f.write(content1+"<div id='content_left'"+ulist[0][:-10].replace(r'<em>人工智能</em>', '人工智能')+content2)
    except:
        fab()
    
fab()
print("ok")


