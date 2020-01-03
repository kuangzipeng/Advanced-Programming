#!/usr/bin/env python
# coding: utf-8

# In[105]:


##Week3_homework


def get_startday(mon):  ##获取每个月1号对应的星期
    if mon == 1:
        startday=2
    else:
        days=0
        for i in range(mon):
            days = days + get_day(i)
        startday=(2+days)%7
    return startday

print('2020'.center(82))
print()
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekend=['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa','Su']
mon_dict={1:'January',2:'Febuary',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

calendar = dict.fromkeys([x for x in range(12)], '')##需要输出的日历字典

for i in range(12):
    calendar[i] += (mon_dict[i+1]+'\n')
    for each in weekend:
        calendar[i] += (each + ' ')
    calendar[i] += '\n'                  #将月份和星期输入到列表，标识符“\n”
    
    ndays = [x for x in range(1,days[i]+1)] #推导式,根据月份生成对应的【1，2，3……】日期列表
    for j in range(get_startday(i+1)):
        ndays.insert(0, '  ') #根据get_startday函数结果在ndays列表最前面插入空格
 
    for j in range(days[i]+get_startday(i+1)):
        if (j + 1) % 7:
            calendar[i] += (str(ndays[j]).rjust(2) + ' ')
        else:
            calendar[i] += (str(ndays[j]).rjust(2) + '\n')##遇到七的倍数的字符，在其后加一个换行符
     
for each in calendar:
    calendar[each] = calendar[each].split('\n') ##将一维数组切成二维数组
    
for i in range(0, 12, 3):
    max_len = max(len(calendar[i]), len(calendar[i+1]), len(calendar[i+2]))
    for j in range(3):
        while len(calendar[i+j]) < max_len:
            calendar[i+j] += [' ']  ##一行三个月份，当长度最长的月份未打印完之前，需要在其他两个月份列表最后加入空格

    for j in range(max_len):
        if j == 0: ##打印calendar列表里的每个数组的第一个元素，即月份
            print(calendar[i][j].center(17), end=' ' * 15)
            print(calendar[i+1][j].center(17), end=' ' * 15)
            print(calendar[i+2][j].center(17))
        elif j == 1: ##打印calendar列表里的每个数组的第二个元素，即星期
            print(calendar[i][j].ljust(15), end=' ' * 10)
            print(calendar[i+1][j].ljust(15), end=' ' * 10)
            print(calendar[i+2][j])
        else: ##打印calendar列表里的每个数组的其他元素，即日期
            print(calendar[i][j].ljust(20), end=' ' * 11)
            print(calendar[i+1][j].ljust(20), end=' ' * 11)
            print(calendar[i+2][j])
    print()

##本代码最后一部分的打印，并不是完全靠自己想出来敲出来，而是参考了CSDN上的文章，理解其思想后再自己打出来的
    


# In[ ]:




