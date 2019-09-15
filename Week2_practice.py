#!/usr/bin/env python
# coding: utf-8

# In[102]:


print(ord("A"),ord("Z"))


# In[4]:


print(ord('a'),ord('z'))


# In[87]:


x=65
lis=[]
for x in range(65,91):
    tup = (chr(x),chr(x+32))
    lis.append(tup)
for i in lis:
    print(i)


# In[112]:


import os 
filename = []
for i in range(1,51):
    name="./file"+str(i)
    filename.append(name)
path = r"C:\Download"
for name in filename:
    os.mkdir(path+name)


# In[ ]:




