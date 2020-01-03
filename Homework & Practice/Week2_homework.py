#!/usr/bin/env python
# coding: utf-8

# In[1]:


#第一题

#方法一
i=1
total1=0
while (i<=10000):
    if(i%2==0):
        total1=total1+i  
    i=i+1 
print(total1)

##

i=0
total2=0
while (i<=10000):
    if(i%3==0):
        total2=total2+i  
    i=i+1 
print(total2)

#方法二
i=0
total3=0
for i in range (4,10001,4):
    total3+=i
print(total3)

##

i=0
total4=0
for i in range (5,10001,5):
    total4+=i
print(total4)


# In[36]:


#第二题
asciilist = []
for i in range(32,128):
    asciilist.append(chr(i))
print(len(asciilist))
for i in range(0,len(asciilist),20):
    print(asciilist[i:i+20])


# In[ ]:




