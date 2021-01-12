#-*- coding:utf-8 -*-
from selenium import webdriver
import pandas as pd
import time
import re
driver = webdriver.PhantomJS(executable_path='C:/Users/Administrator/Downloads/phantomjs-2.1.1-windows/bin/phantomjs')
def newNoBug(scname):
    zz=r'百度为您找到相关结果约(.*?)个'
    zzx=re.compile(zz,re.DOTALL)
    try:
        driver.get("https://www.baidu.com/")
        time.sleep(5)
        url=u'智能科学与技术 '+scname+' "智能科学与技术 '+scname+'"'
        driver.find_element_by_id('kw').send_keys(url)
        driver.find_element_by_id('su').click()
        time.sleep(6)
        
        #print(zzx.findall(driver.find_element_by_class_name('nums_text').text)) #----------------------------------------------num1
        num1=int(zzx.findall(driver.find_element_by_class_name('nums_text').text)[0].replace(r',',''))
        print(num1)
#print(driver.get_cookies())
        driver.find_element_by_class_name('search_tool').click()
        time.sleep(1.5)
#driver.save_screenshot("baidu0.png")
        driver.find_element_by_class_name('search_tool_tf').click()
#time.sleep(5)
#driver.save_screenshot("baidu1.png")
#print(driver.find_elements_by_css_selector('li'))
        driver.find_elements_by_xpath("//a[text()='一天内']")[0].click()
        time.sleep(6)
#driver.save_screenshot("baidu2.png")
        driver.find_elements_by_xpath("//span[text()='清除']")[0].click()
        time.sleep(0.2)
        #print(driver.find_element_by_class_name('nums_text').text)#----------------------------------------------num2
        num2=int(zzx.findall(driver.find_element_by_class_name('nums_text').text)[0].replace(r',',''))
        print(num2)
        time.sleep(1)
        driver.find_element_by_class_name('search_tool').click()
        time.sleep(1.5)
        driver.find_element_by_class_name('search_tool_tf').click()
        driver.find_elements_by_xpath("//a[text()='一周内']")[0].click()
        time.sleep(6)
#driver.save_screenshot("baidu2.png")
        driver.find_elements_by_xpath("//span[text()='清除']")[0].click()
        time.sleep(0.2)
        #print(driver.find_element_by_class_name('nums_text').text)#----------------------------------------------num3
        num3=int(zzx.findall(driver.find_element_by_class_name('nums_text').text)[0].replace(r',',''))
        print(num3)
        time.sleep(1)
        driver.find_element_by_class_name('search_tool').click()
        time.sleep(1.5)
        driver.find_element_by_class_name('search_tool_tf').click()
        driver.find_elements_by_xpath("//a[text()='一月内']")[0].click()
        time.sleep(6)
#driver.save_screenshot("baidu2.png")
        driver.find_elements_by_xpath("//span[text()='清除']")[0].click()
        time.sleep(0.2)
        #print(driver.find_element_by_class_name('nums_text').text)#----------------------------------------------num4
        num4=int(zzx.findall(driver.find_element_by_class_name('nums_text').text)[0].replace(r',',''))
        print(num4)
    except:
        num1,num2,num3,num4=newNoBug(scname)
    return num1,num2,num3,num4
    #driver.close()
"""
print(driver.find_elements_by_css_selector('li')[5].text)
driver.find_elements_by_css_selector('li')[5].click()
time.sleep(6)
driver.save_screenshot("baidu2.png")
print(driver.find_elements_by_css_selector('li')[6].text)
print(driver.find_elements_by_css_selector('li')[7].text)
print(driver.find_elements_by_css_selector('li')[8].text)
"""
#driver.save_screenshot("baidu.png")

#driver.quit()


"""
后期如需改爬百度指数参考https://my.oschina.net/u/3280685/blog/903371
#弃用方案
#-*- coding:utf-8 -*-
import re
import urllib.request
import time
starttime = time.time()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            
            }

gjcstr="智能科学与技术"
gjcstr = urllib.parse.quote(gjcstr)
###### 规则1
def fuc1(scname):
    print('\r已用时:','%0.2f'%round(time.time() - starttime, 2),'秒',end="")
    #path='https://www.baidu.com/s?q1='+str(gjcstr.encode("utf-8"))[2:-1].upper()+'+'+str(scname.encode("utf-8"))[2:-1].upper()+'&q2='+str(gjcstr.encode("utf-8"))[2:-1].upper()+'+'+str(scname.encode("utf-8"))[2:-1].upper()+'&q3=&q4=&gpc=stf&ft=&q5=&q6=&tn=baiduadv'
    path='https://www.baidu.com/s?q1='+gjcstr+'+'+scname+'&q2='+gjcstr+'+'+scname+'&q3=&q4=&gpc=stf&ft=&q5=&q6=&tn=baiduadv'
    #print(path.replace(r'\X','%'))
    #print(path)
    a=urllib.request.Request(url=path, headers=headers)
    b=urllib.request.urlopen(a).read().decode('utf-8')
    zz=r'百度为您找到相关结果约(.*?)个'
    zzx=re.compile(zz,re.DOTALL)
    ulist=zzx.findall(b)
    #print(b)
    returnum=0
    try:
        print("ok?")
        returnum=int(ulist[0].replace(r',',''))
        print(returnum)
        return returnum
    except:
        print("no")
        fuc1(scname)
###### 规则2
def fuc2(scname):
    print('\r已用时:','%0.2f'%round(time.time() - starttime, 2),'秒',end="")
    #path='https://www.baidu.com/s?q1='+str(gjcstr.encode("utf-8"))[2:-1].upper()+'+'+str(scname.encode("utf-8"))[2:-1].upper()+'&q2='+str(gjcstr.encode("utf-8"))[2:-1].upper()+'+'+str(scname.encode("utf-8"))[2:-1].upper()+'&q3=&q4=&gpc=stf&ft=&q5=&q6=&tn=baiduadv'
    path='https://www.baidu.com/s?q1='+gjcstr+'+'+scname+'&q2='+gjcstr+'+'+scname+'&q3=&q4=&gpc=stf%3D1594645949.589%2C1595250749.589%7Cstftype%3D1&ft=&q5=&q6=&tn=baiduadv'
    #print(path.replace(r'\X','%'))
    #print(path)
    a=urllib.request.Request(url=path, headers=headers)
    b=urllib.request.urlopen(a).read().decode('utf-8')
    zz=r'百度为您找到相关结果约(.*?)个'
    zzx=re.compile(zz,re.DOTALL)
    ulist=zzx.findall(b)
    #print(b)
    try:
        #print(ulist[0])
        print("is",int(ulist[0].replace(r',','')),end=" ")
        #if int(ulist[0].replace(r',',''))==None:
        #   time.sleep(1)
        #   fuc2(scname)
        
        return int(ulist[0].replace(r',',''))
    except:
        fuc2(scname)
###### 规则3
def fuc3(scname):
    print('\r已用时:','%0.2f'%round(time.time() - starttime, 2),'秒',end="")
    #path='https://www.baidu.com/s?q1='+str(gjcstr.encode("utf-8"))[2:-1].upper()+'+'+str(scname.encode("utf-8"))[2:-1].upper()+'&q2='+str(gjcstr.encode("utf-8"))[2:-1].upper()+'+'+str(scname.encode("utf-8"))[2:-1].upper()+'&q3=&q4=&gpc=stf&ft=&q5=&q6=&tn=baiduadv'
    path='https://www.baidu.com/s?q1='+gjcstr+'+'+scname+'&q2='+gjcstr+'+'+scname+'&q3=&q4=&gpc=stf%3D1595164349.589%2C1595250749.589%7Cstftype%3D1&ft=&q5=&q6=&tn=baiduadv'
    #print(path.replace(r'\X','%'))
    #print(path)
    a=urllib.request.Request(url=path, headers=headers)
    b=urllib.request.urlopen(a).read().decode('utf-8')
    zz=r'百度为您找到相关结果约(.*?)个'
    zzx=re.compile(zz,re.DOTALL)
    ulist=zzx.findall(b)
    #print(b)
    try:
        #print(ulist[0])
        print("is",int(ulist[0].replace(r',','')),end=" ")
        #if int(ulist[0].replace(r',',''))==None:
        #   time.sleep(1)
        #   fuc3(scname)
        
        return int(ulist[0].replace(r',',''))
    except:
        fuc3(scname)
###### 规则4
def fuc4(scname):
    print('\r已用时:','%0.2f'%round(time.time() - starttime, 2),'秒',end="")
    #path='https://www.baidu.com/s?q1='+str(gjcstr.encode("utf-8"))[2:-1].upper()+'+'+str(scname.encode("utf-8"))[2:-1].upper()+'&q2='+str(gjcstr.encode("utf-8"))[2:-1].upper()+'+'+str(scname.encode("utf-8"))[2:-1].upper()+'&q3=&q4=&gpc=stf&ft=&q5=&q6=&tn=baiduadv'
    path='https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd='+gjcstr+'+'+scname+'+%22'+gjcstr+'+'+scname+'%22&medium=0'   
    #print(path.replace(r'\X','%'))
    #print(path)
    a=urllib.request.Request(url=path, headers=headers)
    b=urllib.request.urlopen(a).read().decode('utf-8')
    zz=r'找到相关资讯(.*?)篇'
    zzx=re.compile(zz,re.DOTALL)
    ulist=zzx.findall(b)
    #print(b)
    try:

        if int(ulist[0].replace(r',',''))!=None:
            return int(ulist[0].replace(r',',''))
        
    except:
        fuc4(scname)

# 爬

for line in open("sclist.txt",encoding='utf-8'):
    scname=line[:-1]
    scname = urllib.parse.quote(scname)
    fen=fuc1(scname)
    print(line[:-1],"->",fen)
    time.sleep(1)
"""
try:
    IN=open('scin.txt',mode='r')
    scinNum=int(IN.read())
except:
    scinNum=0
print("start for ",scinNum)
nk=0;
for line in open("sclist.txt",encoding='utf-8'):
    print("load-->",nk,scinNum)
    if nk<scinNum:
        nk+=1
        continue
    scname=line[:-1]
    print(scname)
    n1,n2,n3,n4=newNoBug(scname)
    point=n1*0.03+n2*3000+n3*300+n4*30
    print("----------------------------",n1,n2,n3,n4,"->",point)
    dataframe = pd.DataFrame({'name':[scname],'point':[point]})
    dataframe.to_csv('saveP.csv', mode='a', sep=',',index=False,header=False)
    scinNum+=1
    nk+=1
    scin=open('scin.txt',mode='w')
    scin.write(str(scinNum))
    scin.close()
    time.sleep(1)
driver.quit()
print("start 2 ")
label = pd.read_csv('saveP.csv',header=None)
labelOK=label.sort_values(by=1,axis=0,ascending=False)[:10]
print(labelOK)
okstr="["
okstr2="['"
for k,row in labelOK.iterrows():
    #print(k,row[0],row[1])
    okstr+=str(row[1])
    okstr+=","
    okstr2+=str(row[0])
    okstr2+="','"
okstr+="]"
okstr2+="']"
print(okstr)
print(okstr2)
print("start 3 ")
with open('content1_1.txt','r',encoding='utf-8') as f:
  content1 = f.read()
with open('content2_2.txt','r',encoding='utf-8') as f:
  content2 = f.read()
with open('content3.txt','r',encoding='utf-8') as f:
  content3 = f.read()
with open("index2.html", "w", encoding='utf-8') as f:
        f.write(content1+content2+okstr+";var xinforma = "+okstr2+content3)
print("over")
scinNum=0
scin=open('scin.txt',mode='w')
scin.write(str(scinNum))
scin.close()
with open('saveP.csv', 'w'):
    pass
