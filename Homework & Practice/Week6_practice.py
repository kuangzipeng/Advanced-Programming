#!/usr/bin/env python
# coding: utf-8

# In[15]:


import os
path = "D:/Advanced-Programming/books"
files = os.listdir(path)
name_list=[]
len_list=[]
for filename in files:
    name_list.append(filename)
    fn='D:/Advanced-Programming/books/'+filename
    f=open(fn,'r')
    length=f.read()
    len_list.append(len(length))
    f.close()
dict_=dict(zip(name_list,len_list))
print(dict_)
    


# In[20]:


import json
json_dict=json.dumps(dict_)
with open("D:/Advanced-Programming/books/json_dict", "w") as f:
    json.dump(json_dict, f)


# In[27]:


import pickle
dict_string_1 = pickle.dumps(dict_, 1)
with open("D:/Advanced-Programming/books/dict_.pkl", "wb") as f:
    pickle.dump(dict_string_1, f)


# In[ ]:




