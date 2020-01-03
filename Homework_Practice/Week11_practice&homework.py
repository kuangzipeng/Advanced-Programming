#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import random
import time
import json
from lxml import etree
from pyquery import PyQuery as pq

class ProxyPool():
    def __init__(self):
        # 初始化读取proxy站点配置文件

        # 初始化读取proxy池存储位置（文件、数据库、NoSQL...)

        # 定时扫描proxy可用性、删除失效代理
        pass

    def check_a_proxy(self):
        pass

class KKBaseDownloader():
    def __init__(self):
        # 初始化代理池对象
        self.proxyp = ProxyPool()
        # 初始化headers配置列表文件路径
        self.headers_cfg_pth=''
        # 初始化最小、最大暂停间隔
        self.interval_min_max = (5,30)
        pass
    
    def gen_an_ua(self):
        self.ua_list = ["Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0"]

        return random.choice(self.ua_list)

    def get_a_proxy(self):
        proxys = [

        ]
        idx = random.randint(1,len(proxys))
        return proxys[idx]

class KKNavDl(KKBaseDownloader):
    def __init__(self,init_url):
        super(KKNavDl,self).__init__()
        self.url_tgt = init_url

    def fetch_html(self):
        ua = self.gen_an_ua()
        headers = {'User-Agent':ua}
        # _proxy = self.get_a_proxy()
        # r = requests.get(self.url_tgt,proxies=_proxy)
        r = requests.get(self.url_tgt,headers=headers)
        if r.status_code==200:
            if r.encoding == 'ISO-8859-1':
                encodings = requests.utils.get_encodings_from_content(r.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r.apparent_encoding
            encode_content = r.content.decode(encoding, 'replace').encode('utf-8', 'replace')
            return encode_content
        else:
            return ''

class KKBaseExtractor():
    def __init__(self,html='<html></html>'):
        self.doc = pq(html)

class KKNavExt(KKBaseExtractor):
    def __init__(self,html):
        super(KKNavExt,self).__init__(html)

    def parse(self):
        lis = self.doc('.list_box_2>ul>li')
        nav_links=[]
        for i in range(0,len(lis)):
            pq_li = pq(lis[i])
            title=str(pq_li('h2 a').text())
            s=len(title)
            t=len(str(pq_li('li').text()))
            n=len(str(pq_li('p').text()))
            info=str(pq_li('li').text()[s+1:t-n-1])
            date=str(pq_li('p').text()[0:9])
            author=str(pq_li('p').text()[14:19])
            keywords=str(pq_li('span').text())
            href=str(pq_li.find('a').attr('href'))
            Net={"Title":title,"Info":info,"Date":date,"Author":author,"Keywords":keywords,"Link":href}
            nav_links.append(Net)
        return nav_links

navDl = KKNavDl(init_url='http://www.kekenet.com/read/news/keji/')
html = navDl.fetch_html()
navExt = KKNavExt(html)
nav_links=navExt.parse()
print(nav_links)


# In[73]:


with open("news.json","w") as f:
     json.dump(nav_links,f)


# In[80]:


file = open("news.json",encoding='utf-8')
line = json.load(file)
line


# In[ ]:


import pymysql
import logging
import pandas as pd
 
db_server = 'localhost'
db_user = 'root'
db_pass = ''
db_name='kekenet'


#写入数据到数据库中
def writeDb(sql,db_data=()):
    """
    连接mysql数据库（写），并进行写的操作
    """
    try:
        conn = pymysql.connect(db=db_name,user=db_user,passwd=db_pass,charset="utf8")
        cursor = conn.cursor()
    except Exception as e:
        print(e)
        logging.error('数据库连接失败:%s' % e)
        return False
 
    try:
        cursor.execute(sql, db_data)
        conn.commit()
    except Exception as e:
        conn.rollback()
        logging.error('数据写入失败:%s' % e)
        return False
    finally:
        cursor.close()
        conn.close()
    return True
 
 

sql = "INSERT INTO week11_kekenet(title,info,time,author,keywords,link)VALUES(%s,%s,%s,%s,%s,%s)"
for i in range(0,len(line)):
    data =[line[i]["Title"],line[i]["Info"],line[i]["Date"],line[i]["Author"],line[i]["Keywords"],line[i]["Link"]]
    result = writeDb(sql, data)


# In[ ]:




