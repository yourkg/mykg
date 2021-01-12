#-*- coding:utf-8 -*-
import re
import urllib.request
import time
xx=0

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
           	}

#path='https://www.baidu.com/s?&wd=%E5%8D%8A%E5%AF%BC%E4%BD%93&ie=utf-8'
path='https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=%E5%8D%8A%E5%AF%BC%E4%BD%93'
'''
with open('content1.txt','r',encoding='utf-8') as f:
  content1 = f.read()
with open('content2.txt','r',encoding='utf-8') as f:
  content2 = f.read()
'''


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
    Newpage=ulist[0][:-10].replace(r'<em>半导体</em>', '半导体')
    Nulist=re.compile(r'm-path=""(.*?)</div></div></div>',re.DOTALL).findall(Newpage)
    print(len(Nulist))
    for i in Nulist:
        biaoti=re.compile(r'"news-title_1YtI1">(.*?)</h3>',re.DOTALL).findall(i)
        print("大标题：",biaoti[0])
        try:
           tupian=re.compile(r'<img src="(.*?)" alt=""',re.DOTALL).findall(i)
           print("图片：",tupian[0].replace(r'amp;', ''))
        except:
           print("图片：","没有")
        laizi=re.compile(r'c-gap-right">(.*?)</span>',re.DOTALL).findall(i)
        print("大标题：",laizi[0])
        shijian=re.compile(r'"c-color-gray2 c-font-normal">(.*?)</span>',re.DOTALL).findall(i)
        print("大标题：",shijian[0])
        miaoshu=re.compile(r'text"><!--s-text-->(.*?)<!--/s-text--></span>',re.DOTALL).findall(i)
        print("描述：",miaoshu[0])
        print("----------------------------------------------------------------------------------")

    try:
        with open("ndex.html", "w", encoding='utf-8') as f:
            #f.write(ulist[0][200:-150])
            #f.write("<div id='content_left'"+ulist[0][:-10])
            f.write("<div id='content_left'"+ulist[0][:-10].replace(r'<em>半导体</em>', '半导体').replace(r'百度快照', ''))
    except:
        fab()    
fab()
print("ok")


