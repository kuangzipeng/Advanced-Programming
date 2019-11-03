#!/usr/bin/env python
# coding: utf-8

# In[71]:


##程序名sys.argv.py
import re
import os
import sys
path = "D:/Advanced-Programming/books/"
filename = sys.argv[1]
fn=path+filename
name=os.path.splitext(filename) ##去掉后缀名
fn_EN=path+name[0]+'_EN.txt' 
fn_ZH=path+name[0]+'_ZH.txt'
try:
    with open(fn, "r") as f:
        string=f.read()
        str_en = re.sub(u"([\u4e00-\u9fa5]|[\（\）\《\》\——\；\，\、\？\。\……\“\”\<\>\！\：\·\•])","",string)##去掉中文字符
        str_zh = re.sub(u"([\u0041-\u005a\u0061-\u007a]|[\.\'\"\‘\?\．])","",string)##去掉英文字符
    with open(fn_EN, 'w') as f0:
        f0.write(str_en)
    with open(fn_ZH, 'w') as f1:
        f1.write(str_zh)
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("已完成")
    

    


# In[ ]:




