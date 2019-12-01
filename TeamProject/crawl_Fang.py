#!/usr/bin/env python
# coding: utf-8

# In[14]:


import csv
from bs4 import BeautifulSoup
import requests
from pyquery import PyQuery as pq

def get_NewHouse(url):
    r=requests.get(url)
    r.raise_for_status()
    r.encoding = 'utf-8'
    html=r.text
    doc=pq(html)   
    lis=doc('.nlcd_name')   
    price=doc('.nhouse_price')   
    name_list=[]
    price_list=[]
    for a in lis:
        name_list.append(pq(a).text())
    for span in price:
        price_list.append(pq(span).text())
    
    list=[name_list,price_list]
    output= {}
    output=dict(zip(name_list, price_list))
    print(output)

    
def getURL(url):
    res = requests.get(url)
    res.encoding = 'gb2312'
    html = res.text            #获取网页内容
    soup = BeautifulSoup(html,'lxml')
    lis = soup.find('li',class_="quyu_name dingwei")
    url= BeautifulSoup(str(lis),"lxml")
    url_lis = url.find_all('a')
    pre='https://newhouse.fang.com'
    distrcit_link = []
    for i in range(1,19):
        links=pre+url_lis[i]['href']
        distrcit_link.append(links)
    num=0
    for i in distrcit_link:
        crawlFang(i,num)   #num用于区分各区网址
        num=num+1


def crawlFang(url,num): #定义一个爬取字段的函数    
    district=['chaoyang','haidian','fengtai','xicheng','dongcheng','changping','daxing','tongzhou','fangshan','shunyi','shijingshan','miyun','mentougou','huairou','yanqing','pinggu','yanjiao','beijingzhoubian']
    namelis=[]
    addresslis=[]
    infolis=[]
    statuslis=[]    
    pre='https://newhouse.fang.com/house/s/'
    NextPage_link = [] 
    if(num==1 or num==2 or num==8): #两页
        for i in range(1,3):
            links=pre+district[num]+'/b9'+str(i)
            NextPage_link.append(links)
    elif(num==6): #四页
        for i in range(1,5):
            links=pre+district[num]+'/b9'+str(i)
            NextPage_link.append(links)
    elif(num==0 or num==5 or num==7 or num==9):
        for i in range(1,4): #三页
            links=pre+district[num]+'/b9'+str(i)
            NextPage_link.append(links)
    else:
        links=pre+district[num]+'/b91'
        NextPage_link.append(links)
        
    for i in NextPage_link:       
        r = requests.get(i)
        r.raise_for_status()
        r.encoding = 'gb2312'
        web_con=r.text
        doc=pq(web_con)
        name=doc('.nlcd_name')
        for a in name:
            namelis.append((pq(a).text()))
            
        info = doc('.house_type')
        for b in info:
            infolis.append((pq(b).text()))
    
        address=doc('.address')
        for c in address:
            addresslis.append((pq(c).text()))
    
        status = doc('.fangyuan')
        for d in status:
            statuslis.append((pq(d).text()))    
        
    writefile(namelis,addresslis,infolis,statuslis,num)

    
def writefile(namelis,addresslis,infolis,statuslis,num):
    location=['朝阳','海淀','丰台','西城','东城','昌平','大兴','通州','房山','顺义','石景山','密云','门头沟','怀柔','延庆','平谷','燕郊','北京周边']     
    with open(location[num]+'.csv','w',newline='',encoding='utf-8-sig') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(['楼盘','具体位置','户型','楼盘状态'])
        count=0
        for j in namelis:
            writer.writerow([namelis[count],addresslis[count],infolis[count],statuslis[count]]) #括号里为要写入csv文档的对象
            count=count+1
        csvfile.close()#关闭csv

    
NewHouse_url="https://newhouse.fang.com/house/saledate/201911.htm"
get_NewHouse(NewHouse_url)
url = "https://newhouse.fang.com/house/s/"
getURL(url)


# In[11]:





# In[ ]:




